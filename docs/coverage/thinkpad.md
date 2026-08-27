# ThinkPad Coverage

Last updated: 2026-08-27

## Coverage summary

| Family | Model | Status | Primary sources | Key gaps |
| --- | --- | --- | ---: | --- |
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

1. Continue T Series backward from the researched T410/T410s generation into T400/T400s and earlier documented generations.
2. Continue forward from T490 with T490s and T14/T14s generations, preserving Intel/AMD and slim-model identity boundaries.
3. Resolve whether T490 Secure Access / Healthcare Edition machine types should remain configuration variants or become a separate canonical identity.
4. Resolve T410i/T410si, T420i/T420si, and T430i/T430si alias-versus-canonical granularity if Lenovo documentation establishes separate hardware identities rather than processor/configuration tiers.
5. Add X Series and X1 families, starting with generations that have complete Lenovo PSREF/HMM coverage.
6. Add L, E, P, W, A, R, Z, Edge, Yoga, Tablet, and historical IBM-era families.
7. Build explicit machine-type and MTM mappings from official service/PSREF documentation.
8. Add historical IBM ThinkPad models with authoritative IBM manuals and archived product documentation.

## Identity notes

- Lenovo's October 2009 T410s/T410/T510/W510 service guide maps ThinkPad T410 to machine types 2516, 2518, 2519, 2522, 2537, 2538, and 2539.
- The same Lenovo service guide maps ThinkPad T410s to machine types 2901, 2904, 2907, 2912, 2924, 2926, and 2928.
- T410i and T410si are currently represented as aliases/configuration tiers because Lenovo PSREF/service documentation places those brands inside the same T410/T410s machine-type families; finer-grained identity remains open.
- Lenovo support explicitly maps ThinkPad T420/T420i to machine types 4177, 4178, 4179, 4180, 4236, 4237, and 4238.
- Lenovo support explicitly maps ThinkPad T420s/T420si to machine types 4170, 4171, 4172, 4173, 4174, 4175, and 4176.
- T420i and T420si are currently represented as aliases/configuration tiers because the authoritative machine-type mappings overlap the T420/T420s families; this remains open for finer-grained identity research.
- Lenovo support explicitly maps ThinkPad T430/T430i to machine types 2342, 2344, 2345, 2347, 2349, 2350, and 2351.
- Lenovo support explicitly maps ThinkPad T430s/T430si to machine types 2352 through 2358.
- Lenovo support explicitly maps ThinkPad T430u to machine types 3351, 3352, 3353, 6273, and 8614.
- T430i and T430si are currently represented as aliases/configuration tiers because the authoritative machine-type mappings overlap the T430/T430s families; this remains open for finer-grained identity research.
- Lenovo primary sources directly establish ThinkPad T440 machine types 20B6 and 20B7.
- Lenovo primary sources directly establish ThinkPad T440s machine types 20AQ and 20AR.
- Lenovo PSREF records establish ThinkPad T440p machine types 20AN and 20AW.
- Lenovo primary sources directly establish ThinkPad T450 machine types 20DJ, 20BU, and 20BV.
- Lenovo primary sources directly establish ThinkPad T450s machine types 20BW and 20BX.
- No T450p canonical record is counted without authoritative Lenovo evidence establishing such a product identity; the prior backlog wording was an era placeholder, not proof of a model.

## Coverage rules

This table is an index only. Canonical YAML records under `data/thinkpad/models/` are the source of truth. A model is not counted as researched until major specification categories and authoritative provenance are present.
