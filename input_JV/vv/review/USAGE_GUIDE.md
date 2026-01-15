# How to Use the MST AI Review Prompts

## Overview

You have **three prompt options** for AI-assisted manuscript review tailored to the MST special issue on "Data-Centric Exploration and Explanation of Physical and Engineering Phenomena":

1. **Single-Stage Prompt** - All-in-one comprehensive review
2. **Stage 1 Prompt** - High-level assessment / gate decision
3. **Stage 2 Prompt** - Detailed section-by-section review

## Which Approach Should You Use?

### Use Single-Stage When:
- You want one comprehensive review
- You're reviewing a shorter manuscript (<15 pages)
- You want everything in one conversation
- You're doing a quick self-check

### Use Two-Stage When:
- You want to screen before deep review
- You're reviewing longer manuscripts (>15 pages)
- You want separate "gate decision" vs "detailed feedback"
- You're iterating on revisions (quick Stage 1 check, detailed Stage 2 when needed)

## Integration with V&V Framework

These prompts support the Paper V&V Framework quality gates:

| V&V Gate | Review Stage | Purpose |
|----------|--------------|---------|
| Gate 1: Draft Complete | Stage 1 | Quick check: does draft meet minimum standards? |
| Gate 3: Review Complete | Stage 2 | Detailed feedback before co-author review |
| Gate 4: Submission Ready | Single-Stage | Final comprehensive check |

## How to Use Single-Stage Prompt

**Step 1:** Start a new conversation with Claude (or use Claude Code)

**Step 2:** Provide your manuscript (paste text, upload file, or reference path)

**Step 3:** Copy-paste the entire `MST_Review_Prompt_Single_Stage.md` content

**Step 4:** Add at the end:
```
Please review the attached/above manuscript using the criteria above.
```

**Step 5:** Claude will provide:
- Overall score and recommendation
- Detailed scores for all 8 criteria
- Strengths and weaknesses
- Required/recommended/optional changes
- Section-by-section feedback
- MST-specific guidance

## How to Use Two-Stage Prompts

### STAGE 1: Initial Assessment

**Step 1:** Start a new conversation with Claude

**Step 2:** Provide your manuscript

**Step 3:** Copy-paste the entire `MST_Review_Prompt_Stage1.md` content

**Step 4:** Add:
```
Please conduct the Stage 1 assessment for the manuscript above.
```

**Step 5:** Claude will provide:
- Gate decision (Proceed/Reject/Redirect)
- High-level scores on 5 critical dimensions
- Fatal flaws identification (if any)
- Recommendation on whether to proceed to Stage 2

**Decision Point:**
- If Stage 1 says **REJECT** → Fix major issues first
- If Stage 1 says **PROCEED** → Continue to Stage 2

### STAGE 2: Detailed Review

**Step 6:** In the SAME conversation, copy-paste `MST_Review_Prompt_Stage2.md`

**Step 7:** Add:
```
Now please conduct the Stage 2 detailed review, building on your Stage 1 assessment.
```

**Step 8:** Claude will provide:
- Section-by-section detailed feedback
- Figure/table quality assessment
- Uncertainty analysis review
- Actionable revision requirements
- Writing quality analysis
- Reproducibility assessment

## MST Special Issue Criteria

The prompts emphasize these special issue priorities:

| Criterion | Weight | Focus |
|-----------|--------|-------|
| Data-Centric Contribution | 20% | Novel insights from systematic data analysis |
| Physics-Informed Modeling | 15% | Grounded in physical/biomechanical principles |
| Measurement Methodology | 15% | Sound, reproducible measurement approach |
| Uncertainty Quantification | 15% | Rigorous uncertainty analysis |
| Experimental Design | 10% | Appropriate design and statistics |
| Originality | 10% | Novel contribution to field |
| Clarity | 10% | Clear presentation and organization |
| Reproducibility | 5% | Others can replicate the work |

## Tips for Best Results

### 1. Manuscript Format
- **Best:** Markdown or plain text - Claude sees full content
- **Good:** Word docs - Claude can extract text
- **Works:** PDFs - text extraction may lose some formatting

### 2. Iterative Review
Use these prompts multiple times:
- v1.0 draft → Get review → Make revisions
- v1.1 draft → Re-review → See improvements
- v2.0 draft → Final review before submission

### 3. Follow-Up Questions
After initial review, ask:
- "Can you elaborate on the uncertainty quantification issues?"
- "Provide specific suggestions for strengthening the data-centric contribution"
- "Which figures need the most improvement and how?"
- "Draft an improved abstract based on your feedback"

### 4. Self-Review Before Co-Author Review
Run Stage 1 before sending to co-authors:
- Catches obvious issues early
- Saves co-author time
- Identifies areas needing your attention

### 5. Calibration
If Claude seems too harsh or lenient:
```
Please calibrate your review to MST standards for the special issue on
"Data-Centric Exploration and Explanation." Be rigorous but fair.
```

## Example Workflow

### Pre-Submission Workflow
```
1. Complete first draft
2. Run Stage 1 quick check
   → Fix any fatal flaws identified
3. Run Stage 2 detailed review
   → Address all required changes
   → Consider recommended changes
4. Send to co-authors
5. Incorporate co-author feedback
6. Run Single-Stage final review
7. Submit to MST
```

### Revision Workflow (after peer review)
```
1. Address reviewer comments
2. Run Single-Stage review on revised manuscript
3. Check that reviewer concerns are addressed
4. Verify no new issues introduced
5. Submit revision
```

## Integration with Claim Registry

After running a review, update the claim registry:
- Mark claims that received positive feedback as stronger
- Flag claims that received criticism for verification
- Add any new claims suggested by the review

## Common Issues and Fixes

### Issue: "Review doesn't address special issue fit"
**Fix:** Emphasize at the start:
```
This manuscript is being prepared for the MST special issue on
"Data-Centric Exploration and Explanation of Physical and Engineering Phenomena."
Please evaluate fit for this specific special issue.
```

### Issue: "Feedback too general"
**Fix:** Add:
```
Please be extremely specific. Reference section numbers, figure numbers,
and provide concrete examples of issues and specific text suggestions.
```

### Issue: "Missing uncertainty analysis feedback"
**Fix:** Ask specifically:
```
Please provide detailed feedback on the uncertainty analysis.
Is it GUM-compliant? Are all sources identified? Is the budget complete?
```

## Files in This Folder

```
input_JV/vv/review/
├── USAGE_GUIDE.md                    ← This file
├── MST_Review_Prompt_Single_Stage.md ← Comprehensive review
├── MST_Review_Prompt_Stage1.md       ← Gate decision
└── MST_Review_Prompt_Stage2.md       ← Detailed review
```

---

**Remember:** These prompts are tools to assist your review process, not replace your expertise. Always apply your own judgment and domain knowledge. The goal is to catch issues early and improve manuscript quality before submission.
