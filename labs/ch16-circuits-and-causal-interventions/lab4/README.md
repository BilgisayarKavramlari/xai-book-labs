# Lab 16.4: Attribution Patching versus Real Patching

Chapter 16, Circuits and Causal Interventions · Run-only notebook · About 40 minutes · Last checked: 2026-11-24 (end-to-end run in about 1 minute on a laptop CPU, after the one-time model download)

## Goal

Estimate the patching effect of every attention head of GPT-2 small from one backward pass (attribution patching; Nanda, 2023; Syed et al., 2023), compare the estimates with exact activation patching, and find where the approximation fails.

## Tools and versions

`env/requirements-llm.txt`: Python 3.10, torch 2.6.0, transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4, matplotlib 3.10.9. Notebook: `attribution_patching.ipynb`.

## Data and model

GPT-2 small (124 million parameters; the Hugging Face model card, openai-community/gpt2, lists the MIT license). The same 48 generated IOI prompts as Lab 16.2.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** exact head patching takes 144 runs; attribution patching one backward pass. Correlation over the 144 heads about 0.98. Largest gaps: 9.9 (exact about 0.27, estimate about 0.40), 8.6 (0.34 versus 0.42), 5.5 (0.35 versus 0.29), 3.0 (0.15 versus 0.12); 10.7 is close (-0.50 versus -0.47).
3. **Checkpoint 2:** for whole residual stream vectors, the estimate is close at the final position in late layers (for example layer 9: 0.98 exact, 0.89 estimated) but far off at S2 in early layers (layer 0: 1.00 exact, 0.03 estimated; layer 4: 1.00 exact, 0.30 estimated).

## Expected results

Values can move in the second decimal with other versions or a GPU. The pattern should hold: good agreement for head-sized patches, poor agreement for large patches in early layers, where Nanda (2023) and Kramar et al. (2024) expect the first-order approximation to fail.

## What to hand in

The scatter plot, the table of the five largest disagreements, the residual stream table, and a one-paragraph usage rule for a team (when the fast estimate may be used alone and when exact patching must confirm it), plus answers to the notebook's three questions.

## Self-check

A high correlation over all heads does not license trusting the estimate for one head: 9.9's estimate is about 50 percent too high. If your usage rule does not require confirming the top candidates with exact patching, revise it.
