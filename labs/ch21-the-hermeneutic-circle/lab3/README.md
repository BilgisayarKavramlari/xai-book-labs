# Lab 21.3: A Mini Hermeneutic Circle Test

Chapter 21, The Hermeneutic Circle · Notebook (run, then edit the "Your turn" cells) · About 60 minutes, of which about 5 to 8 minutes of computation · Last checked: 2026-11-24 (end-to-end run in 289 seconds on a laptop CPU with the versions below)

*Disclosure: the author of the book designed the Hermeneutic Circle Test and maintains HermAI.*

## Goal

Compute the Hermeneutic Circle Test profile for four explainers (KernelSHAP, LIME, HermAI 0.1.8 with each of its two perturbation generators) and two controls (random attributions, sign-flipped KernelSHAP) on 100 test applicants of a German Credit random forest, and reproduce the data case study of Chapter 21.

## What `hct_mini.py` is, and is not

A short teaching re-implementation of the components defined in Seker (2026), "Measuring the hermeneutic circle in explainable AI", *Machine Learning and Knowledge Extraction* 8(11), 381, https://doi.org/10.3390/make8110381, Sections 3.1-3.6: Horizon Plausibility (split-conformal 10-nearest-neighbor novelty test, alpha 0.05, plus integer and range conditions), Claim Verification Rate (on-horizon replacement with the 30 nearest comparable training records, pass if the sign matches and the effect is at least max(0.01, 1.96 SE)), Part-Whole Agreement and the Hermeneutic Horizon Radius (depth-4 global tree, depth-3 regional trees at 1/2, 1/4 and 1/8 of the data, exact TreeSHAP, top-3 sign agreement gated by decision agreement, threshold 2/3), and Hermeneutic Gain (logistic, 3-NN and depth-3 tree readers; budgets 10, 20, 40, 80; ten training sets per budget; five random draws for the baseline).

It is **not** the reference implementation, which is released with the paper as supplementary code. Deliberate simplifications: one dataset and one model; no meaning units (the largest absolute correlation between two German Credit features is 0.59, below the paper's 0.9 grouping threshold, so every unit is a single feature); no HermAI-H explainer (it is not part of the released hermai package); the sign-flip control flips KernelSHAP instead of HermAI-H; HermAI's claims are the three sentences its narrative states (top three coefficients, slope signs), while its attribution vector (slope times deviation from the training mean) is used for PWA and HG, as in the paper.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, **shap 0.49.1**, **lime 0.2.0.1**, **hermai 0.1.8** (with seaborn 0.13.2). See `env/requirements.txt`; install hermai with `pip install hermai==0.1.8` and run `pip check`.

## Data

German Credit (Statlog), from OpenML (`credit-g`); see `data/german-credit.md` (CC BY 4.0 as listed by UCI). Split: 700 train (of which 525 reference and 175 calibration for the horizon), 300 test, stratified, `random_state=0`. Positive class: bad credit risk; refusal at a predicted probability of 0.5 or more.

## Steps

1. Run the notebook `mini_hct_german_credit.ipynb` from this folder.
2. **Checkpoint 1:** 700 / 525 / 175 / 300 rows; test AUC 0.787; 45 test applicants refused; largest correlation 0.59.
3. **Checkpoint 2:** 100 explained applicants, 45 of them refused.
4. **Checkpoint 3:** HP 0.955 (KernelSHAP), 0.001 (LIME), 0.000 (both HermAI generators); real test records 0.92. CVR 0.927, 0.773, 0.287, 0.297; random 0.227; sign-flip 0.003. `CVR_vector` for HermAI 0.790 and 0.823. PWA 0.457, 0.463, 0.410, 0.450; random 0.040; sign-flip 0.003. HG 0.123 for KernelSHAP and sign-flip alike. PGI 0.187 for KernelSHAP and sign-flip alike.
5. **Checkpoint 4:** HermAI slope reading 0.603 and 0.670; inversion 0.667 and 0.690; counterfactuals always found, change 11.56 and 11.47 features on average, never inside the horizon.
6. **Checkpoint 5:** featured applicant (test row 77): risk 0.668; KernelSHAP claims verified with effects +0.130, +0.073, +0.064; PWA by scale 0.33, 0.33, 1.0, 0.67; radius 0.25; all three HermAI sentences fail.
7. **Checkpoint 6:** credit history "no credits/all paid": bad rate 0.625 among 24 training applicants; loans up to 1,000 DM: 0.387.
8. **Your turn:** the three tasks at the end of the notebook.

## Expected results

All random draws are seeded (KernelSHAP and HermAI through NumPy's global state before each call, LIME through `random_state`, readers and controls through `default_rng`). The random forest predicts with parallel threads, so a few regional-whole results can differ in the third decimal between runs (for example PWA at the quarter scale, 0.363 or 0.367 for KernelSHAP); the chapter's figures came from one run and this notebook from another. The pattern should hold with other versions: possible evidence only for KernelSHAP, sentences that contradict their own vectors for HermAI 0.1.8, controls that fail exactly the components designed to catch them.

## Questions

1. Why is HP zero for LIME on German Credit but not on a dataset with continuous measurements? Is a fractional loan duration an impossible case or a harmless one?
2. HermAI's attribution vectors pass 0.79 of the claims but its sentences only 0.29. What does that tell you about evaluating vectors instead of what readers receive?
3. Pick one applicant with a radius of 0 for KernelSHAP: are its claims verified? Is it a poor explanation or local structure?
4. HG is low for every explainer here. Does that make the explanations useless? What else could explain it?

## What to hand in

The profile table, two sentences on why HP is zero for three explainers on these data, and your reading of one applicant with a radius of 0. These go into Dossier artifact 21.

## Self-check

If you report HP without saying whether the measurement-scale condition was used, compare `HP` with `HPdist`. If you rank explainers by the `HCT` index alone, reread the chapter: the index hides which interpreter rejected the explanation.
