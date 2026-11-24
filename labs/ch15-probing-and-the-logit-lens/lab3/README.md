# Lab 15.3: A Truth Probe with Controls

Chapter 15, Reading Representations: Probing and the Logit Lens · Code notebook (run, read and answer; no code needs to be written) · About 60 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 2 minutes)

## Goal

Reproduce the chapter's case study: probe GPT-2 small for the truth of statements about cities, add baselines and a control task, and test the probe on negations and paraphrases, in the spirit of Marks and Tegmark (2024).

## Tools and versions

`truth_probe_with_controls.ipynb`, Python 3.10, the language-model environment in `env/requirements-llm.txt`: torch 2.6.0 (CPU), transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4, pandas 2.0.3, scikit-learn 1.7.2, matplotlib 3.10.9. Jupyter kernel: `xai-llm-venv`.

## Data

72 well-known cities and their countries, written in the notebook; for each city one wrong country drawn at random with a fixed seed. 288 statements: plain true, plain false, negated false (right country after "not") and negated true. A paraphrase template, "X is a city located in Y.", for the plain statements. GPT-2 small from the Hugging Face Hub.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** GPT-2 prefers the right country for 99 percent of cities (71 of 72); after "is not in" the right country still has the higher mean log probability (-5.22 against -10.26).
3. **Checkpoint 2:** in the results table (saved as `truth_results.csv`), the logistic probe scores 0.904 at layer 5 and 0.910 at layer 8; the mass-mean probe 0.932 at layers 8 and 9; the random GPT-2 stays between 0.47 and 0.54; the plain probe on negated statements scores 0.340 at layer 8; on the paraphrase, accuracy is 0.500 from layer 7 while AUROC is 0.823 at layer 8; trained on plain and negated, 0.904 at layer 8.
4. **Checkpoint 3:** correlation of the layer-8 probe score with the model's log probability of the country: 0.73 (plain) and 0.82 (negated).
5. **Checkpoint 4:** the control task reaches 0.82 to 0.94 in layers 1 to 9.

## Expected results

The numbers above with the pinned versions and seeds.

## Questions

1. Why are cities held out by group (GroupKFold) rather than statements at random? What would go wrong otherwise?
2. The probe scores far below chance on negated statements. What does it read instead of truth? Use the scatter plot.
3. On the paraphrase, why can AUROC stay near 0.8 while accuracy falls to exactly 0.5? What would you change in a production monitor because of this?
4. The control task reaches about 0.9. Does that undermine the truth result? Explain with the split.
5. Which intervention (Chapter 16) would tell you whether GPT-2 small uses the direction found by the probe trained on plain and negated statements?

## What to hand in

The results table, the scatter plot and a one-page note to a product owner on whether a probe like this could flag false answers from a support assistant, with the three tests you would require of a vendor.

## Self-check

If the random-network column is far above 0.5, the random model was not initialized (check that `init_weights()` ran); if layer 0 is far above 0.5, the activations were not read at the last token.
