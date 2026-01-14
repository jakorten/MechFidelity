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

This section describes the standardized methodology for quantifying manikin mechanical properties, building on validated measurement apparatus from prior work [6]. The protocol addresses both compression and ventilation characterization with explicit uncertainty quantification following GUM guidelines [14].

### 4.1 Measurement Philosophy

Two fundamental principles guide the characterization protocol:

**In phantoma validation:** Sensors and mechanical properties must be characterized in the integrated system configuration, not in isolation. Our prior work demonstrated a 5.6% calibration shift between isolated (*ex phantoma*) and integrated (*in phantoma*) sensor configurations [6], confirming that component specifications cannot predict system-level behavior.

**SI traceability:** All measurements trace to SI primary standards through a documented chain: (1) SI primary standards → (2) reference instruments (mass flow meter, calibrated calipers) → (3) automated actuation system → (4) manikin under test. This hierarchy ensures measurement validity and inter-laboratory reproducibility.

### 4.2 Compression Characterization Apparatus

#### 4.2.1 Hardware Configuration

The compression test apparatus comprises:

- **Actuation:** CNC linear actuator (BlackBox X32 controller, GrblHAL firmware) with ±0.01 mm positioning accuracy
- **Displacement measurement:** VL53L4CD time-of-flight (ToF) sensor (STMicroelectronics), 940 nm VCSEL, 1 mm resolution, 0–50 mm range, 50 Hz sampling
- **Reference standard:** Mitutoyo CD-15CPX digital caliper (±0.01 mm), cross-validated with Mitutoyo LH-600 Linear Height Gage
- **Force measurement:** Load cell integrated with actuator [specifications to be added based on available equipment]
- **Environmental monitoring:** SHT45 temperature/humidity sensor (±0.1°C, ±1.0% RH)
- **Data acquisition:** STM32F405 microcontroller with synchronized sampling

#### 4.2.2 Test Protocol

**Pre-test preparation:**
1. Thermal stabilization: 30-minute warm-up period (τ = 12.3 min thermal time constant)
2. Environmental logging: Record ambient temperature (22±2°C) and humidity (45±5% RH)
3. Zero calibration: Verify actuator home position against reference caliper

**Compression cycle protocol:**
1. Position actuator at manikin chest surface (0 mm reference)
2. Execute controlled compression to target depth (e.g., 40 mm for infant, 50 mm for adult)
3. Record force and displacement at 50 Hz throughout compression and release phases
4. Return to surface position
5. Inter-cycle pause (2 seconds) to allow tissue recovery

**Test sequence:**
- Depth sweep: 10, 20, 30, 40, 50 mm (5 depths × 20 cycles = 100 cycles)
- Rate variation: 100, 110, 120 CPM at 40 mm depth (3 rates × 20 cycles = 60 cycles)
- Extended cycling: 150 consecutive cycles at 40 mm to assess fatigue/drift

#### 4.2.3 Derived Parameters

From force-displacement data, extract:

**Stiffness ($k$):** Slope of force-displacement curve
$$k = \frac{\Delta F}{\Delta x} \quad \text{[N/mm]}$$

**Damping ($d$):** From hysteresis loop analysis
$$d = \frac{W_{loop}}{2\pi f A^2} \quad \text{[N·s/mm]}$$

where $W_{loop}$ is the hysteresis loop area, $f$ is compression frequency, and $A$ is displacement amplitude.

**Nonlinearity index:** Fit to Gruben polynomial model [8]:
$$F = k_1 z + k_2 z^2 + k_3 z^3 + k_4 z^4 + d_0 \dot{z} + d_1 z \dot{z}$$

Report the ratio of higher-order coefficients to linear coefficient as a nonlinearity metric.

### 4.3 Ventilation Characterization Apparatus

#### 4.3.1 Hardware Configuration

The ventilation test apparatus comprises:

- **Actuation:** Linear actuator with 100 mL calibration syringe, pneumatic valve control (pressure, vacuum, bleed valves)
- **Flow measurement:** Sensirion SDP810-500Pa differential pressure sensor (DPS), ±0.75% of reading, 0–500 Pa range, 100 Hz sampling
- **Reference standard:** Bronkhorst FLEXI-FLOW Compact mass flow meter (MFM), SI-traceable certificate, ±0.8% accuracy
- **Volume derivation:** $V = \int K \sqrt{|\Delta P(t)|} \, dt$, where $K$ is the configuration-specific calibration coefficient
- **Environmental monitoring:** SHT45 temperature/humidity sensor
- **Data acquisition:** STM32F405 microcontroller

#### 4.3.2 Test Protocol

**Pre-test preparation:**
1. Leak test: Verify airway seal integrity
2. Configuration-specific calibration: Determine $K$ coefficient for each manikin (in phantoma)
3. Environmental logging: Record temperature and humidity

**Ventilation cycle protocol:**
1. Actuator delivers controlled volume through manikin airway
2. Record differential pressure and reference flow simultaneously at 100 Hz
3. Compute delivered volume via pressure integration
4. Compare against MFM reference

**Test sequence:**
- Volume sweep: 12.25, 24.5, 36.75, 49.0, 61.25, 73.5 mL (6 volumes × 100 cycles = 600 cycles)
- Clinical target emphasis: Additional 200 cycles at guideline-recommended volume (e.g., 24.5 mL for 3.5 kg infant)

#### 4.3.3 Derived Parameters

**Compliance ($C_{rs}$):**
$$C_{rs} = \frac{V_{delivered}}{P_{peak} - P_{baseline}} \quad \text{[mL/cmH}_2\text{O]}$$

**Resistance ($R_{rs}$):**
$$R_{rs} = \frac{P_{peak} - P_{plateau}}{\dot{V}_{peak}} \quad \text{[cmH}_2\text{O/L/s]}$$

where $P_{peak}$ is peak inspiratory pressure, $P_{plateau}$ is plateau pressure (during inspiratory hold), and $\dot{V}_{peak}$ is peak flow rate.

### 4.4 Uncertainty Quantification

Following GUM methodology [14], measurement uncertainty comprises:

**Type A (statistical):** Evaluated from repeated measurements
$$u_A = \frac{s}{\sqrt{n}}$$

where $s$ is sample standard deviation and $n$ is number of observations.

**Type B (systematic):** Evaluated from reference standard specifications, calibration certificates, and environmental factors
$$u_B = \sqrt{\sum_i u_{B,i}^2}$$

**Combined uncertainty:**
$$u_c = \sqrt{u_A^2 + u_B^2}$$

**Expanded uncertainty:** Reported at 95% confidence level
$$U = k \cdot u_c \quad (k = 2)$$

#### 4.4.1 Uncertainty Budget: Compression

| Source | Type | Contribution |
|--------|------|--------------|
| Reference caliper | B | ±0.01 mm |
| ToF sensor repeatability | A | ~0.3% CV |
| Actuator positioning | B | ±0.01 mm |
| Temperature effects | B | [to be characterized] |
| **Combined (k=2)** | — | **±2.23 mm** |

#### 4.4.2 Uncertainty Budget: Ventilation

| Source | Type | Contribution |
|--------|------|--------------|
| MFM reference standard | B | ±0.8% |
| DPS repeatability | A | ~3.3% CV |
| Calibration residuals | B | [configuration-specific] |
| Temperature effects | B | [to be characterized] |
| **Combined (k=2)** | — | **±2.29%** |

### 4.5 Manikins Under Test

The characterization protocol will be applied to a representative sample of commercial manikins:

**Table 8: Manikins under test**

| Manufacturer | Model | Type | Age Category |
|--------------|-------|------|--------------|
| Laerdal | Resusci Baby QCPR | Training | Infant |
| Laerdal | Little Junior QCPR | Training | Child |
| Laerdal | Resusci Anne QCPR | Training | Adult |
| Ambu | Ambu Baby | Training | Infant |
| [Additional] | [TBD] | — | — |

**Unit-to-unit variation:** Where possible, multiple units of the same model will be tested to characterize manufacturing consistency.

### 4.6 Data Management

All raw data, derived parameters, and uncertainty calculations will be archived in structured format (JSON/CSV) with:
- Unique test identifier
- Manikin serial number
- Environmental conditions
- Complete time-series data
- Derived mechanical parameters with uncertainties

Data will be made available as supplementary material to enable independent verification and meta-analysis.

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

### 7.1 Principal Findings

This work presents the first systematic framework for quantifying the engineering fidelity of CPR training manikins against human biomechanical reference data. Three principal findings emerge:

**First, comprehensive human reference data exists but has not been applied to manikin validation.** The Ruiz de Gauna dataset (n=615 OHCA patients, 1.15M compressions) provides statistically robust chest compression mechanics parameters [5], while the Huang dataset (n=205 infants) provides infant ventilation mechanics [11]. These datasets enable construction of evidence-based reference envelopes rather than relying on expert opinion or anatomical assumptions.

**Second, anatomical fidelity does not guarantee functional fidelity.** The Thielen et al. [3] design achieved correct *shape* of nonlinear force-displacement behavior through anatomical mimicry, but incorrect *magnitude*—their manikin was "considerably lower" in stiffness than human reference values. This exemplifies the form-function distinction: high anatomical fidelity (form) is neither necessary nor sufficient for high engineering fidelity (function).

**Third, system-level validation is essential.** Our prior work demonstrated 5.6% calibration shifts between isolated and integrated sensor configurations [6], with 120–130× deviations from component datasheet predictions. This confirms that manikin mechanical properties must be characterized *in phantoma*, not inferred from component specifications.

### 7.2 Implications for Manikin Design

The engineering fidelity framework has direct implications for manikin design philosophy:

**Target functional equivalence, not structural mimicry.** A simplified mechanism (e.g., tuned spring-damper system) that produces correct force-displacement behavior is functionally equivalent to anatomical complexity for skill transfer purposes. The trainee's muscles respond to mechanical feedback, not internal anatomy.

**Validate at system level.** Component-level specifications are insufficient. Mechanical properties emerge from the integrated system and must be measured accordingly.

**Account for compression/recoil asymmetry.** Human chest damping during recoil is 1.7× higher than during compression [5]. Current manikins with symmetric spring-damper behavior cannot replicate this physiologically important characteristic.

**Consider time-varying properties.** Human chest stiffness decreases ~35% during sustained CPR [5]. Static manikin characterization may miss clinically relevant dynamics.

### 7.3 Implications for Training

If manikins deviate substantially from human mechanical properties, what are the consequences for skill transfer?

**Force calibration:** Trainees who learn on overly soft manikins may apply insufficient force during real CPR; those trained on overly stiff manikins may apply excessive force, risking injury.

**Rate adaptation:** The natural compression rate that "feels right" depends on the mechanical feedback. Incorrect stiffness may lead to rate deviations in clinical practice.

**Ventilation technique:** Airway resistance and compliance affect the "feel" of bag-mask ventilation. Manikins with unrealistic ventilation mechanics may poorly prepare trainees for real infant airways.

The Engineering Fidelity Index provides a quantitative basis for evaluating whether specific fidelity gaps are likely to affect skill transfer—enabling evidence-based rather than assumption-based training device selection.

### 7.4 Relationship to Simulation Fidelity Literature

This work operationalizes concepts from the simulation fidelity literature:

**Norman et al. [2]** found "minimal relationship between simulation fidelity and transfer of learning," but their analysis focused on *physical* (visual) fidelity, not *functional* (mechanical) fidelity. Engineering fidelity is a distinct construct.

**Hamstra et al. [1]** called for "reconsidering fidelity" with emphasis on functional task alignment. The EFI framework directly addresses this call by quantifying the functional parameters relevant to CPR skill acquisition.

**Psychological fidelity** (stress, realism) remains outside the scope of this mechanical characterization but represents an important complementary dimension for comprehensive manikin evaluation.

### 7.5 Limitations

Several limitations constrain the current work:

**Adult compression vs. infant focus.** The most robust human reference data (Ruiz de Gauna) characterizes adult chest mechanics. Infant and pediatric chest biomechanics remain poorly characterized, limiting validation of infant manikins against human ground truth.

**Static characterization.** The protocol characterizes steady-state mechanical properties. Dynamic changes during extended CPR (fatigue, softening) are acknowledged in the reference model but not yet implemented in manikin testing.

**Limited manikin sample.** [Specific limitations to be documented based on actual testing conducted.]

**Single-site validation.** Inter-laboratory reproducibility has not yet been established, though the standardized protocol and SI traceability are designed to enable this.

### 7.6 Future Directions

Several extensions would strengthen the engineering fidelity framework:

1. **Pediatric biomechanical studies:** Clinical characterization of infant/child chest mechanics to establish age-appropriate reference envelopes

2. **Dynamic characterization:** Time-varying mechanical properties during sustained compressions

3. **Multi-center validation:** Inter-laboratory comparison to establish protocol reproducibility

4. **Training outcome correlation:** Prospective studies linking EFI scores to clinical skill transfer

5. **Manufacturer engagement:** Collaboration with manikin manufacturers to integrate engineering fidelity into design specifications

---

## 8. Conclusion

This paper presents a data-driven framework for quantifying the engineering fidelity of CPR training manikins. By synthesizing published clinical datasets, we construct human reference envelopes for chest compression mechanics (adults) and ventilation mechanics (infants). A standardized characterization protocol with SI-traceable measurements and GUM-compliant uncertainty quantification enables objective comparison between manikins and human reference data.

The Engineering Fidelity Index (EFI) transforms qualitative assessments ("high fidelity," "realistic feel") into quantitative metrics actionable for procurement decisions, regulatory standards, and design optimization. Rather than assuming that expensive, visually realistic manikins provide superior training, the EFI enables evidence-based evaluation of the mechanical properties that actually matter for skill transfer.

Key findings include:

1. **Comprehensive human reference data exists** for adult compression mechanics (n=615 patients) and infant ventilation mechanics (n=205 infants), enabling evidence-based manikin validation

2. **Anatomical fidelity ≠ functional fidelity:** Prior work achieving anatomical mimicry failed to match human force-displacement magnitude, demonstrating that form is neither necessary nor sufficient for function

3. **System-level validation is essential:** Component specifications cannot predict integrated system behavior; in phantoma characterization is required

4. **Critical gap identified:** Infant chest compression biomechanics remain uncharacterized, limiting validation of infant manikins against human ground truth

The engineering fidelity framework provides the measurement science foundation for a paradigm shift: from assumption-based to evidence-based CPR training device evaluation. We call for manufacturer transparency regarding mechanical specifications, regulatory standards incorporating engineering fidelity requirements, and continued clinical research to fill the identified evidence gaps.

---

## Acknowledgments

[To be added]

## Author Contributions

[To be added]

## Conflicts of Interest

The authors declare no conflicts of interest.

## Data Availability

Raw characterization data and analysis scripts will be made available as supplementary material upon publication.

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

[14] JCGM 100:2008. Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM). Joint Committee for Guides in Metrology.

[15] ISO 5725-1:1994. Accuracy (trueness and precision) of measurement methods and results — Part 1: General principles and definitions.

---

*Draft document - not for distribution*
