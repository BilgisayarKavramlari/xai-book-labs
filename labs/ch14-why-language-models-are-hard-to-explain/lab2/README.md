# Lab 14.2: Five Attributions for One Token

Chapter 14, Why Language Models Are Hard to Explain · Code notebook (run, read and answer; one optional edit) · About 60 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 70 to 105 seconds after GPT-2 small was cached)

## Goal

Explain one prediction of GPT-2 small with five methods (last-layer attention, attention rollout, gradient times input, integrated gradients, occlusion), see how the replacement used by occlusion and the choice of target change the answer, and measure how often the methods agree across 30 sentences. This notebook reproduces the chapter's figures of five methods, three replacements and plain versus contrastive targets.

## Tools and versions

`five_attributions.ipynb`, Python 3.10, in the language model environment `env/requirements-llm.txt`: torch 2.6.0 (CPU), transformer-lens 2.18.0 (the 2.x `HookedTransformer` API), transformers 4.57.6, numpy 1.26.4, scipy 1.15.3, matplotlib 3.10.9. Jupyter kernel name used for the check: `xai-llm-venv`. Do not install these into the main environment; transformer-lens 2.x needs numpy below 2.

## Data and model

GPT-2 small (124 million parameters; OpenAI, 2019), downloaded from the Hugging Face hub on first use (about 500 MB) and cached. Sentences are written in the notebook. No other data.

## Steps

1. Open the notebook with the `xai-llm-venv` kernel (or any kernel from `env/requirements-llm.txt`) and run the cells in order.
2. **Checkpoint 1:** p(she) = 0.176 and p(he) = 0.096 after "The nurse who interviewed the engineer said that".
3. **Checkpoint 2:** last-layer attention puts 0.61 on the start token and rollout 0.99; gradient times input gives its largest score (0.44) to *engineer*; integrated gradients gives about 1.58 to the start token and its scores add up to about 3.7; deletion gives +2.59 to *nurse* and -1.58 to *engineer*.
4. **Checkpoint 3:** deletion and the average-embedding replacement agree (*nurse* +2.59 and +2.92; *engineer* -1.58 and -1.71); the end-of-text replacement makes every token positive.
5. **Checkpoint 4:** for "why she?" deletion's top token is *said* (5.39); for "why she rather than he?" it is *nurse* (2.59).
6. **Checkpoint 5:** across 30 sentences, deletion's top token is an occupation in 77 percent; agreement with deletion on the top token is 80 percent for the average embedding, 17 percent each for gradient times input and integrated gradients, 0 percent for attention.
7. Optional: change `my_sentence` in the last code cell and compare the methods on a sentence of your own.

## Expected results

The numbers above, with the pinned versions. Other versions of torch or transformer-lens can change the second decimal; the pattern (attention on the start token, gradients disagreeing with occlusion, the end-of-text replacement inflating everything, the target changing the top token) should hold.

## Questions

1. Which row of the heatmap would you show a developer who asks which word made the model say *she*, and which would you refuse to show? Use the words *faithful* and *baseline*.
2. Integrated gradients kept its completeness promise. Why is that not enough to make it a good explanation here?
3. Which replacement would you defend for occlusion in a resume-screening model, and how would you test that choice?

## What to hand in

The agreement table from Checkpoint 5, the sentence (from the 30 or your own) where the methods disagree most, with its table of scores, and a paragraph answering Question 1.

## Self-check

If attention does not put most of its weight on the start token, check that the model was loaded with the default `prepend_bos` setting. If the 30-sentence cell is very slow, close other programs; it runs about 1,000 batched forward and backward passes.

## Sources

- Radford, A., et al. (2019). Language models are unsupervised multitask learners (GPT-2).
- Abnar, S., and Zuidema, W. (2020). Quantifying attention flow in transformers. ACL 2020.
- Sundararajan, M., Taly, A., and Yan, Q. (2017). Axiomatic attribution for deep networks. ICML 2017.
- Yin, K., and Neubig, G. (2022). Interpreting language models with contrastive explanations. EMNLP 2022.
