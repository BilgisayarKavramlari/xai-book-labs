# Lab 20.2: An Evaluation Suite for Five Explainers

Chapter 20, Is the Explanation Any Good? · Run-only notebook (one optional edit) · About 75 minutes · Last checked: 2026-11-24 (end-to-end run in about 50 seconds on a laptop CPU)

## Goal

Reproduce the chapter's running example, from deletion curves to the scorecard, and change one setting to see which conclusions move.

## Tools and versions

`evaluation_suite.ipynb`; Python 3.10, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, matplotlib 3.10.9 (`env/requirements.txt`, kernel `xai-lab-venv`). Every method and test is written out in numpy; nothing else is needed.

## Data

Synthetic, standardized credit-style data generated in the notebook (4,000 rows, ten features, seed 0; no download). Income, debt ratio and missed payments always affect the true risk; utilization matters only when missed payments are above average; loan amount is correlated with debt ratio (about 0.8) but has no effect; the other five features are noise. Because the true structure is known, a planted-truth test is possible. The data is invented and is not a real lender's data.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1 (Part A):** test AUC 0.877.
3. **Checkpoint 2:** for applicant 1 (predicted risk 0.234) the gradient's top three are missed_payments (+1.07), income (-0.62), inquiries (+0.58); gradient times input's are missed_payments (-1.75), region_code (-0.84), income (+0.69).
4. **Checkpoint 3 (Part B):** deletion areas SHAP 0.344, occlusion 0.395, gradient times input 0.425, LIME-style 0.699, gradient 0.708, random order 0.705; insertion areas 0.931, 0.926, 0.900, 0.724, 0.699, 0.703.
5. **Checkpoint 4 (Part C):** with nearest-neighbor fill, SHAP 0.442 and random order 0.685; with random-draw fill, 0.431 and 0.677.
6. **Checkpoint 5 (Part D):** planted-truth precision LIME-style 0.924, SHAP 0.757, gradient 0.576, occlusion 0.531, gradient times input 0.501, random 0.338; rank correlation with the shuffled-label model (test AUC 0.509): gradient times input 0.431, occlusion 0.369, SHAP 0.096, gradient -0.043, LIME-style -0.067.
7. **Checkpoint 6 (Part E):** top-3 Jaccard under small input changes LIME-style 0.957, SHAP 0.857, occlusion 0.767, gradient 0.709, gradient times input 0.660; under reruns LIME-style 0.933, SHAP 0.792, deterministic methods 1.0.
8. **Checkpoint 7 (Part F):** mean feature agreement 0.573, mean signed rank agreement 0.181; the scorecard has no method that wins every column.
9. Optional (Part G): set `SEED = 1` and rerun. With the pinned versions the test AUC becomes 0.882, SHAP's deletion area 0.368, LIME-style's planted precision 0.931, and the mean signed rank agreement 0.196. The broad pattern holds; one detail moves (gradient times input becomes slightly more stable than the gradient under input changes, 0.71 against 0.695).

## Expected results

The numbers above, exactly, with the pinned versions (all randomness is seeded; another scikit-learn version may change the network and the last digits). The lessons: each test asks a different question (contributions versus slopes); the replacement value changes the size of a result; planted truth checks the data's answer, not the model's; methods that multiply by the input partly survive randomization; stability can be had without faithfulness; and methods agree on features far more often than on order and sign.

## Questions

The notebook ends with five questions. Answer them in your hand-in.

## What to hand in

The scorecard, the setting you changed (seed, background size, noise level, number of LIME samples or replacement value) and a paragraph on which verdicts survived it. This can be the core of the Chapter 20 portfolio artifact.

## Self-check

If your paragraph says one method is "the most faithful" without naming the test and its replacement value, rewrite it: the chapter's point is that a method is good for a question, under a test.
