# Lab 17.2: Medical Features in GPT-2 Small

Chapter 17, Features, Superposition and Sparse Autoencoders · Run-only notebook (language model environment) · About 50 minutes · Last checked: 2026-11-24 (end-to-end run in about 40 seconds on a laptop CPU, after downloads)

## Goal

Load a published sparse autoencoder (SAE) for the residual stream of GPT-2 small, measure its sparsity and reconstruction, find latents that are selective for medical text, and test them two ways: by removing them (are they necessary?) and by adding their directions to an unrelated prompt (are they sufficient?), against a random-direction control.

## Environment and versions

Use the language model environment in `env/requirements-llm.txt` (kernel `xai-llm-venv`): Python 3.10, torch 2.6.0, transformer-lens 2.18.0 (HookedTransformer API), transformers 4.57.6, numpy 1.26.4. The notebook also uses huggingface_hub 0.36.2 and safetensors 0.8.0, which are installed with transformers. No SAE library is needed: the notebook loads the SAE weights directly, so you can see every step.

Notebook: `medical_features_gpt2.ipynb`.

## Data and models

- GPT-2 small (124M parameters, OpenAI, MIT license), downloaded by TransformerLens from Hugging Face on first use (about 500 MB).
- SAE: `jbloom/GPT2-Small-SAEs-Reformatted`, hook `blocks.8.hook_resid_pre` (the residual stream entering layer 8), 24,576 latents, trained on OpenWebText (about 75 MB, MIT license). The same latents are browsable on Neuronpedia as `gpt2-small/8-res-jb`.
- Text: 26 short invented sentences in four topics (medicine, sports, code, finance), written in the notebook. No personal data.

## Steps and checkpoints

1. **Part A, quality.** Encode the corpus. **Checkpoint 1:** 301 tokens, about 63 active latents per token out of 24,576, about 16 percent of the variance unexplained; next-token loss 3.83 clean, 3.95 with the SAE spliced in, 7.62 with the layer mean-ablated, so about 97 percent of the loss is recovered.
2. **Part B, selectivity and output effects.** **Checkpoint 2:** the six most medical-selective latents are 9151, 357, 14773, 6435, 9818 and 23479. Several fire on words such as "the" or "." inside medical sentences (they track context). Their output effects are medical (for example 9818 pushes up "pneumonia", "tuberculosis"; 23479 pushes up "symptoms", "nausea").
3. **Part C, ablation.** **Checkpoint 3:** removing the top 1, 3 or 6 latents leaves the next-token predictions for a hospital prompt almost unchanged ("MRI" stays first at about 0.16; total variation 0.03 to 0.08).
4. **Part D, steering.** **Checkpoint 4:** "On Saturday morning I went to the" continues with a grocery store; adding latent 9151's direction at strength 40 gives an emergency room and a diagnosis; a random direction of the same length leaves the grocery store.

## Expected results

The numbers above come from the versions listed, on CPU, with the seeds in the notebook. Other versions can move them slightly; the pattern (most loss recovered but a sixth of the variance missing; selective latents not necessary for the prediction but sufficient to steer) should hold.

## Questions

In the notebook: a feature card for one latent; reconciling Parts C and D with the words selective, necessary and sufficient; what else you would need to claim that GPT-2 "uses a concept of disease".

## What to hand in

The four checkpoint results, a feature card for one latent (label, top tokens, output effects, ablation and steering results, one counterexample from your own test sentence), and one paragraph separating correlational from causal evidence. Compare your label with the one on the latent's Neuronpedia page.

## Self-check

If you concluded from Part C that the latents "do not matter", reread the chapter's Myth vs. Reality box: absence of an ablation effect shows redundancy, not irrelevance. If you concluded from Part D that GPT-2 "has a medical concept", ask what a random control and a second prompt would add.
