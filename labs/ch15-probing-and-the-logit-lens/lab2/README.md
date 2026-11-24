# Lab 15.2: Watching a Model Change Its Mind

Chapter 15, Reading Representations: Probing and the Logit Lens · Code notebook (run, read and answer; no code needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 2.5 minutes)

## Goal

Apply the logit lens to GPT-2 small, find the layer where an answer forms, and compare the logit lens with a fitted affine lens (a simplified relative of the tuned lens of Belrose et al., 2023) on held-out text.

## Tools and versions

`logit_and_affine_lens.ipynb`, Python 3.10, the language-model environment in `env/requirements-llm.txt`: torch 2.6.0 (CPU), transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4, pandas 2.0.3, matplotlib 3.10.9. Jupyter kernel used for the check run: `xai-llm-venv`.

## Data

GPT-2 small (124M parameters) from the Hugging Face Hub, downloaded on first use. Four prompts written for the lab. For the lens comparison, 192 sequences of 64 tokens sampled from GPT-2 itself with a fixed seed (GPT-2 has no public validation set); 144 sequences fit the translators and 48 are used for evaluation.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** for "To reset your password, click the link we sent to your", the top guess is `' own'` (probability about 1.00) from layer 1 to 6; `' email'` leads from layer 7 (0.58), peaks at layer 10 (0.86) and ends at 0.68.
3. **Checkpoint 2:** the Eiffel Tower prompt ends on `' London'`, with `' Paris'` second; `' Tokyo'` has 0.86 at layer 10 and 0.10 at the output.
4. **Checkpoint 3:** in the comparison table, the affine lens has lower KL than the logit lens at every layer from 0 to 11 (for example 2.58 against 6.24 bits at layer 6) and higher top-token agreement (0.315 against 0.171 at layer 6). The table is saved as `lens_results.csv`.

## Expected results

The numbers above with the pinned versions and seeds. Other versions of torch may change the sampled text slightly; the pattern (the fitted lens much closer in early and middle layers, both equal at layer 12) should hold.

## Questions

1. At which layer does the answer to each prompt first reach rank 0? Is the layer the same for factual prompts and for the password prompt?
2. Why does the logit lens fail so badly at layer 0? Use the term representation drift.
3. The fitted lens here is trained by least squares to predict the final residual stream; the tuned lens is trained to match the output distribution. Give one reason the second objective might be better.
4. Write two prompts from your own sector (for example an insurance claim or a flight change) and describe, without running anything, what you expect the lens to show. If you can run code, try them with `lens_table` in a copy of the notebook.

## What to hand in

Lens tables for two prompts of your choice, the comparison table, and a paragraph on one layer where the two lenses disagree about the top token and which one you would trust.

## Self-check

If KL is not exactly 0 at layer 12 for both lenses, the final-layer read is wrong: check that the last row uses `blocks.11.hook_resid_post`.
