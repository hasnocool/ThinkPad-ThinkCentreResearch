# Validation Rules

## Purpose

Validation protects the repository from the two largest long-term risks: duplicated product identities and unsupported specifications.

## Required checks for every research change

### 1. Repository placement

Confirm every changed file is in its canonical directory and uses lowercase kebab-case naming.

Reject:

- arbitrary model files at repository root;
- mixed ThinkPad/ThinkCentre model directories;
- temporary/scratch files;
- duplicated alternate folder structures.

### 2. YAML validity

Every `.yaml`/`.yml` data file must parse successfully.

When validation scripts exist, use a non-blocking/concurrent implementation where useful, but keep filesystem traversal deterministic and bounded.

### 3. Required identity fields

Every model record must have, at minimum:

```text
schema_version
record_type=model
product_line
canonical_name
slug
status
sources
```

Every source record must have, at minimum:

```text
schema_version
record_type=source
id
title
publisher
document_type
url
accessed
official
```

### 4. Slug/path consistency

For a model record:

```text
data/<product_line>/models/<slug>.yaml
```

The filename stem and `slug` must match.

### 5. Source-reference integrity

Every referenced source ID must resolve to exactly one source catalog record.

Flag:

- missing source IDs;
- duplicate source IDs;
- malformed URLs;
- missing access dates;
- model records with no sources.

### 6. Duplicate identity detection

Check new/modified records against the existing dataset using:

- normalized canonical name;
- slug;
- aliases;
- machine types;
- MTMs;
- family/generation relationships.

A shared MTM between two canonical records is a high-priority collision that requires investigation.

### 7. Coverage synchronization

New, renamed, merged, deprecated, or deleted model records must be reflected in the corresponding `docs/coverage/` index.

Coverage status must match the underlying evidence level.

### 8. Provenance review

Review every newly added substantive specification and ask:

- which source supports it?
- does that source actually apply to this model/MTM/region?
- is the value directly stated or inferred?
- is there conflicting evidence?

Unsupported facts must be removed, sourced, or clearly marked as inference/uncertainty.

### 9. URL/source sanity

Prefer canonical HTTPS URLs.

For critical historical documents, add an archive URL when practical, but do not replace the original URL with an archive-only citation unless the original is no longer available.

### 10. Diff quality

Before committing:

- inspect changed files;
- ensure unrelated records were not reformatted;
- ensure a bulk tool did not erase unknown/conflicting fields;
- ensure aliases/MTMs were not accidentally dropped;
- ensure no copied source text violates repository policy.

## Recommended automated validator

When the data tree exists, maintain a Python 3.12 validator under `scripts/validate_research.py` that checks at least:

- YAML parsing;
- schema-required keys;
- path/slug agreement;
- unique model slugs;
- unique source IDs;
- source-reference resolution;
- obvious duplicate MTM ownership;
- ISO date formats;
- allowed coverage status values;
- URL shape;
- duplicate aliases after normalization.

The validator should provide actionable errors containing the file path and field.

## Allowed coverage statuses

```text
stub
partial
researched
conflicted
deprecated
```

Do not add ad-hoc synonyms such as `done`, `complete-ish`, or `wip`.

## Validation failure policy

Never make a dataset appear valid by deleting conflicting evidence or weakening a rule without explanation.

If a legitimate historical edge case violates a validator rule:

1. document the case;
2. make the rule capable of representing it explicitly;
3. add a regression fixture/test when tooling exists;
4. keep the exception narrow.

## Definition of a clean research PR

A clean PR has:

- coherent research scope;
- no known duplicate canonical records;
- valid structured data;
- resolvable source references;
- updated coverage indexes;
- no unsupported claims presented as facts;
- documented unresolved conflicts;
- a concise validation summary in the PR description.
