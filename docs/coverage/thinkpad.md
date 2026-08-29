# ThinkPad Coverage

Last updated: 2026-08-29

## Coverage summary

| Family | Model | Status | Primary sources | Key gaps |
| --- | --- | --- | ---: | --- |
| T Series | ThinkPad T43 | researched | 2 | Exact product-wide announcement/discontinuation dates; complete MTM-to-region mapping; dimensions/weights and per-MTM T43/T43p split |
| T Series | ThinkPad T43p | researched | 2 | Exact product-wide announcement/discontinuation dates; complete MTM-to-region mapping; dimensions/weights and per-MTM T43/T43p split |
| T Series | ThinkPad T60 | researched | 2 | Resolve T60/T60p per-model machine-type split; complete MTM-to-region mapping; normalize chassis dimensions/weights and later widescreen variants from primary product sheets |
| T Series | ThinkPad T60p | researched | 2 | Resolve T60/T60p per-model machine-type split; complete MTM-to-region mapping; normalize workstation GPU/display/adapter combinations and exact launch chronology |
| T Series | ThinkPad T61 | researched | 3 | Resolve T61/T61p per-model machine-type split; complete MTM-to-region mapping; normalize chassis dimensions/weights and full panel/GPU combinations from primary product sheets |
| T Series | ThinkPad T61p | researched | 3 | Resolve T61/T61p per-model machine-type split; complete MTM-to-region mapping; normalize exact workstation display/GPU/adapter combinations and discontinuation chronology |
| T Series | ThinkPad T400 | researched | 3 | Complete MTM-to-region mapping; exact first product announcement/discontinuation dates; enumerate configuration-specific CPU/battery/adapter combinations |
| T Series | ThinkPad T400s | researched | 3 | Complete MTM-to-region mapping; discontinuation date; enumerate touch/non-touch and low-voltage CPU variants by MTM |
| T Series | ThinkPad T410 | researched | 3 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; resolve T410i identity granularity |
| T Series | ThinkPad T410s | researched | 3 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; resolve T410si identity granularity; fill exact dimensions/weight from primary PSREF sheets |
| T Series | ThinkPad T420 | researched | 2 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; resolve T420i identity granularity |
| T Series | ThinkPad T420s | researched | 2 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; resolve T420si identity granularity |
| T Series | ThinkPad T430 | researched | 2 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; resolve T430i identity granularity |
| T Series | ThinkPad T430s | researched | 2 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; resolve T430si identity granularity |
| T Series | ThinkPad T430u | researched | 2 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates; enumerate regional CPU/GPU variants |
| T Series | ThinkPad T440 | researched | 3 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates |
| T Series | ThinkPad T440p | researched | 3 | Complete MTM-to-region mapping; exact first product-wide announcement/discontinuation dates |
| T Series | ThinkPad T440s | researched | 3 | Complete MTM-to-region mapping; exact product-wide announcement/discontinuation dates |
| T Series | ThinkPad T450 | researched | 2 | Complete MTM-to-region mapping; exact announcement/discontinuation dates |
| T Series | ThinkPad T450s | researched | 2 | Complete MTM-to-region mapping; exact announcement/discontinuation dates |
| T Series | ThinkPad T460 | researched | 2 | Complete MTM-to-region mapping; exact announcement/discontinuation dates |
| T Series | ThinkPad T460p | researched | 2 | Complete MTM-to-region mapping; exact announcement/discontinuation dates |
| T Series | ThinkPad T460s | researched | 2 | Complete MTM-to-region mapping; exact announcement/discontinuation dates |
| T Series | ThinkPad T470 | researched | 2 | Complete MTM-to-region mapping; exact discontinuation date |
| T Series | ThinkPad T470p | researched | 4 | Complete MTM-to-region mapping; exact discontinuation date |
| T Series | ThinkPad T470s | researched | 3 | Complete MTM-to-region mapping; exact discontinuation date |
| T Series | ThinkPad T480 | researched | 2 | Exact launch/discontinuation dates; complete MTM-to-region mapping |
| T Series | ThinkPad T480s | researched | 3 | Complete MTM-to-region mapping; discontinuation date; validate later special-bid variants |
| T Series | ThinkPad T490 | researched | 3 | Complete MTM-to-region mapping; discontinuation date; resolve Secure Access / Healthcare Edition identity scope |

## Priority research backlog

1. Continue T Series backward from T43/T43p into T42/T42p, T41/T41p, T40/T40p, T30, and earlier IBM-era generations.
2. Resolve T43/T43p per-model machine-type mapping from primary PSREF/product sheets; current HMM/support material exposes combined pools.
3. Resolve the T60/T60p machine-type split from primary product/PSREF sources.
4. Resolve the T61/T61p machine-type split from primary product/PSREF sources.
5. Continue forward from T490 with T490s and T14/T14s generations, preserving Intel/AMD and slim-model identity boundaries.
6. Resolve T410i/T410si, T420i/T420si, and T430i/T430si alias-versus-canonical granularity.
7. Add X Series and X1 families, then L, E, P, W, A, R, Z, Edge, Yoga, Tablet, and historical IBM-era families.
8. Build explicit machine-type and MTM mappings from official service/PSREF documentation.

## Identity notes

- T43 and T43p are separate canonical identities because Lenovo documents T43p as a workstation-oriented member of the family, but the available support/HMM sources combine machine-type pools; no speculative split is made.
- IBM/Lenovo support identifies T43/T43p-era systems in machine-type groups including 1871-1876 and 2668, 2669, 2678, 2679, 2686, 2687.
- Exact dimensions/weights and product-wide chronology remain unknown where authoritative primary evidence was not available.

## Coverage rules

This table is an index only. Canonical YAML records under `data/thinkpad/models/` are the source of truth. A model is not counted as researched until major specification categories and authoritative provenance are present.
