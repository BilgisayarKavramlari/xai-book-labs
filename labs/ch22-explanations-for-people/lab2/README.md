# Lab 22.2: Did the Explanation Help? Analyzing a Reliance Study

Chapter 22, Explanations for People · Notebook with a run-only path · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in under 5 seconds on a laptop CPU)

## Goal

Analyze a simulated user study with three conditions (AI only, AI with an attribution chart, AI with an explanation that lets users verify the answer). Compute accuracy, overreliance and underreliance per participant with bootstrap intervals, and compare them with satisfaction ratings. Decide which explanation you would ship.

## Tools and versions

Python 3.10 with numpy 2.2.6 and pandas 2.3.3 (`env/requirements.txt`; Jupyter kernel `xai-lab-venv`). Notebook: `did_the_explanation_help.ipynb`.

## Data

Synthetic, generated in the notebook with seed 22: 180 participants (60 per condition), 24 two-option cases each, an AI that is right on 75 percent of cases, a participant who is right alone on 68 percent, and a satisfaction rating from 1 to 7. The simulation builds in two mechanisms reported in the literature cited in the chapter: an attribution chart that raises the tendency to follow the AI regardless of correctness, and a verifiable explanation that lets participants detect wrong AI answers more often than right ones.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** mean overreliance A 0.667, B 0.784, C 0.309; mean accuracy A 0.722, B 0.736, C 0.820; mean satisfaction A 4.10, B 5.63, C 4.48.
3. **Checkpoint 2:** bootstrap differences (participants resampled): overreliance B minus A +0.117, interval about [+0.04, +0.19]; C minus B -0.476; accuracy C minus A +0.098, interval about [+0.07, +0.13].
4. Read Step 4: across all participants, satisfaction correlates positively with overreliance (about +0.24).
5. Coding path: do Exercises 1 and 2 (a solution to Exercise 1 is printed at the end: calibration A 0.171, B 0.117, C 0.546).

## Expected results

The checkpoints exactly (deterministic). Condition B wins on satisfaction and loses on overreliance; condition C wins on accuracy and calibration.

## Questions

1. Why must the bootstrap resample participants rather than individual decisions?
2. A product manager sees only satisfaction and agreement. Which condition would they ship, and what would go wrong?
3. What would a real study need that this simulation lacks (think about the audience, the cases where the AI is wrong and preregistration)?

## What to hand in

A one-page results summary: the three measures with intervals per condition, satisfaction, your recommendation and one sentence answering Question 3.

## Self-check

If your recommendation rests on overall agreement, reread the chapter's Key Idea on appropriate reliance: agreement that rises on wrong cases as much as on right ones is compliance, not understanding.
