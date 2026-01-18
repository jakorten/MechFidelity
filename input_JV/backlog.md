# Project Backlog

**Paper:** Engineering Fidelity of CPR Training Manikins
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
- [x] Confirm compression apparatus availability — **Load cell installed, needs firmware integration**
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
- [ ] Engineering fidelity index calculation

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

### DR-001: Reference Model Scope (DECIDED — REVISED)
**Decision:** Infant ventilation (primary) + Infant compression (secondary)

**Rationale:**
- Only infant manikins available
- Test equipment suitable for infant manikins only
- Human reference exists for infant ventilation (Huang 2016, n=205)
- No human reference exists for infant compression — characterization is **descriptive only**
- Strongest novelty: no prior infant manikin ventilation benchmark

**Implications:**
- Ventilation: fidelity index against human reference (Huang 2016)
- Compression: descriptive characterization (force-displacement curves, stiffness)
- DYMH-103 load cell (0-49 N) suitable for infant compression (14-30 N range)
- Bronkhorst EL-PRESS P-502C for airway pressure

See: `DR-001_reference_model_scope.md`

### DR-002: Manikin Selection (IN PROGRESS)
**Decision needed:** Which infant manikins to characterize?

**Status:** Sufficient manikins available (own inventory + WKZ access)

**Action:** Define test matrix - which models, how many units per model

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
| Dr. Jeroen Veen | - | Promotor | |
| Timo de Raad | WKZ, NRR, ERC | Co-author | Clinical/resuscitation expertise |
| Prof. Arjen ten Pas | LUMC | Advisor | Potential lamb data provider (DR-003) |
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

---

## Next Session Priorities

1. **MPXV5010GP ×5 ordered** (2026-01-15) — pin-compatible replacement for MPXV5050
   - 0-10 kPa range, ±0.25 kPa accuracy
   - Backup / blocked airway detection
2. **Bronkhorst: EL-PRESS (0-100 mbar) confirmed** (2026-01-16)
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
3. **Inventory infant manikins** (DR-002)
4. **Load cell firmware integration** — hardware ready
   - DYMH-103 (0-5kg = 0-49N) — suitable for infant compression (14-30 N)
   - HX711 ADC (Sparkfun, 24-bit) — available
   - STM32F405 — needs firmware update for HX711 readout
   - **WAITING:** Calibration weights availability check (HAN lab)
   - TODO: Wire HX711 → STM32, add readout code, calibrate
5. ~~Decision on reference model scope (DR-001)~~ — **DECIDED: infant ventilation (primary) + compression (secondary)**
