# Literature Overview: Mechanical Models for Mechanical Fidelity

**Purpose:** Template models from literature to adapt for infant manikin fidelity assessment
**Created:** 2026-01-18
**Status:** Work in progress

---

## Conceptual Framework

For each domain (ventilation, compression), we need two types of literature:

| Type | Purpose | Example |
|------|---------|---------|
| **MODEL** | Mathematical template describing system behavior | Van Meurs, Gruben |
| **REFERENCE** | Biological target values to compare against | Huang 2016, Lamb data |

```
MODEL (equations)  +  REFERENCE (target values)  →  FIDELITY ENVELOPE  →  TEST MANIKINS
```

---

## Summary Table

| Domain | MODEL Source | REFERENCE Source | Status |
|--------|--------------|------------------|--------|
| **Ventilation** | Van Meurs Ch.9, Hyatt Ch.7 | Huang 2016 (infant, n=205) | ✓ Complete |
| **Compression** | Gruben/Thielen, Lim 2024 | Lamb ~3.5kg (Arjen ten Pas) | Lamb data pending |

**Key insight:** Both domains follow the same equation of motion structure:
- **Ventilation:** P = V/C + R×V̇ (elastic + resistive)
- **Compression:** F = k×d + c×ḋ (elastic + damping)

---

## EQUATION SUMMARY (Quick Reference)

### Ventilation

| Equation | Form | Description |
|----------|------|-------------|
| **Equation of motion** | `P = V/C + R×V̇` | Pressure from elastic + resistive terms |
| Compliance definition | `C = ΔV/ΔP` | Volume change per pressure change |
| Resistance definition | `R = ΔP/V̇` | Pressure drop per flow |
| Series compliance | `1/C_total = 1/C_L + 1/C_cw` | Lung + chest wall in series |

| Symbol | Parameter | Unit | Infant Reference |
|--------|-----------|------|------------------|
| P | Airway pressure | cmH₂O | - |
| V | Volume | mL | Vt = 24.5 mL |
| V̇ | Flow | mL/s or L/s | - |
| C | Compliance | mL/cmH₂O | 7.8 ± 4.6 |
| R | Resistance | cmH₂O·s/L | ~55 |

### Compression

| Equation | Form | Description |
|----------|------|-------------|
| **Equation of motion** | `F = k×d + c×ḋ` | Force from elastic + damping terms |
| **With non-linearity** | `F = k₁d + k₂d² + k₃d³ + k₄d⁴ + d₀ḋ + d₁d·ḋ` | Full Gruben polynomial |
| Stiffness definition | `k = ΔF/Δd` | Force change per displacement |
| Damping definition | `c = ΔF/ḋ` | Force per velocity |

| Symbol | Parameter | Unit | Infant Reference |
|--------|-----------|------|------------------|
| F | Force | N | - |
| d | Displacement | mm | Target: 27 mm |
| ḋ | Velocity | mm/s | - |
| k | Stiffness | N/mm | Pending (lamb) |
| c | Damping | N·s/mm | Pending (lamb) |

### Structural Parallel

| | Ventilation | Compression |
|--|-------------|-------------|
| **Equation** | P = V/C + R×V̇ | F = k×d + c×ḋ |
| **Driving variable** | Pressure P | Force F |
| **State variable** | Volume V | Displacement d |
| **Rate variable** | Flow V̇ | Velocity ḋ |
| **Elastic parameter** | Compliance C | Stiffness k |
| **Resistive parameter** | Resistance R | Damping c |
| **Loop slope** | 1/C | k |
| **Loop width** | 2×R×V̇_max | 2×c×ḋ_max |
| **Loop area** | Work (resistance) | Energy (hysteresis) |

---

## VENTILATION

### Models

#### Van Meurs - Basic Lung Mechanics Model

**Source:** van Meurs WL. *Modeling and Simulation in Biomedical Engineering*. McGraw-Hill. Chapter 9.

**Model Structure:**
```
                    ┌─────────┐
    Pmus(t) ───────►│  Basic  │───► V(t), f(t), Pth(t)
                    │  Lung   │
                    │Mechanics│
                    └─────────┘
```

**Component Diagram:**
- Airway resistance R in series with parallel compliances
- Lung compliance C_L
- Chest wall compliance C_cw
- Muscle pressure generator Pmus(t)

**Mathematical Model:**

State equation (alveolar volume):
```
dV_a(t)/dt = -(C_L + C_cw)/(C_L × C_cw × R) × [V_a(t) - FRC] + (1/R) × Pmus(t)
```

Flow rate:
```
f_a(t) = -(C_L + C_cw)/(C_L × C_cw × R) × [V_a(t) - FRC] + (1/R) × Pmus(t)
```

Intrathoracic pressure:
```
P_th(t) = [V_a(t) - FRC]/C_cw - Pmus(t)
```

**Key Parameters:**
| Parameter | Symbol | Unit | Description |
|-----------|--------|------|-------------|
| Lung compliance | C_L | mL/cmH₂O | Lung tissue elasticity |
| Chest wall compliance | C_cw | mL/cmH₂O | Chest wall elasticity |
| Airway resistance | R | cmH₂O·s/mL | Flow resistance |
| Functional residual capacity | FRC | mL | End-expiratory volume |

**Relevance for Manikins:**
- Single-compartment model suitable for manikin representation
- Parameters C and R directly measurable
- Simplification: manikin has no muscle pressure → passive inflation only

---

#### Hyatt - Resistance and Compliance Definitions

**Source:** Scanlon PD, Hyatt RE. *Hyatt's Interpretation of Pulmonary Function Tests*. 5th ed. Wolters Kluwer, 2019. Chapter 7.

**Resistance Definition:**
```
R = ΔP / V̇
```
- Units: cmH₂O/L/s (or cmH₂O·s/L)
- Rpulm = (Ppl - Pao) / V̇  (includes tissue resistance)
- Raw = (Palv - Pao) / V̇   (airway resistance only)
- Normal adults: 1-3 cmH₂O/L/s
- **Key insight:** Resistance varies inversely with lung volume

**Compliance Definition:**
```
CL = ΔV / ΔP
```
- Units: L/cmH₂O (or mL/cmH₂O)
- Static compliance (CLstat): measured at zero flow
- Dynamic compliance (CLdyn): measured during breathing
- Normal adults: 0.150-0.250 L/cmH₂O (150-250 mL/cmH₂O)
- **Key insight:** Compliance varies directly with lung size

**Respiratory System Compliance (series combination):**
```
1/Crs = 1/CL + 1/Ccw
```
Or using elastance (E = 1/C):
```
Ers = EL + Ecw
```

**Clinical Ranges (Adult):**
| Condition | CLstat | Notes |
|-----------|--------|-------|
| Normal | 150-250 mL/cmH₂O | Varies with size |
| Fibrosis | ~50 mL/cmH₂O | Stiff lungs |
| Emphysema | >500 mL/cmH₂O | Floppy lungs |

---

#### P-V Relationship (Equation of Motion)

**The fundamental equation for respiratory mechanics:**
```
P = V/C + R × V̇
```
Where:
- P = Airway pressure (cmH₂O)
- V = Volume above FRC (mL)
- C = Compliance (mL/cmH₂O)
- R = Resistance (cmH₂O·s/mL or cmH₂O/L/s)
- V̇ = Flow rate (mL/s or L/s)

**This creates a P-V loop because:**
- During **inspiration**: V̇ > 0 → P = V/C + R×(+flow) → higher pressure
- During **expiration**: V̇ < 0 → P = V/C + R×(-flow) → lower pressure

**Loop characteristics:**
| Feature | Determined by |
|---------|---------------|
| Slope of loop | 1/C (compliance) |
| Width of loop | 2 × R × V̇_max (resistance) |
| Loop area | Energy dissipated (work against resistance) |

**Structural parallel with compression:**
| Domain | Elastic term | Resistive term | Equation |
|--------|--------------|----------------|----------|
| Ventilation | V/C | R × V̇ | P = V/C + R×V̇ |
| Compression | k × d | c × ḋ | F = k×d + c×ḋ |

This parallel means the same analysis approach applies to both domains.

---

### Reference Data

#### Battisti 2012 - Neonatal Values

**Source:** Battisti O et al. *Lung Compliance and Airways Resistance in Healthy Neonates*. Pediatr Therapeut 2012.

**Data (healthy neonates, n=32):**

| Parameter | Day 1 | Day 3 | Day 7 | Day 14 | Day 21 |
|-----------|-------|-------|-------|--------|--------|
| Crs (mL/cmH₂O) | 1.37±0.37 | 1.60±0.40 | 1.67±0.41 | 1.62±0.44 | 1.56±0.42 |

**Key Findings:**
- 20% increase in Crs after birth
- Females had significantly higher Crs values
- RDS reduces Crs ~4× in acute phase

#### Huang 2016 - Infant Reference Values (PRIMARY)

**Source:** Huang J et al. *Reference values for resistance and compliance in healthy infants*. J Thorac Dis 2016; 8(3):513-519.

**Reference Data (n=205):**

| Age Range | Compliance | Resistance |
|-----------|------------|------------|
| 1-24 weeks | ~78 mL/kPa (7.8 mL/cmH₂O) | ~6.4 kPa/L/s |
| 73-96 weeks | ~171 mL/kPa | ~3.7 kPa/L/s |

**Target for 3.5 kg infant manikin:**
| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Compliance | C | 7.8 ± 4.6 | mL/cmH₂O |
| Resistance | R | ~55 | cmH₂O·s/L |
| Tidal volume | Vt | 24.5 | mL (7 mL/kg) |

---

## COMPRESSION

### Models

#### Gruben/Thielen - Force-Displacement Model

**Sources:**
- Gruben KG et al. IEEE Trans Biomed Eng 1990, 1999
- Thielen M et al. Proc IMechE Part H 2017

**Model Equation:**
```
F = F_e + F_d
```

Where:
- **Elastic component:** `F_e = k(z) × z`
- **Damping component:** `F_d = μ(z) × ż`

**Nonlinear stiffness:**
```
k(z) = k₁ + k₂·z + k₃·z² + k₄·z³
```

**Displacement-dependent damping:**
```
μ(z) = d₀ + d₁·z
```

**Full polynomial form:**
```
F = k₁·z + k₂·z² + k₃·z³ + k₄·z⁴ + d₀·ż + d₁·z·ż
```

**Key Parameters:**
| Parameter | Symbol | Unit | Description |
|-----------|--------|------|-------------|
| Linear stiffness | k₁ | N/mm | Initial slope |
| Quadratic stiffness | k₂ | N/mm² | Non-linearity |
| Cubic stiffness | k₃ | N/mm³ | Progressive stiffening |
| Quartic stiffness | k₄ | N/mm⁴ | Higher-order term |
| Initial damping | d₀ | N·s/mm | Velocity-dependent loss |
| Depth-dependent damping | d₁ | N·s/mm² | Depth-velocity interaction |

**Thielen 2017 Key Finding:**
- Novel manikin shows nonlinear behavior (k₂, k₃, k₄ non-zero)
- Classical manikins: only k₂ non-zero (nearly linear)
- Human chest: all higher-order terms present

---

#### Lim 2024 - Equation of Motion

**Source:** Lim H et al. *Variable Stiffness and Damping Mechanism for CPR Manikin*. IEEE JTEHM 2024.

**Equation of motion:**
```
F_ext = k×d + c×ḋ
```

Where:
- F_ext = External force (N)
- d = Displacement (mm)
- k = Stiffness (N/mm)
- c = Damping coefficient (N·s/mm)
- ḋ = Velocity (mm/s)

**System ranges achieved:**
| Parameter | Range | Human chest range |
|-----------|-------|-------------------|
| Stiffness | 5.34-13.59 N/mm | 4-10 N/mm (at 50mm) |
| Damping | 0.127-0.511 N·s/mm | 0.08-0.38 N·s/mm |

**Key insight:** Both stiffness AND damping must be controllable to simulate human chest variation.

---

### Reference Data

#### Adult Compression (for context, not our target)

**Sources:** Lim 2024, Tomlinson 2007, Ruiz de Gauna 2023, Neurauter 2009

| Property | Value | Source |
|----------|-------|--------|
| Stiffness at 50mm | 4-10 N/mm | Lim 2024 |
| Damping at 30mm | 0.08-0.38 N·s/mm | Lim 2024 |
| Force for 38mm | 27.5±13.6 kg | Tomlinson 2007 |
| Dynamic softening | -34.6% over 3000 compressions | Ruiz de Gauna 2023 |

**Key Quotes:**
> "Commonly used CPR training manikins...usually have spring loaded chests with a **linear relationship between force and depth**." - Tomlinson 2007

> "Mechanical properties of commercially available CPR training manikins remain constant and **no information on these properties is provided by the manufacturers**." - Lim 2024

#### Infant Compression Reference - PENDING

**Status:** No human infant data exists (ethical constraints)

**Surrogate Reference:** Lamb data (~3.5 kg) from Arjen ten Pas (LUMC) - pending DR-003

---

#### Animal Models in Neonatal Resuscitation Research

| Aspect | Piglet | Lamb |
|--------|--------|------|
| **Primary use** | Chest compression mechanics | Ventilation/fetal transition |
| **Chest mechanics** | Similar to infant | Different geometry |
| **Circulation model** | Postnatal | Fetal → neonatal |
| **Lung state** | Air-filled | Fluid → air transition |
| **Weight** | 1.7-2.4 kg | ~3.5 kg |

**Piglet model:**
- Chest geometry similar to human infant (broader chest)
- Similar chest size and stiffness
- Stiffness: 4.8 N/mm initially, 2.9 N/mm after 200 compressions (Neurauter 2009)
- Well-established for CPR research

**Key piglet reference - Schmölzer 2023:**
- O'Reilly M, Schmölzer GM et al. (2023). *Comparison of hemodynamic effects of chest compression delivered via machine or human in asphyxiated piglets*. Pediatric Research.
- Weight: 2.12 ± 0.17 kg (matches term infant)
- Age: 0-3 days (neonatal)
- Force recorded during mechanical compressions
- **Potential data source:** Force-displacement data for stiffness calculation
- Contact: georg.schmoelzer@me.com (email draft ready)

**Lamb model:**
- Ideal for fetal-to-neonatal transition studies
- Used for ventilation/oxygenation research (fluid-filled → air-filled lungs)
- Larger size allows instrumentation
- Different chest geometry than piglets

**Note:** Piglet data may be more directly relevant for compression mechanics, but lamb data is what's potentially available via LUMC collaboration. Worth confirming with Arjen ten Pas what parameters are typically measured on lambs.

**Required Parameters (same as model):**
| Parameter | Symbol | Unit | Status |
|-----------|--------|------|--------|
| Stiffness | k | N/mm | Pending |
| Non-linearity | k_nl | N/mm² | Pending |
| Damping | μ | N·s/mm | Pending |
| Sample size | n | - | Pending |
| Weight range | - | kg | Pending |

---

## MODEL ADAPTATION FOR INFANT MANIKINS

### Ventilation Model (Simplified for Passive Manikin)

Since manikins have no muscle pressure generator, the model simplifies to:

**Pressure-Volume relationship:**
```
P_aw = V/C + R × dV/dt
```

Where:
- P_aw = Airway pressure (cmH₂O)
- V = Volume (mL)
- C = Total compliance (mL/cmH₂O)
- R = Airway resistance (cmH₂O·s/mL)
- dV/dt = Flow (mL/s)

**P-V Loop:**
- Inflation limb: P = V/C + R×flow (positive flow)
- Deflation limb: P = V/C - R×|flow| (negative flow)
- Loop width proportional to R
- Slope proportional to 1/C

**Target Envelope (Huang 2016):**
- C = 7.8 ± 4.6 mL/cmH₂O
- For Vt = 24.5 mL: P_peak = 2-8 cmH₂O

---

### Compression Model (Simplified for Manikins)

**Quasi-static (low rate):**
```
F = k × d + k_nl × d²
```

**With damping (at CPR rates):**
```
F = k × d + k_nl × d² + μ × ḋ
```

Where:
- k = Linear stiffness (N/mm)
- k_nl = Non-linearity coefficient
- μ = Damping coefficient (N·s/mm)
- d = Displacement (mm)
- ḋ = Velocity (mm/s)

**Hysteresis Loop:**
- Compression limb: F = f(d, +ḋ)
- Release limb: F = f(d, -ḋ) × (1 - damping_fraction)
- Loop area = Energy dissipated

---

## GAPS AND NEXT STEPS

### Literature Status

| Item | Status | Notes |
|------|--------|-------|
| Ventilation model | ✓ Complete | Van Meurs, Hyatt |
| Ventilation reference | ✓ Complete | Huang 2016 (infant) |
| Compression model | ✓ Complete | Gruben/Thielen, Lim 2024 |
| Compression reference | **PENDING** | Lamb data from Arjen ten Pas (DR-003) |

### Remaining Gaps

| Gap | Status | Action |
|-----|--------|--------|
| Infant compression reference | Pending | Await lamb data from LUMC |
| Manikin characterization data | Our contribution | Experimental work |

### Next Steps

1. [x] ~~Add Hyatt reference for ventilation~~ - Done
2. [ ] Obtain lamb data from Arjen ten Pas (LUMC) - DR-003 in progress
3. [ ] Define infant-specific parameter ranges for compression
4. [ ] Create reference envelope plots with uncertainty bands
5. [ ] Design experimental protocol to measure manikin parameters

---

## References

### Ventilation Models
1. van Meurs WL. *Modeling and Simulation in Biomedical Engineering: Applications in Cardiorespiratory Physiology*. McGraw-Hill. Chapter 9.
2. Scanlon PD, Hyatt RE. *Hyatt's Interpretation of Pulmonary Function Tests*. 5th ed. Wolters Kluwer, 2019. Chapter 7.

### Ventilation Reference Data
3. Huang J et al. (2016). Reference values for resistance and compliance in healthy infants. J Thorac Dis 8(3):513-519.
4. Battisti O et al. (2012). Lung Compliance and Airways Resistance in Healthy Neonates. Pediatr Therapeut 2:114.

### Compression Models
5. Gruben KG et al. (1990). Identification of dynamic mechanical parameters of the human chest. IEEE Trans Biomed Eng 37(2):211-217.
6. Thielen M et al. (2017). An innovative design for cardiopulmonary resuscitation manikins. Proc IMechE Part H. DOI: 10.1177/0954411917691555
7. Lim H et al. (2024). Variable Stiffness and Damping Mechanism for CPR Manikin. IEEE JTEHM. DOI: 10.1109/JTEHM.2024.3429422

### Compression Reference Data (Adult)
8. Tomlinson AE et al. (2007). Compression force-depth relationship during out-of-hospital CPR. Resuscitation 72:364-370.
9. Ruiz de Gauna S et al. (2023). Characterization of mechanical properties of adult chests. Comput Methods Programs Biomed 242:107847.
10. Neurauter A et al. (2009). Comparison of mechanical characteristics of the human and porcine chest. Resuscitation.

### Compression Reference Data (Infant/Neonatal Animal Surrogate)
11. O'Reilly M, Schmölzer GM et al. (2023). Comparison of hemodynamic effects of chest compression delivered via machine or human in asphyxiated piglets. *Pediatric Research*. doi:10.1038/s41390-023-2827-1
12. Lamb data from Arjen ten Pas (LUMC) - awaiting DR-003

---

*Document to be updated as literature review progresses*
