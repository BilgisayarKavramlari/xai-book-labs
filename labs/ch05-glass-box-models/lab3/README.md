# Lab 5.3: Points, Rules and a Confounded Shape

Chapter 5, Glass-Box Models: Accuracy You Can Read · Notebook with one optional cell to change · About 75 minutes · Last checked: 2026-11-24 (executed end to end with the versions below)

## Goal

Build a small integer points card for a medical decision and see what rounding costs; watch an additive model learn a treatment effect as a protective factor, edit it and measure the edit; and compute Bayesian credible intervals that show which effects rest on little data.

## Tools and versions

`points_rules_confounding.ipynb`, Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, and **interpret-core 0.7.8**. Runs in under a minute on a laptop.

## Data

- Part A: Breast Cancer Wisconsin (Diagnostic), 569 cases with 30 measurements of cell nuclei and a malignant or benign label, bundled with scikit-learn (no download). Original source: Wolberg, W., Mangasarian, O., Street, N., and Street, W. (1993), UCI Machine Learning Repository, https://doi.org/10.24432/C5DW2B (CC BY 4.0 as listed by UCI). A teaching dataset; nothing here is diagnostic advice.
- Part B: synthetic pneumonia-style records generated in the notebook (20,000 patients; age, asthma, respiration rate). The effects are invented so that the truth is known: asthma raises untreated risk by +0.6 on the log-odds scale, and intensive care for every asthmatic patient changes it by `ICU_EFFECT` (default -1.5).
- Part C: German Credit (Statlog) from OpenML, as in Lab 5.2. Data card: `data/german-credit.md`.

## Steps

1. Run the cells in order.
2. **Checkpoint A:** an L1 logistic regression picks five yes-or-no items (each "measurement above its training median"), for example `worst concavity` and `worst area`; rounding the weights gives points of 1 or 2. Test AUC is 0.952 with exact weights and 0.954 with integer points. The share of malignant cases is 0 at 0 points and about 0.9 at 7 points, with small, wobbly groups in between.
3. **Checkpoint B1:** the EBM learns an asthma effect of about -0.94 (true untreated +0.6); test AUC 0.725.
4. **Checkpoint B2:** after editing the asthma term to +0.6 relative to no asthma, test AUC falls to 0.702.
5. **Optional:** set `ICU_EFFECT = 0.0` and rerun Part B. The learned effect should be about +0.5, near the true +0.6, and the edit should no longer cost accuracy (test AUC about 0.708 before and after).
6. **Checkpoint C:** with a Normal(0, 1) prior and the Laplace approximation, `checking_status_no checking` (394 applicants) has an odds ratio of 0.23 (0.15 to 0.34); `purpose_retraining` (9 applicants) has 0.46 with an interval from 0.12 to 1.71.

## Expected results

The numbers above, with the pinned versions and seeds. The lessons: integer points can cost almost nothing in ranking; an additive model shows a treatment effect plainly, and correcting it makes the model fit the historical data worse but serve its purpose better; credible intervals reveal which effects should never be stated as reasons.

## Questions

A. Write the points card from Part A as a person would use it. Which item would be hardest to measure consistently, and what does that do to the score's stability?

B. In Part B, who should approve the edit, and what three facts must the record contain?

C. In Part C, which effects would you be willing to give an applicant as a reason, and which not? Use the intervals.

## What to hand in

The points card with its two AUC values, the asthma term before and after the edit with both AUC values, your answers to A to C, and three sentences on what you would record about the edit.

## Self-check

If you concluded that the edit in Part B was a mistake because AUC fell, ask what the model will be used for and on which patients.
