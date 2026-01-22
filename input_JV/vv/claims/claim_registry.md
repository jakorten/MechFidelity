# Claim Registry

**Paper:** Mechanical Fidelity of Infant CPR Manikins (MST Special Issue)
**Last Updated:** 2026-01-21 (Infant stiffness gap confirmed; Kent/Nysæther sources added)
**Thesis:** Data-driven reference model enables objective evaluation of infant manikin fidelity

**Scope:** Infant ventilation (primary, with fidelity index) + Infant compression (secondary, descriptive) — per DR-001 rev.

---

## Coverage Summary

| Priority | Total | Verified | Needs Evidence | Coverage |
|----------|-------|----------|----------------|----------|
| P0 | 11 | 7 | 4 | 64% |
| P1 | 9 | 6 | 3 | 67% |
| P2 | 1 | 0 | 1 | 0% |
| **Total** | **21** | **13** | **8** | **62%** |

**Target:** >=85% overall, 100% P0

**Note:** Ventilation claims evaluated against human reference (fidelity index); Compression claims descriptive only (no human reference for infants)

---

## Claim Registry (Section-Ordered)

### Section 1: Introduction

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| I1 | Mechanical fidelity concept links to perspective paper | P1 | Proposition paper | [ ] |
| I2 | No systematic benchmark exists for infant manikin ventilation | P0 | Literature gap | [x] VERIFIED: Reiss 2015 calls for manikin C/R characterization but none exists; Thielen 2017: "even SimMan 3G and Apollo do not fulfil all requirements" |
| I3 | First data-driven reference model for infant manikin ventilation | P0 | Novelty claim | [x] VERIFIED: No infant manikin ventilation benchmark found in literature |
| I4 | Force application profile affects outcomes independently of depth | P1 | O'Reilly 2024 | [x] VERIFIED: Piglet model (n=12): machine CC at 32% depth > human CC at 38% depth for stroke volume and LV contractility |
| I5 | Classical manikins have linear F-D; humans have nonlinear F-D | P1 | Thielen 2017, Tomlinson 2007 | [x] VERIFIED: Thielen: manikins have only k₂≠0, humans have k₂,k₃,k₄≠0; Tomlinson: progressivity 1.41±0.25 |

### Section 2: Human Reference Model -- Infant Ventilation Mechanics

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| V1 | Infant compliance ~78 mL/kPa (1-24 wks) to ~171 mL/kPa (73-96 wks) | P0 | Huang 2016 | [x] VERIFIED: Table 2, n=205, 77.95±46.16 to 170.58±50.14 mL/kPa |
| V2 | Infant resistance ~6.4 kPa/L/s (1-24 wks) to ~3.7 kPa/L/s (73-96 wks) | P0 | Huang 2016 | [x] VERIFIED: Table 2, n=205, median 6.39 to 3.74 kPa/L/s |
| V3 | Infant chest wall 3× more compliant than lungs (Ccw/CL ≈ 3:1) | P1 | Stoecklin 2024, Diedericks 2025 | [x] VERIFIED: Stoecklin 2024 (n=23): Ccw/kg 3.0 vs CL/kg 0.95; Diedericks 2025 (FASEB review): "CCW ~3× CL in term, ~5× in preterm" |

### Section 3: Uncertainty Envelope

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| U1 | Human data shows natural variability requiring range-based model | P1 | Inference | [ ] |
| U2 | Manikins within envelope = adequate mechanical fidelity | P1 | Definition | [ ] |

### Section 4: Manikin Characterization Protocol

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| M1 | Protocol based on IEEE TIM methodology | P0 | [OWN WORK] | [ ] |
| M2 | Multiple infant manikin models tested | P0 | [OWN DATA] | [ ] |
| M3 | Unit-to-unit variation assessed | P1 | [OWN DATA] | [ ] |

### Section 5a: Results -- Ventilation Fidelity

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| RV1 | Manikin compliance values (to be measured) | P0 | [OWN DATA] | [ ] |
| RV2 | Manikin resistance values (to be measured) | P0 | [OWN DATA] | [ ] |
| RV3 | Deviation from human reference (to be calculated) | P0 | [OWN DATA] | [ ] |

### Section 5b: Results -- Compression Characterization (Descriptive)

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| RC1 | Infant manikin stiffness values (to be measured) | P0 | [OWN DATA] | [ ] |
| RC2 | Infant manikin force-displacement curves (to be measured) | P0 | [OWN DATA] | [ ] |
| RC3 | Comparison between manikin models (no human reference) | P1 | [OWN DATA] | [ ] |

**Note:** No human reference exists for infant chest compression mechanics. RC1-RC3 are descriptive characterization only.

### Section 5c: Human Reference Model -- Infant Compression (Literature Gap)

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| C5 | Infant chest compression stiffness (N/mm) does not exist in published literature | P0 | Kent 2010, Kent 2009, Nysæther 2009 | [x] VERIFIED: Kent 2010: "No experimental data exist"; youngest data is 6-7yo (Kent 2012); expert consensus reached but N/mm values unpublished (Nysæther 2009) |
| C6 | Youngest published chest stiffness data is 6-7 years old (not infant) | P1 | Kent 2009, Kent 2012 | [x] VERIFIED: Kent 2009 n=18 ages 8-22yo (309±55N at 39±5mm); Kent 2012 PMHS ages 6-7yo |
| C7 | Infant compression depth varies with age (2.7 cm at 0-2 mo) | P1 | Ikeyama 2024 (n=555) | [x] VERIFIED: 0-2mo: 2.7cm, 49% over-compressed at 4cm target |
| C8 | Scaling adult chest data to pediatric does not work | P1 | Kent 2010 | [x] VERIFIED: "Scaling...did not successfully predict the pediatric behavior" |

### Section 6: Mechanical Fidelity Index

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| EF1 | Ventilation fidelity score formula | P1 | [OWN WORK] | [ ] |
| EF2 | Index enables procurement decisions | P2 | Inference | [ ] |

### Section 7: Discussion

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| D1 | First systematic infant manikin ventilation benchmark | P0 | Novelty claim | [x] VERIFIED: No multi-manikin infant ventilation benchmark found |
| D2 | Addresses gap identified by Reiss 2015 | P0 | Literature gap | [x] VERIFIED: Reiss 2015 explicitly calls for manikin C/R characterization |
| D3 | First systematic infant manikin compression characterization | P1 | Novelty claim | [ ] |
| D4 | Compression data enables future validation when human reference available | P2 | Future work | [ ] |

---

## Out of Scope (per DR-001)

The following claims were verified but excluded due to infant-only focus. Preserved here for future reference:

### Adult Compression Claims (Verified but Excluded)

| ID | Claim | Source | Verification |
|----|-------|--------|--------------|
| C1 | Adult chest stiffness 3-11 N/mm | Nysæther 2008 (n=59) | [x] Mean 270±150 N at 38mm → ~7 N/mm avg |
| C2 | Adult chest damping ~0.17 N·s/mm | Nysæther 2008 (n=59) | [x] 169±60 N·s/m |
| C3 | Force-displacement is non-linear | Tomlinson 2007 (n=91) | [x] Progressivity factor 1.41±0.25 |
| C4 | Stiffness decreases ~35% after 3000 compressions | Ruiz de Gauna 2023 (n=615) | [x] 34.6% (95% CI 33.0-36.1) |

**Reason excluded:** Only infant manikins available; adult manikins not in scope.

### Source Locations (for reference)

| Source | File |
|--------|------|
| Nysæther 2008 | `/research/articles/md_out/Manikins_With_Human_Like_Chest_Propertie.md` |
| Ikeyama 2024 | `input_JV/literature/pdfs/ikeyama_2024_infant_cc_depth.pdf` |
| Diedericks 2025 | `input_JV/literature/pdfs/diedericks_2025_chest_wall.pdf` |
| O'Reilly 2024 | `input_JV/literature/pdfs/oreilly_2024_machine_vs_human_cc.pdf` |
| Thielen 2017 | `input_JV/literature/pdfs/thielen_2017_humanlike_thorax.pdf` |
| Kent 2009 | PMID 19085159 (Stapp Car Crash J) |
| Kent 2010 | PMID 20058561 (Stapp Car Crash J) |
| Kent 2012 | PMID 22931180 (Traffic Inj Prev) |
| Nysæther 2009 | PMID 19699023 (Resuscitation) |

---

## Priority Guide

### P0 (Critical) -- Must be 100% verified

These claims, if wrong, break the paper:

| ID | Risk if Wrong |
|----|---------------|
| V1-V2 | Human reference model invalid |
| I2-I3, D1-D2 | Novelty claim challenged |
| RV1-RV3 | Ventilation results invalid |
| RC1-RC2 | Compression results invalid |
| M1-M2 | Protocol credibility lost |
| C5 | Infant compression gap claim challenged |

### P1 (Important) -- Target 90%

Strengthen but don't break argument:
- I4: Force profile importance (supports mechanical fidelity concept)
- I5: Linear vs nonlinear F-D gap (supports mechanical fidelity concept)
- V3: Chest wall compliance context
- U1-U2: Envelope methodology
- M3: Variation analysis
- EF1: Fidelity formula
- C6: Youngest stiffness data is 6-7yo (strengthens C5)
- C7: Infant compression depth varies with age
- C8: Adult-to-pediatric scaling doesn't work
- RC3: Manikin comparison
- D3: Compression novelty

### P2 (Supporting) -- Target 70%

Nice to have:
- EF2: Procurement implication
- D4: Future work

---

## Source Verification Checklist

### Literature Sources (verify exact values)

| Source | Claims | What to Check | Status |
|--------|--------|---------------|--------|
| Huang 2016 | V1, V2 | Infant compliance 78-171 mL/kPa, resistance 3.7-6.4 kPa/L/s (n=205) | [x] VERIFIED |
| Stoecklin 2024 | V3 | Preterm Ccw/CL ratio ~3:1 | [x] VERIFIED |
| Diedericks 2025 | V3 | Review: CCW ~3× CL term, ~5× preterm | [x] VERIFIED |
| Reiss 2015 | I2, D2 | Call for manikin C/R characterization | [x] VERIFIED |
| O'Reilly 2024 | I4, C5 | Force profile > depth (piglet n=12); used animal model due to human data gap | [x] VERIFIED |
| Thielen 2017 | I2, I5 | SimMan/Apollo inadequate; classical manikins linear vs human nonlinear F-D | [x] VERIFIED |
| Kent 2009 | C5, C6 | CPR-based F-D ages 8-22yo: 309±55N at 39±5mm (n=18) | [x] VERIFIED |
| Kent 2010 | C5, C8 | "No experimental data exist"; scaling doesn't work | [x] VERIFIED |
| Kent 2012 | C6 | PMHS response targets ages 6-7yo | [x] VERIFIED |
| Nysæther 2009 | C5 | Expert consensus on infant stiffness but N/mm unpublished | [x] VERIFIED |

### Own Data (verify data files exist and analysis correct)

| Data Source | Claims | What to Check |
|-------------|--------|---------------|
| Ventilation tests | RV1, RV2, RV3 | Data files exist, analysis reproducible |
| Compression tests | RC1, RC2, RC3 | Data files exist, analysis reproducible |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| [ ] | Not yet verified |
| [~] | In progress |
| [x] | Verified |
| [!] | Problem -- needs attention |

---

*Registry created: 2026-01-15*
*Scope change: 2026-01-15 — Infant ventilation focus (DR-001)*
*Scope revision: 2026-01-16 — Added infant compression (descriptive) per DR-001 rev.*
*Updated: 2026-01-21 — Added I4, I5, C5 (P0), C6, C8 from literature search; infant stiffness gap definitively confirmed*
*Current: 13/21 claims verified (62%), 7/11 P0 verified (64%)*
*Remaining P0: M1, M2 (own work), RV1-RV3, RC1-RC2 (own data - pending experiments)*
