# Lab 16.2: Activation Patching on GPT-2 Small

Chapter 16, Circuits and Causal Interventions · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 6 minutes on a busy laptop CPU, after the one-time model download)

## Goal

Reproduce the chapter's case study: patch the residual stream and single attention heads of GPT-2 small on indirect object identification (IOI) prompts (Wang et al., 2023), in both directions and with two corruptions, then knock out the name mover heads and look for self-repair.

## Tools and versions

`env/requirements-llm.txt`: Python 3.10, torch 2.6.0, transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4, pandas 2.0.3, matplotlib 3.10.9. Notebook: `activation_patching_gpt2.ipynb`.

## Data and model

GPT-2 small (124 million parameters; the Hugging Face model card, openai-community/gpt2, lists the MIT license; downloaded once, about 500 MB). 48 prompts generated in the notebook from one template ("When A and B went to the [place], B gave a [object] to") with a fixed seed, plus a corrupted version of each (S2 replaced by the IO name) and an ABC version (S2 replaced by a third name). No personal data.

## Steps

1. Open the notebook and run the cells in order. Section 2 is the slowest (180 forward passes).
2. **Checkpoint 1:** logit difference clean about 3.74, corrupted about -3.88, ABC about 0.96; 100 percent of clean prompts correct.
3. **Checkpoint 2:** in the residual stream map, the S2 column is close to 1 up to layer 7 (0.96), 0.75 before layer 8 and 0.11 before layer 9; the END column is 0.35 before layer 8 and 0.98 before layer 9.
4. **Checkpoint 3:** denoising top heads: 10.7 (-0.50), 5.5 (+0.35), 8.6 (+0.34), 8.10 (+0.31), 9.9 (+0.27), 7.9 (+0.21), 11.10 (-0.21). Noising top heads: 10.7 (-0.44), then 9.9, 5.5, 8.6 and 8.10 at about +0.22.
5. **Checkpoint 4:** ABC denoising puts 8.10 first among positive heads (about +0.45); 5.5 falls to about +0.15; the two head maps correlate at about 0.92.
6. **Checkpoint 5:** knocking out heads 9.9, 9.6 and 10.0 (mean over ABC prompts) lowers the logit difference only to about 3.5, although their direct contribution was about 5.4; 10.10 rises from about 0.46 to 1.33 and 10.7 goes from about -2.38 to about 0.
7. Section 6 saves the result tables to `results/` (these are the tables used in Lab 16.1).

## Expected results

The numbers come from torch 2.6.0 on CPU with the seeds in the notebook; other versions or a GPU can move them in the second decimal. The chapter's self-repair figure uses a different set of ABC prompts for the mean (three random names) and reports 3.53; the notebook reports about 3.51.

## What to hand in

The residual stream map, the two head maps, the ABC comparison and the knockout table, each with two sentences of interpretation, and answers to the three questions at the end of Section 5.

## Self-check

If you concluded that a head with a small noising effect is unimportant, compare its denoising effect and its direct contribution: redundant heads can hide each other under noising, and self-repair can hide them under knockouts. If your interpretation of the ABC result says the S2-swap result was "wrong", reread the chapter: each corruption asks a different question.
