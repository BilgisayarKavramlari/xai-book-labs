# Lab 12.2: Dissect a Small Network, then Test a Concept

Chapter 12, Concepts Inside Networks · Run-only notebook · About 45 minutes · Last checked: 2026-11-24 (end-to-end run in about 20 seconds on a laptop CPU)

## Goal

Label the units of a small convolutional network with concepts (network dissection, Bau et al., 2017), see how much better a direction made of many units segments each concept (Net2Vec, Fong and Vedaldi, 2018), and run TCAV (Kim et al., 2018) with the random-concept test.

## Tools and versions

Python 3.10, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, torch 2.6.0, matplotlib 3.10.9. Notebook: `dissect_and_test.ipynb`. It also runs in a hosted notebook service with a CPU runtime.

## Data

Synthetic images generated in the notebook (gray noise with patches of stripes, dots and checkerboard), with exact concept masks. Nothing is downloaded.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** test accuracy per label about 0.99.
3. **Checkpoint 2:** 14 of 16 units pass the IoU threshold of 0.04, but the best IoU is only about 0.33, and many units have a second-best IoU above 0.15.
4. **Checkpoint 3:** best single unit IoU about 0.28 to 0.33 per concept; linear combination about 0.78 to 0.82.
5. **Checkpoint 4:** TCAV for stripes 1.00; for dots about 0.13 (significantly below 0.5); random versus random 0.52 with a standard deviation of about 0.13.

## Expected results

The numbers above come from torch 2.6.0 on CPU with the seeds in the notebook. Another version or a GPU can move them by a few hundredths; the pattern (weak single units, strong directions, a wide random spread) should hold.

## Questions

In the notebook: three questions on unit labels, directions and concept-set design.

## What to hand in

The dissection table, the single-unit versus combination numbers and the TCAV results, each with one sentence of interpretation, and your answers to the three questions.

## Self-check

If you wrote that the dots concept is "unimportant" because its TCAV score is low, look again: a score far below 0.5 that passes the test means moving toward dots lowers the stripes logit, which is a finding too.
