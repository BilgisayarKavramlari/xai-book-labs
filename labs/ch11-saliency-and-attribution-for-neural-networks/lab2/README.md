# Lab 11.2: Six Maps, One Image

Chapter 11, Where the Network Looks · Run-only notebook (one optional edit) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 30 seconds on a laptop CPU)

## Goal

Compute six attribution maps (gradient, gradient times input, SmoothGrad, Integrated Gradients, Grad-CAM, occlusion) for one small convolutional network, check the completeness of Integrated Gradients, and measure how often each map lands on the true finding.

## Tools and versions

`six_maps_one_image.ipynb`; Python 3.10, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, matplotlib 3.10.9, torch 2.6.0 (CPU). Every method is written out in about five lines of PyTorch.

## Data

Synthetic, chest-radiograph-like 32 by 32 images generated in the notebook (no download). Positives carry a faint round opacity whose mask is known, so every map can be scored. In this lab the corner token is independent of the label. The data and seeds are those of the chapter's figures. Not medical data.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1 (Part A):** test AUROC 0.969.
3. **Checkpoint 2 (Part C):** the logit changes by 11.449 from the average healthy baseline to the input; Integrated Gradients with 2 steps misses by 0.898, with 32 steps by 0.013, with 128 steps by 0.004; gradient times (input minus baseline) sums to 13.082.
4. **Checkpoint 3 (Part D), over 60 positive images without the token:** share of attribution on the opacity and how often the hottest pixel lies within two pixels of it: Gradient 0.105 and 0.63; Gradient x input 0.152 and 0.72; SmoothGrad 0.063 and 0.22; Integrated Gradients 0.314 and 0.98; Grad-CAM 0.070 and 0.23; Occlusion 0.146 and 0.73.
5. Optional: set `SEED = 1` in Part A and rerun everything. With the versions above, Grad-CAM's peak lands on the opacity in 53 percent of images and SmoothGrad's in 93 percent: the ranking of methods changes with nothing but a new training run.

## Expected results

The numbers above, exactly, with the pinned versions (all randomness is seeded; PyTorch on another CPU or version may differ in the last digit). The lessons: Integrated Gradients needs enough steps and a stated baseline; methods answer different questions; and a localization ranking is a property of one trained model, not of a method.

## Questions

The notebook ends with five questions. Answer them in your hand-in.

## What to hand in

A half-page table of the six methods with their two scores from Checkpoint 3, one sentence per method on the question it answers, and your answers to the questions.

## Self-check

If your table ranks the methods without saying which model and which training run produced the numbers, add both. Chapter 20 shows how faithfulness, not localization, is measured.
