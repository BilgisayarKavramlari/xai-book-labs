# Lab 4.3: Gradients and Embeddings from Scratch

Chapter 4, Inside Deep Networks and Transformers · Run-only notebook (optional extension changes one dictionary) · About 75 minutes · Last checked: 2026-11-24 (executed end to end with the versions below)

## Goal

Compute input gradients for a small network and see three ways they misstate an input's role (cancelling paths, a switched-off unit, saturation). Then learn word embeddings from a synthetic corpus whose gender statistics you control, and measure how faithfully a direction in the embedding reflects those statistics.

## Tools and versions

`gradients_and_embeddings.ipynb`, Python 3.10, numpy 2.2.6, matplotlib 3.10.9 (see `env/requirements.txt`). No other library is needed. Runs in under a minute on a laptop.

## Data

All synthetic and generated in the notebook: a two-input toy network with hand-set weights, a one-input S-shaped score, and a template corpus of 18,000 short sentences in which twelve occupations appear with *she* or *he* words at shares you can read and change. Nothing is downloaded. The shares are invented for teaching and are not labor statistics.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1 (Part A1):** the gradient for years is 0.0 both by backpropagation and by finite differences, although raising years changes both hidden units.
3. **Checkpoint 2 (Part A2):** with skill match 0.1, hidden unit 1 outputs 0 and passes no gradient.
4. **Checkpoint 3 (Part A3):** slopes of 0.375 at 3 years and about 0.0008 at 8 years; actual change from 0 to 8 years 0.988 against a gradient-times-change of about 0.007; the average gradient along the path recovers about 0.984.
5. **Checkpoint 4 (Part B1):** correlation between corpus share and projection on the *she* minus *he* direction of about 0.94; *nurse* has the largest positive projection.
6. **Checkpoint 5 (Part B2):** every gendered pair gives a correlation between 0.94 and 0.96 in this corpus.
7. **Checkpoint 6 (Part B3):** after compressing the shares toward 50 percent, the largest projection barely shrinks (about 0.63 against 0.69) and the correlation stays about 0.91.

## Expected results

The numbers in the checkpoints above, exactly, with the pinned versions (all randomness is seeded). The main lessons: a gradient is local sensitivity, not contribution; an embedding's geometry mirrors the statistics of its corpus; and the size of a projection is not the size of the association in the data.

## Questions

A. For each of the three gradient cases, write one sentence a developer could put in a model report to warn readers about what the gradient does not show.

B. In a real embedding you do not know the corpus statistics. Which two checks from this lab would you run on a vendor's embedding, and what would each result tell you?

## Optional extension

Change two values in `OCC` (for example, make *pilot* 0.6 and *nurse* 0.4), rerun Part B and report the new correlation and the new positions of the two words.

## What to hand in

Your numbers for Checkpoints 1, 3, 4 and 6, answers to Questions A and B, and one paragraph on what this lab implies for auditing real embeddings.

## Self-check

If you concluded from Part B3 that a weakly skewed corpus produces a weak direction, look at the numbers again.
