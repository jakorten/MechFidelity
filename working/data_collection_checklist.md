# Data Collection Checklist

**Paper:** Mechanical Fidelity of CPR Training Manikins
**Deadline:** March 31, 2026
**Target:** Complete data collection by mid-February 2026

---

## 1. Pre-Collection Setup

### 1.1 Equipment Verification
- [ ] CNC actuator (BlackBox X32) operational and calibrated
- [ ] VL53L4CD ToF sensor firmware updated (62.9mm offset correction)
- [ ] Load cell calibrated against reference weights
- [ ] Sensirion SDP810-500Pa DPS functional
- [ ] Bronkhorst MFM SI-traceable certificate current
- [ ] Mitutoyo caliper calibration verified
- [ ] SHT45 environmental sensor functional
- [ ] STM32F405 data acquisition tested
- [ ] 100 mL calibration syringe available

### 1.2 Software Verification
- [ ] `cpr_multi_cycle_tester.py` tested
- [ ] `cpr_compression_validator.py` tested
- [ ] Ventilation controller firmware uploaded
- [ ] Data logging scripts verified (JSON/CSV output)
- [ ] Analysis scripts prepared

### 1.3 Manikins Secured
| Manikin | Manufacturer | Available | Serial # |
|---------|--------------|-----------|----------|
| [ ] Resusci Baby QCPR | Laerdal | | |
| [ ] Little Junior QCPR | Laerdal | | |
| [ ] Resusci Anne QCPR | Laerdal | | |
| [ ] Ambu Baby | Ambu | | |
| [ ] [Additional infant] | | | |
| [ ] [Additional adult] | | | |

**Goal:** Minimum 3 infant + 2 adult manikins; ideally 2 units of same model for unit-to-unit variation

---

## 2. Compression Characterization

### 2.1 Per-Manikin Protocol

**Pre-test:**
- [ ] Record manikin ID, serial number, manufacture date (if available)
- [ ] Photograph manikin chest area
- [ ] Position manikin on rigid surface
- [ ] Mount actuator assembly
- [ ] 30-minute thermal stabilization
- [ ] Record ambient T (target: 22±2°C) and RH (target: 45±5%)
- [ ] Zero calibration against Mitutoyo caliper

**Test Sequence:**

| Test | Description | Cycles | Est. Time |
|------|-------------|--------|-----------|
| [ ] Depth sweep | 10, 20, 30, 40, 50 mm | 5 × 20 = 100 | 15 min |
| [ ] Rate variation | 100, 110, 120 CPM @ 40mm | 3 × 20 = 60 | 10 min |
| [ ] Extended cycling | 150 cycles @ 40mm | 150 | 15 min |
| **Total** | | **310 cycles** | **~40 min** |

**Post-test:**
- [ ] Verify no manikin damage
- [ ] Export data (JSON + CSV)
- [ ] Quick visual inspection of force-displacement curves
- [ ] Note any anomalies

### 2.2 Data Files Required

Per manikin:
```
/data/compressions/{manikin_id}/
├── metadata.json          # Manikin info, environmental conditions
├── depth_sweep.csv        # Force, displacement, time
├── rate_variation.csv
├── extended_cycling.csv
└── plots/
    ├── force_displacement.png
    └── hysteresis_loops.png
```

### 2.3 Derived Parameters to Extract

| Parameter | Symbol | Unit | Method |
|-----------|--------|------|--------|
| Stiffness | k | N/mm | Linear regression slope |
| Compression damping | d_c | N·s/mm | Hysteresis analysis |
| Recoil damping | d_r | N·s/mm | Hysteresis analysis |
| Nonlinearity coefficients | k₁–k₄ | — | Gruben polynomial fit |
| Fatigue drift | Δk | % | Extended cycling trend |

---

## 3. Ventilation Characterization

### 3.1 Per-Manikin Protocol

**Pre-test:**
- [ ] Record manikin ID
- [ ] Inspect airway patency
- [ ] Connect ventilation apparatus
- [ ] Leak test (seal mask/tube connection)
- [ ] Configuration-specific K calibration (grid search)
- [ ] Record ambient T and RH

**Test Sequence:**

| Test | Description | Cycles | Est. Time |
|------|-------------|--------|-----------|
| [ ] Volume sweep | 12.25, 24.5, 36.75, 49.0, 61.25, 73.5 mL | 6 × 100 = 600 | 45 min |
| [ ] Clinical target | 24.5 mL (infant) | 200 | 15 min |
| **Total** | | **800 cycles** | **~60 min** |

**Post-test:**
- [ ] Export data
- [ ] Verify calibration coefficient stability
- [ ] Note any leaks or anomalies

### 3.2 Data Files Required

Per manikin:
```
/data/ventilations/{manikin_id}/
├── metadata.json          # Manikin info, K coefficient, conditions
├── volume_sweep.csv       # Pressure, flow, volume, time
├── clinical_target.csv
└── plots/
    ├── volume_accuracy.png
    └── pressure_volume_loops.png
```

### 3.3 Derived Parameters to Extract

| Parameter | Symbol | Unit | Method |
|-----------|--------|------|--------|
| Compliance | C_rs | mL/cmH₂O | V / ΔP |
| Resistance | R_rs | cmH₂O/L/s | ΔP / flow |
| Calibration coefficient | K | Pa⁻¹/²·mL·s⁻¹ | Grid search |
| Volume accuracy | RMSE | % | vs. MFM reference |

---

## 4. Reference Envelope Comparison

### 4.1 Compression (Adults)

| Parameter | Human Reference | Unit | Source |
|-----------|-----------------|------|--------|
| Stiffness | 92–113 | N/cm | Ruiz de Gauna 2023 |
| Compression damping | 2.4–3.3 | N·s/cm | Ruiz de Gauna 2023 |
| Recoil damping | 4.0–5.8 | N·s/cm | Ruiz de Gauna 2023 |
| Nonlinearity | Required | — | Multiple |

### 4.2 Ventilation (Infants)

| Parameter | Human Reference | Unit | Source |
|-----------|-----------------|------|--------|
| Compliance | 78–171 | mL/kPa | Huang 2016 |
| Resistance | 3.74–6.39 | kPa/L/s | Huang 2016 |

---

## 5. Analysis Checklist

### 5.1 Per-Manikin Analysis
- [ ] Calculate stiffness (k) ± uncertainty
- [ ] Calculate damping (d_c, d_r) ± uncertainty
- [ ] Fit Gruben polynomial, extract coefficients
- [ ] Calculate compliance (C_rs) ± uncertainty
- [ ] Calculate resistance (R_rs) ± uncertainty
- [ ] Compare to reference envelope (within/outside)

### 5.2 Cross-Manikin Analysis
- [ ] Generate comparison table (all manikins vs. reference)
- [ ] Plot force-displacement overlays
- [ ] Calculate Mechanical Fidelity Index (MFI) for each
- [ ] Rank manikins by MFI
- [ ] Assess unit-to-unit variation (same model)

### 5.3 Figures for Paper

| Figure | Description | Status |
|--------|-------------|--------|
| Fig. 1 | Compression apparatus schematic | [ ] |
| Fig. 2 | Ventilation apparatus schematic | [ ] |
| Fig. 3 | Force-displacement curves (all manikins vs. human) | [ ] |
| Fig. 4 | Hysteresis loop comparison | [ ] |
| Fig. 5 | Ventilation compliance/resistance vs. reference | [ ] |
| Fig. 6 | MFI ranking bar chart | [ ] |

### 5.4 Tables for Paper

| Table | Description | Status |
|-------|-------------|--------|
| Table 1 | Human reference values (compression) | [x] In draft |
| Table 2 | Human reference values (ventilation) | [x] In draft |
| Table 3 | Manikin compression parameters | [ ] |
| Table 4 | Manikin ventilation parameters | [ ] |
| Table 5 | MFI scores and ranking | [ ] |
| Table 6 | Unit-to-unit variation | [ ] |

---

## 6. Timeline

| Week | Dates | Activity |
|------|-------|----------|
| 1 | Jan 13–19 | Equipment setup, software verification |
| 2 | Jan 20–26 | Compression testing (3–4 manikins) |
| 3 | Jan 27–Feb 2 | Compression testing (remaining) + analysis |
| 4 | Feb 3–9 | Ventilation testing (all manikins) |
| 5 | Feb 10–16 | Analysis, MFI calculation, figures |
| 6 | Feb 17–23 | Write Section 5, revise draft |
| 7 | Feb 24–Mar 2 | Co-author review |
| 8 | Mar 3–9 | Revisions |
| 9 | Mar 10–16 | Final polish |
| 10 | Mar 17–23 | Buffer |
| 11 | Mar 24–31 | **Submit by March 31** |

---

## 7. Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Equipment failure | Test all equipment in Week 1; have backup sensors |
| Manikin unavailability | Confirm access NOW; identify alternatives |
| Time overrun | Prioritize infant manikins (novel contribution) |
| Unexpected results | Document everything; results are results |
| Load cell issues | Can still characterize displacement/stiffness from depth data |

---

## 8. Quick Reference: Key Numbers

**Compression targets:**
- Adult: 50 mm depth, 100–120 CPM
- Infant: 40 mm depth (~1/3 thorax)

**Ventilation targets (3.5 kg infant):**
- Volume: 21–28 mL (ERC 2025)
- Test range: 12.25–73.5 mL

**Human reference (adult compression):**
- Stiffness: 104.9 N/cm (95% CI: 102–108)
- Recoil damping 1.7× compression damping

**Human reference (infant ventilation):**
- Compliance: 78–171 mL/kPa (age-dependent)
- Resistance: 3.74–6.39 kPa/L/s (age-dependent)

---

*Checklist created: January 2026*
*Last updated: [date]*
