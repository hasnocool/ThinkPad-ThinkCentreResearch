# scripts/validate_research.py
"""Validate canonical ThinkPad/ThinkCentre research records.

Designed for Python 3.12+. The validator is deterministic, read-only, and reports
all discovered errors in one run so research agents can fix a complete batch.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment setup failure
    raise SystemExit(
        "PyYAML is required. Install development dependencies with "
        "`python -m pip install -r requirements-dev.txt`."
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
MODEL_ROOTS = {
    "thinkpad": ROOT / "data" / "thinkpad" / "models",
    "thinkcentre": ROOT / "data" / "thinkcentre" / "models",
}
SOURCE_ROOT = ROOT / "sources" / "catalog"
ALLOWED_STATUSES = {"stub", "partial", "researched", "conflicted", "deprecated"}
DATE_RE = re.compile(r"^(?:\d{4}|\d{4}-\d{2}|\d{4}-\d{2}-\d{2})$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def iter_yaml_files(path: Path) -> Iterable[Path]:
    if not path.exists():
        return ()
    return tuple(sorted((*path.rglob("*.yaml"), *path.rglob("*.yml"))))


def load_yaml(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot parse YAML: {exc}")
        return None

    if not isinstance(payload, dict):
        errors.append(f"{path.relative_to(ROOT)}: top-level YAML value must be a mapping")
        return None
    return payload


def normalize_identity(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def validate_date(value: Any, field: str, path: Path, errors: list[str]) -> None:
    if value is None:
        return
    text = str(value)
    if not DATE_RE.fullmatch(text):
        errors.append(
            f"{path.relative_to(ROOT)}: {field} must be YYYY, YYYY-MM, or YYYY-MM-DD; got {text!r}"
        )


def validate_url(value: Any, field: str, path: Path, errors: list[str]) -> None:
    if value in (None, ""):
        return
    parsed = urlparse(str(value))
    if parsed.scheme != "https" or not parsed.netloc:
        errors.append(f"{path.relative_to(ROOT)}: {field} must be a canonical HTTPS URL")


def collect_source_references(value: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "source_ids" and isinstance(child, list):
                refs.update(item for item in child if isinstance(item, str))
            else:
                refs.update(collect_source_references(child))
    elif isinstance(value, list):
        for child in value:
            refs.update(collect_source_references(child))
    return refs


def main() -> int:
    errors: list[str] = []
    source_by_id: dict[str, Path] = {}
    model_by_slug: dict[str, Path] = {}
    canonical_names: dict[str, list[Path]] = defaultdict(list)
    aliases: dict[str, list[tuple[Path, str]]] = defaultdict(list)
    machine_types: dict[str, list[Path]] = defaultdict(list)
    mtms: dict[str, list[Path]] = defaultdict(list)

    for path in iter_yaml_files(SOURCE_ROOT):
        data = load_yaml(path, errors)
        if data is None:
            continue

        required = {
            "schema_version",
            "record_type",
            "id",
            "title",
            "publisher",
            "document_type",
            "url",
            "accessed",
            "official",
        }
        missing = sorted(required - data.keys())
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing source fields: {', '.join(missing)}")

        if data.get("record_type") != "source":
            errors.append(f"{path.relative_to(ROOT)}: record_type must be 'source'")

        source_id = data.get("id")
        if isinstance(source_id, str):
            if source_id in source_by_id:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate source id {source_id!r}; first seen in "
                    f"{source_by_id[source_id].relative_to(ROOT)}"
                )
            else:
                source_by_id[source_id] = path
        else:
            errors.append(f"{path.relative_to(ROOT)}: id must be a string")

        validate_url(data.get("url"), "url", path, errors)
        validate_url(data.get("archive_url"), "archive_url", path, errors)
        for field in ("publication_date", "revision_date", "accessed"):
            validate_date(data.get(field), field, path, errors)

    for product_line, model_root in MODEL_ROOTS.items():
        for path in iter_yaml_files(model_root):
            data = load_yaml(path, errors)
            if data is None:
                continue

            required = {
                "schema_version",
                "record_type",
                "product_line",
                "canonical_name",
                "slug",
                "status",
                "sources",
            }
            missing = sorted(required - data.keys())
            if missing:
                errors.append(f"{path.relative_to(ROOT)}: missing model fields: {', '.join(missing)}")

            if data.get("record_type") != "model":
                errors.append(f"{path.relative_to(ROOT)}: record_type must be 'model'")
            if data.get("product_line") != product_line:
                errors.append(
                    f"{path.relative_to(ROOT)}: product_line must be {product_line!r} for this directory"
                )

            slug = data.get("slug")
            if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
                errors.append(f"{path.relative_to(ROOT)}: invalid lowercase kebab-case slug {slug!r}")
            else:
                if path.stem != slug:
                    errors.append(
                        f"{path.relative_to(ROOT)}: filename stem must match slug {slug!r}"
                    )
                if slug in model_by_slug:
                    errors.append(
                        f"{path.relative_to(ROOT)}: duplicate model slug {slug!r}; first seen in "
                        f"{model_by_slug[slug].relative_to(ROOT)}"
                    )
                else:
                    model_by_slug[slug] = path

            canonical_name = data.get("canonical_name")
            if isinstance(canonical_name, str):
                canonical_names[normalize_identity(canonical_name)].append(path)

            status = data.get("status")
            if status not in ALLOWED_STATUSES:
                errors.append(f"{path.relative_to(ROOT)}: unsupported status {status!r}")

            sources = data.get("sources")
            if not isinstance(sources, list) or not sources:
                errors.append(f"{path.relative_to(ROOT)}: sources must be a non-empty list")
                source_refs: set[str] = set()
            else:
                source_refs = {item for item in sources if isinstance(item, str)}

            source_refs.update(collect_source_references(data))
            for source_id in sorted(source_refs):
                if source_id not in source_by_id:
                    errors.append(
                        f"{path.relative_to(ROOT)}: unresolved source reference {source_id!r}"
                    )

            identity = data.get("identity")
            if isinstance(identity, dict):
                for alias in identity.get("aliases", []) or []:
                    if isinstance(alias, str):
                        aliases[normalize_identity(alias)].append((path, alias))
                for machine_type in identity.get("machine_types", []) or []:
                    if isinstance(machine_type, str):
                        machine_types[machine_type.casefold()].append(path)
                for mtm in identity.get("mtms", []) or []:
                    if isinstance(mtm, str):
                        mtms[mtm.casefold()].append(path)

            validate_date(data.get("last_verified"), "last_verified", path, errors)

    for normalized, paths in canonical_names.items():
        if normalized and len(paths) > 1:
            rendered = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            errors.append(f"duplicate normalized canonical name across: {rendered}")

    for normalized, values in aliases.items():
        owners = {path for path, _ in values}
        if normalized and len(owners) > 1:
            rendered = ", ".join(str(path.relative_to(ROOT)) for path in sorted(owners))
            errors.append(f"duplicate normalized alias across models: {rendered}")

    for label, ownership in (("machine type", machine_types), ("MTM", mtms)):
        for identifier, paths in ownership.items():
            unique_paths = sorted(set(paths))
            if len(unique_paths) > 1:
                rendered = ", ".join(str(path.relative_to(ROOT)) for path in unique_paths)
                errors.append(f"duplicate {label} {identifier!r} owned by multiple models: {rendered}")

    if errors:
        print(f"Research validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Research validation passed: {len(model_by_slug)} model(s), "
        f"{len(source_by_id)} source(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
