# Repository Organization

## Goal

Keep a very large historical hardware dataset navigable as coverage grows across decades of ThinkPad and ThinkCentre products.

## Canonical paths

```text
data/thinkpad/families/<family-slug>.yaml
data/thinkpad/models/<model-slug>.yaml
data/thinkcentre/families/<family-slug>.yaml
data/thinkcentre/models/<model-slug>.yaml
sources/catalog/<source-slug>.yaml
sources/notes/<source-slug>.md
docs/coverage/thinkpad.md
docs/coverage/thinkcentre.md
docs/methodology/*.md
docs/references/*.md
scripts/*.py
```

Use YAML for normalized research data and Markdown for explanation, methodology, source notes, and human-readable coverage summaries.

## File naming

Use lowercase kebab-case.

Examples:

```text
thinkpad-t480.yaml
thinkpad-x1-carbon-gen-6.yaml
thinkcentre-m75q-gen-2.yaml
thinkcentre-m920-tiny.yaml
```

Do not encode CPU, RAM, storage, region, operating system, or retailer SKU into the canonical filename unless that distinction is part of the official model identity.

## Product identity

Treat these as attributes of a canonical product record, not automatically as separate records:

- MTM / machine type and model numbers;
- region-specific SKUs;
- CTO configurations;
- processor bins;
- storage/RAM combinations;
- operating-system preload;
- color variations;
- minor wireless-card substitutions;
- reseller naming differences.

Create separate records when evidence indicates a genuinely distinct generation, chassis/platform, officially distinct model, or materially different system marketed as its own product.

## Family records

Family files summarize relationships shared across several canonical models. They should contain only facts that actually apply across the described family scope.

Good candidates:

- naming lineage;
- generation map;
- shared platform/chassis relationships;
- predecessor/successor links;
- product-positioning notes;
- known model list;
- family-level source references.

Do not duplicate all model specifications into the family record.

## Model records

A model file is the canonical home for normalized specifications and identity metadata for one product model/generation.

When adding information:

1. search by canonical name;
2. search by common aliases;
3. search by MTM/machine type;
4. search the relevant family file;
5. update an existing model when it is the same product.

## Source catalog

Every reusable source should have a catalog record in `sources/catalog/`.

The model files should reference source IDs instead of repeating full bibliographic metadata everywhere.

Use `sources/notes/` only when a source requires extraction notes, page mappings, ambiguity notes, archived-link notes, or interpretation details.

## Coverage documents

Coverage documents are human-readable indexes, not the source of truth.

They should make it easy to see:

- researched families/models;
- partial/stub records;
- missing generations;
- unresolved identity questions;
- priority research gaps.

A model record is authoritative over a coverage table if the two disagree; fix the coverage table in the same change.

## Duplicate handling

When duplicates are discovered:

1. determine the canonical identity using authoritative sources;
2. merge unique sourced facts into the canonical record;
3. preserve aliases and MTMs;
4. update references/indexes;
5. delete the duplicate only after useful provenance has been retained;
6. mention the merge in the commit/PR summary.

Never keep duplicate records merely because their filenames were created by different research runs.

## Temporary research

Do not commit scratch downloads, generated HTML, browser dumps, PDFs of uncertain redistribution status, or arbitrary temporary files.

If temporary artifacts are needed for extraction, keep them outside the repository or ensure they are ignored.

## Adding a new category

If genuinely new information cannot fit this structure:

1. explain why existing locations are inadequate;
2. extend `AGENTS.md` and this guide;
3. define the schema in `SCHEMA.md`;
4. migrate related records consistently;
5. avoid leaving two competing conventions.
