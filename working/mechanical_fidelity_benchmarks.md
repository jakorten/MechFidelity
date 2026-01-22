# Mechanical Fidelity Benchmarks: Literature Review

**Date:** 2025-12-20
**Purpose:** Summarize available biomechanical data for CPR manikin mechanical fidelity requirements
**Context:** Supporting evidence for proposition paper on mechanical fidelity

---

## 1. The Core Question

To validate that a manikin's mechanical response matches human physiology, we need **reference data** — biomechanical benchmarks from actual humans. This note summarizes what exists in the literature.

---

## 2. Adult Thorax Biomechanics

### 2.1 Stiffness Values

| Parameter | Value | Source |
|-----------|-------|--------|
| Human chest stiffness | **4–10 N/mm** (at 50mm depth) | Variable Stiffness Manikin Study, IEEE J-BHI 2024 |
| Human chest damping | 0.08–0.38 N·s/mm (at 30mm) | Same study |
| Commercial manikin range | 5.34–13.59 N/mm | Same study |

**Reference:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11329213/

### 2.2 Force-Depth Relationship (Clinical CPR)

| Parameter | Value | Source |
|-----------|-------|--------|
| Mean applied force | 30.3 ± 8.2 kg (≈297 N) | Tomlinson et al. 2007 |
| Mean compression depth achieved | 42 ± 8 mm | Same study |
| Force required for 38mm depth | <50 kg (490 N) in 96% of patients | Same study |
| Force for guideline-compliant 50mm | 445–556 N (100–125 lbs) | Chest compression force study |

**Reference:** https://pubmed.ncbi.nlm.nih.gov/17141936/

### 2.3 Live vs Cadaver Comparison (Critical Finding)

| Condition | Force at 40mm Deflection | Source |
|-----------|--------------------------|--------|
| Live CPR (perfused tissue) | **286 N** | Arbogast et al. 2006 |
| Post-mortem cadaver | **588 N** | Same study |

**Implication:** Live human tissue is significantly **softer** than cadaver tissue. Cadaver-based benchmarks may overestimate required stiffness.

**Reference:** https://pubmed.ncbi.nlm.nih.gov/17311162/

### 2.4 Non-Linear Behavior

Human chests exhibit:
- **Non-linear** force-displacement (stiffness increases with depth)
- **Hysteresis** (different loading vs unloading curves)
- **Viscoelastic** response (rate-dependent)

Most commercial manikins show **linear** spring behavior — this behavioral mismatch may be more significant than absolute stiffness values.

---

## 3. Manikin Characterization Data

### 3.1 Variable Stiffness Manikin (Resusci Anne QCPR)

| Spring Setting | Stiffness | Peak Force (1st min) | Depth Achieved |
|----------------|-----------|----------------------|----------------|
| Soft | 0.6 kg/mm (5.9 N/mm) | 47.9 ± 16.2 kgf | 51.9 ± 7.6 mm |
| Standard | 0.9 kg/mm (8.8 N/mm) | 52.9 ± 12.7 kgf | 41.3 ± 11.4 mm |
| Hard | 1.2 kg/mm (11.8 N/mm) | 67.9 ± 14.9 kgf | 34.2 ± 11.5 mm |

**Reference:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9573907/

### 3.2 Commercial Manikin Survey (Historical)

Force required at various depths across 8 manikin types:

| Depth | Force Range |
|-------|-------------|
| 1 cm | 6.3–14 kp (62–137 N) |
| 2 cm | 11.6–30 kp (114–294 N) |
| 3 cm | 17–38 kp (167–373 N) |
| 4 cm | 22.5–54 kp (221–530 N) |
| 5 cm | 28.5–69 kp (280–677 N) |

**Key observation:** Spring-based manikins (Ambu Man, Resusci Anne) show linear behavior; foam-based (Little Anne) show decreasing resistance with depth.

**Reference:** https://www.sciencedirect.com/science/article/abs/pii/030095729500874S

### 3.3 Human vs Manikin Comparison

> "Human chests are stiffer (i.e., require greater force to compress a given distance) compared with manikin chests at chest compression depths of 1.5–2 inches."

**Implication:** Commercial manikins may be **too soft**, not too stiff — contrary to initial hypothesis.

---

## 4. Infant/Pediatric Data

### 4.1 What Exists

| Parameter | Value | Source |
|-----------|-------|--------|
| Optimal infant compression force | **3.8–4.3 kg (37–42 N)** | Two-thumb biomechanics study |
| Two-thumb technique force | 4.04 ± 1.83 kg | Same study |
| Two-finger technique force | 3.22 ± 1.11 kg | Same study |
| Target depth (infant) | ≥40 mm | AHA/ERC 2025 guidelines |
| Child (8-22y) force at max deflection | 309 ± 55 N | Maltese 2008 |

**Reference:** https://pubmed.ncbi.nlm.nih.gov/31633625/

### 4.2 The Critical Gap

> "No direct force-displacement curves for human neonates exist in literature."

Manikin stiffness for infants was determined by **expert opinion** — healthcare providers with pediatric CPR experience ranked manikins by "feel" and consensus determined "realistic" stiffness.

**Reference:** https://pubmed.ncbi.nlm.nih.gov/19699023/

**Implication:** There is no ground-truth biomechanical data for infant/neonate thorax. All infant manikin mechanical properties are based on subjective assessment, not objective measurement.

---

## 5. How Systematic Is Manikin Specification? (Critical Finding)

A key question: has manikin mechanical fidelity been established systematically, or ad hoc?

### 5.1 Two Contrasting Approaches

| Aspect | Aase et al. 2008 (Adults) | Tomlinson et al. 2009 (Pediatric) |
|--------|---------------------------|-----------------------------------|
| **Method** | Patient-derived measurement | Expert consensus |
| **Sample** | 59 cardiac arrest patients | 63 healthcare providers |
| **Data collection** | Defibrillator with force sensor + accelerometer during real CPR | Subjective "feels like" assessment |
| **Output** | 8 interchangeable chest profiles covering measured human range | Consensus on which spring "feels right" |
| **Validation** | ±30 N or ±2 mm accuracy at 30-50mm depth | Kappa agreement statistics only |
| **Rigor** | **Systematic — metrologically validated** | **Ad hoc — no objective measurement** |

### 5.2 The Aase 2008 Approach (Gold Standard)

This is **the most rigorous approach found in the literature**:

1. **Measurement:** Chest stiffness and damping of 59 cardiac arrest patients measured during out-of-hospital CPR using instrumented defibrillator
2. **Translation:** Created manikins with 8 interchangeable force-depth profiles representing the measured range
3. **Validation:** Verified using same equipment; accuracy within ±30 N or ±2 mm between 30-50mm depth
4. **Result:** Manikins that demonstrably replicate human chest mechanics

**Reference:** https://pubmed.ncbi.nlm.nih.gov/18990635/

### 5.3 The Tomlinson 2009 Approach (Expert Opinion)

For pediatric manikins, the approach was **not systematic**:

1. **Sample:** Convenience sample of 63 international healthcare providers
2. **Method:** Experts performed compressions on manikins with varying spring stiffness, masked to settings
3. **Task:** Identify which manikin "most closely matched actual children they had treated"
4. **Agreement:**
   - Initial agreement: **43-46%** — barely above chance
   - After excluding "outlier" assessments: ~90%
5. **Validation:** None — no comparison to objective human data

**Critical limitation:** The study explicitly notes "further study is needed to evaluate whether enhanced manikin biofidelity will improve CPR performance" — acknowledging uncertainty about real-world validity.

**Reference:** https://pubmed.ncbi.nlm.nih.gov/19699023/

### 5.4 Summary: Specification by Population

| Population | Systematic Specification? | Method | Source |
|------------|---------------------------|--------|--------|
| **Adult** | **Yes** | Patient-derived measurement (n=59) | Aase 2008 |
| **Child (5y)** | **No** | Expert opinion (43% initial agreement) | Tomlinson 2009 |
| **Infant (6mo)** | **No** | Expert opinion (46% initial agreement) | Tomlinson 2009 |
| **Neonate** | **No data found** | — | — |

### 5.5 No Regulatory Standard Exists

There is **no ISO or regulatory standard** for CPR manikin mechanical properties:

| Standard Body | Requirement | Covers Mechanical Fidelity? |
|---------------|-------------|----------------------------|
| **AHA 2019** | Instrumented feedback (depth, rate) | **No** — feedback only |
| **ISO** | No CPR manikin standard exists | N/A |
| **Manufacturers** | Self-specified | Variable, unvalidated |

### 5.6 Implication for Proposition Paper

This finding strengthens the argument:

> "For adult manikins, one research group (Aase 2008) demonstrated that systematic patient-derived specification is feasible — yet this approach has not been widely adopted. For pediatric and infant manikins — where excessive force risk is arguably highest — specifications rely solely on expert consensus with <50% initial agreement. No regulatory standard mandates mechanical characterization of any kind."

This supports calling for:
1. Adoption of patient-derived specification methodology (Aase approach)
2. Regulatory requirements for mechanical characterization
3. Research to establish pediatric/neonatal biomechanical benchmarks

---

## 6. Upper Bounds: Injury Thresholds

### 6.1 Rib Fracture Incidence

| Population | Fracture Incidence | Source |
|------------|-------------------|--------|
| Adults | 55–97% | Systematic review 2024 |
| Children | 0–2% | Same review |

**Reference:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11458643/

### 6.2 Maximum Recommended Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Maximum depth (adult) | ≤60 mm (2.4 inches) | AHA 2020 |
| Commonly cited fracture threshold | ~60 lbs (270 N) | CPR injury literature |

**Reference:** https://link.springer.com/article/10.1007/s00068-024-02678-6

---

## 7. Derived Requirements (Proposed)

Based on available evidence, defensible mechanical fidelity boundaries:

### 7.1 Adult Manikin

| Dimension | Lower Bound | Upper Bound | Rationale |
|-----------|-------------|-------------|-----------|
| Stiffness | 4 N/mm | 10 N/mm | Human range at 50mm depth |
| Force at 50mm | 200 N | 500 N | Clinical CPR force data |
| Behavior | Non-linear | With hysteresis | Human tissue characteristic |
| Full recoil | Required | — | Guideline requirement |

### 7.2 Infant Manikin

| Dimension | Lower Bound | Upper Bound | Rationale |
|-----------|-------------|-------------|-----------|
| Force at 40mm | 30 N | 50 N | Two-thumb technique data |
| Depth achievable | ≥40 mm | — | AHA/ERC guidelines |
| Stiffness | Unknown | Unknown | **No human reference data exists** |

---

## 8. Implications for the Proposition Paper

### 8.1 Nuance Required

The original hypothesis suggested manikins are "too stiff" leading to excessive force habits. The evidence suggests a more nuanced picture:

1. **Absolute stiffness:** Commercial manikins may actually be **too soft**, not too stiff
2. **Behavioral mismatch:** The **linear vs non-linear** response difference may be more significant
3. **Infant gap:** No biomechanical ground truth exists — this strengthens the call for research

### 8.2 Reframing Options

**Option A: Emphasize behavioral fidelity**
> "Manikins exhibit linear spring behavior while human tissue shows non-linear viscoelastic response with hysteresis — this behavioral mismatch may be more significant than absolute stiffness values."

**Option B: Emphasize the measurement gap**
> "Neither stiffness nor behavioral response of commercial manikins has been validated against human biomechanical data — for infants, no such reference data even exists."

**Option C: Narrow scope to sensors**
> Acknowledge mechanical fidelity gap in discussion, but keep primary argument focused on sensor validity (where we have strong evidence: 5.6% shift, 120-130× deviation).

### 8.3 Recommendation

Given that:
- Sensor validity claims (H1-H2) have strong evidence from own work
- Mechanical fidelity claims (H5-H7) lack definitive human benchmarks
- The stiffness direction may be opposite to initial hypothesis

**Suggested approach:** Lead with sensor validity problem (strong evidence), acknowledge mechanical fidelity as an open question requiring further research, and call for establishment of biomechanical benchmarks as part of the paper's recommendations.

---

## 9. Key Sources

| Topic | Key Reference |
|-------|---------------|
| Human stiffness range | PMC11329213 (IEEE J-BHI 2024) |
| Clinical force-depth | Tomlinson 2007 (Resuscitation) |
| Live vs cadaver | Arbogast 2006 (Stapp Car Crash J) |
| **Systematic adult specification** | **Aase 2008 (Resuscitation)** |
| Manikin characterization | PMC9573907 (Heliyon 2022) |
| Infant force data | PMC (JAHA 2020) |
| Infant stiffness (expert opinion) | Tomlinson 2009 (Resuscitation) |
| Rib fracture incidence | PMC11458643 (Eur J Trauma 2024) |

---

*Document created: 2025-12-20*
*Updated: 2025-12-20 — Added section on systematic vs ad-hoc specification*
*For discussion with: Supervisors/Colleagues*
