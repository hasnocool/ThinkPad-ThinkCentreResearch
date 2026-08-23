# Canonical Research Schema

## Format

Use YAML for canonical structured records. Keep key ordering generally consistent so diffs remain readable.

Unknown information should normally be omitted or represented as `null` only when an explicit unknown value is meaningful. Never use guessed placeholders.

Dates should use ISO 8601 when known:

```yaml
release_date: 2018-01-03
source_accessed: 2026-08-22
```

A year-only value may be used when the exact date cannot be verified:

```yaml
release_year: 2018
```

## Model record

Recommended shape:

```yaml
schema_version: 1
record_type: model
product_line: thinkpad
canonical_name: ThinkPad T480
slug: thinkpad-t480
family: t-series
generation: null
status: partial

identity:
  manufacturer: Lenovo
  predecessor: ThinkPad T470
  successor: ThinkPad T490
  aliases: []
  machine_types: []
  mtms: []
  regions: []

release:
  announcement_date: null
  release_date: null
  release_year: 2018
  discontinued_date: null

form_factor:
  class: laptop
  chassis: null
  dimensions_mm: null
  starting_weight_kg: null

platform:
  chipset: null
  cpu_options: []
  gpu_options: []

memory:
  technology: null
  slots: null
  soldered: null
  official_max_gb: null
  observed_max_gb: null

storage:
  interfaces: []
  bays: []
  slots: []

display:
  options: []

networking:
  ethernet: []
  wlan: []
  wwan: []
  bluetooth: []

ports: []
expansion: []

power:
  adapters: []
  batteries: []
  psu: []

software:
  operating_systems: []

serviceability:
  replaceable_components: []
  upgrade_notes: []
  limitations: []

sources: []
conflicts: []
notes: []
last_verified: null
```

Remove irrelevant sections rather than forcing empty data into every record. For example, ThinkCentre desktop records usually do not need a `display` section.

## ThinkPad-specific fields

Where known, capture:

- internal/removable battery configuration;
- battery capacity options in Wh;
- charging connector and supported adapters;
- display size, resolution, panel technology, brightness, touch support, and color gamut when sourced;
- docking connector or USB-C/Thunderbolt docking support;
- keyboard/backlight options;
- WWAN antenna/readiness distinctions when documented.

## ThinkCentre-specific fields

Where known, capture:

- chassis/form factor such as Tiny, SFF, Tower, Nano, AIO;
- internal PSU wattage/rating;
- external adapter wattage for Tiny/Nano systems;
- PCIe slot layout;
- M.2 slot/key usage;
- drive bays;
- riser requirements;
- optional serial/parallel/display modules;
- vPro/management platform options when documented.

## Variant representation

Use structured variants when a specification changes by MTM, region, chassis option, or configuration.

Example:

```yaml
platform:
  cpu_options:
    - value: Intel Core i5-8250U
      source_ids: [lenovo-psref-t480-2018]
    - value: Intel Core i7-8650U
      source_ids: [lenovo-psref-t480-2018]
```

If the difference is substantial enough to create a distinct official product identity, create a separate canonical model record and link the records.

## Provenance on claims

Whenever practical, attach source IDs directly to structured claims.

Preferred:

```yaml
memory:
  technology: DDR4-2400
  source_ids:
    - lenovo-psref-t480-2018
```

For complex or conflicting claims:

```yaml
conflicts:
  - field: memory.official_max_gb
    claims:
      - value: 32
        source_ids: [lenovo-psref-example]
      - value: 64
        source_ids: [lenovo-support-example]
    status: unresolved
    note: Source scopes may differ; requires MTM-level verification.
```

## Source catalog record

Recommended shape:

```yaml
schema_version: 1
record_type: source
id: lenovo-psref-t480-2018
title: ThinkPad T480 Platform Specifications
publisher: Lenovo
document_type: psref
url: https://example.invalid/
archive_url: null
document_id: null
publication_date: null
revision_date: null
accessed: 2026-08-22
official: true
scope:
  product_lines: [thinkpad]
  models: [ThinkPad T480]
notes: []
```

Source IDs must be stable and unique.

## Family record

Recommended shape:

```yaml
schema_version: 1
record_type: family
product_line: thinkpad
name: T Series
slug: t-series
status: partial
models: []
predecessor: null
successor: null
sources: []
notes: []
last_verified: null
```

Family records should describe relationships, not replicate the full specifications of every member.

## Coverage metadata

Human-readable coverage documents live in `docs/coverage/`, but automated tooling may later maintain structured coverage metadata.

When added, use fields such as:

```yaml
canonical_name: ThinkPad T480
slug: thinkpad-t480
status: researched
primary_sources: 2
secondary_sources: 1
last_verified: 2026-08-22
open_gaps:
  - exact discontinuation date
```

## Stable identifiers

Do not change a canonical slug merely for cosmetic reasons. Renames require updating every reference in the same change.

MTMs and machine types are identifiers associated with the product; they are not substitutes for the stable repository slug.

## Schema evolution

When schema changes are needed:

1. update this document;
2. increment `schema_version` only for meaningful compatibility changes;
3. update validation tooling if present;
4. migrate affected records consistently;
5. do not leave old/new schemas mixed without an explicit migration plan.
