# ThinkPad Coverage

Last updated: 2026-08-28

## Coverage summary

| Family | Model | Status | Primary sources | Key gaps |
| --- | --- | --- | ---: | --- |
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

1. Continue T Series backward into T43/T43p and earlier IBM-era systems using IBM/Lenovo withdrawn PSREF books, HMMs, and archived official product literature.
2. Resolve the T60/T60p machine-type split from primary product/PSREF sources; the current Lenovo HMM exposes a combined service-family pool and is not sufficient to assign every MT safely.
3. Resolve the T61/T61p machine-type split from primary product/PSREF sources; current Lenovo HMMs expose combined service-family pools and are not sufficient to assign every MT safely.
4. Continue forward from T490 with T490s and T14/T14s generations, preserving Intel/AMD and slim-model identity boundaries.
5. Resolve whether T490 Secure Access / Healthcare Edition machine types should remain configuration variants or become a separate canonical identity.
6. Resolve T410i/T410si, T420i/T420si, and T430i/T430si alias-versus-canonical granularity if Lenovo documentation establishes separate hardware identities rather than processor/configuration tiers.
7. Add X Series and X1 families, starting with generations that have complete Lenovo PSREF/HMM coverage.
8. Add L, E, P, W, A, R, Z, Edge, Yoga, Tablet, and historical IBM-era families.
9. Build explicit machine-type and MTM mappings from official service/PSREF documentation.

## Identity notes

- Lenovo's January 5, 2006 T60 Series announcement establishes the T60 generation and documents Intel Centrino Duo and WWAN-capable configurations.
- Lenovo's January 2007 T60/T60p HMM covers machine types 1951, 1952, 1953, 1954, 1955, 1956, 2007, 2008, 2009, 2613, 2623, and 2637 as a combined service family.
- That combined HMM pool is intentionally not split between T60 and T60p canonical records until primary PSREF/product evidence establishes the per-model mapping.
- Lenovo explicitly identifies T60p as a mobile workstation in its August 15, 2006 Linux-workstation announcement, supporting a separate canonical identity despite shared service documentation.
- Lenovo announced the first ThinkPad T61 14.1-inch widescreen notebook on May 9, 2007.
- Lenovo separately unveiled the ThinkPad T61p 15.4-inch widescreen mobile workstation on July 10, 2007, explicitly positioning it as a workstation and documenting NVIDIA Quadro FX 570M graphics.
- Lenovo's 14.1-inch T61/T61p HMM covers machine types 8889, 8890, 8891, 8892, 8893, 8894, 8895, 8896, 8897, 8898, 8899, 8900, 8938, and 8939 as a combined service family.
- Lenovo's 15.4-inch widescreen T61/T61p HMM covers machine types 6463, 6464, 6465, 6466, 6467, 6468, 6471, 6457, 6458, 6459, 6460, 6461, 6462, and 6470 as a combined service family.
- Those HMM machine-type pools are intentionally not split between canonical T61 and T61p records until primary product/PSREF evidence establishes the per-model mapping.
- Lenovo's September 2009 T400/R400 HMM maps ThinkPad T400 to machine types 2764, 2765, 2766, 2767, 2768, 2769, 2773, 6473, 6474, 6475, 7417, 7420, 7425, and 7434.
- Lenovo's October 2009 T400s HMM maps ThinkPad T400s to machine types 2801, 2808, 2809, 2815, 2823, 2824, and 2825.
- T400s is represented separately from T400 because Lenovo documents a distinct slim chassis, distinct service architecture, a separate June 23, 2009 announcement, and a non-overlapping machine-type range.
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
