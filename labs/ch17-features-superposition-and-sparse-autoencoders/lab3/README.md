# Lab 17.3: Superposition and Dictionaries You Can Check

Chapter 17, Features, Superposition and Sparse Autoencoders · Run-only notebook (two optional edit cells) · About 40 minutes · Last checked: 2026-11-24

## Goal

Reproduce the toy model of superposition (Elhage et al., 2022), watch how many features two neurons store as sparsity changes, see interference, then train sparse autoencoders where the true features are known and measure whether better reconstruction means better features.

## Environment and versions

Main lab environment (`env/requirements.txt`, kernel `xai-lab-venv`): Python 3.10, numpy 2.2.6, torch 2.6.0, matplotlib 3.10.9. CPU only. Notebook: `superposition_and_dictionaries.ipynb`.

## Data

Synthetic only, generated in the notebook with fixed seeds: sparse features (zero, or uniform between zero and one), and sparse codes over random unit directions. Nothing is downloaded.

## Steps and checkpoints

1. **Part A.** Train the five-feature, two-neuron toy model at six densities. **Checkpoint 1:** 2 features stored when dense, 4 at moderate sparsity, 5 when each feature is active in 5 percent of inputs or less (the switch points can move a little with the seed).
2. **Interference.** **Checkpoint 2:** with one feature on, it is rebuilt cleanly; with two on, values leak or cancel according to the cosine between their directions.
3. **Part B.** 24 features through 8 ReLU neurons, then an SAE with 48 latents. **Checkpoint 3:** about 4 features per neuron, about 1.5 per SAE latent (most latents respond to one feature); blank rows are features the toy network did not store.
4. **Part C.** SAEs with 48, 96 and 192 latents and six penalties on data with 96 true features (about 1.9 active per sample). **Checkpoint 4:** unexplained variance falls steadily with more active latents; recovery of true features is near zero for dense dictionaries, about 0.85 to 1.0 for the 96- and 192-latent dictionaries near 1.3 to 3.6 active latents, and lower again at the strongest penalty; the 48-latent dictionary stays below about 0.4.

## Expected results

The chapter's figures (toy superposition, neurons versus latents, reconstruction versus recovery) were produced by the same code with the same seeds in the book's figure script; small differences in the step counts here can move individual numbers by a few hundredths. Run time on a laptop CPU: about 3 minutes (measured 180 seconds on 2026-11-24, on a busy machine).

## Questions

In the notebook: which features are dropped first and why; whether a neuron label written from top activations would be faithful; which measurements you would use to choose a dictionary on a real model, and what they could not tell you.

## What to hand in

The table of stored features by density, the Part B summary line, the Part C table and plot, and three sentences on which dictionary you would choose and why.

## Self-check

If you chose the dictionary with the lowest unexplained variance, look at its recovery. On real models you cannot see recovery, which is why Chapter 17 asks for interventions, stability checks and baselines.
