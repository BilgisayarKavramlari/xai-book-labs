# Lab 24.3: A Colorado-Style Disparity Test and Its Explanation

Chapter 24, Law, Standards and Audits · Code notebook (two settings may be edited; no other code needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end in a few seconds on a laptop CPU)

## Goal

Run the two steps of the Colorado Division of Insurance's draft quantitative test for life insurance underwriting on synthetic data: test whether groups are declined at significantly different rates with the allowed controls, attribute the difference to the variables of the underwriting model, and test a remediation. The notebook reproduces the chapter's figure `ch24-disparity`.

## Status of the rule (as of November 2026; not legal advice)

Colorado SB21-169 (2021) bars unfair discrimination through external consumer data and the models that use them. Governance Regulation 10-1-1 applies to life insurers since November 2023 and, as amended, to private passenger auto and health benefit plan insurers (effective October 15, 2025). The quantitative testing regulation described here was exposed as a **draft** in September 2023 and had **not been adopted** as of November 2026; a Division bulletin reissued in June 2026 waives the reporting of quantitative testing until it is. The draft's design is taken from the Division's presentation to the NAIC on October 11, 2023: race and ethnicity estimated with BIFSG; a prescribed logistic regression with policy type, face amount, age, gender and tobacco use as controls; a second test of each model variable when a significant difference appears; external data variables that contribute deemed unfairly discriminatory.

## Tools and versions

`disparity_test.ipynb`, Python 3.10, numpy 2.2.6, pandas 2.3.3, matplotlib 3.10.9 (all in `env/requirements.txt`). Logistic regressions and their standard errors are computed with a short numpy routine in the notebook, so no statistics package is needed. Jupyter kernel used for the check run: `xai-lab-venv`.

## Data

40,000 synthetic applicants generated in the notebook with fixed seeds. Groups are invented labels (reference and groups 1 to 3); group membership is observed directly here, whereas the draft would estimate it with BIFSG. By construction, an external lifestyle index differs in mean by group and carries little information about claims beyond what traditional factors already carry. The results describe the simulation, not real people or real insurers.

## Steps

1. Run all cells with the default settings.
2. **Checkpoint 1:** decline rates 0.146 (reference), 0.154, 0.164 and 0.147.
3. **Checkpoint 2 (step 1):** group 2 log-odds about 0.202 (p below 0.001), group 1 about 0.100 (p about 0.018), group 3 not significant.
4. **Checkpoint 3 (step 2):** for group 2 the external lifestyle index contributes about +0.082 of a total score gap of about +0.082.
5. **Checkpoint 4 (remediation):** refit without the index; group 2 log-odds about 0.029 (p about 0.56). The share of eventual claims that are declined barely moves (0.472 with the index, 0.468 without).
6. **Experiments:** set `INDEX_SHIFT = [0, 0, 0, 0]` and rerun; then restore it and try `DECLINE_SHARE` of 0.05 and 0.30.

## Expected results

With the defaults, a significant decline gap for groups 1 and 2 that an additive attribution assigns almost entirely to the external index, and that disappears, at almost no cost in claim capture, when the index is removed. With no group shift in the index, step 1 finds nothing to explain.

## What to hand in

The step 1 table, the step 2 attribution, the remediation result, your two experiments, and half a page on what this test cannot tell you (estimated group membership, the choice of attribution definition, correlated variables that may take over the removed variable's role, and the difference between a statistical disparity and "unfair discrimination" in law).

## Self-check

- Why is step 2 an explanation problem rather than a fairness metric?
- Name another definition of a variable's contribution and say how it could change the answer.
- What would you log so that a regulator could re-run your test a year later?
