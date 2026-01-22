---
status: Accepted
date: 2026-01-15
---

# Decision: Adopt V&V methodology from Proposition repository

## Context

The MechanicalFidelity paper needs a rigorous development methodology to ensure:
- All claims are verifiable and traced to sources or data
- Progress is tracked systematically
- Session continuity is maintained across AI-assisted work sessions
- Quality gates prevent premature submission

The related Proposition repository has a proven methodology adapted from the SU2049 Cyberphysical Systems V&V approach.

## Options Considered

### Option A: Adopt Proposition methodology (adapted)
- (+) Already proven in related project
- (+) Comprehensive: covers claims, verification, quality gates
- (+) Anti-hallucination measures built in
- (+) Consistent approach across related papers
- (+) Session continuity designed for AI-assisted work
- (-) Some overhead in setup and maintenance
- (-) Needs adaptation for data-heavy technical paper (vs. perspective paper)

### Option B: Ad-hoc approach
- (+) No setup overhead
- (+) Maximum flexibility
- (-) Risk of inconsistent quality
- (-) No systematic claim verification
- (-) Session continuity problems
- (-) Harder to track progress

### Option C: Minimal tracking only
- (+) Low overhead
- (+) Some structure via backlog
- (-) Missing verification framework
- (-) Risk of unverified claims in final paper

## Decision

**Option A: Adopt Proposition methodology (adapted)**

The methodology will be adapted for the MST paper's needs:
- Additional focus on experimental data verification (not just literature)
- Data file traceability added to claim registry
- Folder structure includes `data/` for experimental results

Key components adopted:
1. `METHODOLOGY.md` -- Workflow phases and confidence tagging
2. `PAPER_VV_FRAMEWORK.md` -- V&V approach with quality gates
3. `claim_registry.md` -- Central claim tracking
4. Decision records (DR-*) -- Document key choices
5. `backlog.md` -- Task tracking

## Revisit If

- Methodology proves too heavyweight for paper scope
- Team prefers different approach
- Deadline pressure requires streamlining
