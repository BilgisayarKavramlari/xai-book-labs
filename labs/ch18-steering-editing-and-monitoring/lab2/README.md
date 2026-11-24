# Lab 18.2: Build a Steering Vector

Chapter 18, Steering, Editing and Monitoring Models · Run-only notebook with one editable cell · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 5.5 minutes on a laptop CPU, plus a one-time model download)

## Goal

Build a contrastive (difference-of-means) steering vector for positive versus negative sentiment in finance sentences, add it to GPT-2 small's residual stream, and test it like an explanation: stability, dose-response, a random-vector control, a side-effect measure, a layer sweep, and a reading test with the same vector.

## Tools and versions

Python 3.10 and the language-model environment in `env/requirements-llm.txt`: torch 2.6.0, transformer-lens 2.18.0 (HookedTransformer API), transformers 4.57.6, numpy 1.26.4. Notebook: `build_a_steering_vector.ipynb` (kernel `xai-llm-venv`; any kernel with these packages works). CPU only.

## Data and model

GPT-2 small (124M parameters, OpenAI, 2019), downloaded by TransformerLens from the Hugging Face Hub (about 550 MB) under its MIT license. All sentences are written in the notebook: 50 positive and 50 negative template sentences over ten finance subjects to build the vector, eight neutral prompts to steer, one neutral finance paragraph for the side-effect measure, and 150 held-out sentences for the reading test.

## Steps and checkpoints

1. Run the cells in order.
2. **Checkpoint 1:** the layer-6 vector has length 36.8; vectors built from two disjoint halves of the subjects have cosine 0.995.
3. **Checkpoint 2:** the positive-minus-negative logit gap is +1.64 without steering, +6.24 at strength 1 (range +4.24 to +7.20 over the eight prompts) and -2.10 at strength -1; random vectors of the same length give +2.22 at strength 1. Loss on the neutral paragraph: 3.33 nats per token unsteered, 3.91 at strength 1, 5.56 at strength 2 (random: 3.98 and 6.03).
4. **Checkpoint 3:** greedy continuations of "The quarterly report from the bank was" turn approving at strength 1 and degenerate into repetition at strength 2.
5. **Checkpoint 4:** at strength 0.5 the effect rises from +1.02 (layer 0) to about +3 (layers 6 to 9) and falls to +1.59 (layer 11); random vectors stay within 0.27 of zero.
6. **Checkpoint 5:** projected on the vector, held-out positive and negative sentences separate with AUROC 1.00, but 78 percent of negated negatives ("not terrible") are read as negative.
7. **Your turn:** edit the two word lists in the last cell to build a vector for a contrast you care about (for example cautious versus promotional investment language), and repeat Steps 2 and 5 by editing the relevant cells' word lists.

## Expected results

The checkpoint numbers come from the versions above on CPU. Other versions of torch or TransformerLens can change them in the second decimal; the pattern (specific effect, unspecific cost, middle layers strongest, negation misread) should hold. Generated text can name real organizations; it is model output, not information.

## Questions

1. The random vector raised the loss on neutral text as much as the sentiment vector. What does that tell you about where the side effect comes from?
2. Which layer would you choose, and on what evidence? Would your answer change if you cared about side effects most?
3. The vector reads sentiment perfectly on held-out sentences and fails on negation. Write the test you would add before using it as a monitor.

## What to hand in

A one-page intervention report: the claim, the settings (layer, strength, building data), the five checks with their numbers, one failure found by reading generations, and a recommendation.

## Self-check

If your report says the vector "is" the model's sentiment concept, revisit Chapter 18's section "What steering does not tell you": you have shown that the direction is sufficient to move these outputs, not that the model uses it, and only it, on its own.
