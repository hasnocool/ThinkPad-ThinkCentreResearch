# ThinkPad & ThinkCentre Research

A provenance-first research dataset for IBM/Lenovo ThinkPad and ThinkCentre systems.

The long-term goal is to catalog as many verified ThinkPad and ThinkCentre models and meaningful variants as possible while preserving machine-type identity, source provenance, historical relationships, and important serviceability details.

## Current coverage

| Product line | Canonical models | Researched | Partial/stub |
| --- | ---: | ---: | ---: |
| ThinkPad | 19 | 19 | 0 |
| ThinkCentre | 1 | 1 | 0 |

Current canonical records:

- ThinkPad T420
- ThinkPad T420s
- ThinkPad T430
- ThinkPad T430s
- ThinkPad T430u
- ThinkPad T440
- ThinkPad T440p
- ThinkPad T440s
- ThinkPad T450
- ThinkPad T450s
- ThinkPad T460
- ThinkPad T460p
- ThinkPad T460s
- ThinkPad T470
- ThinkPad T470p
- ThinkPad T470s
- ThinkPad T480
- ThinkPad T480s
- ThinkPad T490
- ThinkCentre M75q Gen 2

See `docs/coverage/thinkpad.md` and `docs/coverage/thinkcentre.md` for the live coverage indexes and research gaps.

## Repository layout

```text
data/
  thinkpad/
    families/
    models/
  thinkcentre/
    families/
    models/
sources/
  catalog/
  notes/
docs/
  coverage/
  methodology/
  references/
scripts/
```

Canonical specifications are YAML records under `data/`. Human-readable coverage and methodology live under `docs/`. Source metadata is stored separately under `sources/catalog/` so model records can use stable source IDs without duplicating bibliographic information.

## Research principles

1. Prefer IBM/Lenovo PSREF, Hardware Maintenance Manuals, official support documentation, and other primary sources.
2. One canonical record represents one actual product model/generation; MTMs, regional SKUs, and normal configuration variants remain attributes unless evidence shows a distinct product identity.
3. Every substantive specification must be traceable to a source.
4. Conflicting evidence is preserved and marked rather than silently overwritten.
5. Unknown values remain unknown instead of being guessed.
6. Coverage indexes are summaries; canonical YAML records are the source of truth.

## Data status

Model records use the statuses defined in `agents/RESEARCH.md`:

- `stub`
- `partial`
- `researched`
- `conflicted`
- `deprecated`

A file existing does not mean the model is fully researched.

## Contributing and autonomous research

All contributors and agents must read `AGENTS.md` first. Focused guidance is under `agents/` for organization, research, schema, and validation.

Before adding a model, search existing names, slugs, aliases, machine types, MTMs, and family records to avoid duplicates. Add or update the corresponding source catalog records and coverage index in the same change.

## Validation

Run the research validator before opening a pull request:

```bash
python3 scripts/validate_research.py
```

The validator checks YAML parsing, required fields, path/slug consistency, source-reference integrity, duplicate source/model identifiers, status values, URLs, dates, and machine-type collisions.

## Research roadmap

The immediate priority is to expand outward from the current T420-T490 anchor into coherent family lineages:

- ThinkPad T Series backward into T410/T410s and earlier generations and forward through T490s/T14/T14s, then X/X1, L, E, P/W, A/R/Z, Yoga/Tablet, Edge, and historical IBM families.
- ThinkCentre M-series Tiny/SFF/Tower lineages, then Neo, Edge, AIO, Nano, and historical IBM/Lenovo systems.
- Machine-type/MTM mapping and release chronology from authoritative documentation.
- Family and generation indexes that make the full historical catalog easy to browse.

See `TODO.md` for the maintained research queue.
