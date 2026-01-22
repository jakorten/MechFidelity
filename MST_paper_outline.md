# MST Special Issue Paper Outline

**Target:** Measurement Science and Technology - Special Issue on "Data-Centric Exploration and Explanation of Physical and Engineering Phenomena"

**Deadline:** March 31, 2026

**Call for papers:** https://iopscience.iop.org/collections/mst-251119-1003

---

## Proposed Title

> "Mechanical Fidelity of CPR Training Manikins: A Data-Driven Reference Model for Chest Compression and Ventilation Mechanics"

**Note:** "Mechanical fidelity" emphasizes that we assess how the manikin *responds* (stiffness, compliance, damping), not how it *looks*. Traditional "high-fidelity" refers to visual realism—a manikin may look like an infant without responding like one. See DR-004 for terminology decision.

---

## Core Concept

Build a **human reference model** from medical/clinical literature, then systematically compare multiple CPR training manikins against that model to quantify the "mechanical fidelity gap."

```
Human Reference Model          →    Manikin Characterization    →    Fidelity Gap Analysis
(from medical literature)            (empirical testing)              (model vs. reality)
```

---

## Why This Fits the Special Issue

| Theme from Call | How This Paper Fits |
|-----------------|---------------------|
| Data-driven discovery | Reference model synthesized from published clinical datasets |
| Physics-informed modeling | Grounded in biomechanics (force-displacement, compliance, resistance) |
| Advanced sensing & instrumentation | Standardized manikin characterization protocol |
| Uncertainty quantification | Human variability → acceptable range envelope |
| Biomedical engineering | Direct application to medical simulation |

---

## Paper Structure

### 1. Introduction
- Mechanical fidelity concept: response vs appearance (link to perspective paper)
- Key framing: "A manikin may look like an infant without responding like one"
- Gap: no systematic benchmark for manikin mechanical properties
- Contribution: first data-driven reference model for compressions AND ventilations

### 2. Human Reference Model Construction

#### 2.1 Chest Compression Mechanics (Adults)

| Parameter | Description | Sources |
|-----------|-------------|---------|
| Stiffness (k) | Force per unit displacement (N/mm) | Tomlinson 2007, Lim 2024 |
| Damping (d) | Energy dissipation (N·s/mm) | Lim 2024, Ruiz de Gauna 2023 |
| Nonlinearity | Force-displacement curve shape | Tomlinson 2007 |
| Dynamic changes | Softening over repeated compressions | Ruiz de Gauna 2023 |

**Key values (adults):**
- Stiffness: 5.3–13.6 N/mm at 50mm depth (Lim 2024)
- Damping: 0.13–0.51 N·s/mm (Lim 2024)
- Stiffness decrease: ~35% after 3000 compressions (Ruiz de Gauna 2023)

#### 2.2 Chest Compression Mechanics (Infants/Pediatrics)

| Parameter | Status | Sources |
|-----------|--------|---------|
| Stiffness | Largely uncharacterized | Babic 2017, Thielen 2017 (manikin design only) |
| Compliance changes | Known to differ from adults | Papastamelos 1995 |

**Note:** Major evidence gap - infant mechanical properties are largely unknown. This paper could contribute novel data.

#### 2.3 Ventilation Mechanics (Infants)

| Parameter | Values | Sources |
|-----------|--------|---------|
| Compliance | ~80 mL/kPa (1-24 wks) → ~170 mL/kPa (73-96 wks) | Huang 2016 |
| Resistance | ~6 kPa/L/s (1-24 wks) → ~4 kPa/L/s (73-96 wks) | Huang 2016, Battisti 2012 |

**Advantage:** Human reference data EXISTS for ventilation - the manikin comparison is missing.

### 3. Uncertainty Envelope

- Human data shows natural variability
- Reference model should define acceptable RANGE, not single target
- Manikins within envelope = adequate mechanical fidelity
- Manikins outside envelope = quantified fidelity gap

### 4. Manikin Characterization Protocol

#### 4.1 Compression Testing
- Apparatus: force-displacement measurement system
- Protocol: standardized compression cycles
- Measurements: stiffness, damping, nonlinearity
- Repeated measures: assess drift/fatigue

#### 4.2 Ventilation Testing
- Apparatus: flow sensor + pressure sensor
- Protocol: standardized ventilation volumes
- Measurements: delivered volume, airway pressure, flow rate
- Derived: compliance, resistance

#### 4.3 Manikins Under Test
- Multiple manufacturers
- Multiple models (infant, child, adult)
- Replicates of same model (unit-to-unit variation)

### 5. Results

#### 5.1 Compression Fidelity
- Force-displacement curves for each manikin
- Overlay with human reference envelope
- Quantified deviation metrics

#### 5.2 Ventilation Fidelity
- Compliance and resistance for each manikin
- Comparison to human reference values
- Quantified deviation metrics

#### 5.3 Unit-to-Unit Variation
- Same-model replicates: how consistent?
- Implications for training standardization

### 6. Mechanical Fidelity Index

Propose a quantified metric for manikin selection:
- Compression fidelity score (deviation from reference stiffness/damping)
- Ventilation fidelity score (deviation from reference compliance/resistance)
- Combined mechanical fidelity index
- Actionable for procurement decisions

**Note:** Per VIM, "accuracy" cannot be given a numerical value. We define "fidelity index" as our own metric: normalized deviation from human reference values.

### 7. Discussion

- First systematic multi-manikin benchmark
- Ventilation fidelity: novel contribution
- Limitations: adult compression data vs. infant focus
- Implications for training program design
- Future work: dynamic (time-varying) characterization

### 8. Conclusion

- Data-driven reference model enables objective manikin evaluation
- Mechanical fidelity can now be quantified, not assumed
- Distinguishes mechanical response from visual appearance
- Call for manufacturer transparency on mechanical properties

---

## Timeline

| Period | Activity |
|--------|----------|
| Jan 2026 | Data collection: compression + ventilation characterization |
| Feb 2026 | Analysis: reference model fitting, manikin comparison |
| Early Mar 2026 | Writing: first draft + co-author feedback |
| Mid-Late Mar 2026 | Revision + submit by March 31 deadline |

---

## Resources Required

- [ ] Access to multiple manikins (confirmed: available)
- [ ] Force-displacement measurement apparatus (from TIM work)
- [ ] Flow/pressure measurement for ventilations
- [ ] Human reference data compilation (partially done)

---

## Relationship to Other Papers

| Paper | Venue | Status | Relationship |
|-------|-------|--------|--------------|
| Sensor validation | IEEE TIM | Under review | Methodology foundation |
| TEF RCT | IEEE THMS | Under review | Training effectiveness evidence |
| Perspective paper | Resuscitation | In preparation | Conceptual framework |
| **This paper** | MST | Planned | Technical methodology + data |

**Synergy:** The perspective paper argues FOR mechanical fidelity; this MST paper provides the TOOLS to measure it.

---

## Key References

### Compression Mechanics
- Tomlinson AE et al. (2007). Compression force-depth relationship during OHCA CPR. *Resuscitation*. 72(3):364-370.
- Ruiz de Gauna S et al. (2023). Characterization of mechanical properties of adult chests. *Comput Methods Programs Biomed*. 242:107847.
- Lim H et al. (2024). Variable stiffness and damping mechanism for CPR manikin. *IEEE J Transl Eng Health Med*. 12:542-549.

### Infant/Pediatric
- Babic N et al. (2017). Test protocol to evaluate infant CPR training manikins. *Proc IEEE MeMeA*. 1-6.
- Thielen M et al. (2017). Innovative design for CPR manikins based on human-like thorax. *Proc Inst Mech Eng H*. 231(3):243-249.
- Papastamelos C et al. (1995). Developmental changes in chest wall compliance. *J Appl Physiol*. 78(1):179-184.

### Animal Surrogate (Neonatal Compression)
- O'Reilly M, Schmölzer GM et al. (2023). Comparison of hemodynamic effects of chest compression delivered via machine or human in asphyxiated piglets. *Pediatric Research*. doi:10.1038/s41390-023-2827-1.
  - Neonatal piglet model: 2.12 ± 0.17 kg, 0-3 days old
  - Validated CPR model matching term infant weight
  - Force recorded during mechanical compressions (stiffness derivable)

### Ventilation Mechanics
- Huang J et al. (2016). Reference values for resistance and compliance in healthy infants. *J Thorac Dis*. 8(3):513-519.
- Battisti O et al. (2012). Lung compliance and airways resistance in healthy neonates. *Pediatr Therapeut*. 2(2):114.

---

## Notes

- This paper fills the ventilation fidelity gap identified in the perspective paper
- Unique contribution: first systematic compression + ventilation benchmark
- Data-centric framing required for special issue fit
- Consider physics-informed modeling component for stronger fit
- **Terminology:** "Mechanical fidelity" chosen to contrast with visual "high fidelity" (see DR-004)
