# Paper Validation & Verification Framework

**Adapted from:** SU2049 Cyberphysical Systems V&V Methodology via Proposition repository

**Purpose:** Treat academic paper production as a system requiring systematic validation and verification.

---

## 1. Core Principle

> A paper is a system. Claims are components. Sources are tests. Reviewers are stakeholders.

Just as embedded systems require systematic V&V to ensure reliability, academic papers require systematic verification to ensure correctness and credibility.

---

## 2. V&V Mapping

| Embedded Systems V&V | Paper Production V&V |
|---------------------|---------------------|
| System requirements | Paper goals (what must the paper demonstrate?) |
| Components | Claims (individual statements of fact/data) |
| Unit tests | Claim verification (source exists, data supports claim) |
| Test coverage | % of claims with verified sources |
| Static analysis | Automated checks (BibTeX, word count, structure) |
| HIL testing | Expert review (co-author, domain expert) |
| Digital twin oracle | Reference documents (guidelines, exemplars) |
| CI/CD pipeline | Build automation (LaTeX compile, checks) |
| Stakeholder validation | Peer review simulation |
| Traceability matrix | Claim -> Evidence -> Audit trail |
| SIL classification | Claim priority (P0/P1/P2) |

---

## 3. Claim Priority Classification

Analogous to Safety Integrity Levels (SIL):

| Priority | Meaning | Verification Required |
|----------|---------|----------------------|
| **P0** | Core argument claim -- paper fails without it | Must have [VERIFIED] source OR [OWN DATA] with exact location |
| **P1** | Supporting claim -- strengthens argument | Should have [HIGH CONF] or better |
| **P2** | Context/background claim -- nice to have | [MED CONF] acceptable |

### Coverage Targets

| Priority | Target Coverage |
|----------|----------------|
| P0 claims | 100% verified |
| P1 claims | 90% verified |
| P2 claims | 70% verified |
| **Overall** | **>=85% verified** |

---

## 4. Test Types

### 4.1 Unit Tests (Claim-Level)

Each claim verified independently:

```markdown
CLAIM: "Human adult chest stiffness ranges 5.3-13.6 N/mm at 50mm depth"
|-- Source: Lim et al. 2024
|-- Location: Table 2, Results section
|-- Values: 5.3-13.6 N/mm (range across subjects)
|-- DOI: 10.1109/JTEHM.2024.3410652
'-- Status: [VERIFIED]
```

```markdown
CLAIM: "Manikin X shows stiffness of 8.2 N/mm at 50mm depth"
|-- Source: Own experimental data
|-- Data file: data/compression/manikin_x_test_001.csv
|-- Analysis: scripts/analyze_compression.py
|-- Figure: Fig. 3a
'-- Status: [OWN DATA]
```

### 4.2 Static Analysis (Automated Checks)

| Check | Tool/Method | Pass Criteria |
|-------|-------------|---------------|
| LaTeX compiles | `pdflatex` exit code 0 | No errors |
| BibTeX valid | `biber` exit code 0 | All refs resolve |
| DOIs exist | Web lookup | All DOIs return 200 |
| Word count | `texcount` | Within MST limit |
| Data files exist | Script check | All referenced files present |
| Figure sources | Manual check | All figures from own data or cited |

### 4.3 Integration Tests (Argument Flow)

- Claims connect logically
- No contradictions between sections
- Evidence supports conclusions
- Reference model -> Manikin data -> Gap analysis flow is coherent

### 4.4 System Tests (Full Paper)

- Paper achieves stated goals
- Data-centric framing clear (required for MST special issue)
- Meets journal requirements

### 4.5 Acceptance Tests (Stakeholder)

| Stakeholder | Test |
|-------------|------|
| Co-author | Review and signoff |
| Domain expert | Technical accuracy check |
| Simulated reviewer | Critical reading with reviewer mindset |

---

## 5. Oracle Documents

Reference documents that define "correct" behavior:

### 5.1 Specification Oracle
- **MST Author Guidelines** -- Journal requirements (word count, structure, data policy)
- **Paper goals** -- What the paper must demonstrate

### 5.2 Behavioral Oracle
- **Exemplar papers** -- Successful MST papers, especially from special issues
- **Own empirical work** -- IEEE TIM, IEEE THMS as source of validated methodology

### 5.3 Domain Oracle
- **Human reference data** -- Tomlinson 2007, Lim 2024, etc. (ground truth for comparison)
- **AHA/ERC Guidelines** -- CPR standards context

---

## 6. Traceability Matrix

Every claim traceable from requirement to evidence:

```
Paper Goal (Requirement)
    |
Claim (Component)
    |
Evidence (Source OR Data)
    |
Verification (Audit)
    |
Status (Pass/Fail)
```

### Example

| Goal | Claim | Evidence | Audit | Status |
|------|-------|----------|-------|--------|
| G1: Establish human reference | "Adult stiffness 5.3-13.6 N/mm" | Lim 2024, Table 2 | audit_section2.md | [ ] |
| G2: Characterize manikins | "Manikin X shows Y N/mm" | data/compression/manikin_x.csv | audit_section5.md | [ ] |
| G3: Quantify fidelity gap | "Manikin X deviates Z% from human range" | Calculated from G1+G2 | audit_section6.md | [ ] |

---

## 7. Workflow Integration

### Pre-Writing (Data Collection)
1. Define paper goals (requirements.md)
2. Collect human reference data from literature
3. Conduct manikin experiments
4. Process and verify data

### During Writing
1. Register each claim in claim_registry.md
2. Find and verify sources immediately
3. Tag confidence level
4. Link data claims to specific files

### Post-Draft
1. Run static analysis checks
2. Generate coverage report
3. Audit unverified claims
4. Expert review (HIL equivalent)

### Pre-Submission
1. 100% P0 claims verified
2. All static checks pass
3. Co-author signoff
4. Simulated peer review complete
5. Data availability statement prepared

---

## 8. Folder Structure

```
input_JV/vv/
|-- PAPER_VV_FRAMEWORK.md    <- This file
|-- claims/
|   '-- claim_registry.md    <- All claims with priority & status
|-- audits/
|   |-- section_X_audit.md   <- Per-section claim audits
|   '-- coverage_report.md   <- Overall verification coverage
|-- oracles/
|   |-- author_guidelines.md <- MST requirements (spec)
|   '-- exemplar_papers.md   <- Reference successful papers
|-- tests/
|   |-- static_checks.md     <- Checklist for automated checks
|   '-- build_log.md         <- LaTeX/BibTeX build results
'-- validation/
    |-- coauthor_review.md   <- Co-author feedback
    '-- reviewer_checklist.md<- Simulated peer review
```

---

## 9. Quality Gates

### Gate 1: Draft Complete
- [ ] All sections drafted
- [ ] Claim registry populated
- [ ] P0 claims identified
- [ ] Data files organized

### Gate 2: Verification Complete
- [ ] P0 claims 100% verified
- [ ] P1 claims 90% verified
- [ ] Coverage report generated
- [ ] Static checks pass

### Gate 3: Review Complete
- [ ] Co-author signoff
- [ ] Expert review (if applicable)
- [ ] Simulated peer review done

### Gate 4: Submission Ready
- [ ] All gates passed
- [ ] MST requirements met
- [ ] Final proofread complete
- [ ] Data availability prepared

---

*Adapted from SU2049 KIEM HighTech V&V methodology via Proposition repository*
*Version: 1.0*
*Created: 2026-01-15*
