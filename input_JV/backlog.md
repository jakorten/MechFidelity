# Project Backlog

**Paper:** Mechanical Fidelity of CPR Training Manikins
**Target:** MST Special Issue - March 31, 2026

---

## Open Tasks

### Methodology Setup
- [x] Adopt V&V methodology from Proposition (DR-000)
- [x] Create directory structure
- [x] Create claim registry template
- [x] Add AI-assisted review prompts (adapted from TIM review guide)
- [ ] Populate claim registry with initial claims from outline

### Human Reference Model (Literature)
- [x] Extract existing data from Proposition repo
- [x] Obtain PDFs: Lim 2024, Tomlinson 2007, Ruiz de Gauna 2023, Neurauter 2009 (from Proposition)
- [x] Obtain PDFs: Huang 2016, Battisti 2012 (open access downloads)
- [x] Verify stiffness/damping values (C1, C2) — **Nysæther 2008 is primary source for human data; Lim 2024 describes manikin range**
- [x] Verify Tomlinson 2007 non-linearity (C3) — **Confirmed: progressivity factor 1.41±0.25**
- [x] Verify Ruiz de Gauna 2023 dynamic softening (C4) — **Confirmed: 34.6% decrease**
- [x] Verify Huang 2016 infant compliance/resistance (V1, V2) — **Confirmed: 78-171 mL/kPa, 3.7-6.4 kPa/L/s**
- [x] Verify infant compression data gap (C5) — **Confirmed via Babic 2017, Thielen 2017**
- [x] Verify novelty claims (I2, I3, D1, D2) — **No competing work found**
- [x] Found Nysæther 2008 — primary source for human chest properties (n=59)
- [x] Found Morin 2024 — adult ventilation reference values (compliance 37-40 mL/cmH₂O)

### Experimental Planning
- [ ] Define manikin test matrix (which manikins, how many replicates)
- [x] Confirm compression apparatus availability — **DONE: Load cell firmware complete, verified ±0.13 N accuracy**
- [~] Design/source ventilation measurement apparatus — **Need MPXV5010DP (~€10) for airway pressure; SDP810+MFM for flow ready**
- [ ] Create experimental protocol document
- [ ] Plan data file naming convention

### Data Collection (pending)
- [ ] Compression characterization -- infant manikins (DYMH-103 load cell)
- [ ] Ventilation characterization -- infant manikins (Bronkhorst EL-PRESS + SDP810)
- [ ] Unit-to-unit variation testing

### Analysis (pending)
- [ ] Reference model fitting (uncertainty envelope)
- [ ] Manikin comparison analysis
- [ ] Mechanical fidelity index calculation

### Writing (pending)
- [ ] Draft Section 1: Introduction
- [ ] Draft Section 2: Human Reference Model
- [ ] Draft Section 3: Uncertainty Envelope
- [ ] Draft Section 4: Characterization Protocol
- [ ] Draft Section 5: Results
- [ ] Draft Section 6: Fidelity Index
- [ ] Draft Section 7: Discussion
- [ ] Draft Section 8: Conclusion

### Oracles (pending)
- [x] Download MST author guidelines — **See `vv/oracles/MST_Author_Guidelines.md`**
- [ ] Find exemplar papers from MST special issues
- [ ] Document data availability requirements

---

## Delayed Decisions

### DR-001: Reference Model Scope (DECIDED — REVISED 2026-01-18)
**Decision:** Infant ventilation (primary) + Infant compression (primary)

**Rationale:**
- Only infant manikins available
- Test equipment suitable for infant manikins only
- Human reference exists for infant ventilation (Huang 2016, n=205)
- Animal surrogate reference for infant compression via:
  - **Route A:** Schmölzer piglet data (request existing force-displacement)
  - **Route B:** LUMC lamb measurements (perform ourselves)

**Piglet reference available:**
- Weight: 2.12 ± 0.17 kg (matches term infant)
- Age: 0-3 days, validated CPR model
- Force recorded in experiments → can extract stiffness

**Implications:**
- Ventilation: fidelity index against human reference (Huang 2016)
- Compression: fidelity index against animal surrogate reference
- DYMH-103 load cell (0-49 N) suitable for infant compression (14-30 N range)
- Bronkhorst EL-PRESS P-502C for airway pressure

See: `DR-001_reference_model_scope.md`

### DR-002: Manikin Selection (IN PROGRESS)
**Decision needed:** Which infant manikins to characterize?

**Status:** Sufficient manikins available (own inventory + WKZ access)

**Action:** Define test matrix - which models, how many units per model

### DR-004: Framework Terminology (DECISION NEEDED)
**Decision needed:** What to call the framework?

**Options:**
- **A:** Mechanical Fidelity Assessment
- **B:** Quantitative Fidelity Framework

**Context:** "Mechanical fidelity" is confusing—conflates with visual "high fidelity." Need terminology that emphasizes mechanical response vs appearance.

See: `working/DR-004_framework_terminology.md`

### DR-003: Lamb Reference Data (IN PROGRESS)
**Decision needed:** Can lamb chest compression data serve as reference for infant manikin validation?

**Potential source:** Arjen ten Pas (LUMC) - advisor, potential data provider

**If available, need:**
- Force-displacement measurements (stiffness k in N/mm)
- Hysteresis data (damping coefficient)
- Sample size (n) and weight range
- Publication/source for citation

**Hardware:** Transport dedicated CNC setup to LUMC via trailer. IMU (BHI360) as backup only.

**Impact:** Would enable fidelity index for compression (not just descriptive characterization)

---

## Collaborators

| Name | Affiliation | Role | Notes |
|------|-------------|------|-------|
| Prof. dr. dr. Egon L. van den Broek | - | Promotor | |
| Dr. Jeroen Veen | - | Co-promotor | |
| Timo de Raad | WKZ, NRR, ERC | Co-author | Clinical/resuscitation expertise |
| Prof. dr. Arjen ten Pas | LUMC | Advisor | Potential lamb data provider (DR-003) |
| Jozua van Duuren | WKZ | Co-author/Advisor | Specialized nurse, involved in prior papers |

---

## Completed

### Session 2026-01-15 (Initial Setup)
- [x] Created `input_JV/` directory structure
- [x] Created `input_JV/vv/` V&V framework folders
- [x] Adapted `METHODOLOGY.md` from Proposition
- [x] Adapted `PAPER_VV_FRAMEWORK.md` from Proposition
- [x] Created `claim_registry.md` template with initial claims from outline
- [x] Created DR-000 (methodology adoption decision)
- [x] Created this backlog
- [x] Updated CLAUDE.md with new structure
- [x] Added AI-assisted review prompts adapted from TIM review guide:
  - `MST_Review_Prompt_Single_Stage.md` - comprehensive review
  - `MST_Review_Prompt_Stage1.md` - gate decision (proceed/reject)
  - `MST_Review_Prompt_Stage2.md` - detailed section-by-section review
  - `USAGE_GUIDE.md` - how to use the review prompts
- [x] Set up literature folder structure (`input_JV/literature/`)
- [x] Extracted human reference data from Proposition repo:
  - Adult compression: Lim 2024, Tomlinson 2007, Ruiz de Gauna 2023, Neurauter 2009
  - Infant ventilation: Huang 2016
  - Key quotes and evidence gaps identified
  - See `extracted_data_from_proposition.md`

---

## Notes

- Deadline: March 31, 2026
- Related paper: Proposition (perspective/conceptual framework)
- This paper: technical methodology + empirical data
- Key unique contribution: ventilation fidelity (less studied than compressions)

### Session 2026-01-15 (Literature V&V + Apparatus Planning)
- [x] Verified all verifiable P0 literature claims (C1-C5, V1-V2, I2-I3, D1-D2)
- [x] Identified Nysæther 2008 as primary source for human chest properties
- [x] Added Nysæther 2008 to paper_draft.md references
- [x] Contextualized Lim 2024 as manikin design (not human reference)
- [x] Created article summaries: Babic 2017, Nysæther 2008, Morin 2024
- [x] Updated claim registry to 48% coverage (10/21 verified)
- [x] Apparatus planning: load cell firmware needed, MPXV5010DP needed for ventilation
- Remaining P0 claims blocked by: M1-M2 (own work), RC1-RC2/RV1-RV3 (experiments)

### Session 2026-01-16 (Literature + Oracles)
- [x] Added new PDFs: Diedericks 2025, Reiss 2025, Ikeyama 2024, novel_cc_2025, survive_2024
- [x] Renamed PDFs to consistent format
- [x] Removed irrelevant jotten2008.pdf (telecommunications)
- [x] Strengthened V3 claim with Diedericks 2025 (FASEB review): "CCW ~3× CL term, ~5× preterm"
- [x] Created article summary: diedericks_2025_chest_wall_summary.md
- [x] Fetched MST author guidelines → `vv/oracles/MST_Author_Guidelines.md`
- [x] **Revised DR-001 scope:** infant ventilation (primary) + infant compression (secondary)
- [x] Updated claim registry with infant compression claims (RC1-RC3, C5, C7, D3, D4)
- [x] DYMH-103 load cell (0-49 N) confirmed suitable for infant compression (14-30 N)
- Next: DR-002 (manikin inventory), load cell integration, experimental protocol

### Session 2026-01-19 (Load Cell Integration)
- [x] **Load cell firmware completed and verified**
  - STM32F405 + HX711 (Sparkfun red) + DYMH-103 (0-5 kg)
  - Pin config: DAT→PB10, CLK→PB11, VDD+VCC→3.3V
  - Custom firmware: TARE, CAL (kg input), START/STOP streaming, READ, RAW, STATUS
  - Source: `software/loadcell/`
- [x] **HX711 wiring issue resolved**
  - Problem: VDD (3.3V) and VCC (5V) on different rails
  - Solution: Both VDD and VCC to 3.3V
- [x] **Calibration verified** (preliminary, with kitchen-weighed masses)

  | Gewicht | Verwacht | Gemeten | Fout |
  |---------|----------|---------|------|
  | 0 g | 0.00 N | 0.007 N | +0.007 N ✓ |
  | 301 g | 2.95 N | 3.081 N | +0.13 N |
  | 1.501 kg | 14.72 N | 14.691 N | -0.03 N ✓ |
  | 2.001 kg | 19.63 N | 19.628 N | -0.002 N ✓ |

  **Result:** Max error 0.13 N at low range, <0.035 N in working range (14-30 N). Within ±0.5 N spec.

- [x] **Calibration protocol created** — `software/loadcell/CALIBRATION.md`
- [x] **DR-005 created** — Acknowledgements registry
  - Herold Cremer (HAN): calibration weights, F1 class (kg range) available next week
  - Dr. Gertjan Lugthart (LUMC Pediatrics): facilitating collaboration
  - Arjan Bikkel, Peter Brouwer (Bronkhorst): pressure/flow sensor support
- [x] **3D printed calibration extension available** — `Calibration extension for Compression Actuator Load Cell.stl`

**Next steps:**
- Final calibration with Herold Cremer's F1 weights (volgende week)
- Begin manikin compression characterization

---

## Next Session Priorities

1. ~~**Load cell firmware integration**~~ — **DONE** ✓
2. **Final calibration with F1 weights** (Herold Cremer, HAN) — volgende week
3. **Inventory infant manikins** (DR-002)
4. **MPXV5010GP ×5 ordered** (2026-01-15) — pin-compatible replacement for MPXV5050
   - 0-10 kPa range, ±0.25 kPa accuracy
   - Backup / blocked airway detection
5. **Verify FLEXI-FLOW flow range setting** — currently 2 ln/min (TBC), may need 0.5 ln/min for infant volumes
6. **Bronkhorst: EL-PRESS (0-100 mbar) confirmed** (2026-01-16)
   - Bronkhorst will provide overpressure sensor
   - SI-traceable, factory calibrated
   - Primary sensor for Paw measurement + calibration reference

   **Order specification:**
   ```
   Model:    P-502C (EL-PRESS)
   Type:     Gauge (overpressure relative to atmosphere)
   Range:    0-100 mbar
   Use:      Airway pressure (Paw) measurement, infant ventilation
   Interface: RS232 or Modbus (compatible with existing MFM setup)
   ```

### Session 2026-01-21 (Literature & Gap Confirmation)
- [x] Inventorized O'Reilly 2024 — machine vs human CC in piglets; force profile > depth
- [x] Inventorized Thielen 2017 — human-like thorax design; classical manikins linear, humans nonlinear
- [x] Added claims I4 (force profile), I5 (linear vs nonlinear gap)
- [x] **Confirmed infant chest stiffness gap definitively:**
  - Kent 2010: "No experimental data exist" for pediatric F-D
  - Kent 2009: Youngest data ages 8-22yo (n=18)
  - Kent 2012: PMHS ages 6-7yo (youngest available)
  - Nysæther 2009: Expert consensus but N/mm unpublished
  - Kent 2010: Adult-to-pediatric scaling fails
- [x] Upgraded C5 to P0; added C6, C8
- [x] Claim registry: 13/21 verified (62%), 7/11 P0 (64%)
- [x] Validated DR-001 scope (ventilation fidelity index, compression descriptive only)
- [x] Decided NOT to attempt scaling — would undermine C8 claim
