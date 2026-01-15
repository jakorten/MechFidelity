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
- [ ] Compression characterization -- adult manikins
- [ ] Compression characterization -- infant manikins
- [ ] Ventilation characterization -- infant manikins
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
- [ ] Download MST author guidelines
- [ ] Find exemplar papers from MST special issues
- [ ] Document data availability requirements

---

## Delayed Decisions

### DR-001: Reference Model Scope (PENDING)
**Decision needed:** How comprehensive should the human reference model be?

**Options:**
- Option A: Adults + infants, compressions + ventilations (full scope from outline)
- Option B: Focus on infants only (where we have more unique data)
- Option C: Focus on ventilations only (biggest evidence gap)

**Blocked by:**
- [ ] Assessment of available human reference data
- [ ] Assessment of available manikins for testing
- [ ] Discussion with co-authors

### DR-002: Manikin Selection (PENDING)
**Decision needed:** Which manikins to characterize?

**Options:**
- TBD after resource assessment

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

---

## Next Session Priorities

1. Order MPXV5010DP pressure sensor (~€10)
2. Load cell firmware integration
3. Decision on reference model scope (DR-001)
4. Manikin availability assessment
