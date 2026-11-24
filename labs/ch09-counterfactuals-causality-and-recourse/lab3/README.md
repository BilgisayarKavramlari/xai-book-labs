# Lab 9.3: Causal Recourse and Recourse That Lasts

Chapter 9, What Would Have to Change? Counterfactuals, Causality and Recourse · Run-only notebook (one cell to edit at the end) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below; about 3 minutes on a laptop CPU)

## Goal

Part A: in an invented world where we know the causes, compare three pieces of advice for a declined applicant: a counterfactual that treats features as independent, a causal intervention, and a cheap proxy change that moves the score without changing the outcome. Part B: measure how many recourses for the German Credit model survive retraining, and what a safety margin costs.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scipy 1.15.3, scikit-learn 1.7.2 (see `env/requirements.txt`). The notebook is `causal_and_robust_recourse.ipynb`.

## Data

Part A uses synthetic data generated in the notebook from a stated structural causal model (5,000 invented applicants; nothing about real people). Part B uses German Credit (Statlog) from OpenML (`credit-g`); see `data/german-credit.md`.

## The invented structural causal model

- income := U_I (thousands per month, gamma distributed)
- savings := 2 x income + U_S
- phone := 1 if income + U_P > 3 (a registered telephone, caused by income, causing nothing)
- repay := 1 if 0.9 x income + 0.2 x savings + U_R > 3.7

A logistic regression is fitted on income, savings and phone to predict repay.

## Steps

1. Run Part A. **Checkpoint 1:** fitted weights about 1.28 (income), 0.43 (savings) and 0.19 (telephone), intercept -6.22; repayment rate 0.541. The telephone gets a positive weight although it causes nothing.
2. **Checkpoint 2:** for the applicant (income 2.5k, savings 5k, no telephone) the model score is 0.30 and the true repayment probability 0.32. Income must rise by 0.66k with savings held fixed, but only by 0.39k when savings follow; after that intervention the model score is 0.50 and the true probability 0.53. Registering a telephone gives a model score of 0.34 and leaves the true probability at 0.32.
3. **Checkpoint 3:** for the 2,361 declined applicants, giving everyone a telephone raises the mean model score from 0.172 to 0.191 and leaves the mean true repayment probability at 0.179.
4. Run Part B (about three minutes). **Checkpoint 4:** the share of recourses still approved after retraining, averaged over 20 bootstrap models, is 0.638 with no margin, 0.699 at 0.05, 0.772 at 0.10 and 0.826 at 0.15; the median cost rises from 0.203 to 0.265, 0.353 and 0.676.
5. **Your turn:** pick an applicant whose recourse fails under several retrained models and print the 20 scores it receives.

## Expected results

Part A results are exact for the seed in the notebook. Part B numbers match Chapter 9's durability figure (scikit-learn 1.7.2, `random_state=0`); other versions may move them by a few hundredths.

## Questions

1. In Part A, the model gives the telephone a positive weight even though it causes nothing. Why? What would happen to the weight if income were measured perfectly and included?
2. Why does the causal intervention need a smaller rise in income than the counterfactual that holds savings fixed? Construct a variant of the model where the causal answer needs a larger change.
3. In Part B, would you rather offer applicants a margin of 0.10 or a promise to honor recourse for six months? Argue from the applicant's and the lender's side.

## What to hand in

The results of the three pieces of advice in Part A, the durability table from Part B, your answers to the questions and a three-sentence policy on what a lender should promise an applicant who follows a recourse.

## Self-check

If the telephone move changed the true repayment probability in your run, you edited the structural model; the telephone causes nothing by construction. If the share of recourses that survive retraining does not rise with the margin, check that you searched with `thr=THR + margin` but evaluated at `THR`.
