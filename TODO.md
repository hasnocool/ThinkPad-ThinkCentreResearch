# Research TODO

This queue tracks high-value coverage work. Keep it aligned with `docs/coverage/` and remove or refine items as canonical records are completed.

## ThinkPad

- [x] Research the T43 generation anchor: T43 and T43p with IBM/Lenovo support and HMM sources; preserve unresolved per-model machine-type mapping instead of guessing.
- [x] Research the T60 generation anchor: T60 and T60p with authoritative Lenovo HMM and announcement sources; preserve unresolved per-model machine-type mapping instead of guessing.
- [x] Research the T61 generation anchor: T61 and T61p with authoritative Lenovo HMM and announcement sources; preserve unresolved per-model machine-type mapping instead of guessing.
- [x] Research the T400 generation anchor: T400 and T400s with authoritative Lenovo PSREF/HMM and announcement sources.
- [x] Research the T410 generation anchor: T410 and T410s with authoritative Lenovo PSREF/service identity sources.
- [x] Research the T420 generation anchor: T420 and T420s with authoritative Lenovo PSREF/service identity sources.
- [x] Research the T430 generation anchor: T430, T430s, and T430u with authoritative Lenovo PSREF/service identity sources.
- [x] Research the T440 generation anchor: T440, T440s, and T440p with authoritative Lenovo PSREF/service identity sources.
- [x] Research the T450 generation anchor: T450 and T450s with authoritative Lenovo PSREF/service identity sources.
- [x] Research the T460 generation anchor: T460, T460s, and T460p with authoritative Lenovo PSREF identity/specification sources.
- [x] Research the T470 generation anchor: T470, T470s, and T470p with authoritative Lenovo PSREF identity/specification sources.
- [ ] Resolve T43/T43p machine-type-to-canonical-model mapping from primary PSREF/product sheets; current HMM/support material provides combined pools.
- [ ] Continue T Series backward from T43/T43p into T42/T42p, T41/T41p, T40/T40p, T30, and earlier IBM-era generations while preserving historical naming and ownership transitions.
- [ ] Resolve T60/T60p machine-type-to-canonical-model mapping from primary PSREF/product sheets; the HMM currently provides a combined service-family pool only.
- [ ] Resolve T61/T61p machine-type-to-canonical-model mapping from primary PSREF/product sheets; the HMMs currently provide combined service-family pools only.
- [ ] Continue T Series forward from the researched T480s/T490 anchor: T490s, T14/T14s generations and related AMD/Intel variants.
- [ ] Resolve whether T410i/T410si, T420i/T420si, and T430i/T430si should remain aliases/configuration tiers or become distinct canonical records if primary sources establish separate hardware identities.
- [ ] Resolve whether T490 Secure Access / Healthcare Edition machine types should remain configuration variants or become a distinct canonical model record.
- [ ] Build X Series and X1 lineage, including X1 Carbon generations and X-series convertibles/tablets.
- [ ] Catalog P Series and predecessor W Series mobile workstations.
- [ ] Catalog L and E Series generations.
- [ ] Catalog A, R, Z, Edge, Yoga, Tablet, and other Lenovo-era ThinkPad families.
- [ ] Catalog IBM-era ThinkPad families using IBM manuals and archived official documentation.
- [ ] Add machine-type and MTM mappings for every canonical ThinkPad record where authoritative sources expose them.
- [ ] Add release/announcement/discontinuation chronology when directly supported by sources.

## ThinkCentre

- [ ] Expand M75q Tiny lineage across generations.
- [ ] Catalog contemporary Intel M-series Tiny systems alongside AMD equivalents.
- [ ] Catalog M-series SFF and Tower variants as separate chassis identities where appropriate.
- [ ] Catalog ThinkCentre Neo systems.
- [ ] Catalog ThinkCentre Edge systems.
- [ ] Catalog ThinkCentre AIO systems.
- [ ] Catalog Nano and other compact ThinkCentre form factors.
- [ ] Catalog historical IBM/Lenovo ThinkCentre generations.
- [ ] Add machine-type and MTM mappings for every canonical ThinkCentre record where authoritative sources expose them.
- [ ] Track optional I/O modules, PSU/adapter choices, storage layouts, expansion slots, and form-factor differences.

## Dataset and tooling

- [ ] Add structured release chronology indexes once enough dated records exist.
- [ ] Add generated family/model indexes derived from canonical YAML without making generated output the source of truth.
- [ ] Add regression fixtures for duplicate aliases/MTMs and historical identity edge cases.
- [ ] Add link-checking that distinguishes temporary network failures from confirmed dead sources.
- [ ] Add archive URLs for critical historical sources when original official URLs become unstable.
- [ ] Track coverage counts automatically from canonical records.
