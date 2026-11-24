# Lab 18.1: Steer, Then Audit

Chapter 18, Steering, Editing and Monitoring Models · No code · 45 to 60 minutes · Last checked: 2026-11-24

## Goal

Steer a language model with one internal feature or vector, compare its default and steered answers on prompts the steering is meant for and prompts it is not, and write an intervention audit card of the kind a model validator would accept.

## Tools

Option A (live): a public steering interface. As of late 2026, Neuronpedia's Steer page (https://www.neuronpedia.org/steer) lets you pick a model with inference enabled, add a feature from its sparse autoencoder dictionaries (by search, or by source and index) or a custom vector, set a strength with a slider (positive adds, negative removes), and see the default and steered replies side by side. Its documentation (https://docs.neuronpedia.org/steering, checked 2026-11-24) says that creating custom vectors requires signing in and that the service is rate-limited. Which models and features are available changes; use whatever small model is offered.

Option B (offline): the worksheet `worksheet.md` in this folder holds saved greedy continuations of GPT-2 small, default and steered with the Chapter 18 finance sentiment vector at strengths 1 and 2, on three target prompts and three off-target prompts. Everything in this lab can be done from the worksheet alone.

## Steps

1. Choose the intervention. Option A: search the feature list for a concept relevant to finance or customer service (for example praise, caution, risk or money) and read its top activating examples before you steer with it. Write one sentence saying what you believe the feature represents. Option B: the intervention is the sentiment vector; your belief is "it makes finance text more positive".
2. Write six prompts: three where the steering should matter (for example a customer's description of a bank visit) and three where it should not (a factual question, an instruction about a calculation, a sentence about a contract). Option B readers use the worksheet's prompts.
3. Run each prompt at strength 0 and at two non-zero strengths (Option A: start small and double). Record the replies.
4. **Checkpoint 1:** for each target prompt, did the reply move in the direction you named? For each off-target prompt, did anything change? In the worksheet, the off-target prompts change too: at strength 2 the compound-interest and capital-of-France prompts turn into product talk.
5. **Checkpoint 2:** look for a side effect that the name of the feature did not predict. In the worksheet, the "positive sentiment" vector drifts toward promotional language ("a great opportunity to share our products"), which in a regulated firm is a communications problem, not a tone improvement.
6. Option A only: try the same strength with a feature you believe is unrelated, as a rough control. Does it change the target prompts as much?

## What to hand in

A one-page intervention audit card with these fields: model and date; intervention (feature or vector, layer if known, strengths tried); the claim you tested in one sentence; three target and three off-target comparisons (default versus steered, one line each); the control you used or why you had none; at least one side effect; stability (did the effect hold on all target prompts?); recommendation (evidence only, usable with conditions, or not usable) and who should sign off.

## Self-check

If your card says "the feature controls X" on the basis of three prompts and no control, rewrite the claim as "on these prompts, adding this direction moved outputs toward X, with these side effects". Chapter 18's Myth vs. Reality box explains why.
