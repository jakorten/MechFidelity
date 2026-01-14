# Literature Review: Engineering Fidelity of CPR Training Manikins

**Purpose:** Systematic review of biomechanical reference data for constructing human reference models for chest compression and ventilation mechanics.

**Date:** January 2026

---

## 1. Executive Summary

This review synthesizes the available literature on human thorax biomechanics relevant to CPR manikin engineering fidelity. Key findings:

1. **Chest Compression Mechanics:** Robust human reference data exists for adults (n=615 patients, Ruiz de Gauna 2023), including stiffness, damping, and their evolution during CPR
2. **Ventilation Mechanics:** Reference data exists for infant respiratory compliance and resistance (n=205 infants, Huang 2016)
3. **Critical Gap:** Pediatric/infant chest compression biomechanics remain largely uncharacterized
4. **Behavioral Fidelity:** Human tissue exhibits non-linear viscoelastic behavior with hysteresis; commercial manikins typically show linear spring behavior

---

## 2. Chest Compression Mechanics: Human Reference Data

### 2.1 Viscoelastic Model Parameters (Adults)

The most comprehensive dataset comes from Ruiz de Gauna et al. (2023), analyzing **1,156,608 chest compressions from 615 OHCA patients**.

**Viscoelastic Model:**
```
F(t) = k·x(t) + d·v(t)
```
Where:
- k = elastic coefficient (stiffness)
- d = damping coefficient (viscosity)
- x(t) = chest displacement
- v(t) = chest velocity

**Reference Values at CPR Initiation:**

| Parameter | Value | 95% CI | Unit |
|-----------|-------|--------|------|
| Stiffness (k) | 104.9 | 102.0–107.8 | N/cm |
| Compression damping (dc) | 2.868 | 2.751–2.984 | N·s/cm |
| Recoil damping (dr) | 4.889 | 4.648–5.129 | N·s/cm |

**Key Finding:** Recoil damping is significantly higher than compression damping (p < 0.001). This asymmetry is not modeled in commercial manikins.

### 2.2 Population Differences

| Characteristic | Effect on Stiffness | Effect on Damping |
|----------------|---------------------|-------------------|
| Sex | Women lower k (96.8 vs 109.2 N/cm) | No significant difference |
| Age | No significant effect | dr increases with age |
| Body habitus | Not characterized | Not characterized |

### 2.3 Dynamic Changes During CPR

**Critical finding:** Chest mechanical properties change significantly during resuscitation.

| Parameter | Decrease after 3000 compressions |
|-----------|----------------------------------|
| Stiffness (k) | ↓ 34.6% |
| Compression damping (dc) | ↓ 48.8% |
| Recoil damping (dr) | ↓ 37.2% |

**Implications for Manikins:**
- Static mechanical properties do not capture real CPR dynamics
- Time-varying properties may relate to tissue fatigue or injury
- Current manikins cannot simulate this softening phenomenon

### 2.4 Force-Displacement Relationship

From Tomlinson et al. (2007) during actual OHCA CPR:

| Parameter | Value | Source |
|-----------|-------|--------|
| Mean applied force | 297 ± 80 N | Tomlinson 2007 |
| Mean compression depth | 42 ± 8 mm | Tomlinson 2007 |
| Force for 38mm depth | < 490 N (96% of patients) | Tomlinson 2007 |

### 2.5 Live vs. Cadaver Comparison

**Critical finding from Arbogast et al. (2006):**

| Condition | Force at 40mm Deflection |
|-----------|--------------------------|
| Live CPR (perfused tissue) | **286 N** |
| Post-mortem cadaver | **588 N** |

**Implication:** Live human tissue is approximately **2× softer** than cadaver tissue. Cadaver-based manikin specifications may substantially overestimate required stiffness.

---

## 3. Chest Compression Mechanics: Manikin Characterization

### 3.1 Variable Stiffness Manikin (Lim et al. 2024)

Novel manikin system achieving adjustable non-linear behavior:

| Parameter | Range Achieved | Human Reference |
|-----------|----------------|-----------------|
| Stiffness | 5.34–13.59 N/mm | 4–10 N/mm |
| Damping | 0.127–0.511 N·s/mm | 0.08–0.38 N·s/mm |

**Key innovations:**
- Variable stiffness mechanism (VSM) using silicone bands
- Variable damper (VD) using controllable valves
- Achieved non-linear force-displacement with hysteresis
- Demonstrated independent control of stiffness and damping

### 3.2 TU/e Human-Like Thorax Manikin (Thielen et al. 2017)

Anatomically realistic infant manikin design featuring:
- Human-like thorax structure
- Embedded flow sensors for ventilation measurement
- Non-linear force-displacement mimicking human CPR
- Integrated feedback capability

**Significance:** Demonstrates feasibility of engineering fidelity in infant manikins with embedded sensing.

### 3.3 Commercial Manikin Survey

From historical characterization studies:

| Depth | Force Range (Commercial Manikins) |
|-------|-----------------------------------|
| 1 cm | 62–137 N |
| 3 cm | 167–373 N |
| 5 cm | 280–677 N |

**Behavioral characteristic:** Spring-based manikins (Resusci Anne, Ambu Man) show **linear** behavior; foam-based (Little Anne) show decreasing resistance with depth.

### 3.4 Systematic vs. Ad-hoc Specification

| Population | Specification Method | Rigor Level |
|------------|---------------------|-------------|
| **Adult** | Patient-derived measurement (n=59) | Systematic (Aase 2008) |
| **Child** | Expert opinion (43% agreement) | Ad-hoc (Tomlinson 2009) |
| **Infant** | Expert opinion (46% agreement) | Ad-hoc (Tomlinson 2009) |
| **Neonate** | No data found | None |

**Critical gap:** No ISO or regulatory standard exists for CPR manikin mechanical properties.

---

## 4. Ventilation Mechanics: Human Reference Data (Infants)

### 4.1 Respiratory Compliance and Resistance (Huang et al. 2016)

**Study population:** 205 healthy infants, 1–96 weeks old, Southeast China

**Overall Reference Values:**

| Parameter | Value | Range | Unit |
|-----------|-------|-------|------|
| Respiratory resistance (Rrs) | 5.04 (median) | 3.73–6.82 | kPa/L/s |
| Respiratory compliance (Crs) | 119.52 ± 60.47 | 17.2–287 | mL/kPa |

### 4.2 Age-Dependent Changes

| Age Group | Rrs (kPa/L/s) | Crs (mL/kPa) |
|-----------|---------------|--------------|
| 1–24 weeks | 6.39 | 77.95 ± 46.16 |
| 25–48 weeks | 5.11 | 123.51 ± 50.64 |
| 49–72 weeks | 4.20 | 141.17 ± 44.75 |
| 73–96 weeks | 3.74 | 170.58 ± 50.14 |

**Pattern:** Resistance decreases with age/growth; compliance increases with lung development.

### 4.3 Neonatal Reference Data (Battisti et al. 2012)

**Study population:** 32 healthy neonates (preterm and term), longitudinal measurements

**Reference Values (Day 1):**

| Parameter | Value | Unit |
|-----------|-------|------|
| Compliance (Crs) | 1.37 ± 0.37 | mL/cmH₂O |
| Resistance (Rrs) | 0.048 ± 0.17 | cmH₂O/mL/s |

**Postnatal Evolution:**
- Compliance increases ~20% after birth, plateaus by day 7
- Female neonates have significantly higher compliance
- More premature infants have higher resistance

### 4.4 Unit Conversion Reference

For comparison across studies:

| Parameter | SI Unit | Alternative | Conversion |
|-----------|---------|-------------|------------|
| Compliance | mL/kPa | mL/cmH₂O | 1 kPa = 10.2 cmH₂O |
| Resistance | kPa/L/s | cmH₂O/L/s | 1 kPa = 10.2 cmH₂O |

---

## 5. Ventilation Mechanics: Manikin Gap Analysis

### 5.1 Current State

**Critical finding:** No systematic characterization of CPR training manikin ventilation mechanics exists in the literature.

While compression fidelity has received attention, ventilation fidelity assessment is essentially absent:

| Aspect | Compression | Ventilation |
|--------|-------------|-------------|
| Human reference data | Extensive | Available (infants) |
| Manikin characterization | Some studies | **None found** |
| Fidelity comparison | Limited | **None found** |
| Standardized protocol | None | **None** |

### 5.2 Significance for This Paper

This represents a **major contribution opportunity**:
1. Human reference data for infant ventilation mechanics EXISTS
2. Manikin ventilation characterization is MISSING
3. This paper can provide the first systematic ventilation fidelity benchmark

---

## 6. Physiological Modeling Foundation

### 6.1 Cardiorespiratory Modeling Framework (van Meurs)

Willem van Meurs' textbook "Modeling and Simulation in Biomedical Engineering: Applications in Cardiorespiratory Physiology" provides theoretical foundation for:

- Physiological control system modeling
- Circulation and respiration mechanics
- Model validation methodology
- Simulator design principles

**Relevance:** Provides conceptual framework for building physics-informed reference models.

### 6.2 Viscoelastic Model Validation

The Ruiz de Gauna (2023) viscoelastic model achieved:
- R² = 97.9% (95% CI: 97.8–98.1) fit to human data
- Significantly outperformed pure elastic model (R² = 85.8%)
- Stable performance across prolonged CPR

**Implication:** Simple spring-damper model accurately characterizes human chest mechanics when compression/recoil asymmetry is accounted for.

---

## 7. Identified Gaps and Research Opportunities

### 7.1 Critical Evidence Gaps

| Gap | Impact | Priority |
|-----|--------|----------|
| Pediatric/infant chest stiffness | Cannot validate infant manikins | HIGH |
| Ventilation fidelity metrics | No benchmark exists | HIGH |
| Time-varying manikin properties | Cannot simulate fatigue | MEDIUM |
| Inter-unit manikin variation | Unknown reproducibility | MEDIUM |

### 7.2 Opportunities for This Paper

1. **First ventilation fidelity benchmark:** Characterize manikin C and R against Huang/Battisti reference data
2. **Combined compression + ventilation:** Novel integrated analysis
3. **Engineering Fidelity Index:** Quantified, actionable metric
4. **Multi-manikin comparison:** Systematic cross-manufacturer benchmark

---

## 8. Summary: Reference Model Parameters

### 8.1 Adult Chest Compression Reference Envelope

| Parameter | Lower Bound | Upper Bound | Source |
|-----------|-------------|-------------|--------|
| Stiffness (k) | 4 N/mm | 10 N/mm | Lim 2024, Ruiz de Gauna 2023 |
| Compression damping | 0.08 N·s/mm | 0.38 N·s/mm | Lim 2024 |
| Recoil damping | Higher than compression | ~1.7× compression | Ruiz de Gauna 2023 |
| Force at 50mm | 200 N | 500 N | Tomlinson 2007 |
| Behavior | Non-linear with hysteresis | — | Multiple sources |

### 8.2 Infant Ventilation Reference Envelope

| Parameter | Lower Bound | Upper Bound | Age Range | Source |
|-----------|-------------|-------------|-----------|--------|
| Compliance (Crs) | 78 mL/kPa | 171 mL/kPa | 1–96 weeks | Huang 2016 |
| Resistance (Rrs) | 3.74 kPa/L/s | 6.39 kPa/L/s | 1–96 weeks | Huang 2016 |

### 8.3 Infant Chest Compression Reference

| Parameter | Status | Note |
|-----------|--------|------|
| Stiffness | **UNKNOWN** | No human reference data exists |
| Damping | **UNKNOWN** | Expert opinion only (Tomlinson 2009) |
| Force at 40mm | 37–42 N | Two-thumb technique studies |

---

## 9. Key References

### Compression Mechanics
- Ruiz de Gauna S et al. (2023). Comput Methods Programs Biomed. 242:107847.
- Lim H et al. (2024). IEEE J Transl Eng Health Med. 12:542-549.
- Tomlinson AE et al. (2007). Resuscitation. 72(3):364-370.
- Arbogast KB et al. (2006). Stapp Car Crash J. 50:131-145.
- Aase SO et al. (2008). Resuscitation. 77(3):312-318.

### Ventilation Mechanics
- Huang J et al. (2016). J Thorac Dis. 8(3):513-519.
- Battisti O et al. (2012). Pediatr Therapeut. 2(2):114.

### Manikin Design
- Thielen M et al. (2017). Proc Inst Mech Eng H. 231(3):243-249.
- Chen W et al. (2010). IEEE Trans Inf Technol Biomed. 14(6):1468-1474.

### Theoretical Foundation
- van Meurs W. Modeling and Simulation in Biomedical Engineering. McGraw-Hill.

---

*Document created: January 2026*
*For: MST Special Issue Paper on Engineering Fidelity*
