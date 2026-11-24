# Lab 10.3: Which Training Cases Matter?

Chapter 10, Explaining with Examples and Training Data · Run-only notebook (one optional cell to edit) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 20 seconds on a laptop CPU)

## Goal

Compare influence function estimates with actual leave-one-out retraining, see that the most similar training cases are not the most influential ones, and find planted wrong labels with self-influence (influence function), TracIn and Data Shapley, including a check of how stable Data Shapley is across runs.

## Tools and versions

Python 3.10, numpy 2.2.6, scikit-learn 1.7.2, matplotlib 3.10.9. Notebook: `which_training_cases_matter.ipynb`. The influence function, TracIn and Monte Carlo Data Shapley are written out in numpy so that you can read every step; libraries such as Captum (TracIn) and Kronfluence (EK-FAC influence functions) implement them for PyTorch models (checked 2026-11-24; Chapter 23 compares tools).

## Data

The Wisconsin Diagnostic Breast Cancer data bundled with scikit-learn (`load_breast_cancer`): 569 cases, 30 features computed from images of cell nuclei, label 1 benign and 0 malignant; original source UCI, https://doi.org/10.24432/C5DW2B, CC BY 4.0. The lab uses 200 training and 200 validation cases and flips 20 training labels on purpose. Use the data to learn methods, not to draw clinical conclusions.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** 200 training cases with 20 flipped labels, 200 validation cases.
3. **Checkpoint 2:** for validation case 77 the influence estimate and retraining correlate at 0.979; the top five lists share four cases.
4. **Checkpoint 3:** the ten nearest and the ten most influential training cases share 4 of 10; 6 of the ten most influential carry a flipped label.
5. **Checkpoint 4:** in the first 40 cases inspected, self-influence (influence function) finds 20 of 20 flipped labels, TracIn self-influence 20 of 20 and Data Shapley (60 orderings) 17 of 20.
6. **Checkpoint 5:** two Data Shapley runs with different random orderings correlate at 0.649 and share 15 of their 20 lowest-valued cases.
7. Optional: change the number of flipped labels to 40 in the first cell and rerun.

## Expected results

The numbers above come from the versions listed with the seeds in the notebook. The Data Shapley numbers are Monte Carlo estimates and can move by a few cases with another version; the pattern (influence close to retraining, all methods far better than random at finding wrong labels, Data Shapley visibly noisy) should hold.

## Questions

1. Part A worked almost perfectly. Name two reasons it would not work as well for a deep network (Basu et al., 2021; Bae et al., 2022).
2. Why does a flipped label have high self-influence? Two sentences, no formulas.
3. Data Shapley needed thousands of model fits here, for 200 cases. What would you use for 2 million cases, and what would you lose?
4. Optional: with 40 flipped labels, which method degrades most?

## What to hand in

A half-page note with the correlation from Part A, the overlap from Part B, the label-finding results from Part C and the stability result from Part D, each with one sentence of interpretation, plus your answers to the questions.

## Self-check

If your note reports Data Shapley values without saying how many orderings were used and how stable they were, add both: an attribution score without its stability is not evidence.
