# MST Paper - Supervisor Summary

**Updated:** January 15, 2026

---

## Paper Overview

**Title:** "Engineering Fidelity of CPR Training Manikins: A Data-Driven Reference Model for Chest Compression and Ventilation Mechanics"

**Target:** Measurement Science and Technology - Special Issue on *"Data-Centric Exploration and Explanation of Physical and Engineering Phenomena"*

**Deadline:** March 31, 2026 (~2.5 months remaining)

**Link:** https://iopscience.iop.org/collections/mst-251119-1003

---

## Current Progress

### Literature Verification: 69% P0 Complete

| Priority | Verified | Total | Coverage |
|----------|----------|-------|----------|
| P0 (Critical) | 9 | 13 | **69%** |
| P1 (Important) | 1 | 7 | 14% |
| P2 (Supporting) | 0 | 1 | 0% |
| **Total** | **10** | **21** | **48%** |

**Note:** Remaining P0 claims require our own experimental data (M1, M2, RC1-RC2, RV1-RV3).

### Verified Human Reference Sources

| Domain | Source | Key Data |
|--------|--------|----------|
| **Adult compression** | Nysæther 2008 (n=59 OHCA) | Stiffness ~3-11 N/mm, damping 0.17 N·s/mm |
| **Non-linearity** | Tomlinson 2007 (n=91) | Progressivity factor 1.41±0.25 |
| **Dynamic softening** | Ruiz de Gauna 2023 (n=615) | 34.6% stiffness decrease after 3000 compressions |
| **Infant ventilation** | Huang 2016 (n=205) | Compliance 78-171 mL/kPa, resistance 3.7-6.4 kPa/L/s |
| **Adult ventilation** | Morin 2024 / Charbonney 2018 | Compliance 37-40 mL/cmH₂O, resistance 20 cmH₂O·s/L |

### Confirmed Novelty Claims

- **I2:** No systematic benchmark exists for manikin mechanical properties (only Baubin 1995, 30y old)
- **I3:** First data-driven reference model combining compressions AND ventilations
- **D1:** First systematic multi-manikin benchmark against human reference
- **D2:** Ventilation fidelity is novel contribution (Reiss 2015 called for it, none exists)

---

## Apparatus Status

### Compression Testing
| Component | Status |
|-----------|--------|
| CNC actuator (BlackBox X32) | Operational |
| ToF displacement sensor | Operational, calibrated |
| Load cell | **Installed, needs firmware integration** |

### Ventilation Testing
| Component | Status |
|-----------|--------|
| SDP810 + orifice (flow) | Operational |
| Bronkhorst MFM (reference) | Operational, SI-traceable |
| Airway pressure sensor | **Need MPXV5010DP (~€10)** |

**Gap:** Current sensors insufficient for airway pressure measurement (need 0-20 cmH₂O range for infant manikins).

---

## Remaining Work

### Phase 1: Apparatus (1-2 weeks)
- [ ] Load cell firmware integration + calibration
- [ ] Order and integrate MPXV5010DP pressure sensor
- [ ] System verification with one manikin

### Phase 2: Data Collection (2-3 weeks)
- [ ] Compression characterization (adult + infant manikins)
- [ ] Ventilation characterization (infant manikins)
- [ ] Unit-to-unit variation testing

### Phase 3: Analysis & Writing (3-4 weeks)
- [ ] Reference model fitting with uncertainty envelope
- [ ] Engineering fidelity index calculation
- [ ] Draft all sections
- [ ] Co-author review and revision

---

## Key Decisions Pending

### DR-001: Reference Model Scope
**Options:**
- A: Adults + infants, compressions + ventilations (full scope)
- B: Focus on infants only (unique data)
- C: Focus on ventilations only (biggest literature gap)

**Recommendation:** Option A if timeline permits; Option C as fallback (strongest novelty).

### DR-002: Manikin Selection
- Which models to include?
- How many replicates per model?
- Dependent on availability assessment

---

## Risk Assessment

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Tight timeline (2.5 months) | Medium | Leverage TIM methodology, narrow scope if needed |
| Equipment delays | Low | MPXV5010DP widely available (~€10) |
| Manikin access | Low | Multiple models already available |
| Co-author availability | Medium | Early draft circulation |

---

## Fit with Publication Strategy

```
IEEE TIM (under review)     → Sensor validation methodology
IEEE THMS (under review)    → Training effectiveness (RCT)
Resuscitation (in prep)     → Conceptual framework (perspective)
MST (in progress)           → Technical benchmark methodology  ← THIS PAPER
```

The perspective paper argues *for* engineering fidelity; **this MST paper provides the tools to measure it.**

---

## Unique Contribution

This paper fills a critical gap: while compression mechanics have some prior characterization (Baubin 1995, Nysæther 2008), **no systematic benchmark exists that:**
1. Tests multiple commercial manikins against human reference data
2. Includes ventilation mechanics (compliance, resistance)
3. Provides a quantitative fidelity index for procurement decisions

The ventilation fidelity angle is particularly novel—Reiss 2015 explicitly called for manikin compliance/resistance characterization, but no such work has been published.

---

## Next Steps

1. **Immediate:** Order MPXV5010DP, complete load cell integration
2. **This week:** Finalize manikin test matrix, begin compression testing
3. **Decision needed:** Scope confirmation (DR-001)

---

*Summary generated: 2026-01-15*
