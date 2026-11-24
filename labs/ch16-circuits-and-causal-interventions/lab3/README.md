# Lab 16.3: Find and Knock Out Induction Heads

Chapter 16, Circuits and Causal Interventions · Run-only notebook with one optional edit · About 40 minutes · Last checked: 2026-11-24 (end-to-end run in about 40 seconds on a laptop CPU, after the one-time model download)

## Goal

Find the induction heads of GPT-2 small with a repeated random-token test (Olsson et al., 2022), knock them out, and compare the effect with a control set of heads.

## Tools and versions

The language-model environment of this repository, `env/requirements-llm.txt`: Python 3.10, torch 2.6.0, transformer-lens 2.18.0 (the `HookedTransformer` API; version 4.x removed it), transformers 4.57.6, numpy 1.26.4, matplotlib 3.10.9. Notebook: `induction_heads.ipynb`. It also runs in a hosted notebook service with a CPU runtime after installing the same versions.

## Data and model

GPT-2 small (124 million parameters; weights released by OpenAI; the Hugging Face model card, openai-community/gpt2, lists the MIT license, downloaded once, about 500 MB). The input is random token IDs generated in the notebook with a fixed seed. Nothing else is downloaded.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** mean loss about 12.4 nats on the first copy of the random sequence and about 0.41 on the repeated copy.
3. **Checkpoint 2:** the five heads with the highest induction score are 5.5 (about 0.94), 6.9, 7.10, 5.1 (about 0.91 to 0.92) and 7.2 (about 0.84); the strongest previous-token head is 4.11 (about 0.99), in an earlier layer.
4. **Checkpoint 3:** mean-ablating the top six heads raises the repeated-copy loss to about 5.7 nats; mean-ablating six control heads leaves it at about 0.43.
5. Optional edit: change `SEQ` to 20 and to 100 and rerun from that cell.

## Expected results

The numbers above come from torch 2.6.0 on CPU with the seeds in the notebook. Other versions or a GPU can move them in the second decimal; the pattern (a handful of heads in layers 5 to 7, a large loss increase when they are removed, almost none for the control) should hold.

## What to hand in

The two score tables, the loss plot and a paragraph (150 to 250 words) on what the knockout shows and what it does not show about in-context learning, plus answers to the three questions in the notebook.

## Self-check

If your paragraph says that these six heads "are" GPT-2's in-context learning, reread the chapter's section on induction heads: the test used random repeated tokens, and Olsson et al. (2022) labeled their evidence for large models with MLP layers as mainly correlational. The control set is what lets you say the effect is specific to these heads and not to removing any six heads.
