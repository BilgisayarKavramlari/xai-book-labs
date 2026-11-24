# Lab 11.3: A Shortcut Hunt in Two Hospitals

Chapter 11, Where the Network Looks · Run-only notebook (one optional edit) · About 75 minutes · Last checked: 2026-11-24 (end-to-end run in about 60 seconds on a laptop CPU)

## Goal

Reproduce, in a laboratory, the pattern of the chapter's case study: a network trained on confounded "two hospital" data looks excellent inside its hospitals, loses half its performance elsewhere, and leans on a source token. Find the shortcut with Expected Gradients, confirm it with interventions, see how the baseline changes Integrated Gradients, and run a cascading randomization sanity check.

## Tools and versions

`shortcut_hunt_two_hospitals.ipynb`; Python 3.10, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, matplotlib 3.10.9, torch 2.6.0 (CPU).

## Data

Synthetic, chest-radiograph-like 32 by 32 images generated in the notebook. In the confounded training set the corner token appears on 90 percent of positive and 10 percent of negative images; in the clean training set and in the external test set it is independent of the label. Same data and seeds as the chapter's figures. Not medical data; the "hospitals" are invented.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1 (Part A):** confounded network AUROC 0.978 internal and 0.730 external; clean network 0.960 and 0.969.
3. **Checkpoint 2 (Part B):** over 30 positive images with the token, Expected Gradients puts 0.319 of the confounded network's attribution on the token (which covers 1.4 percent of the image) and 0.177 on the opacity; the clean network puts 0.012 and 0.309.
4. **Checkpoint 3 (Part C):** adding the token to 246 healthy images moves the confounded network's mean probability from 0.028 to 0.756 (clean network 0.325 to 0.303); removing it from 250 positive images moves it from 0.919 to 0.124 (clean network 0.854 to 0.864).
5. **Checkpoint 4 (Part D):** the model's probability for each baseline and the opacity share of the Integrated Gradients map: black 0.984 and 0.144; blurred 1.000 and 0.016; noise 1.000 and 0.039; average healthy image 0.137 and 0.408.
6. **Checkpoint 5 (Part E):** rank correlations with the trained network's maps as layers are randomized from the top (trained, +output, +conv3, +conv2, +conv1): Gradient 1, 0.62, 0.41, 0.18, -0.03; Gradient x input 1, 0.70, 0.65, 0.49, 0.45; Integrated Gradients 1, 0.74, 0.61, 0.49, 0.39; Grad-CAM 1, 0.26, -0.01, 0.35, -0.15; Guided backprop 1, 0.76, 0.66, 0.33, 0.06.
7. Optional: in the first code cell, change the confounding to 0.7 and 0.3, rerun all cells, and record how Checkpoints 1 to 3 change.

## Expected results

The numbers above, exactly, with the pinned versions. The pattern should hold on any machine: accuracy hides the shortcut, attribution points to it, interventions confirm it, the baseline changes the answer, and methods that multiply by the input keep part of the image even in a destroyed network.

## Questions

The notebook ends with five questions. Answer them in your report.

## What to hand in

A one-page shortcut report in the format of the chapter's case study: background, what accuracy showed, what the attributions showed, what the interventions showed, and a recommendation (deploy, fix the data, or reject), each with the numbers from your run.

## Self-check

If your report says the network "looks at the token" without the intervention numbers from Part C, add them. If it trusts a map without the sanity check from Part E, say which methods passed.
