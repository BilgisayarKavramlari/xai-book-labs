# Lab 5.2: The Glass-Box Baseline

Chapter 5, Glass-Box Models: Accuracy You Can Read · Run-only notebook (no code to write) · About 60 minutes (the cross-validation cell takes a few minutes) · Last checked: 2026-11-24 (executed end to end with the versions below)

## Goal

Fit five glass-box models and two black boxes on a public credit dataset with one validation design, test whether the accuracy gap is real, read the best glass box, check how stable its reading is, and test a monotonicity constraint. Then write the comparison a model risk team would ask for. This is the raw material for Dossier artifact 5.

## Tools and versions

`glass_box_baseline.ipynb`, Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, matplotlib 3.10.9, and **interpret-core 0.7.8** (InterpretML; install it in addition to `env/requirements.txt`). Runs on a laptop CPU in about five minutes.

## Data

German Credit (Statlog), 1,000 applicants, 20 attributes, good or bad credit label, loaded from OpenML (`credit-g`). Data card: `data/german-credit.md` (CC BY 4.0 as listed by UCI). Remember from Lab 1.2 that these applicants were already selected by a lender.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** 1,000 rows, 20 columns, bad rate 0.3.
3. **Checkpoint 2 (seven models):** with the pinned versions, mean AUC over 5-fold cross-validation repeated twice: random forest 0.797, EBM 0.793, spline GAM 0.792, logistic regression 0.792, binned logistic 0.784, gradient boosting 0.782, depth-3 tree 0.700; fold standard deviations 0.03 to 0.04.
4. **Checkpoint 3 (paired gap):** best black box (random forest) minus best glass box (EBM): mean +0.003, standard deviation of fold gaps 0.017; the black box is better in 60 percent of folds.
5. **Checkpoint 4 (reading the EBM):** `checking_status` is the most important term (about 0.64), followed by `purpose`, `savings_status` and `duration`. The `no checking` bar is the most negative (lowest risk).
6. **Checkpoint 5 (stability):** across five bootstrap refits, only `checking_status` is in the top three every time; the other places move, and pairwise terms sometimes appear.
7. **Checkpoint 6 (monotonicity):** gradient boosting without a constraint has five downward steps in average risk as duration grows (AUC 0.780); with an increasing constraint, none (AUC 0.778).

## Expected results

The numbers above, exactly, with the pinned versions (all randomness is seeded). Other versions may move them by a few thousandths; the pattern should hold: several families tie, the shallow tree lags, the reading of the top term is stable and the rest is not.

## Questions

A. Is the random forest's advantage worth its explanation cost for a lender using this model? Answer with the paired gap and its spread.

B. The EBM says having no checking account lowers risk. Would you show this term to an applicant as a reason? What would you do about it before deployment?

C. Which of the instabilities in Checkpoint 5 would matter to a validator, and how would you report them?

## What to hand in

A one-page comparison table (seven models, mean and spread, the paired gap), the three EBM shapes plotted in the notebook with two sentences each, your stability result, the monotonicity result, and a half-page recommendation to a model risk committee: which model to deploy and what the black box would add in explanation work.

## Self-check

If your recommendation picks the random forest because its mean AUC is highest, reread Checkpoint 3: is a gap of 0.003 with a spread of 0.017 evidence of anything?
