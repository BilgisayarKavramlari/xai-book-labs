# Lab 23.4: Same Model, Two Loaders

Chapter 23, Choosing, Measuring and Using XAI Tools · Code notebook (run and read; no code needs to be written) · About 30 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 10 seconds after the model download)

## Goal

Check a language-model interpretability library against a second implementation of the same model, and find out which of its outputs can be compared across tools and which cannot.

## Tools and versions

`same_model_two_loaders.ipynb`, Python 3.10, the language-model environment in `env/requirements-llm.txt`: torch 2.6.0 (CPU), transformer-lens 2.18.0 (with the `HookedTransformer` API), transformers 4.57.6, numpy 1.26.4, pandas. Jupyter kernel used for the check run: `xai-llm-venv`.

TransformerLens 4.0 (September 2026) removed `HookedTransformer.from_pretrained`; its recommended `TransformerBridge` keeps the raw Hugging Face weights by default unless a compatibility mode is switched on. Keep 2.18.0 for this notebook. The lesson of the lab is exactly this kind of change.

## Data

GPT-2 small (124M parameters) from the Hugging Face Hub, downloaded on first use (about 500 MB). Four short prompts written for the lab (credit, a name-mover sentence, airlines, healthcare).

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** the three loaders give the same top token on every prompt (' had', ' Mary', ' weather', ' minor'). Next-token log-probabilities agree to within about 0.0004.
3. **Checkpoint 2:** raw logits from the TransformerLens default loader differ from the reference by about 99 to 130 units, while log-probabilities and the logit difference between two candidate answers agree to about 0.0001. The default loader centers the unembedding, which shifts all logits at a position by the same constant.
4. **Checkpoint 3:** the residual stream from the default loader differs from the reference by about 4.6 to 4.9 units at layers 6 and 11; the no-processing loader matches within about 0.0005.

## Expected results

The table in section 2 with the values above. Exact digits can differ slightly with other CPU builds of torch; differences of the order of 0.0001 are floating-point noise, differences of the order of 1 to 100 are a different definition of the quantity.

## What to hand in

The summary table from section 3 and a short paragraph for a tool memo: which quantities your team may compare across libraries (for example log-probabilities and logit differences) and which it may not without the same loader settings (raw logits, residual-stream activations), and the version pins you would record.

## Self-check

- Can you explain why a constant shift in all logits leaves softmax probabilities unchanged?
- Would a probe trained on default-loader activations work on raw Hugging Face activations? (Not without care: the activations are centered differently.)
- Which single line of this notebook would you turn into an automated test that runs when a library is upgraded?
