# Lab 12.3: Concept Bottlenecks, Interventions and Leakage

Chapter 12, Concepts Inside Networks · Run-only notebook, one optional edit · About 40 minutes · Last checked: 2026-11-24 (end-to-end run in about 15 seconds on a laptop CPU)

## Goal

Build independent, sequential and joint concept bottleneck models (Koh et al., 2020) and a standard network, test whether correcting concepts at test time helps, and measure leakage: information in the concept scores beyond the concepts (Mahinpei et al., 2021).

## Tools and versions

Python 3.10, numpy 2.2.6, scikit-learn 1.7.2, torch 2.6.0. Notebook: `bottlenecks_and_leakage.ipynb`.

## Data

Synthetic inspection records generated in the notebook: 30 measurements per part from four binary concepts (scratch, dent, discoloration, misalignment) and one unlabeled factor. 6,000 training and 3,000 test parts. Nothing is downloaded.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** standard network 0.836; independent bottleneck 0.791 rising to 0.889 when all four concepts are corrected; joint model 0.832 falling to 0.626; joint concept accuracy 0.690 against 0.928 for the independent concept model.
3. **Checkpoint 2:** R squared for the unlabeled factor: 0.00 from true concepts, 0.08 from independent scores, 0.62 from joint scores.
4. Optional: set the joint concept weight to 1.0 and rerun.

## Expected results

As above (torch 2.6.0, CPU). The ordering should survive small version changes.

## What to hand in

The intervention table and the leakage numbers with a three-sentence interpretation, the result of the optional edit, and your answers to the three questions in the notebook.

## Self-check

If you concluded that the joint model is "better" because it starts with higher accuracy, reread the leakage section: its advantage comes from a code no inspector can read or correct.
