# Lab 26.2: A Readable Middle

Chapter 26, Casebook: Explainability Across Industries · Code notebook (run, read and answer; no code needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in a few seconds)

## Goal

Build a two-stage pipeline on synthetic scans (a segmentation stage that produces a tissue map, and a referral stage that reads only tissue volumes), break it with a device shift, find the failure in the intermediate tissue map and repair it by refitting the first stage only. The design follows the idea of De Fauw et al. (2018), the chapter's healthcare case; the data and models are toys.

## Tools and versions

`readable_middle.ipynb`, Python 3.10, the main environment in `env/requirements.txt`: numpy 2.2.6, scikit-learn 1.7.2, matplotlib 3.10.9. Jupyter kernel used for the check run: `xai-lab-venv`.

## Data

Synthetic 32 x 32 "scans" generated in the notebook: three tissue classes (retina, fluid, bright deposits) with known labels. Device 2 is the same tissue seen brighter, with lower contrast and different noise. No real images are used.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** the referral stage prints as a two-level tree: refer if fluid volume is above about 0.08, otherwise refer if deposit volume is above about 0.03.
3. **Checkpoint 2:** on device 1, referral error about 1 percent and pixel accuracy of the tissue map above 99 percent. On device 2 with the same first stage, referral error about 50 percent and pixel accuracy near 1 percent. The example scan's tissue map labels the whole scan as deposit.
4. **Checkpoint 3:** after refitting the first stage on 20 device-1 scans plus 10 device-2 scans, with the referral stage untouched, device 2 referral error about 3 percent (pixel accuracy above 99 percent) and device 1 still about 3 percent.
5. Read the last markdown cell and write your paragraph.

## Expected results

| Condition | Referral error | Pixel accuracy |
|---|---|---|
| Device 1, stage 1 fit on device 1 | 1.0% | 99.8% |
| Device 2, same stage 1 | 50.0% | 1.3% |
| Device 2, stage 1 refit, stage 2 unchanged | 3.0% | 99.3% |

The numbers are reproducible with the pinned versions and the fixed seed.

## What to hand in

The results table and one paragraph: what can the tissue map tell a clinician about a referral, and what can it not tell them? Name the method from Part III of the book you would use for the second question.

## Self-check

- Why could the repair leave the referral stage unchanged?
- Would an end-to-end model have shown you where it failed on device 2? What would you have looked at instead?
- In the real system the second stage is a deep network. What does a correct tissue map not guarantee about it?
