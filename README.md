# Mechanical Fidelity of CPR Training Manikins

A research paper for **Measurement Science and Technology** (IOP Publishing) - Focus Collection on *"Data-Centric Exploration and Explanation of Physical and Engineering Phenomena"*

**Deadline:** March 31, 2026

**Invitation:** Personal recommendation by Guest Editor Rui Yuan (Wuhan University of Science and Technology)

**Collection page:** https://iopscience.iop.org/collections/mst-251119-1003

## Overview

This paper develops a data-driven reference model for CPR training manikin characterization, combining chest compression and ventilation mechanics.

### Core Concept

```
Human Reference Model    →    Manikin Characterization    →    Fidelity Gap Analysis
(from medical literature)      (empirical testing)              (model vs. reality)
```

1. Build a human reference model from medical/clinical literature
2. Systematically test multiple CPR manikins against this reference
3. Quantify the "mechanical fidelity gap" for each manikin

## Key Contributions

- First systematic benchmark combining compression AND ventilation fidelity
- Data-driven reference model synthesized from published clinical datasets
- Quantified mechanical fidelity index for manikin procurement decisions
- Novel ventilation fidelity analysis (largely unstudied area)

## Mechanical Fidelity Index (MFI)

The MFI is a quantified metric to score how well a manikin replicates human biomechanics:

```
MFI = w_c * F_compression + w_v * F_ventilation
```

| Component | Description |
|-----------|-------------|
| F_compression | Normalized score for stiffness + damping within human envelope |
| F_ventilation | Normalized score for compliance + resistance within human envelope |
| w_c, w_v | Weighting factors (adjustable based on training priorities) |

**Scoring:**
- **MFI = 1.0** - Perfect match to human reference center
- **MFI = 0.0** - Deviation equals full envelope width

Higher MFI = more physiologically realistic manikin. This provides training centers a single number to compare manikins for procurement decisions.

## Paper Structure

1. **Introduction** - Mechanical fidelity concept and research gap
2. **Human Reference Model** - Compression and ventilation mechanics from literature
3. **Uncertainty Envelope** - Acceptable range from human variability
4. **Manikin Characterization Protocol** - Standardized testing methodology
5. **Results** - Fidelity comparison across multiple manikins
6. **Mechanical Fidelity Index** - Quantified metric proposal
7. **Discussion & Conclusion**

## Related Work

| Paper | Venue | Relationship |
|-------|-------|--------------|
| Sensor validation | IEEE TIM | Methodology foundation |
| TEF RCT | IEEE THMS | Training effectiveness evidence |
| [Perspective paper](https://github.com/jakorten/Proposition.git) | Resuscitation | Conceptual framework |
| **This paper** | MST | Technical methodology + data |

The perspective paper argues *for* mechanical fidelity; this paper provides the *tools to measure* it.

## Current Status

| Section | Status |
|---------|--------|
| 1. Introduction | Draft complete |
| 2. Human Reference Model | Draft complete |
| 3. Uncertainty Envelope | Draft complete |
| 4. Manikin Characterization Protocol | Draft complete |
| 5. Results | Awaiting data collection |
| 6. Mechanical Fidelity Index | Draft complete |
| 7. Discussion | Draft complete |
| 8. Conclusion | Draft complete |

**Next steps:** Data collection (target: mid-February 2026)

## Repository Structure

```
├── MST_paper_outline.md          # Detailed paper outline
├── MST_paper_supervisor_summary.md  # Executive summary for supervisors
├── CLAUDE.md                     # AI assistant guidance
└── working/
    ├── paper_draft.md            # Current paper draft (~4,750 words)
    ├── literature_review.md      # Comprehensive literature synthesis
    ├── apparatus_expansion.md    # Hardware requirements for manikin testing
    ├── data_collection_checklist.md  # Testing protocol checklist
    ├── articles/                 # Converted reference papers (markdown)
    ├── datasheets/               # Bronkhorst MFM documentation
    │   ├── 6264-ff-m11-en-datasheet.md
    │   ├── 917158-manual-flexi-flow-compact.md
    │   └── N0551_N2510646_A_m.md
    └── scripts/
        └── ventilation_mechanics.py  # C/R calculation module
```

## Key References

### Compression Mechanics
- Tomlinson AE et al. (2007). *Resuscitation*. 72(3):364-370.
- Ruiz de Gauna S et al. (2023). *Comput Methods Programs Biomed*. 242:107847.
- Lim H et al. (2024). *IEEE J Transl Eng Health Med*. 12:542-549.

### Ventilation Mechanics
- Huang J et al. (2016). *J Thorac Dis*. 8(3):513-519.
- Battisti O et al. (2012). *Pediatr Therapeut*. 2(2):114.

## Author

Jan Korten

## License

All rights reserved. Academic research in progress.
