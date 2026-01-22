# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

**READ THIS FIRST** in every session.

---

## Repository Overview

This repository contains the **Mechanical Fidelity Paper** - a technical measurement science paper on CPR manikin characterization.

**Target:** Measurement Science and Technology - Special Issue on "Data-Centric Exploration and Explanation of Physical and Engineering Phenomena"

**Deadline:** March 31, 2026

---

## Core Concept

**Key distinction:** Traditional "high-fidelity" manikins are classified by *visual realism* (looks like an infant). Our work focuses on *mechanical fidelity* (responds like an infant). A manikin may look like an infant without responding like one.

Build a **human reference model** from medical/clinical literature for both chest compressions and ventilations, then systematically compare multiple CPR training manikins against that model to quantify the mechanical fidelity gap.

```
Human Reference Model          ->    Manikin Characterization    ->    Fidelity Gap Analysis
(from medical literature)            (empirical testing)              (mechanical response)
```

**Terminology (see DR-004):** "Mechanical fidelity" emphasizes response properties (stiffness, compliance, damping) rather than appearance.

---

## Session Continuity

### Starting a Session
1. **Read this file** (CLAUDE.md) -- you're doing this now
2. **Read `input_JV/backlog.md`** -- current tasks and priorities
3. **Check recent DRs** in `input_JV/DR-*.md` -- any pending decisions?
4. **Resume from last state** -- don't restart completed work

### Ending a Session
1. Update `input_JV/backlog.md` with progress
2. Commit changes
3. Update this file if major milestones reached

---

## Key Files

| File | Purpose |
|------|---------|
| `MST_paper_outline.md` | Detailed paper structure |
| `MST_paper_supervisor_summary.md` | Summary for supervisors |
| `input_JV/backlog.md` | Current tasks and priorities |
| `input_JV/METHODOLOGY.md` | AI-augmented workflow |
| `input_JV/vv/claim_registry.md` | All paper claims with verification status |
| `input_JV/DR-*.md` | Decision records |

---

## Directory Structure

```
MechanicalFidelity/
|-- CLAUDE.md                    <- This file (read first)
|-- MST_paper_outline.md         <- Paper structure
|-- MST_paper_supervisor_summary.md
|-- input_JV/                    <- Working documents
|   |-- METHODOLOGY.md           <- Workflow methodology
|   |-- backlog.md               <- Task tracking
|   |-- DR-*.md                  <- Decision records
|   '-- vv/                      <- V&V Framework
|       |-- PAPER_VV_FRAMEWORK.md
|       |-- claims/
|       |   '-- claim_registry.md
|       |-- audits/              <- Per-section audits
|       |-- oracles/             <- Author guidelines, exemplars
|       |-- tests/               <- Static checks
|       '-- validation/          <- Co-author review
|-- paper/                       <- LaTeX source (TBD)
|-- data/                        <- Experimental data (TBD)
'-- references.bib               <- Bibliography (TBD)
```

---

## Methodology

This project uses a **V&V (Verification & Validation) framework** adapted from the Proposition repository:

- **Claims** are registered and tracked with priority levels (P0/P1/P2)
- **Confidence tags** indicate verification status ([VERIFIED], [OWN DATA], etc.)
- **Quality gates** must pass before submission
- **Decision records** document key choices

See `input_JV/METHODOLOGY.md` for full details.

---

## Current Status

**Phase:** Setup complete, ready for literature verification and experimental planning

**Next priorities:**
1. Verify P0 literature claims (human reference values)
2. Decide reference model scope (DR-001 pending)
3. Assess manikin availability
4. Plan experiments

---

## Related Repositories

| Repository | Purpose | Relationship |
|------------|---------|--------------|
| **Proposition** | Perspective paper on mechanical fidelity concept | Provides conceptual framework |
| **This repo** | Technical methodology + empirical data | Provides measurement tools |

The Proposition paper argues FOR mechanical fidelity assessment; this MST paper provides the TOOLS to measure it.

---

## Build Commands

TBD - LaTeX setup to be added when paper writing begins.

```bash
# When paper/ directory is set up:
pdflatex paper/main.tex
biber paper/main
pdflatex paper/main.tex
pdflatex paper/main.tex
```

---

*Last updated: 2026-01-18*
