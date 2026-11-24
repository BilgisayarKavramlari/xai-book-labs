# Lab 15.4: Asking the Right Question

Chapter 15, Reading Representations: Probing and the Logit Lens · Code notebook (run, read and answer; no code needs to be written) · About 30 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 10 seconds)

## Goal

Reproduce two lessons of the chapter on synthetic data: the labeling of a probe decides whether a representation looks linear (the mine-or-theirs result of Nanda et al., 2023), and a property can be decodable without being used (amnesic probing, Elazar et al., 2021).

## Tools and versions

`asking_the_right_question.ipynb`, Python 3.10, the main environment in `env/requirements.txt`: numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2. Jupyter kernel: `xai-lab-venv`. No language model, no download.

## Data

Generated in the notebook with fixed seeds: (1) 6,000 synthetic "boards" of 16 squares stored in a 64-dimensional vector relative to the player to move; (2) 8,000 inputs of 20 Gaussian features for a small network trained to decide whether the sum of the first two is positive.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** mean accuracy over eight squares: linear probe with black/white labels 0.656, nonlinear (MLP) probe 0.984, linear probe with mine/theirs labels 0.995.
3. **Checkpoint 2:** the network's task accuracy is 0.99. Probe accuracy is 0.843 for the ignored property and 0.991 for the needed one. After removal, task accuracy is 0.990 (ignored property removed) and 0.488 (needed property removed).

## Expected results

The numbers above with the pinned versions and seeds (the chapter's figures use a separate seed and show 0.83 and 0.52; the pattern is the same).

## Questions

1. Why can no linear probe read "black" in this representation? Write the rule for "black" in terms of "mine" and "whose turn".
2. The nonlinear probe reaches 0.98 for black and white. Is that evidence that the representation stores color? What else could explain it?
3. After removing the ignored property, a fresh probe falls to about 0.54. Why not exactly 0.5?
4. Translate the second experiment to a language model: which property would you remove from a support assistant's activations, and which behavior would you measure?

## What to hand in

The two result tables and a paragraph on what each probe, without the second experiment, would have led you to conclude.

## Self-check

If removing the needed property leaves task accuracy near 0.99, the removal did not run on the hidden layer that feeds the output: check that `task()` receives the projected activations.
