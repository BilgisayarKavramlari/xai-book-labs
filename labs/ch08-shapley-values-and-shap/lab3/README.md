# Lab 8.3: Backgrounds, Correlation and Estimators

Chapter 8, Shapley Values and SHAP · Notebook with a few cells to edit · About 75 minutes · Last checked: 2026-11-24 (end-to-end run; about 20 seconds on a laptop CPU)

## Goal

Build Shapley values from scratch, check them against a library, and watch them change with feature correlation, the value function (interventional or observational) and the sampling budget. Finish with SHAP interaction values.

## Tools and versions

Python 3.10, numpy 2.2.6, scikit-learn 1.7.2, matplotlib 3.10.9, shap 0.49.1 (with numba 0.68.1). Or open `backgrounds_correlation_estimators.ipynb` in a hosted notebook service and install shap first.

## Data

Synthetic only, generated in the notebook with fixed seeds. No download and no license questions.

## Steps

1. Open the notebook and run Section 1.
   **Checkpoint 1:** the from-scratch values (all 4,096 coalitions, background of 50 rows) and the library's interventional TreeSHAP values agree to better than $10^{-7}$ and add up to the gap of 3.350. $x_1$ gets 3.207; $x_2$ and $x_3$ get -0.431 and -0.361, mostly their shares of the $x_2 x_3$ interaction.
2. Run Section 2.
   **Checkpoint 2:** at a correlation of 0.9, interventional values are about (0.99, 0.00, 1.00); observational values about (0.55, 0.45, 1.00).
   **Checkpoint 3:** the plot shows the interventional value of $x_2$ flat at 0 and the observational value following $\rho/2$.
   EDIT: change `rho` to 0.0 and 0.95 and rerun the cell.
3. Run Section 3.
   **Checkpoint 4:** at a budget of 1,024 coalitions, relative errors are about 0.02 (permutation sampling), 0.016 (Kernel SHAP, library default) and 0.011 (Kernel SHAP without feature selection). The default keeps only 10 of the 12 features; here the two it drops have small values, so the cost is small. On the 19-feature credit model of Chapter 8, the same default left an error of about 18 percent that more samples did not reduce.
   EDIT: add 2048 to `budgets` if you have time.
4. Run Section 4.
   **Checkpoint 5:** the largest off-diagonal interaction is between features 2 and 3, about -0.379 in each half of the symmetric matrix; each row sums to that feature's path-dependent SHAP value.

## Expected results

The numbers above come from the versions listed with the seeds in the notebook. Monte Carlo noise moves the third decimal in Section 2; sampling noise moves Section 3. The patterns should hold with other versions.

Library note (checked 2026-11-24): in shap 0.49.1, `KernelExplainer.shap_values` uses `l1_reg="num_features(10)"` by default, and `TreeExplainer` uses the interventional method when a background is passed and the path-dependent method otherwise. Both defaults date from shap 0.47: the Kernel default changed from `"auto"` to `"num_features(10)"`, and the Tree default was renamed from `"interventional"` (which already fell back to path-dependent without a background) to `"auto"`, which makes the same switch explicitly. Check both defaults in whatever version you use, and write them into your report.

## Questions

1. Why does the observational value function give credit to $x_2$, which the model never reads? When would that be the answer you want?
2. Which estimator would you use for a model with 300 features and no tree structure, and how would you choose the budget?
3. The interaction values show what a single bar of SHAP values hides. Give one example from credit or medicine where a hidden interaction would change what an operator does.

## What to hand in

The three plots (correlation sweep, estimator errors, interaction matrix) and a half-page note on the settings you would record in any SHAP report: background and its size, value function, output scale, estimator and budget, library version and defaults, seeds.

## Self-check

If your from-scratch values do not match the library, check that you used the same background rows for both. If the observational values of $x_2$ do not grow with the correlation, check which features the value function fills in conditionally.
