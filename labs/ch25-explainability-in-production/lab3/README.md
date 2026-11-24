# Lab 25.3: What Explanations Give Away

Chapter 25, Explainability in Production · Code notebook (run and read; Section 4 asks you to edit one setting) · About 40 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 30 seconds)

## Goal

Measure how much faster a model can be copied when its interface returns TreeSHAP attributions with each decision, test a coarsened explanation as a defense, and run a simple membership check. The notebook reproduces Figure 25.2 of the chapter.

## Tools and versions

`what_explanations_give_away.ipynb`, Python 3.10, the main environment in `env/requirements.txt`: numpy 2.2.6, scikit-learn 1.7.2, matplotlib 3.10.9, shap 0.49.1. Jupyter kernel used for the check run: `xai-lab-venv`.

## Data

Synthetic: scikit-learn `make_classification` with 6,000 rows and 8 features (5 informative, 1 redundant), `random_state=1`. The target model is a gradient-boosted classifier trained on the first 4,000 rows. The attacker draws queries from a multivariate normal with the data's mean and covariance (it knows roughly where inputs lie, but not the training data). No personal data are involved.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** target accuracy on held-out rows 0.9145.
3. Section 1 shows that the base value plus the attributions equals the model's raw score for three points.
4. **Checkpoint 2:** agreement with the target on 4,000 fresh points, averaged over five repetitions:

| Queries | 10 | 25 | 50 | 100 | 200 | 400 | 800 | 1600 |
|---|---|---|---|---|---|---|---|---|
| Labels only | 0.648 | 0.741 | 0.762 | 0.809 | 0.850 | 0.874 | 0.896 | 0.908 |
| Labels and attributions | 0.746 | 0.816 | 0.858 | 0.880 | 0.898 | 0.902 | 0.908 | 0.914 |
| Top three attributions, rounded to 0.5 | 0.700 | 0.806 | 0.842 | 0.859 | 0.884 | 0.892 | 0.897 | 0.899 |

5. **Checkpoint 3:** membership AUC of the attribution-size signal about 0.51 (little leakage by this crude signal for this model; this does not rule out stronger attacks).
6. Section 4: change the number of attributions kept in the defense to 1 and to 5 and record the agreement at 50 and 400 queries.

## Expected results

The copy trained with attributions reaches at 50 queries about the agreement that the label-only copy reaches at 400. Keeping only the top three attributions, rounded, gives away nearly as much as the full vector. The chapter's figure uses a slightly different random sequence, so its values differ in the second or third decimal (for example 0.865 at 50 queries).

## What to hand in

The agreement table with your variants, the membership AUC, and a half-page note to a product owner: what the explanation interface should return to customers, partners and internal analysts, and what each choice costs in usefulness.

## Self-check

- Why does an interface that returns attributions reveal the score even when the score is hidden?
- Why does coarsening fail as a defense here, and what kind of defense would work better (access tiers, rate limits, differential privacy)?
- What would a stronger membership attack use that this one does not?
