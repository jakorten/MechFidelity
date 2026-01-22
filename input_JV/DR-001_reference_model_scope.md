---
status: DECIDED
date: 2026-01-15
updated: 2026-01-16
decision: Option D - Infant Ventilation (Primary) + Compression (Secondary)
---

# Decision: Reference Model Scope

## Context

The paper needs to define what human reference data to include and what manikins to characterize.

**Constraints identified (2026-01-15):**
- Only infant manikins available
- Test equipment suitable for infant manikins only
- Deadline: March 31, 2026

## Available Options (given constraints)

| Option | Human Reference | Novelty | Feasibility |
|--------|-----------------|---------|-------------|
| Infant compression only | **None** (Babic 2017 used scaled adult) | Medium | Cannot validate |
| Infant ventilation only | **Huang 2016 (n=205)** | **High** | **Can validate** |
| **Infant compression + ventilation** | **Partial (ventilation only)** | **High** | **Mixed validity** |

## Decision

**Option D: Infant Ventilation (Primary) + Compression (Secondary)**

### Rationale

1. **Human reference exists for ventilation:** Huang 2016 provides compliance (78-171 mL/kPa) and resistance (3.7-6.4 kPa/L/s) for infants aged 1-96 weeks (n=205)

2. **Strong novelty:** Verified (D2) - no systematic manikin ventilation benchmark exists. Reiss 2015 explicitly called for this work.

3. **Ventilation validation possible:** Can compare manikin C/R values against human reference envelope

4. **Ventilation equipment ready:** SDP810 + MFM operational; Bronkhorst EL-PRESS P-502C for airway pressure

5. **Compression included but without human reference:**
   - DYMH-103 load cell (0-49 N) available; suitable for infant compression forces (14-30 N range per Ikeyama 2024)
   - No human reference data exists for infant chest mechanics (Babic 2017 confirms this gap)
   - Compression data will be **descriptive** (characterizing manikins) rather than **evaluative** (comparing to human reference)

### Scope Definition

| Include | Exclude |
|---------|---------|
| Infant manikin ventilation characterization | Adult manikins |
| Infant manikin compression characterization | Adult ventilation/compression |
| Compliance (C) measurement (ventilation) | — |
| Resistance (R) measurement (ventilation) | — |
| Force-displacement curves (compression) | — |
| Human reference envelope (Huang 2016, ventilation) | — |
| Mechanical fidelity index (ventilation only) | — |
| Compression data (descriptive, no fidelity index) | — |

### Paper Positioning

**Title revision suggestion:**
"Mechanical Fidelity of Infant CPR Manikins: A Data-Driven Reference Model for Respiratory and Compression Mechanics"

**Key claims:**
- First systematic benchmark of infant manikin respiratory mechanics
- Quantitative comparison against human infant reference data (ventilation)
- Mechanical fidelity index for ventilation compliance and resistance
- First characterization of infant manikin compression mechanics (descriptive)

## Implications

### Apparatus
- [x] Flow measurement (SDP810 + MFM) — ready
- [x] Airway pressure sensor — Bronkhorst EL-PRESS P-502C (ordered)
- [x] Load cell — DYMH-103 (0-49 N) available

### Data Collection
- Infant manikins only
- Ventilation characterization: C and R at target tidal volumes
- Compression characterization: force-displacement curves
- Multiple replicates for unit-to-unit variation

### Claims Registry Update Needed
- Re-add compression claims for infant manikins (descriptive characterization)
- Focus on ventilation claims (V1-V2, RV1-RV3) for fidelity evaluation
- Update novelty claims (I2, I3, D1, D2) for combined scope

## Update 2026-01-21: Compression Reference Status

### O'Reilly/Schmölzer 2024 (Pediatric Research)
- **No force data available** — only depth measured (infrared sensor)
- No chest stiffness/compliance measurements
- Supports hypothesis that force profile matters (not just depth)
- Cannot derive infant chest stiffness from this source

### Thielen et al. 2017 (TU/e, Proc IMechE Part H)
- **Provides force-displacement methodology** — polynomial model
- Key finding: Classical manikins are LINEAR, human chest is NONLINEAR
- Model: `F = k₁·z + k₂·z² + k₃·z³ + k₄·z⁴ + d₀·ż + d₁·z·ż`
- **Limitation:** ADULT chest mechanics, not infant
- Explicitly calls out SimMan 3G and Apollo as not meeting fidelity requirements

### Conclusion
1. **Compression remains descriptive** — no infant reference data available
2. **Thielen methodology applicable** — use polynomial model for manikin characterization
3. **Discussion point:** Future work needs device to measure infant chest mechanics at different gestational ages (ethically challenging but technically feasible with non-invasive methods)

### Action Items
- [ ] Check with Mark Thielen about extending methodology to infant scale
- [ ] Consider polynomial model (Gruben) for compression characterization
- [ ] Add discussion section on "measurement gap" for infant chest mechanics

---

## Revisit If

- Adult manikins become available
- Human infant compression data published (enables compression fidelity index)
- Collaboration with Thielen/TU/e on infant-scale measurements
