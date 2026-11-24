# Lab 19.2: Which Source Did the Model Use?

Chapter 19, Explaining LLM Applications: Citations, Traces and Agents · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 30 seconds on a laptop CPU, after the model download)

## Goal

Measure how much each sentence of a context contributes to a language model's answer, by leave-one-out ablation and by a sparse linear surrogate fitted to random ablations (in the spirit of ContextCite, Cohen-Wang et al., 2024); use the result to test a printed citation; and see how much a model relies on context for a fact it already knows.

## Tools and versions

The language-model environment: Python 3.10 with torch 2.6.0, transformers 4.57.6, scikit-learn 1.7.2, scipy 1.15.3, numpy 1.26.4, matplotlib 3.10.9 (see `env/requirements-llm.txt`; Jupyter kernel `xai-llm-venv`). Notebook: `which_source_did_the_model_use.ipynb`.

## Data and model

Six invented policy sentences for a fictional parcel firm (in the notebook). GPT-2 small (124 million parameters, MIT license), downloaded from the Hugging Face hub on first use (about 500 MB).

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** log probability of " 30 days" with the full context is about -2.87 (probability about 0.057).
3. **Checkpoint 2:** leave one out: S2 about 0.24, S6 about 0.21 (the redundant pair), S1 about -0.28; removing S2 and S6 together about 0.65; removing all six sentences about 1.42.
4. **Checkpoint 3:** surrogate from 64 random ablations (Lasso, alpha 0.01): S2 about 0.65, S6 about 0.27, S1 about -0.10, the rest below 0.03. Spearman correlation between predicted and actual log probability on 32 new ablations about 0.94.
5. **Checkpoint 4:** a printed citation to S3 (surrogate weight about 0.03) did not drive the answer. For "The capital of France is ... Paris": removing the Paris sentence lowers log probability by about 2.1, removing all sentences by about 1.8; with no context, " Paris" still has probability about 0.08 against about 0.01 for " 30 days".

## Expected results

The numbers above, to within about 0.01 (the computation is deterministic on CPU; tiny differences can come from library builds).

## Questions

1. Why does leave one out understate S2 and S6? What would a "top source by leave one out" citation rule do here?
2. What does S1's negative attribution mean? Should a product ever show negative attributions to users?
3. GPT-2 small leans on its context even for "Paris". What would you expect from a large model, and why does that matter for post-rationalized citations?
4. What would you need from a hosted model's interface to run this test on a production assistant?

## Optional edit

Change the number of random ablations from 64 to 16 and rerun Section 3. How much do the surrogate weights and the held-out correlation change?

## What to hand in

The attribution chart for the refund question, the Paris results, and one paragraph each on the redundant pair and on what the Paris experiment means for citations.

## Self-check

If the surrogate gives S3 a large weight, check that your ablation masks were drawn with the fixed seed and that the response string starts with a space (" 30 days"); GPT-2's tokenizer treats a leading space as part of the token.
