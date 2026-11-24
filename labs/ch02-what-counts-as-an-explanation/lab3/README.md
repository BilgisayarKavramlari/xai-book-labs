# Lab 2.3: Three Explanations of One Risk Score

Chapter 2, What Counts as an Explanation? · Run-only notebook (no code to write) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run, about 45 seconds on a laptop CPU, with the versions below)

## Goal

Reproduce the chapter's case study. Train a welfare-style risk model on synthetic data, pick one flagged resident by a fixed rule, give her three explanations (a global importance list, a LIME-style local surrogate, exact Shapley values), and test each for faithfulness and stability. Then judge usefulness for three audiences.

## Tools and versions

Python 3.10 or later with:

| Package | Version used |
|---|---|
| numpy | 2.2.6 |
| scikit-learn | 1.7.2 |

These match `env/requirements.txt`. The notebook runs on a laptop CPU or in a hosted notebook service. No other packages are needed: the surrogate and the Shapley values are written out in a few lines so that you can see exactly what they compute.

## Data

A **synthetic** welfare-style dataset of 6,000 invented residents, generated inside the notebook with `numpy.random.default_rng(0)`. Nothing is downloaded. No real person, agency or model is represented. The generator is printed in the notebook; read it before you run it. Two biases are built in on purpose: a subjective caseworker concern flag that is partly bias against residents who have not met a language requirement, and historical labels that record irregularities only for investigated residents, with investigations aimed mostly at the same group. The "true" irregularity never depends on language.

License: the generator and notebook are covered by the repository's code license; the generated data have no restrictions.

## Steps

1. Open `three_explanations.ipynb` and run the cells in order.
2. **Checkpoint 1:** test AUC about 0.72; 180 of 1,800 test residents flagged; threshold about 0.13.
3. **Checkpoint 2:** the chosen resident (Mariam in the chapter) is 45, 11 months on benefit, 2 income changes, no shared address, language requirement met, caseworker concern 1; score about 0.19.
4. **Checkpoint 3:** global importance ranks caseworker concern, shared address, months on benefit first.
5. **Checkpoint 4:** Shapley values: caseworker concern about +0.105, months on benefit about +0.061, shared address about -0.023; they sum to the score minus the background mean (0.191 = 0.058 + 0.133).
6. **Checkpoint 5:** against the most similar unflagged resident, months on benefit is about +0.107 and caseworker concern is 0.
7. **Checkpoint 6 (faithfulness):** after removing two reasons, the mean flagged score is about 0.045 for the Shapley and surrogate rankings and about 0.17 for the global list. The global list's top factor raises the score of only 69 of 180 flagged residents.
8. **Checkpoint 7 (stability):** caseworker concern and months on benefit are in the surrogate's top three in all 30 reruns; shared address in 43 percent. Mean top-3 agreement: surrogate 0.71 (150 samples), 0.80 (1,000 samples); Shapley with a new background 0.77.
9. Answer the three usefulness questions in Section 10 of the notebook.
10. Optional: try the changes in Section 11.

## Expected results

The numbers above. Small differences can appear with other library versions; the pattern should hold: per-person rankings are far more faithful for individuals than the global list; the surrogate's third reason is unstable; exact Shapley values still depend on the background (the foil).

Note the built-in caution: the deletion test replaces features with background values, which is the same operation the Shapley values use, so the test favors them. Chapter 20 introduces tests that do not.

## What to hand in

- The faithfulness table (mean score after 0, 1, 2 and 3 removals for each explanation) and the stability numbers.
- A half-page judgment: which explanation would you give Mariam, her caseworker and an auditor, and why? Name the foil in each case.

## Self-check

- Can you explain why the global list is perfectly stable and still unfaithful for Mariam?
- Did you notice that the model uses `language_req_met` even though the generator never makes irregularity depend on it? Which explanation revealed that, and which step of the Explanation Loop should act on it?
- If your usefulness answers do not mention what each person can *do* with the explanation, revise them.
