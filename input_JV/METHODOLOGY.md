# Methodology: AI-Augmented Technical Paper Development

**Purpose:** Replicable methodology for developing the MST engineering fidelity paper with AI assistance.

**Adapted from:** `C:\local_dev\Proposition\input_JV\METHODOLOGY.md`

---

## 1. Overview

This methodology adapts engineering practices from AI-augmented research to technical measurement science papers. The goal: produce a rigorous, well-sourced paper with verified claims and traceable data.

---

## 2. Workflow Phases

### Phase 0: Problem Framing
1. Define research questions clearly
2. Identify target audience (measurement science researchers, CPR training community)
3. Select outlet format (MST Special Issue - Data-Centric)
4. Document decisions (DR-000, DR-001, etc.)

### Phase 1: Requirements
1. Define paper goals (what must the paper demonstrate?)
2. Specify success criteria (acceptance in MST special issue)
3. Identify key claims that need support
4. Map claims to required evidence/data

### Phase 2: Data Collection & Analysis
1. Compile human reference model from literature
2. Conduct manikin characterization experiments
3. Process and analyze data
4. Document all experimental procedures

### Phase 3: Literature Audit
1. Identify all claims in the argument
2. For each claim:
   - Find supporting source (literature OR own data)
   - Verify source exists (DOI check, data file check)
   - Extract exact citation (page, figure, table)
   - Tag confidence level
3. Flag unsupported claims for resolution

### Phase 4: Writing & Validation
1. Structure paper flow
2. Connect claims to evidence
3. Draft sections
4. Run claim audit (Section 4)
5. Peer/co-author review

### Phase 5: Submission Preparation
1. Format to MST requirements
2. Final citation check
3. Author agreement
4. Submit by March 31, 2026

---

## 3. Confidence Tagging

Tag all claims with confidence levels:

| Tag | Meaning | Action Required |
|-----|---------|-----------------|
| `[VERIFIED]` | Confirmed from source with exact location | None |
| `[HIGH CONF]` | Core result from authoritative source | Spot-check |
| `[MED CONF]` | Believe correct, details uncertain | Verify before using |
| `[LOW CONF]` | Plausible but uncertain | Must verify |
| `[NEEDS SOURCE]` | Cannot confirm without full paper | Human must check |
| `[OWN DATA]` | From our own experiments | Link to data file |
| `[OWN WORK]` | From our published/under-review papers | Link to source paper |

### Example

```markdown
Human adult chest stiffness ranges 5.3-13.6 N/mm [VERIFIED: Lim 2024, Table 2].

Manikin sensors show 5.6% calibration shift [OWN WORK: Korten et al. IEEE TIM, under review].

Manikin X shows stiffness of Y N/mm at 50mm depth [OWN DATA: experiments/compression_test_001.csv].
```

---

## 4. Claim Audit Process

Before finalizing any section, audit all claims.

### 4.1 Audit Template

For each claim:

```markdown
### Claim: [Statement]

**Type:**
- [ ] Literature-based (needs citation)
- [ ] Own empirical work (needs reference to our paper)
- [ ] Own experimental data (needs reference to data file)
- [ ] Logical inference (needs premises stated)

**If literature-based:**
- Source: [Author, Title, Journal, Year]
- Location: [Page, Table, Figure, Section]
- Quote/paraphrase: "[exact text]"
- Verification: [VERIFIED / NEEDS ACCESS / WEB-CHECKED]

**If own work (published/under review):**
- Source paper: [IEEE TIM / IEEE THMS / etc.]
- Specific finding: [statistic, p-value, effect size]

**If own data (this paper):**
- Data file: [path to CSV/data]
- Processing script: [path to analysis script]
- Figure/table: [where it appears in paper]

**If inference:**
- Premise 1: [claim] -> [source]
- Premise 2: [claim] -> [source]
- Conclusion follows: [yes/no/needs work]
```

### 4.2 Audit Workflow

```
Draft section
    |
List all claims (factual statements)
    |
For each claim:
    |-- Literature? -> Find exact citation -> Web-verify
    |-- Own work? -> Link to source paper -> Check accuracy
    |-- Own data? -> Link to data file -> Verify analysis
    '-- Inference? -> Verify premises -> Check logic
    |
Create audit document
    |
Flag gaps as MUST-FIX / SHOULD-FIX / MINOR
    |
Resolve MUST-FIX before proceeding
```

---

## 5. Anti-Hallucination Checklist

Before accepting any literature claim:

- [ ] Is the paper real? (Google Scholar / DOI check)
- [ ] Is the author real? (institutional page)
- [ ] Is the journal real? (publisher website)
- [ ] Does the claim match the paper's scope? (abstract check)
- [ ] Is the exact location cited? (page/table/figure)
- [ ] Have I read the relevant section? (not just abstract)

---

## 6. Document Structure

```
MechanicalFidelity/
|-- CLAUDE.md                    <- Session continuity (READ FIRST)
|-- MST_paper_outline.md         <- Paper structure
|-- input_JV/                    <- Working documents
|   |-- METHODOLOGY.md           <- This file
|   |-- DR-*.md                  <- Decision records
|   |-- backlog.md               <- Open tasks
|   '-- vv/                      <- V&V Framework
|       |-- PAPER_VV_FRAMEWORK.md
|       |-- claims/
|       |   '-- claim_registry.md
|       |-- audits/
|       |   '-- coverage_report.md
|       |-- oracles/
|       |   |-- author_guidelines.md
|       |   '-- exemplar_papers.md
|       |-- tests/
|       |   '-- static_checks.md
|       '-- validation/
|           |-- coauthor_review.md
|           '-- reviewer_checklist.md
|-- paper/                       <- LaTeX source (when writing begins)
|-- data/                        <- Experimental data
|   |-- compression/             <- Compression test data
|   '-- ventilation/             <- Ventilation test data
'-- references.bib               <- Bibliography
```

---

## 7. Decision Records

Use ADR template for all decisions:

```markdown
---
status: Proposed | Accepted | Superseded
date: YYYY-MM-DD
---

# Decision: [Title]

## Context
[Why this decision is needed]

## Options Considered

### Option A: [Name]
- (+) [pro]
- (-) [con]

### Option B: [Name]
- (+) [pro]
- (-) [con]

## Decision
**Option _: [Name]**

[Rationale]

## Revisit If
- [Condition that would trigger reconsideration]
```

Naming convention: `DR-NNN_short_description.md` (e.g., DR-001_reference_model_scope.md)

---

## 8. Session Continuity

### Starting a New Session

1. **Read CLAUDE.md** -- Project overview and current state
2. **Read backlog.md** -- Open tasks and blocked items
3. **Check recent DRs** -- Any decisions pending?
4. **Resume from last state** -- Don't restart work already done

### Ending a Session

1. **Update backlog.md** -- What's done, what's next
2. **Commit changes** -- Don't leave uncommitted work
3. **Update CLAUDE.md** if major progress made

### AI Handoff

If switching AI systems or sessions:
- CLAUDE.md is the primary handoff document
- All context should be recoverable from committed files
- No reliance on conversation memory

---

## 9. Quality Gates

### Before Drafting Section
- [ ] Claims identified
- [ ] Sources located (literature OR data)
- [ ] Confidence tags assigned

### Before Finalizing Section
- [ ] Claim audit complete
- [ ] All MUST-FIX resolved
- [ ] Citations formatted correctly

### Before Submission
- [ ] Full paper audit complete
- [ ] MST requirements met (word count, format, data availability)
- [ ] Co-author review done
- [ ] References double-checked
- [ ] Data files prepared for supplementary material

---

## 10. Paper V&V Framework

**Adapted from:** SU2049 Cyberphysical Systems V&V Methodology

Treat the paper as a system requiring validation and verification.

### Core Mapping

| Embedded Systems | Paper Production |
|-----------------|------------------|
| System requirements | Paper goals |
| Components | Claims |
| Unit tests | Claim verification |
| Test coverage | % claims verified |
| Static analysis | Build checks, word count |
| HIL testing | Expert review |
| Digital twin oracle | Author guidelines, exemplars |
| Stakeholder validation | Peer review simulation |

### Claim Priority (SIL-equivalent)

| Priority | Meaning | Coverage Target |
|----------|---------|-----------------|
| P0 | Core argument -- paper fails without it | 100% |
| P1 | Supporting -- strengthens argument | 90% |
| P2 | Context -- nice to have | 70% |

### Quality Gates

1. **Draft Complete** -- Claims registered, P0 identified
2. **Verification Complete** -- 85% coverage, static checks pass
3. **Review Complete** -- Co-author signoff, expert review
4. **Submission Ready** -- All gates pass

**Full framework:** `input_JV/vv/PAPER_VV_FRAMEWORK.md`

---

*Version: 1.0*
*Created: 2026-01-15*
*Adapted from: Proposition repository methodology*
