# Research Workflow

## Objective

Grow verified coverage of ThinkPad and ThinkCentre hardware while keeping every important claim traceable and avoiding duplicate model records.

## Research unit

Work in bounded batches. Good scopes include:

- one family across several generations;
- one generation across its regional/MTM variants;
- one historical era;
- one authoritative source corpus such as a PSREF edition;
- one unresolved identity/alias cluster.

Avoid random one-field edits across unrelated product lines unless fixing validation issues.

## Source priority

Use the strongest available evidence first:

1. IBM/Lenovo PSREF documents and official specifications.
2. IBM/Lenovo Hardware Maintenance Manuals, user guides, support pages, archived official product pages, platform specifications, and parts/service references.
3. Official regulatory, certification, or component documentation.
4. Reputable archival hardware databases and established technical references.
5. Reviews, retailer pages, forums, and community wikis as secondary evidence only.

Secondary sources may help discover terminology or missing variants, but do not let a weak source silently override primary documentation.

## Source collection

For every reusable source, create or update a source catalog record containing:

- stable source ID;
- title;
- publisher/organization;
- document type;
- URL;
- access date;
- publication/revision date when known;
- official document number when known;
- archive URL when useful;
- notes about scope or reliability.

Do not store full copyrighted manuals unless redistribution is clearly allowed.

## Evidence extraction

Extract facts conservatively.

Good facts include:

- official product/model name;
- family/generation;
- release or announcement date/year;
- machine type / MTM identifiers;
- form factor/chassis;
- processor options;
- chipset/platform;
- GPU options;
- RAM technology, slots, soldered memory, and supported capacity;
- storage interfaces, slots, bays, and supported device types;
- display options for ThinkPads;
- networking and wireless options;
- ports and expansion;
- battery and adapter details for ThinkPads;
- PSU details for ThinkCentres;
- dimensions and weight;
- supported/preloaded operating systems;
- docking/expansion ecosystem;
- serviceability and notable upgrade constraints.

A source does not need to provide every field.

## Exact fact vs inference

Mark inferred relationships clearly.

Examples of inference:

- estimating release year from a review date;
- assuming two MTMs share a chassis because specifications look similar;
- inferring maximum memory from chipset limits rather than Lenovo documentation;
- assuming a region-specific SKU maps to a global model.

Do not write inferred values as unqualified facts.

## Conflicting sources

When sources disagree:

1. preserve both claims with source references;
2. identify whether the difference is regional, revision-specific, CTO-specific, or an error;
3. prefer primary Lenovo/IBM documentation when the scope matches;
4. use an explicit conflict/notes field when unresolved;
5. never delete evidence merely to make the record look clean.

## Identity and deduplication

Before creating a model record, search for:

- exact model name;
- normalized model slug;
- aliases;
- generation name;
- machine type / MTM;
- family relationships.

If a likely match exists, enrich it rather than create another record.

## Coverage status

Use honest coverage states:

- `stub` — identity exists but research is minimal;
- `partial` — useful verified specs exist but important categories remain incomplete;
- `researched` — major known specification categories and authoritative sources are represented;
- `conflicted` — unresolved source/identity conflict prevents normal completion;
- `deprecated` — record retained only for migration/history and should not receive new facts.

Do not mark a record `researched` simply because a file exists.

## Research batch checklist

Before finishing a batch:

- confirm every new model has at least one source reference;
- verify no obvious duplicate exists;
- check aliases and MTMs;
- update family relationships when applicable;
- update coverage documentation;
- ensure new source IDs resolve to source catalog records;
- ensure URLs and access dates are present;
- flag unresolved gaps/conflicts;
- run validation checks;
- inspect the final diff for accidental broad edits.

## Scheduled research behavior

For autonomous runs:

- pick the highest-value visible coverage gap;
- prefer authoritative sources not yet represented;
- finish a coherent batch before starting another;
- update an existing active research branch/PR when appropriate;
- do not create an empty/no-op PR;
- stop rather than guess when identity is ambiguous.
