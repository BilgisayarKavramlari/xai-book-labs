# Lab 12.4: Stickers on Rejected Parts (Case Study)

Chapter 12, Concepts Inside Networks, Run-only notebook, About 60 minutes, Last checked: 2026-11-24 (end-to-end run in about 5 minutes on a laptop CPU, after a one-time download of about 130 MB)

## Goal

Reproduce the chapter's data case: plant a shortcut (a sticker on rejected parts) in a defect classifier trained on real candle photographs, then compare what a behavioral test, an intervention and TCAV (sign and magnitude) reveal about a shortcut model and a clean model.

## Tools and versions

Python 3.10, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, torch 2.6.0, pillow 12.3.0, matplotlib 3.10.9. Notebook: `stickers_on_rejected_parts.ipynb`.

## Data and license

The Candle subset of the VisA (Visual Anomaly) dataset: 1,000 normal and 100 anomalous color photographs, each showing several candles, with pixel masks of the defects. The candles are real; the dataset's authors state that the defects were made by hand to look realistic. Paper: Zou, Jeong, Pemula, Zhang and Dabeer (2022), "SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation", ECCV 2022, https://doi.org/10.1007/978-3-031-20056-4_23 . Page and license: https://github.com/amazon-science/spot-diff ("The data is released under the CC BY 4.0 license"; full text in the repository's LICENSE-DATASET file). CC BY 4.0 allows commercial use and adapted material, with attribution: cite the paper if you publish results.

The full archive is a single uncompressed tar file of about 1.9 GB whose first folder is `candle/`. The notebook streams the archive, keeps that folder and stops, so it reads only about 130 MB (no account needed). The data goes into `data/VisA/candle/` beside the notebook, or into the folder named by the environment variable `XAI_DATA`. Do not commit the data; `data/` is ignored.

## Steps

1. Run the cells in order. The first cell downloads the Candle folder once.
2. **Checkpoint 1:** 19,678 tiles, 542 defective; train 10,861 (217), test 4,412 (134), concept pool 4,405 (191).
3. **Checkpoint 2 (behavior):** shortcut model AUC 0.784, sensitivity 0.18, specificity 0.999 on clean tiles and 0.000 with stickers; clean model AUC 0.822, sensitivity 0.57, specificity 0.865 and 0.601 with stickers. Logit change from a sticker: shortcut +10.0 (good) and +9.4 (defective); clean +0.9 and 0.0.
4. **Checkpoint 3 (TCAV):** sticker TCAV 1.00 (shortcut) and 0.75 (clean), both significant against random runs (0.49 and 0.51 mean). Sticker magnitude relative to the defect concept: 2.24 (shortcut) and 0.63 (clean). Dark speck: 0.70 and 0.61.

## Expected results

The numbers above come from torch 2.6.0 on CPU with the seeds in the notebook. Other versions or hardware can move them; the pattern (TCAV sign scores significant for both models, magnitudes and behavior separating them, and the clean model still losing some pass rate to stickers) is what matters.

## What to hand in

A one-page finding for a quality manager: what the shortcut does, how you found it, which test you would add to model acceptance, and what the TCAV sign score alone would have told you.

## Self-check

If your memo says "TCAV proved the clean model also relies on stickers", look at the intervention numbers again. A positive directional derivative says the output would rise if the activations moved toward the concept; it does not say how much, or that real stickers move the activations that way. If your memo says "the clean model ignores stickers", look at its specificity with stickers.
