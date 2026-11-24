# Lab 23.3: The Scored Comparison

Chapter 23, Choosing, Measuring and Using XAI Tools (the chapter's case study) · Code notebook (run; only the weights may be edited) · About 45 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in under a minute, after Lab 23.2)

## Goal

Measure counterfactual tools on 20 declined applicants, turn all test-drive measurements into a weighted scorecard with written rules, stress-test the weights, and write the recommendation of the case study.

## Tools and versions

`scored_comparison.ipynb`, Python 3.10: numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, dice-ml 0.12 (with raiutils 0.4.3), interpret-core 0.7.8, hermai 0.1.8, seaborn 0.13.2. Jupyter kernel used for the check run: `xai-lab-venv`. HermAI is maintained by the book's author and is scored by the same rules as the other tools.

## Data

German Credit (Statlog), as in Lab 23.2 (UCI, CC BY 4.0, fetched from OpenML as `credit-g`). Run Lab 23.2 first: this notebook reads `../lab2/test_drive_results.json`.

## The scenario

An invented retail bank must approve explanation tooling for its gradient-boosted credit model: principal reasons for declines, a global view for validators, and counterfactual suggestions that never involve age, personal status or foreign-worker status. Four toolsets survived the filter (Alibi was dropped on license; the stack is pinned to Python 3.10):

- A: SHAP TreeExplainer + DiCE on the approved model
- B: Explainable Boosting Machine replacing the model + DiCE
- C: LIME + DiCE
- D: HermAI 0.1.8 alone

## Steps

1. Run all cells in order.
2. **Checkpoint 1 (counterfactuals):** every configuration finds a valid counterfactual for all 20 declines. DiCE with every feature free: 55 percent of counterfactuals change an immutable feature, about 1.7 features changed. DiCE with immutables fixed: 0 percent, about 1.8 features. HermAI 0.1.8: 100 percent, about 11.2 features (it has no option to fix features).
3. Read the scoring rules in section 3. Each rule is written before any total is seen.
4. **Checkpoint 2 (totals):** A 4.68, B 4.40, C 3.60, D 3.15. In 10,000 weight variations, A ranks first in about 94 percent and B in about 6 percent. With "Works with the approved model" at 2.5 percent or less, B leads.
5. Change the weights in section 4 to your own and rerun the last two cells.

## What to hand in

Your scorecard with your weights, the stress-test output, and a one-page tool memo: recommendation, conditions, versions to pin, the strongest alternative and a review date.

## Self-check

- Did you write down why each weight has the value it has?
- Is any of your criteria a property of your situation rather than of the tool? Say so in the memo.
- Does your recommendation survive the stress test? If not, which single weight decides it?
