# DR-001: Reference Model Scope

**Status:** DRAFT - Awaiting co-author input
**Date:** 2026-01-15
**Decision Needed By:** Before experimental planning

---

## Context

The MST paper aims to establish a human reference model for CPR manikin fidelity assessment. We must decide the scope of this model before designing experiments.

## Options

| Option | Scope | Pros | Cons |
|--------|-------|------|------|
| **A** | Adults + infants, compressions + ventilations | Most comprehensive; aligns with outline | Resource intensive; diluted focus |
| **B** | Infants only (compressions + ventilations) | More unique contribution; less competition | Smaller market impact |
| **C** | Ventilations only (adults + infants) | Biggest evidence gap; clearest novelty | Ignores compression data we have |
| **D** | Adults + infants, compressions only | Builds on existing work; fastest path | Misses ventilation gap opportunity |

---

## Human Reference Data Assessment (Completed)

### Adult Compression — **STRONG**

| Parameter | Value | Source | n |
|-----------|-------|--------|---|
| Stiffness | 4-10 N/mm | Nysæther 2008 | 59 |
| Damping | ~0.17 N·s/mm | Nysæther 2008 | 59 |
| Non-linearity | Progressivity 1.41±0.25 | Tomlinson 2007 | 91 |
| Dynamic softening | -34.6% after 3000 compr | Ruiz de Gauna 2023 | 615 |

**Gap:** No systematic manikin benchmark against these values.

### Infant Compression — **PARTIAL**

| Parameter | Value | Source | n |
|-----------|-------|--------|---|
| Target depth (0 mo) | 2.7 cm (2.5-2.9) | Japan 2024 | 555 |
| Target depth (2 mo) | 2.9 cm (2.7-3.2) | Japan 2024 | 555 |
| Target depth (12-23 mo) | 3.6 cm (3.4-4.0) | Japan 2024 | 555 |
| Stiffness/damping | **NO DATA** | Gap | - |
| Force-depth | **NO DATA** | Gap | - |

**Gap:** Depth targets exist but NO force or stiffness data. Babic 2017: "Little research has been performed to evaluate the force required in younger infants."

### Infant Ventilation — **STRONG**

| Parameter | Value | Source | n |
|-----------|-------|--------|---|
| Compliance (Crs) | 78-171 mL/kPa | Huang 2016 | 205 |
| Resistance (Rrs) | 3.7-6.4 kPa/L/s | Huang 2016 | 205 |
| Crs/kg | 0.69 mL/cmH₂O/kg | Stoecklin 2024 | 23 |
| CL/kg | 0.95 mL/cmH₂O/kg | Stoecklin 2024 | 23 |
| Ccw/kg | 3.0 mL/cmH₂O/kg | Stoecklin 2024 | 23 |
| Ccw/CL ratio | ~3:1 (normalizes by 1 year) | Diedericks 2025 | Review |

**Gap:** No manikin characterization against these values.

### Adult Ventilation — **LIMITED**

| Parameter | Value | Source | n |
|-----------|-------|--------|---|
| Compliance | 37-40 mL/cmH₂O | Morin 2024 | Manikin design |
| Resistance | 20 cmH₂O·s/L | Morin 2024 | Manikin design |

**Note:** Morin 2024 already characterized SAM manikin; limited novelty here.

---

## Evidence Gap Analysis

| Domain | Human Data | Manikin Benchmark | MST Contribution Potential |
|--------|------------|-------------------|---------------------------|
| Adult compression | ✓ Strong | ✗ None | **HIGH** - first systematic benchmark |
| Infant compression | ~ Partial (depth only) | ✗ None | **MEDIUM** - can benchmark depth, not force |
| Adult ventilation | ~ Limited | ~ Morin 2024 | **LOW** - already published |
| Infant ventilation | ✓ Strong | ✗ None | **HIGH** - first systematic benchmark |

---

## Manikin Availability (TBD)

| Category | Available | Notes |
|----------|-----------|-------|
| Adult compression | ? | Laerdal, Prestan, others? |
| Infant compression | ? | Baby Anne, Prestan Infant? |
| Infant ventilation | ? | Same as above? |

**Action needed:** Inventory available manikins before final decision.

---

## Preliminary Recommendation

**Option A (Full Scope)** with prioritization:

### Priority 1 (Must Have)
- Adult compression benchmark (strongest human data, no competitor)
- Infant ventilation benchmark (strongest human data, no competitor)

### Priority 2 (Should Have)
- Infant compression benchmark (depth-based only)

### Priority 3 (Could Omit)
- Adult ventilation (Morin 2024 already published; limited novelty)

### Rationale
1. **Unique contribution:** First combined compression + ventilation reference model
2. **Strongest evidence base:** Adult compression + infant ventilation
3. **Resource efficient:** Infant compression uses same manikins as ventilation
4. **Acceptable gap:** Adult ventilation can be cited as future work (or cite Morin 2024)

---

## Blocking Items

- [x] Assessment of human reference data — **COMPLETE** (see above)
- [ ] Manikin availability inventory
- [ ] Co-author discussion
- [ ] Resource/timeline assessment

---

## Decision

**DECIDED: Option B — Infants Only (Compressions + Ventilations)**

### Rationale
- Adult manikins not available for testing
- Infant focus provides clearer novelty (less competing work)
- Strong human reference data for infant ventilation
- Partial human data for infant compression (depth targets)

### Final Scope

| Domain | Include | Human Data Quality | Notes |
|--------|---------|-------------------|-------|
| Infant compression | ✓ | Partial (depth only) | Benchmark against Japan 2024 targets |
| Infant ventilation | ✓ | Strong | Benchmark against Huang 2016, Stoecklin 2024 |
| Adult compression | ✗ | Strong | No manikins available |
| Adult ventilation | ✗ | Limited | No manikins available |

### Key Claims Enabled
- C5: Infant chest properties uncharacterized → MST fills gap
- C7: Infant compression depth targets (2.7-4.0 cm age-dependent)
- V1-V3: Infant ventilation mechanics (compliance, resistance, Ccw/CL ratio)

---

*Created: 2026-01-15*
*Decided: 2026-01-15 — Infants only per resource constraint*
