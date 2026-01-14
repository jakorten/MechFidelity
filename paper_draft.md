# Engineering Fidelity of CPR Training Manikins: A Data-Driven Reference Model for Chest Compression and Ventilation Mechanics

**Target:** Measurement Science and Technology - Special Issue on "Data-Centric Exploration and Explanation of Physical and Engineering Phenomena"

**Authors:** [To be confirmed]

**Draft version:** 0.1 (January 2026)

---

## Abstract

Cardiopulmonary resuscitation (CPR) training manikins are assumed to provide realistic haptic feedback, yet their mechanical properties are rarely validated against human biomechanical reference data. This paper presents a data-driven reference model for CPR manikin characterization, synthesizing published clinical datasets on chest compression mechanics (n=615 adult patients) and infant ventilation mechanics (n=205 healthy infants). We propose a standardized characterization protocol for quantifying manikin stiffness, damping, compliance, and resistance, and introduce an Engineering Fidelity Index (EFI) that enables objective comparison between manikins and human reference envelopes. Application of this framework to multiple commercial manikins reveals [results to be added]. This work provides the measurement science foundation for evidence-based manikin selection and design.

**Keywords:** cardiopulmonary resuscitation, medical simulation, biomechanical characterization, measurement uncertainty, engineering fidelity

---

## 1. Introduction

### 1.1 Background and Motivation

Cardiopulmonary resuscitation (CPR) training relies on surrogate patients—manikins—to develop the psychomotor skills required for effective chest compressions and ventilations. The fidelity of these training devices, that is, their similarity to real human patients, is assumed to influence skill transfer to clinical practice [1,2]. Yet while considerable research has addressed *psychological fidelity* (stress induction, scenario realism) and *visual fidelity* (anatomical appearance), the *engineering fidelity*—the measurable mechanical behavior of the manikin relative to human biomechanics—remains largely uncharacterized.

Current CPR manikins employ simplified mechanical systems, typically a single spring-damper configuration, that produce a linear or weakly nonlinear force-displacement response [3]. Human thorax behavior, in contrast, exhibits pronounced nonlinearity, hysteresis, and time-dependent softening during sustained compressions [4,5]. This mismatch raises a fundamental question: **How closely do training manikins approximate the mechanical response of the human body they purport to simulate?**

### 1.2 The Engineering Fidelity Gap

Previous work has approached manikin characterization from two directions:

**Anatomical fidelity approaches** have sought to replicate human anatomy with increasing precision. Thielen et al. [3] developed an infant manikin with 3D-printed ribs, anatomically shaped lungs, and embedded cardiovascular structures. While their design exhibited nonlinear force-displacement behavior qualitatively similar to humans, the authors acknowledged that "the force required to achieve similar compression depths in humans is considerably higher" [3]—indicating that anatomical mimicry does not guarantee functional equivalence.

**Component-level specifications** from manufacturers provide nominal stiffness values, but these are typically measured *ex phantoma* (isolated components) rather than *in phantoma* (integrated system). Our prior work demonstrated calibration shifts of 5.6% when sensors were integrated into manikins, with deviations of 120–130× from datasheet specifications [6]. This finding suggests that system-level characterization is essential.

**The critical gap** is the absence of:
1. A systematically derived human reference model against which manikins can be evaluated
2. A standardized protocol for manikin mechanical characterization
3. A quantitative metric for engineering fidelity that enables objective comparison

### 1.3 Contribution

This paper addresses these gaps through a data-centric approach:

1. **Human Reference Model:** We synthesize published clinical datasets to construct reference envelopes for:
   - Chest compression mechanics (stiffness, damping, nonlinearity) from adult OHCA patients
   - Ventilation mechanics (compliance, resistance) from healthy infants

2. **Characterization Protocol:** We propose a standardized measurement methodology for quantifying manikin mechanical properties with explicit uncertainty budgets.

3. **Engineering Fidelity Index (EFI):** We introduce a composite metric that quantifies the deviation between a manikin's measured response and the human reference envelope, enabling objective ranking for procurement and design decisions.

4. **Empirical Benchmark:** We apply this framework to characterize multiple commercial manikins, providing the first systematic compression-and-ventilation fidelity comparison.

### 1.4 Paper Organization

Section 2 presents the construction of human reference models from published literature. Section 3 defines the uncertainty envelope accounting for natural human variability. Section 4 describes the manikin characterization protocol. Section 5 presents empirical results. Section 6 introduces the Engineering Fidelity Index. Section 7 discusses implications and limitations, and Section 8 concludes.

---

## 2. Human Reference Model Construction

The reference model synthesizes published clinical and biomechanical data to establish the target mechanical behavior that a high-fidelity manikin should approximate. We address chest compression mechanics (Section 2.1) and ventilation mechanics (Section 2.2) separately, as these involve distinct physiological systems and measurement approaches.

### 2.1 Chest Compression Mechanics

#### 2.1.1 Viscoelastic Model Framework

The human thorax under compression is well-characterized by a viscoelastic model comprising elastic (spring) and viscous (damper) components [4,7,8]. The applied force F(t) relates to chest displacement x(t) and velocity v(t) as:

$$F(t) = F_e(t) + F_d(t) = k \cdot x(t) + d \cdot v(t)$$

where:
- $k$ = elastic coefficient (stiffness), units: N/cm or N/mm
- $d$ = damping coefficient (viscosity), units: N·s/cm or N·s/mm

Critically, the damping behavior differs between compression and recoil phases [5], motivating a model with separate coefficients:

$$F_c(t) = k \cdot x_c(t) + d_c \cdot v_c(t) \quad \text{(compression)}$$

$$F_r(t) = k \cdot x_r(t) - d_r \cdot v_r(t) \quad \text{(recoil)}$$

where $d_c$ and $d_r$ are the compression and recoil damping coefficients, respectively.

#### 2.1.2 Reference Data: Ruiz de Gauna et al. (2023)

The most comprehensive human dataset comes from Ruiz de Gauna et al. [5], who analyzed **1,156,608 chest compressions from 615 adult out-of-hospital cardiac arrest (OHCA) patients**. This dataset provides statistically robust reference values with explicit confidence intervals.

**Table 1: Human chest mechanical properties at CPR initiation (Ruiz de Gauna 2023)**

| Parameter | Mean | 95% CI | Unit |
|-----------|------|--------|------|
| Stiffness ($k$) | 104.9 | 102.0–107.8 | N/cm |
| Compression damping ($d_c$) | 2.868 | 2.751–2.984 | N·s/cm |
| Recoil damping ($d_r$) | 4.889 | 4.648–5.129 | N·s/cm |

**Key findings:**
- Recoil damping is **1.7× higher** than compression damping (p < 0.001)
- Women have lower stiffness than men (96.8 vs. 109.2 N/cm)
- Stiffness decreases ~35% after 3000 compressions
- The viscoelastic model achieves R² = 97.9% fit to measured data

#### 2.1.3 Reference Data: Force-Displacement Relationship

Tomlinson et al. [9] characterized force-displacement during actual OHCA CPR:

**Table 2: Force-displacement reference values (Tomlinson 2007)**

| Parameter | Value | Note |
|-----------|-------|------|
| Mean applied force | 297 ± 80 N | At guideline-compliant depth |
| Mean compression depth | 42 ± 8 mm | During OHCA CPR |
| Force for 38mm depth | < 490 N | 96% of patients |

#### 2.1.4 Live Tissue vs. Cadaver

A critical methodological consideration comes from Arbogast et al. [10], who compared live (perfused) tissue response to post-mortem cadaver data:

| Condition | Force at 40mm Deflection |
|-----------|--------------------------|
| Live CPR (perfused tissue) | **286 N** |
| Post-mortem cadaver | **588 N** |

**Implication:** Live human tissue is approximately **2× softer** than cadaver tissue. Reference models derived from cadaver studies may substantially overestimate the stiffness target for manikin design.

#### 2.1.5 Nonlinear Behavior

Human thorax exhibits nonlinear force-displacement with characteristic hysteresis [4,8]. Gruben et al. [8] modeled this behavior as:

$$F = k_1 z + k_2 z^2 + k_3 z^3 + k_4 z^4 + d_0 \dot{z} + d_1 z \dot{z}$$

where $z$ is displacement and $\dot{z}$ is velocity. The presence of higher-order terms ($k_2$, $k_3$, $k_4$) distinguishes human behavior from the linear response ($F = k_1 z$) typical of simple spring-based manikins.

#### 2.1.6 Adult Compression Reference Envelope

Synthesizing the above sources, we define the adult chest compression reference envelope:

**Table 3: Adult chest compression reference envelope**

| Parameter | Lower Bound | Upper Bound | Source |
|-----------|-------------|-------------|--------|
| Stiffness ($k$) | 92 N/cm | 113 N/cm | Ruiz de Gauna 2023 (±2 SD) |
| Compression damping ($d_c$) | 2.4 N·s/cm | 3.3 N·s/cm | Ruiz de Gauna 2023 |
| Recoil damping ($d_r$) | 4.0 N·s/cm | 5.8 N·s/cm | Ruiz de Gauna 2023 |
| Force at 50mm | 200 N | 500 N | Tomlinson 2007, Lim 2024 |
| Behavior | Nonlinear with hysteresis | — | Multiple sources |
| Compression/recoil asymmetry | Required | — | Ruiz de Gauna 2023 |

### 2.2 Ventilation Mechanics

#### 2.2.1 Respiratory System Model

The respiratory system is characterized by compliance (C) and resistance (R):

$$C_{rs} = \frac{\Delta V}{\Delta P} \quad \text{(compliance: volume change per pressure change)}$$

$$R_{rs} = \frac{\Delta P}{\dot{V}} \quad \text{(resistance: pressure per flow rate)}$$

where $\Delta V$ is tidal volume, $\Delta P$ is pressure change, and $\dot{V}$ is flow rate.

#### 2.2.2 Reference Data: Huang et al. (2016)

Huang et al. [11] measured respiratory mechanics in **205 healthy infants aged 1–96 weeks** using the single occlusion technique (SOT):

**Table 4: Infant respiratory mechanics reference values (Huang 2016)**

| Age Group | Resistance (kPa/L/s) | Compliance (mL/kPa) |
|-----------|---------------------|---------------------|
| 1–24 weeks | 6.39 (median) | 77.95 ± 46.16 |
| 25–48 weeks | 5.11 | 123.51 ± 50.64 |
| 49–72 weeks | 4.20 | 141.17 ± 44.75 |
| 73–96 weeks | 3.74 | 170.58 ± 50.14 |
| **Overall** | **5.04** (range: 3.73–6.82) | **119.52 ± 60.47** |

**Developmental pattern:**
- Resistance **decreases** with age (larger airways)
- Compliance **increases** with age (more elastic tissue, larger lungs)

#### 2.2.3 Reference Data: Battisti et al. (2012)

Battisti et al. [12] provided longitudinal neonatal data (n=32 healthy neonates):

**Table 5: Neonatal respiratory mechanics (Battisti 2012)**

| Day | Compliance (mL/cmH₂O) | Resistance (cmH₂O/mL/s) |
|-----|----------------------|-------------------------|
| 1 | 1.37 ± 0.37 | 0.048 ± 0.17 |
| 3 | 1.60 ± 0.40 | 0.057 ± 0.020 |
| 7 | 1.67 ± 0.41 | 0.052 ± 0.012 |
| 14 | 1.62 ± 0.44 | 0.057 ± 0.013 |

**Key findings:**
- Compliance increases ~20% in first week post-birth
- Female neonates have higher compliance
- More premature infants have higher resistance

#### 2.2.4 Infant Ventilation Reference Envelope

**Table 6: Infant ventilation reference envelope**

| Parameter | Lower Bound | Upper Bound | Age Range | Source |
|-----------|-------------|-------------|-----------|--------|
| Compliance ($C_{rs}$) | 78 mL/kPa | 171 mL/kPa | 1–96 weeks | Huang 2016 |
| Resistance ($R_{rs}$) | 3.74 kPa/L/s | 6.39 kPa/L/s | 1–96 weeks | Huang 2016 |

*Note: Unit conversion: 1 kPa ≈ 10.2 cmH₂O*

### 2.3 Critical Evidence Gap: Infant Chest Compression Mechanics

A systematic review of the literature reveals a **critical gap**: no comprehensive biomechanical characterization of infant chest compression mechanics exists.

**Table 7: Evidence availability by domain**

| Domain | Human Reference Data | Manikin Characterization |
|--------|---------------------|-------------------------|
| Adult compression | ✓ Extensive (n=615) | Limited |
| Infant ventilation | ✓ Available (n=205) | **None found** |
| **Infant compression** | **None found** | Design studies only [3] |

Existing infant manikin designs (e.g., Thielen et al. [3]) are based on anatomical considerations and expert opinion rather than biomechanical validation against human infant data. This represents both a limitation of the current work and an opportunity for future research.

---

## 3. Uncertainty Envelope Definition

### 3.1 Rationale

Human biomechanics exhibit natural variability due to differences in age, sex, body composition, and pathophysiology. A realistic reference model should define an **acceptable range** (envelope) rather than a single target value. Manikins falling within this envelope demonstrate adequate engineering fidelity; those outside can be quantified by their deviation.

### 3.2 Envelope Construction Method

For each mechanical parameter, the reference envelope is constructed as:

$$\text{Envelope} = [\mu - k \cdot \sigma, \mu + k \cdot \sigma]$$

where:
- $\mu$ = population mean from reference dataset
- $\sigma$ = population standard deviation
- $k$ = coverage factor (typically k=2 for ~95% coverage)

When 95% confidence intervals are available directly from the source (as in Ruiz de Gauna 2023), these are used as the envelope bounds.

### 3.3 Handling Asymmetric Distributions

For parameters with skewed distributions (e.g., resistance values from Huang 2016), the envelope is defined using reported percentiles:

$$\text{Envelope} = [P_{2.5}, P_{97.5}]$$

or median with interquartile range when percentiles are unavailable.

### 3.4 Age-Stratified Envelopes

For infant ventilation mechanics, where parameters vary systematically with developmental age, age-stratified envelopes are defined. A manikin designed to represent a 6-month-old infant should be compared against the 25–48 week reference envelope, not the overall population.

---

## 4. Manikin Characterization Protocol

*[Section 4 will detail the measurement apparatus, test procedures, and uncertainty analysis for both compression and ventilation characterization. To be drafted after empirical methodology is confirmed.]*

---

## 5. Results

*[Section 5 will present empirical characterization data for multiple manikins. To be completed after data collection.]*

---

## 6. Engineering Fidelity Index

### 6.1 Concept

The Engineering Fidelity Index (EFI) quantifies how closely a manikin's mechanical response approximates the human reference envelope. A manikin perfectly matching the envelope center scores EFI = 1.0; deviations reduce the score proportionally.

### 6.2 Component Scores

**Compression Fidelity Score (CFS):**

$$CFS = 1 - \frac{1}{N} \sum_{i=1}^{N} \frac{|m_i - \mu_i|}{\sigma_i}$$

where $m_i$ is the manikin's measured value for parameter $i$, $\mu_i$ is the human reference mean, and $\sigma_i$ is the reference standard deviation.

**Ventilation Fidelity Score (VFS):**

Analogously defined for compliance and resistance parameters.

### 6.3 Combined Engineering Fidelity Index

$$EFI = w_c \cdot CFS + w_v \cdot VFS$$

where $w_c$ and $w_v$ are weighting factors reflecting the relative importance of compression and ventilation fidelity for the intended training application.

---

## 7. Discussion

*[To be drafted after results are available.]*

---

## 8. Conclusion

*[To be drafted after discussion.]*

---

## References

[1] Hamstra SJ, Brydges R, Hatala R, et al. Reconsidering fidelity in simulation-based training. *Acad Med*. 2014;89(3):387-392.

[2] Norman G, Dore K, Grierson L. The minimal relationship between simulation fidelity and transfer of learning. *Med Educ*. 2012;46(7):636-647.

[3] Thielen M, Joshi R, Delbressine F, Bambang Oetomo S, Feijs L. An innovative design for cardiopulmonary resuscitation manikins based on a human-like thorax and embedded flow sensors. *Proc Inst Mech Eng H*. 2017;231(3):243-249.

[4] Bankman IN, Gruben KG, Halperin HR, et al. Identification of dynamic mechanical parameters of the human chest during manual cardiopulmonary resuscitation. *IEEE Trans Biomed Eng*. 1990;37(2):211-217.

[5] Ruiz de Gauna S, Gutiérrez JJ, Sandoval CL, et al. Characterization of mechanical properties of adult chests during pre-hospital manual chest compressions through a simple viscoelastic model. *Comput Methods Programs Biomed*. 2023;242:107847.

[6] [IEEE TIM paper reference - to be added]

[7] Tsitlik JE, Weisfeldt ML, Chandra N, et al. Elastic properties of the human chest during cardiopulmonary resuscitation. *Crit Care Med*. 1983;11(9):685-692.

[8] Gruben KG, Halperin HR, Popel AS, Tsitlik JE. Canine sternal force-displacement relationship during cardiopulmonary resuscitation. *IEEE Trans Biomed Eng*. 1999;46(7):788-796.

[9] Tomlinson AE, Nysaether J, Kramer-Johansen J, Steen PA, Dorph E. Compression force-depth relationship during out-of-hospital cardiopulmonary resuscitation. *Resuscitation*. 2007;72(3):364-370.

[10] Arbogast KB, Maltese MR, Nadkarni VM, Steen PA, Nysaether JB. Anterior-posterior thoracic force-deflection characteristics measured during cardiopulmonary resuscitation: comparison to post-mortem human subject data. *Stapp Car Crash J*. 2006;50:131-145.

[11] Huang J, Zhang H, Zhang M, Zhang X, Wang L. Reference values for resistance and compliance based on the single occlusion technique in healthy infants from Southeast China. *J Thorac Dis*. 2016;8(3):513-519.

[12] Battisti O, Bertrand JM, Rouatbi H, Escandar G. Lung compliance and airways resistance in healthy neonates. *Pediatr Therapeut*. 2012;2(2):114.

[13] Lim H, et al. Variable stiffness and damping mechanism for CPR manikin to simulate mechanical properties of human chest. *IEEE J Transl Eng Health Med*. 2024;12:542-549.

---

*Draft document - not for distribution*
