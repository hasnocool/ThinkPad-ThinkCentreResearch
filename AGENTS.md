# AGENTS.md

## Mission

Build and maintain a provenance-first, deduplicated research repository covering as many IBM/Lenovo ThinkPad and ThinkCentre models and meaningful variants as can be verified.

The repository is a research dataset first and prose documentation second. Agents must optimize for correctness, traceability, consistent organization, and incremental coverage.

## Instruction priority

1. Follow this root `AGENTS.md` for every task.
2. Follow the focused guides in `agents/` for organization, research, schema, and validation.
3. Follow more-specific `AGENTS.md` files if they are later added inside subdirectories.
4. Never create a parallel directory layout just because a new source uses different terminology.

## Before every task

Before changing files, answer these questions from the repository state:

1. What model family, generation, machine type, or source is this task about?
2. Does a canonical record already exist?
3. Is the apparent new model actually an alias, regional name, machine-type variant, refresh, or CTO configuration?
4. Which primary sources are available?
5. Which existing files must be enriched instead of duplicated?
6. Does the incoming information fit the canonical schema?
7. Are any claims conflicting, uncertain, or inferred?
8. Which indexes or coverage files must change with the record?
9. Can the changes be validated mechanically or by cross-checking sources?
10. Is every substantive claim traceable to a source?

If these questions cannot be answered, research first. Do not guess.

## Canonical repository layout

Use this structure unless a later migration deliberately replaces it:

```text
.
├── AGENTS.md
├── README.md
├── agents/
│   ├── README.md
│   ├── ORGANIZATION.md
│   ├── RESEARCH.md
│   ├── SCHEMA.md
│   └── VALIDATION.md
├── data/
│   ├── thinkpad/
│   │   ├── families/
│   │   └── models/
│   └── thinkcentre/
│       ├── families/
│       └── models/
├── docs/
│   ├── coverage/
│   ├── methodology/
│   └── references/
├── sources/
│   ├── catalog/
│   └── notes/
└── scripts/
```

Do not store downloaded copyrighted manuals in the repository unless redistribution is clearly permitted. Prefer source metadata and URLs.

## Canonical data rules

- One canonical model record per actual product model/generation.
- Machine Type Model (MTM) values, regional SKUs, CTO configurations, aliases, and marketing-name variations belong inside the canonical record unless they represent a genuinely different product.
- Family-level facts belong in `data/<product>/families/`; model-specific facts belong in `data/<product>/models/`.
- ThinkPad and ThinkCentre are separate top-level product namespaces.
- Use lowercase kebab-case filenames.
- Prefer stable model slugs that do not encode transient details such as a CPU SKU.
- Never silently overwrite conflicting specifications. Preserve both claims with provenance and mark the conflict.
- Unknown is valid. Invented data is not.

## Source policy

Prefer sources in this order:

1. IBM/Lenovo PSREF and official product specifications.
2. IBM/Lenovo Hardware Maintenance Manuals, user guides, platform specifications, support pages, and archived official pages.
3. Regulatory filings and official component/service documentation.
4. Reputable archival databases and established technical references.
5. Retailer listings, reviews, forums, and community wikis only as secondary evidence.

Every source entry must include enough information to identify what was consulted and when. See `agents/RESEARCH.md` and `agents/SCHEMA.md`.

## Required provenance behavior

- Attribute every substantive model specification to one or more sources.
- Record source URL and access date.
- Where possible, record document title, publisher, publication/revision date, and document identifier.
- Distinguish exact source statements from agent inference.
- Never convert an inference into a factual field without evidence.
- When sources disagree, record the disagreement instead of choosing silently.

## Organization rules

- Enrich existing canonical files before adding new files.
- Search filenames, aliases, MTM identifiers, family names, and model names before creating a record.
- Update relevant indexes/coverage summaries whenever canonical records are added, renamed, merged, or retired.
- Keep source notes separate from normalized model data.
- Avoid giant catch-all Markdown files containing unrelated models.
- Do not create files named `misc`, `new`, `temp`, `notes2`, or similarly ambiguous buckets.
- Temporary working files must not be committed.

## Research workflow

For every research batch:

1. Inspect current repository coverage.
2. Choose a bounded family, generation, era, or source corpus.
3. Find authoritative sources.
4. Create/update source catalog entries.
5. Extract verifiable facts.
6. Resolve identity and duplicate questions.
7. Update canonical model/family records.
8. Update coverage/index documentation.
9. Run validation described in `agents/VALIDATION.md`.
10. Review the diff for unsupported claims and accidental duplication.

## Change discipline

Keep commits focused. A research commit should describe what coverage changed, not merely say "update data".

Examples:

- `research: add ThinkPad T480 platform variants`
- `research: catalog ThinkCentre M75q Gen 2 sources`
- `data: merge duplicate ThinkPad X1 Carbon Gen 6 records`
- `docs: update ThinkCentre Tiny coverage index`

Do not mix broad formatting churn with research additions.

## Pull-request expectations

When work is performed on a branch, the PR should state:

- scope of models/families researched;
- authoritative sources added;
- canonical records created/updated/merged;
- unresolved conflicts or gaps;
- validation performed.

Do not automatically merge research PRs unless the user explicitly requests it.

## Autonomous/scheduled-agent behavior

Scheduled research should make meaningful, reviewable progress rather than generate noise.

- Prefer filling an identified coverage gap over randomly touching already complete files.
- Do not open an empty/no-op PR.
- Do not create a second PR for the same active research scope when an existing PR can be updated safely.
- Stop and document a conflict if source evidence is insufficient to resolve product identity.
- Keep coverage metrics honest; a stub is not a fully researched model.

## Definition of done

A new canonical model is done only when:

- identity is unambiguous enough to avoid a likely duplicate;
- at least one authoritative source supports the record, when such a source can be found;
- source metadata/provenance is present;
- core known specifications fit the canonical schema;
- unknown fields remain explicitly unknown/omitted rather than guessed;
- aliases/MTMs are represented where known;
- relevant coverage/index files are updated;
- validation passes or documented exceptions explain why it cannot.
