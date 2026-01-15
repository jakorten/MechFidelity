# Claim Registry

**Paper:** Engineering Fidelity of CPR Training Manikins (MST Special Issue)
**Last Updated:** 2026-01-15
**Thesis:** Data-driven reference model enables objective manikin evaluation and quantification of the engineering fidelity gap

---

## Coverage Summary

| Priority | Total | Verified | Needs Evidence | Coverage |
|----------|-------|----------|----------------|----------|
| P0 | 0 | 0 | 0 | 0% |
| P1 | 0 | 0 | 0 | 0% |
| P2 | 0 | 0 | 0 | 0% |
| **Total** | **0** | **0** | **0** | **0%** |

**Target:** >=85% overall, 100% P0

---

## Claim Registry (Section-Ordered)

### Section 1: Introduction

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| I1 | Engineering fidelity concept links to perspective paper | P1 | Proposition paper | [ ] |
| I2 | No systematic benchmark exists for manikin mechanical properties | P0 | Literature gap | [ ] |
| I3 | First data-driven reference model for compressions AND ventilations | P0 | Novelty claim | [ ] |

### Section 2: Human Reference Model -- Compression Mechanics

#### 2.1 Adults

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| C1 | Adult chest stiffness ranges 5.3-13.6 N/mm at 50mm depth | P0 | Lim 2024 | [ ] |
| C2 | Adult chest damping ranges 0.13-0.51 N*s/mm | P0 | Lim 2024 | [ ] |
| C3 | Force-displacement relationship is non-linear (human) | P0 | Tomlinson 2007 | [ ] |
| C4 | Chest stiffness decreases ~35% after 3000 compressions | P1 | Ruiz de Gauna 2023 | [ ] |

#### 2.2 Infants/Pediatrics

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| C5 | Infant chest mechanical properties are largely uncharacterized | P0 | Literature gap | [ ] |
| C6 | Infant compliance differs from adults | P1 | Papastamelos 1995 | [ ] |

### Section 2: Human Reference Model -- Ventilation Mechanics

| ID | Claim | Priority | Source | Status |
|----|-------|----------|--------|--------|
| V1 | Infant compliance ~80 mL/kPa (1-24 wks) to ~170 mL/kPa (73-96 wks) | P0 | Huang 2016 | [ ] |
| V2 | Infant resistance ~6 kPa/L/s (1-24 wks) to ~4 kPa/L/s (73-96 wks) | P0 | Huang 2016 | [ ] |

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
| D1 | First systematic multi-manikin benchmark | P0 | Novelty claim | [ ] |
| D2 | Ventilation fidelity is novel contribution | P0 | Literature gap | [ ] |

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

| Source | Claims | What to Check |
|--------|--------|---------------|
| Lim 2024 | C1, C2 | Stiffness 5.3-13.6, damping 0.13-0.51 -- exact numbers from Table 2 |
| Tomlinson 2007 | C3 | Non-linear force-displacement -- verify description |
| Ruiz de Gauna 2023 | C4 | 35% decrease -- exact value and conditions |
| Huang 2016 | V1, V2 | Compliance and resistance ranges -- exact values |

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
*Update after each verification pass*
