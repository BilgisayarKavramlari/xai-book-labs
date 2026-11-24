# Lab 24.2: Audit a Month of Adverse Action Notices

Chapter 24, Law, Standards and Audits · Code notebook (run and read; nothing needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end in a few seconds on a laptop CPU)

## Goal

Re-perform every decline notice of a synthetic month against the logged model version, test the notices against four requirements of Regulation B, find the root cause of the failures, and write a finding memo as an auditor would. The notebook reproduces the chapter's figure `ch24-reason-audit`.

## Tools and versions

`adverse_action_audit.ipynb`, Python 3.10, numpy 2.2.6, pandas 2.3.3, matplotlib 3.10.9 (all in `env/requirements.txt`). Jupyter kernel used for the check run: `xai-lab-venv`.

## Data

Synthetic credit applicants generated in the notebook with fixed seeds (no download, no license restrictions): credit used, missed payments in 24 months, age of oldest account, credit applications in 6 months and debt-to-income ratio. Two logistic models are fitted with a short Newton-Raphson routine in numpy: v1 on four inputs and v2 adding debt-to-income. The production log, including its planted faults, is simulated in the notebook; in real work you would load your organization's log.

## Legal basis of the tests (as of November 2026; not legal advice)

- Specific principal reasons: 12 CFR 1002.9(b)(2).
- Reasons must relate only to factors actually scored, and no principal reason may be left out: Supplement I, comment 9(b)(2)-4.
- More than four reasons is not likely to be helpful: comment 9(b)(2)-1.
- Notice within 30 days of a completed application: 1002.9(a)(1).
- Reason selection by comparison with average factor values is one acceptable method: comment 9(b)(2)-5.

These provisions were not changed by the CFPB's May 2025 withdrawal of guidance or its April 2026 amendments to Regulation B.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** v2's debt-to-income weight is about 1.87 (v1 does not score it); default rate 0.184.
3. **Checkpoint 2:** 1,395 decline notices in the month.
4. **Checkpoint 3:** reasons match re-performance in 0.736 of notices; the top reason matches in 0.942; 0.036 cite a factor that is not scored; none lists more than four reasons; 0.017 were sent after 30 days.
5. **Checkpoint 4:** the day chart shows days 10 to 20 far below the rest; 333 of the 514 notices in that window mismatch, and 320 of those omit debt-to-income.

## Expected results

Three findings of different kinds: a systemic one (a reason service out of step with the deciding model for eleven days), a template one (a legacy reason the model never scores) and a process one (late notices). All numbers above are reproducible exactly.

## What to hand in

The findings table, the day-by-day chart and a one-page finding memo: what was found, how many notices, which rule each finding conflicts with, root cause, remediation and the preventive control (for example, a shared version identifier checked at release between the decision model and the reason service).

## Self-check

- Why could no review of the notices themselves, without the log, have found the stale-weights failure?
- Which of the three findings would a sample of 30 notices most likely miss?
- If the model were a gradient-boosted ensemble with SHAP-based reasons, what else would the log need to record for re-performance to be possible (Chapter 23)?
