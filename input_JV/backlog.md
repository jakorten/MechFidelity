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
- [ ] Verify Lim 2024 stiffness/damping values (Claims C1, C2)
- [ ] Verify Tomlinson 2007 non-linearity description (Claim C3)
- [ ] Verify Ruiz de Gauna 2023 dynamic softening (Claim C4)
- [ ] Verify Huang 2016 infant compliance/resistance (Claims V1, V2)
- [ ] Search for additional infant compression data
- [ ] Search for adult ventilation reference data (gap identified)

### Experimental Planning
- [ ] Define manikin test matrix (which manikins, how many replicates)
- [ ] Confirm compression apparatus availability
- [ ] Design/source ventilation measurement apparatus
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

---

## Notes

- Deadline: March 31, 2026
- Related paper: Proposition (perspective/conceptual framework)
- This paper: technical methodology + empirical data
- Key unique contribution: ventilation fidelity (less studied than compressions)

## Next Session Priorities

1. Literature verification pass for P0 claims (human reference values)
2. Decision on reference model scope (DR-001)
3. Manikin availability assessment
4. Experimental planning
