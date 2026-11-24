# Lab 9.2: Recourse for Declined Applicants

Chapter 9, What Would Have to Change? Counterfactuals, Causality and Recourse · Run-only notebook (one cell to edit at the end) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below; about 1 to 2 minutes on a laptop CPU)

## Goal

Train a credit model on a public dataset, find the cheapest change that would turn each declined applicant into an approved one, first with no constraints and then with only actionable changes, compare with DiCE, and check who pays more for recourse and whether one causal link changes the picture. This lab reproduces the data case study of Chapter 9.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2 (see `env/requirements.txt`), plus dice-ml 0.12 (which installs raiutils 0.4.3). Install DiCE with `pip install dice-ml==0.12`. The notebook is `recourse_german_credit.ipynb`; it also runs in a hosted notebook service.

## Data

German Credit (Statlog), 1,000 applicants, 20 attributes, label good or bad credit risk, downloaded from OpenML (`credit-g`). See `data/german-credit.md` for source, license (CC BY 4.0 as listed by UCI) and known limitations. Amounts are in Deutsche Mark (DM). If you are offline, put `german_credit.csv` in `data/` as described in Lab 1.2.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** test AUC 0.847; 87 of 300 test applicants declined at a predicted probability of good risk below 0.6.
3. **Checkpoint 2:** 15 of 87 unconstrained counterfactuals change a feature the applicant cannot change now (age or employment); median cost 0.178 unconstrained and 0.203 actionable; loan duration is the most used feature in both (56 and 64 applicants).
4. **Checkpoint 3:** the chosen applicant asked for 3,345 DM over 24 months and scores 0.594. Four routes: a term of 18 months (cost 0.088), savings one band higher (0.333), an installment rate of 3 instead of 4 (0.333), a checking balance of 200 DM or more (1.0).
5. **Checkpoint 4:** DiCE returns four counterfactuals with a score of at least 0.6. Look for any that move a category in a direction the applicant cannot or should not take. DiCE output can change between versions.
6. **Checkpoint 5:** median cost of actionable recourse 0.265 for the 32 declined applicants recorded as female, 0.176 for the 55 others.
7. **Checkpoint 6:** 63 of 87 recourses shorten the loan; under the assumed structural equation the installment rate rises for 21 of them; the model still approves 86 of 87.
8. **Your turn:** remove the two non-improving moves (closing the checking account, registering a telephone) from `moves`, rerun sections 3 and 6, then allow `duration` to change only upward and rerun.

## Expected results

The numbers above come from scikit-learn 1.7.2 with `random_state=0` and match `figures/scripts/ch09_figs.py` in the book repository. Other versions may move costs by a few hundredths; the pattern should hold: unconstrained counterfactuals sometimes ask for impossible changes, shortening the loan dominates actionable recourse, and the model hardly reacts to the higher installment rate.

## Questions

1. Which features does the unconstrained search use that the actionable search cannot? Would you show any of them to an applicant?
2. Why can a cost function based on the range of each feature make some changes look cheaper than they are for a real person? Propose a better cost for loan duration.
3. The female and other groups differ in median cost. List three reasons other than the model itself that could produce such a difference, and say what data you would need to tell them apart.
4. DiCE and the chapter's search gave different routes for the same applicant. Which would you put in a letter, and why?

## What to hand in

A one-page note: the table of features used (unconstrained versus actionable), the group comparison with your caveats, your answers to the four questions, and two sentences on what changing the action set did in step 8. This feeds the recourse analysis in your Explanation Dossier.

## Self-check

If your actionable recourses ever change age, sex and marital status or foreign-worker status, the action set is wrong. If you report the group difference as a finding about discrimination without caveats, reread the case study's "Who pays more" paragraph.
