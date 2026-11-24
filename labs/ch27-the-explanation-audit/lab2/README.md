# Lab 27.2: The Reference Audit

Chapter 27, The Explanation Audit · Run-only notebook (one optional edit) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 85 seconds on a laptop CPU)

## Goal

Re-perform the evidence of the chapter's case study for a credit model, one audit test per part, and write the finding register and the opinion per use.

## Tools and versions

`reference_audit.ipynb`; Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, shap 0.49.1 (`env/requirements.txt`, kernel `xai-lab-venv`). Another scikit-learn or shap version may change the last digits.

## Data

German Credit (Statlog): 1,000 applicants, 20 attributes, 700 good and 300 bad outcomes (Hofmann, 1994; UCI Machine Learning Repository, CC BY 4.0, DOI 10.24432/C5NC77), fetched from OpenML as `credit-g`. See `data/german-credit.md` for its limits: the data is old and some attributes mix sex and marital status. It is used to learn audit methods, not to judge real lending.

## Steps

1. Open the notebook and run the cells in order. After each part, write one line in a finding register: criterion, condition, finding or no finding.
2. **Checkpoint 1 (Part A, scope):** test AUC 0.778; 57 of 300 test applicants declined (risk above 0.5).
3. **Checkpoint 2 (Part B, glass box):** gradient boosting 0.778 (bootstrap interval 0.722 to 0.830); logistic regression 0.811; difference -0.032, interval -0.073 to +0.008.
4. **Checkpoint 3 (Part C, faithfulness):** mean risk after the three stated reasons are replaced by background values 0.293, after three random features 0.575; gap 0.282 (interval 0.259 to 0.307); 96.5 percent of declined applicants fall below 0.5.
5. **Checkpoint 4 (Part D, stability):** second background, mean top-3 agreement 0.930 (identical for 86.0 percent); five retrains on bootstrap resamples, 0.578 (below 0.5 for 29.8 percent); share of the 57 still declined after each retrain 0.684, 0.544, 0.491, 0.825, 0.702.
6. **Checkpoint 5 (Part E, recourse):** naive generator: 28 of 57 suggestions use an immutable attribute (all age; 19 ask the applicant to be older), 21 use a slow feature or move a loan term the wrong way, 8 are actionable. Justified action set: 56 actionable, 1 without recourse.
7. **Checkpoint 6 (Part F, near-equal models):** 59 models, 17 within 0.01 cross-validated AUC of the reference (0.779); ambiguity 0.243, discrepancy 0.153; 20 applicants declined by every model, 93 by at least one; checking account in every model's top 3.
8. Optional (Part G): change the tolerance `EPS` and rerun Part F.

## Expected results

The numbers above, exactly, with the pinned versions (all randomness is seeded). The lessons: a faithfulness test can pass while stability across retrains fails; a recourse generator without an action set produces advice that is cheap for the model and useless or unlawful for the person; a glass box may match the black box on a small test set; and among equally good models, the global explanation can be shared while individual decisions are not.

## Questions

The notebook ends with five questions. Answer them in your hand-in.

## What to hand in

The finding register (at least four findings in the form criterion, condition, cause, effect, recommendation, with severity) and a one-paragraph opinion for each of three uses: developer debugging, reason codes in decline letters, recourse statements.

## Self-check

If an opinion says "the explanations are reliable" without naming the use and the tests behind it, rewrite it. The chapter's case study gives one possible version to compare with yours after you have written your own.
