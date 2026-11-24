# Lab 23.2: A Test Drive for Explanation Tools

Chapter 23, Choosing, Measuring and Using XAI Tools · Code notebook (run, read and answer; no code needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about four minutes)

## Goal

Measure five explanation tools on one gradient-boosted credit model for correctness against an exact reference, stability over random seeds, cost and agreement, and reproduce Figures 23.2 to 23.4 of the chapter (convergence, stability and agreement).

## Tools and versions

`test_drive_harness.ipynb`, Python 3.10, the main environment in `env/requirements.txt`: numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, shap 0.49.1, lime 0.2.0.1, interpret-core 0.7.8, plus **hermai 0.1.8** and its dependency **seaborn 0.13.2** (add both to the environment: `hermai==0.1.8`, `seaborn==0.13.2`; `pip check` reported no conflicts). Jupyter kernel used for the check run: `xai-lab-venv`.

shap 0.49.1 is the last release that supports Python 3.10 (0.50.0 and later need Python 3.11 or newer). HermAI is maintained by the book's author; it is tested here exactly like the other tools.

## Data

German Credit (Statlog): 1,000 applicants, 20 attributes, label good or bad credit risk (Hofmann, 1994; UCI Machine Learning Repository, CC BY 4.0, DOI 10.24432/C5NC77). The notebook fetches it from OpenML (`credit-g`, version 1) on first run; see `data/german-credit.md`. Categorical attributes are stored as integer codes so that every tool sees the same 20 columns.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** test AUC 0.778; 57 of 300 test applicants have predicted risk above 0.5. The notebook explains the 20 with the highest risk.
3. **Checkpoint 2:** the efficiency check prints an error of order 1e-15. In the convergence table, Kernel SHAP with 64 coalitions has an absurd error (about 1e10: the regression is ill-posed with 20 features); from 128 coalitions the error falls from about 0.020 to 0.002 (4,096 coalitions), and Permutation SHAP from about 0.014 (82 evaluations) to 0.002 (5,122).
4. **Checkpoint 3:** Kernel SHAP with library defaults: mean error about 0.028 and 10 nonzero attributions per applicant out of 20.
5. **Checkpoint 4:** mean top-3 stability over ten seeds: TreeSHAP 1.00, Permutation SHAP 0.975, Kernel SHAP 0.970, LIME 0.853, HermAI 0.858; worst applicants about 0.70, 0.68, 0.50 and 0.54.
6. **Checkpoint 5:** top-3 overlap with TreeSHAP: Kernel 0.94, Permutation 0.98, LIME 0.46, HermAI 0.28.
7. **Checkpoint 6:** EBM test AUC 0.792; its local explanation adds up to the model output exactly.
8. The last cell saves `test_drive_results.json`, which Lab 23.3 reads.

## Expected results

All accuracy, stability and agreement numbers above are reproducible with the pinned versions and seeds. Runtimes depend on your machine; in the check run TreeSHAP took about 2 milliseconds per applicant, Permutation SHAP about 0.06 seconds, Kernel SHAP with defaults about 0.25 seconds, LIME about 0.03 seconds, HermAI about 0.015 seconds and the EBM about 0.2 milliseconds.

## What to hand in

The three result tables and a half-page validation note: which defaults you would change before any of these tools produced adverse action reasons, and why.

## Self-check

- Can you explain why Kernel SHAP with defaults is wrong by a fixed amount that more sampling would not remove?
- Can you explain why LIME and HermAI disagree with TreeSHAP without either being "broken"?
- Which of the tools would you allow to produce reasons that an applicant might ask for twice?
