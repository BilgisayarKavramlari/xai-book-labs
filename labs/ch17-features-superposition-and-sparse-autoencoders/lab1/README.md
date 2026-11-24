# Lab 17.1: Investigate a Feature and a Graph on Neuronpedia

Chapter 17, Features, Superposition and Sparse Autoencoders · No code · About 60 minutes · Last checked: 2026-11-24

## Goal

Read, test and report one feature of an open language model the way an interpretability researcher would, then inspect one attribution graph and write down what it shows and what it leaves out.

## Tools

A web browser and Neuronpedia (https://www.neuronpedia.org/), an open-source interpretability platform. As of 2026-11-24 it hosts sparse autoencoder dictionaries for many open models (including GPT-2 small "res-jb", Gemma Scope for Gemma 2, Gemma Scope 2 for Gemma 3, Llama Scope), feature pages with activating examples, a **Test** box for your own text, a **Steer** tool, and the **Circuit Tracer** attribution graph viewer. Browsing feature pages and featured graphs needs no account. Generating new graphs or saving work may ask you to sign in; that is optional for this lab, and every step has a no-sign-in path.

Privacy: never type real patient, customer or employee data into a public web tool. Use invented text only.

## Part A. A feature card (about 35 minutes)

1. **Pick a feature.** Either search Neuronpedia by explanation for a concept from your Explanation Dossier (for example "symptoms", "loan", "refund"), or start from one of these GPT-2 small layer-8 residual-stream latents that Lab 17.2 found to be selective for medical text: https://www.neuronpedia.org/gpt2-small/8-res-jb/23479 , https://www.neuronpedia.org/gpt2-small/8-res-jb/9818 , https://www.neuronpedia.org/gpt2-small/8-res-jb/9151 .
2. **Read the label and its source.** Note who or what wrote the explanation (most are written by a language model) and its score, if one is shown.
3. **Activating examples at three levels.** Read the top examples, then examples from a middle and a low activation interval (if the page shows intervals). **Checkpoint 1:** write one sentence on whether the label still fits at moderate activations.
4. **Output effects.** Read the positive and negative logits (the tokens the feature pushes up and down).
5. **Your own tests.** In the Test box, enter five invented sentences: two where you expect the feature to fire, two where you expect it not to fire, and one tricky case (a related but different concept, a negation, or another language). **Checkpoint 2:** at least one result should surprise you; if none does, write a harder test.
6. **Steer.** Use the Steer tool with a neutral prompt (for example "On Saturday morning I went to the") at two strengths. Record the default and steered continuations. If steering is not available for your model, write "not available" and say which other evidence you would need.

| Feature card | Your notes |
|---|---|
| Model, layer, dictionary, latent index | |
| Label (and who wrote it) | |
| Top examples (2 or 3, paraphrased) | |
| Middle and low examples: does the label still fit? | |
| Output effects (top 5 up, top 5 down) | |
| Your five test sentences and activations | |
| Steering result at two strengths | |
| One counterexample or hole | |
| Your label, rewritten if needed | |

## Part B. Read an attribution graph (about 25 minutes)

1. Open the Circuit Tracer for Gemma 2 2B: https://www.neuronpedia.org/gemma-2-2b/graph . Choose the featured graph for the prompt about the capital of the state containing Dallas (the example of Lindsey et al., 2025, and Chapter 17).
2. Find the output node for "Austin". Follow the strongest incoming edges back one and two steps. **Checkpoint 3:** you should be able to find features related to Texas and to saying a capital; write down their labels as shown.
3. Find the error nodes (they may be drawn differently from features). Estimate whether they contribute little or a lot to the output.
4. Optional, if you are signed in and graph generation is offered: build a graph for an invented medical prompt such as "A 30-year-old pregnant woman has a severe headache and very high blood pressure. The doctor should check her for", and look for a node that represents a diagnosis the prompt does not name.
5. Write five sentences: what the graph claims, which nodes and edges carry the claim, what intervention would test it, how large the error nodes are, and what the graph cannot tell you (Chapter 17 lists attention, long prompts, inactive features and one-token scope).

## Expected results

Most feature labels hold at the top of the distribution and blur at moderate activations; many features respond to the context of a topic rather than to a single word; steering usually shifts the topic of a continuation, sometimes into repetition at high strength. In the Dallas graph, Texas-related and "say a capital" features sit between the input and "Austin". Exact feature labels and graph layouts change as the site and its models are updated.

## What to hand in

The completed feature card (one page) and the five sentences on the graph. For the Explanation Dossier, add one sentence on whether you would trust this feature as a monitoring signal, and why.

## Self-check

If your feature card contains only top examples and the label, you have described the data, not tested the model. Add at least one intervention (steering) and one counterexample.

## Sources

Lindsey, J., et al. (2025). On the biology of a large language model. https://transformer-circuits.pub/2025/attribution-graphs/biology.html ; Anthropic (2025, May 29). Open-sourcing circuit tracing tools. https://www.anthropic.com/research/open-source-circuit-tracing
