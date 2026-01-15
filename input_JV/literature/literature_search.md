# Literature Search: Human Reference Model

**Purpose:** Compile human reference data for chest compression and ventilation mechanics
**Last Updated:** 2026-01-15
**Status:** Data extracted from Proposition repo - verification needed

---

## Summary

Much of the literature search was already done for the Proposition paper. Key data has been extracted to `extracted_data_from_proposition.md`. This file tracks what still needs verification.

---

## Priority Papers

### Tier 1: Core Human Reference Data (MUST HAVE)

#### Compression Mechanics - Adults

| Paper | Key Data | Proposition | PDF | Verified |
|-------|----------|-------------|-----|----------|
| **Lim et al. 2024** | Stiffness 4-10 N/mm, damping 0.08-0.38 N·s/mm | [x] Extracted | [x] | [ ] |
| **Tomlinson et al. 2007** | Non-linear force-depth, F38 = 27.5±13.6 kg | [x] Extracted | [x] | [ ] |
| **Ruiz de Gauna et al. 2023** | Dynamic stiffness -34.6% during CPR | [x] Extracted | [x] | [ ] |
| **Neurauter et al. 2009** | Stiffness 7.7-8.1 N/mm at 50mm | [x] Extracted | [x] | [ ] |

#### Compression Mechanics - Infants/Pediatrics

| Paper | Key Data | Proposition | PDF | Verified |
|-------|----------|-------------|-----|----------|
| **Papastamelos et al. 1995** | Developmental chest wall compliance | [ ] | [ ] | [ ] |
| **Babic et al. 2017** | Infant CPR manikin test protocol | [ ] | [x] URL | [ ] |
| **Thielen et al. 2017** | Human-like thorax design | [x] Referenced | [ ] | [ ] |

#### Ventilation Mechanics - Infants

| Paper | Key Data | Proposition | PDF | Verified |
|-------|----------|-------------|-----|----------|
| **Huang et al. 2016** | Compliance 119.52±60.47 mL/kPa, Resistance 5.04 kPa/L/s | [x] Extracted | [x] | [x] Web |
| **Battisti et al. 2012** | Compliance 1.37-1.67 mL/cm H₂O/s, Resistance 0.048-0.060 | [x] Extracted | [x] | [x] Web |

**NEW:** Detailed extraction in `md_out/infant_respiratory_reference_values.md`

### Tier 2: Methodology/Modeling Papers

| Paper | Key Data | PDF | Notes |
|-------|----------|-----|-------|
| **Le Rolle et al. 2008** | Newborn lamb vs adult respiratory parameters | [x] | Lamb Cl=0.009, Ccw=0.013 L/cmH₂O |
| **Fresnel et al. 2014** | Pmus model for mechanical lung testing | [x] | Methodology for ventilator bench testing |
| **Athanasiades et al. 2000** | Nonlinear lung model | [x] | Energy analysis approach |
| **Babic et al. 2017** | Infant CPR manikin test protocol | [x] URL | Universal Testing Machine protocol |

### Tier 3: Recent Papers (2022-2025) - TO OBTAIN

**See:** `recent_papers_to_obtain.md` for DOIs and download links

#### Neonatal Respiratory Mechanics

| Paper | Year | Key Data | PDF | Priority |
|-------|------|----------|-----|----------|
| **Stoecklin et al.** | 2024 | First postsurfactant Crs, CL, Ccw in preterm ± BPD | [x] | **OBTAINED** |
| **Reiss et al.** | 2024 | No compliance deterioration in preterm on CMV | [x] Web | **OBTAINED** |
| **Diedericks et al.** | 2025 | Chest wall role at birth (review) | [x] Web | **OBTAINED** |

#### Neonatal Chest Compression / CPR

| Paper | Year | Key Data | PDF | Priority |
|-------|------|----------|-----|----------|
| **Japan CC depth** | 2024 | Target depth 0mo=2.7cm, 2mo=2.9cm (shallower than guidelines!) | [ ] | **HIGH** |
| **SURV1VE Trial** | 2024 | Sustained inflation + CC vs 3:1 ratio in newborns | [ ] | Medium |
| **Novel CC technique** | 2025 | 92.4% adequate rate with novel technique | [ ] | Low |
| **2025 AHA Guidelines** | 2025 | Latest neonatal resuscitation guidelines | [ ] | **HIGH** |

---

## Reference Values (From Proposition)

### Adult Chest Compression

| Parameter | Value | Range | Source | Status |
|-----------|-------|-------|--------|--------|
| Stiffness (N/mm) | 7.7-8.1 | 4-10 | Lim 2024, Neurauter 2009 | Extracted |
| Damping (N·s/mm) | 0.08-0.38 | - | Lim 2024 | Extracted |
| Initial stiffness | 10.5 N/mm | - | Ruiz de Gauna 2023 | Extracted |
| Stiffness after 3000 compr | 6.9 N/mm | -34.6% | Ruiz de Gauna 2023 | Extracted |
| Force at 38mm (kg) | 27.5 ± 13.6 | - | Tomlinson 2007 | Extracted |

### Infant Ventilation

| Parameter | Value | Age Range | Source | Status |
|-----------|-------|-----------|--------|--------|
| Compliance (mL/kPa) | 119.52 ± 60.47 | 1-96 wks | Huang 2016 | **Verified** |
| Compliance range | 80-170 | age-dependent | Huang 2016 | **Verified** |
| Resistance (kPa/L/s) | 5.04 (3.73-6.82) | 1-96 wks | Huang 2016 | **Verified** |
| Compliance (mL/cm H₂O/s) | 1.37-1.67 | Day 1-21 | Battisti 2012 | **Verified** |
| Resistance (cm H₂O/mL/s) | 0.048-0.060 | Day 1-21 | Battisti 2012 | **Verified** |

**See:** `md_out/infant_respiratory_reference_values.md` for full details

### Evidence Gaps (MST Paper Contribution)

| Gap | Status | MST Paper Role |
|-----|--------|----------------|
| Adult compression - manikin comparison | **None** | Fill this gap |
| Infant compression - all | **Very weak** | Fill this gap |
| Adult ventilation - all | **Weak** | Partial contribution |
| Infant ventilation - manikin comparison | **None** | Fill this gap |

---

## Verification Tasks

### Step 1: Obtain PDFs
- [x] Download/locate Lim 2024, Tomlinson 2007, Ruiz de Gauna 2023 (from Proposition)
- [x] Download/locate Huang 2016, Battisti 2012 (open access downloads)
- [x] Check if already in Proposition/articles/pdfs/ (Yes - copied over)

### Step 2: Verify Extracted Values
- [ ] Confirm Lim 2024 stiffness 4-10 N/mm (Table 2?)
- [ ] Confirm Tomlinson 2007 non-linearity quote
- [ ] Confirm Ruiz de Gauna 2023 -34.6% change
- [ ] Confirm Huang 2016 compliance/resistance values

### Step 3: Extract Additional Data
- [ ] Uncertainty/variability for all values
- [ ] Measurement methods used
- [ ] Patient/subject demographics
- [ ] Any manikin comparison data

---

## Key Quotes (From Proposition - To Verify)

### Tomlinson et al. 2007
> "Commonly used CPR training manikins...usually have spring loaded chests with a **linear relationship between force and depth**."

**Verify:** Page number, exact wording

### Lim et al. 2024
> "Mechanical properties of commercially available CPR training manikins remain constant and **no information on these properties is provided by the manufacturers**."

**Verify:** Page number, exact wording

---

## Files

```
input_JV/literature/
├── literature_search.md              ← This file (tracking)
├── extracted_data_from_proposition.md ← Data from Proposition repo
├── pdfs/                             ← Source PDFs
└── md_out/                           ← Verified extractions
```

---

## Cross-Reference

- **Proposition literature search:** `C:\local_dev\Proposition\records_jk\literature_search_mechanical_fidelity.md`
- **Proposition key quotes:** `C:\local_dev\Proposition\records_jk\key_quotes.md`
- **Proposition chapter Section 8:** Human reference data tables

---

*Search consolidated: 2026-01-15*
*Most data extracted from Proposition repo - verification pass needed*
