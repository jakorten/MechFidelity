# Claim Registry

**Paper:** Engineering Fidelity of CPR Training Manikins (MST Special Issue)
**Last Updated:** 2026-01-15 (C5 verified)
**Thesis:** Data-driven reference model enables objective manikin evaluation and quantification of the engineering fidelity gap

---

## Coverage Summary

| Priority | Total | Verified | Needs Evidence | Coverage |
|----------|-------|----------|----------------|----------|
| P0 | 13 | 9 | 4 | 69% |
| P1 | 7 | 1 | 6 | 14% |
| P2 | 1 | 0 | 1 | 0% |
| **Total** | **21** | **10** | **11** | **48%** |

**Target:** >=85% overall, 100% P0

**Last verification:** I2, I3, D1, D2 (2026-01-15) — Novelty claims verified via literature search

---

## Claim Registry (Section-Ordered)

### Section 1: Introduction

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| I1 | Engineering fidelity concept links to perspective paper | P1 | Proposition paper | [ ] |
| I2 | No systematic benchmark exists for manikin mechanical properties | P0 | Literature gap | [x] VERIFIED: Only Baubin 1995 (30y old, no human ref). Recent work (Lim 2024, Morin 2024) develops single manikins, not benchmarks |
| I3 | First data-driven reference model for compressions AND ventilations | P0 | Novelty claim | [x] VERIFIED: No combined compression+ventilation reference model found in literature |

### Section 2: Human Reference Model -- Compression Mechanics

#### 2.1 Adults

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| C1 | Adult chest stiffness ~3-11 N/mm (human), 5.3-13.6 N/mm (manikin range) | P0 | Nysæther 2008 (human), Lim 2024 (manikin) | [x] VERIFIED: Nysæther n=59: mean 270±150 N at 38mm → ~7 N/mm avg. Lim manikin: 5.34-13.59 N/mm |
| C2 | Adult chest damping ~0.17 N·s/mm (human), 0.13-0.51 N·s/mm (manikin range) | P0 | Nysæther 2008 (human), Lim 2024 (manikin) | [x] VERIFIED: Nysæther n=59: 169±60 N·s/m. Lim manikin: 0.127-0.511 N·s/mm |
| C3 | Force-displacement relationship is non-linear (human) | P0 | Tomlinson 2007 | [x] VERIFIED: "strong non-linear relationship" (n=91), progressivity factor 1.41±0.25 |
| C4 | Chest stiffness decreases ~35% after 3000 compressions | P1 | Ruiz de Gauna 2023 | [x] VERIFIED: 34.6% decrease (95% CI 33.0-36.1), n=615, 1.15M compressions |

#### 2.2 Infants/Pediatrics

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| C5 | Infant chest mechanical properties are largely uncharacterized | P0 | Literature gap | [x] VERIFIED: Babic 2017 "Little research has been performed to evaluate the force required in younger infants" — authors used scaled adult data |
| C6 | Infant compliance differs from adults | P1 | Papastamelos 1995 | [ ] |

### Section 2: Human Reference Model -- Ventilation Mechanics

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| V1 | Infant compliance ~78 mL/kPa (1-24 wks) to ~171 mL/kPa (73-96 wks) | P0 | Huang 2016 | [x] VERIFIED: Table 2, n=205, 77.95±46.16 to 170.58±50.14 mL/kPa |
| V2 | Infant resistance ~6.4 kPa/L/s (1-24 wks) to ~3.7 kPa/L/s (73-96 wks) | P0 | Huang 2016 | [x] VERIFIED: Table 2, n=205, median 6.39 to 3.74 kPa/L/s |

### Section 3: Uncertainty Envelope

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| U1 | Human data shows natural variability requiring range-based model | P1 | Inference | [ ] |
| U2 | Manikins within envelope = adequate engineering fidelity | P1 | Definition | [ ] |

### Section 4: Manikin Characterization Protocol

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| M1 | Protocol based on IEEE TIM methodology | P0 | [OWN WORK] | [ ] |
| M2 | Multiple manufacturers tested | P0 | [OWN DATA] | [ ] |
| M3 | Unit-to-unit variation assessed | P1 | [OWN DATA] | [ ] |

### Section 5: Results -- Compression Fidelity

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| RC1 | Manikin stiffness values (to be measured) | P0 | [OWN DATA] | [ ] |
| RC2 | Deviation from human reference (to be calculated) | P0 | [OWN DATA] | [ ] |

### Section 5: Results -- Ventilation Fidelity

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| RV1 | Manikin compliance values (to be measured) | P0 | [OWN DATA] | [ ] |
| RV2 | Manikin resistance values (to be measured) | P0 | [OWN DATA] | [ ] |
| RV3 | Deviation from human reference (to be calculated) | P0 | [OWN DATA] | [ ] |

### Section 6: Engineering Fidelity Index

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| EF1 | Compression fidelity score formula | P1 | [OWN WORK] | [ ] |
| EF2 | Ventilation fidelity score formula | P1 | [OWN WORK] | [ ] |
| EF3 | Combined index enables procurement decisions | P2 | Inference | [ ] |

### Section 7: Discussion

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| D1 | First systematic multi-manikin benchmark | P0 | Novelty claim | [x] VERIFIED: No multi-manikin benchmark against human reference found |
| D2 | Ventilation fidelity is novel contribution | P0 | Literature gap | [x] VERIFIED: Reiss 2015 calls for manikin C/R characterization but none exists |

---

## Priority Guide

### P0 (Critical) -- Must be 100% verified

These claims, if wrong, break the paper:

| ID | Risk if Wrong |
|----|---------------|
| C1-C3 | Human reference model invalid |
| V1-V2 | Ventilation reference invalid |
| RC1-RC2, RV1-RV3 | Core results invalid |
| D1-D2 | Novelty claim challenged |

### P1 (Important) -- Target 90%

Strengthen but don't break argument:
- C4: Dynamic changes angle
- U1-U2: Envelope methodology
- M3: Variation analysis

### P2 (Supporting) -- Target 70%

Nice to have:
- EF3: Procurement implication

---

## Source Verification Checklist

### Literature Sources (verify exact values)

| Source | Claims | What to Check | Status |
|--------|--------|---------------|--------|
| Nysæther 2008 | C1, C2 | Human chest stiffness/damping (n=59 OHCA patients) | [x] VERIFIED: Primary source for human values |
| Lim 2024 | C1, C2 | Manikin system range 5.34-13.59 N/mm, 0.127-0.511 N·s/mm | [x] VERIFIED: Manikin design, cites Nysæther for human ref |
| Tomlinson 2007 | C3 | Non-linear force-displacement (n=91) | [x] VERIFIED: Progressivity factor 1.41±0.25 |
| Ruiz de Gauna 2023 | C4 | 34.6% stiffness decrease (n=615, 1.15M compressions) | [x] VERIFIED |
| Huang 2016 | V1, V2 | Infant compliance 78-171 mL/kPa, resistance 3.7-6.4 kPa/L/s (n=205) | [x] VERIFIED |
| Babic 2017 | C5 | Infant data gap -- "Little research has been performed..." | [x] VERIFIED |
| Thielen 2017 | C5 | Anatomical approach, no human validation | [x] VERIFIED |
| Morin 2024 | -- | Adult ventilation reference: compliance 37-40 mL/cmH₂O, resistance 20 cmH₂O·s/L | [x] NEW: SAM manikin validation paper |

### Own Data (verify data files exist and analysis correct)

| Data Source | Claims | What to Check |
|-------------|--------|---------------|
| Compression tests | RC1, RC2 | Data files exist, analysis reproducible |
| Ventilation tests | RV1, RV2, RV3 | Data files exist, analysis reproducible |

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
*Last update: 2026-01-15 — All verifiable literature claims verified (10/21 claims, 48%)*
*Remaining P0: M1, M2 (own work), RC1-RC2, RV1-RV3 (own data - pending experiments)*
*Update after each verification pass*
