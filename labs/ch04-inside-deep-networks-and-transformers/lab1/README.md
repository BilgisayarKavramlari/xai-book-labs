# Lab 4.1: Watch a Network Build Features

Chapter 4, Inside Deep Networks and Transformers · No code · About 50 minutes · Last checked: 2026-11-24 (both tools loaded and worked in a desktop browser)

## Goal

See with your own eyes what hidden units compute in a small network, and what attention patterns look like in a real (small) language model. Then practice the habit the chapter asks for: mark every observation as *tested* or *untested*.

## Tools

- **A neural network playground**: TensorFlow Playground, https://playground.tensorflow.org/ (free, runs in the browser, no account). It trains a small fully connected network on two-dimensional toy datasets and draws what every neuron computes over the input plane.
- **A transformer explainer**: Transformer Explainer, https://poloclub.github.io/transformer-explainer/ (free, runs a small GPT-2 model in the browser, no account; described in Cho et al., 2024, arXiv:2408.04619). You type text, see the next-token probabilities, and can hover over tokens to see attention weights.

If either tool has moved or changed, check the tool landscape page in `tools/` of this repository. Any interactive tool that trains a small network in the browser, or any viewer that shows a language model's attention for your own text, will do; note the tool and date in your log.

## Data

The playground's built-in synthetic datasets (Circle, Exclusive or, Gaussian, Spiral). Your own three sentences for the transformer explainer. Nothing is downloaded.

## Steps

### Part A: hidden units (about 30 minutes)

1. Open the playground. Choose the **Circle** dataset, keep the two input features x1 and x2 only, and set one hidden layer.
2. Start with 1 hidden neuron and press Run. Watch the test loss. Add neurons one at a time until the test loss falls below about 0.05 and stays there. Record the smallest number that worked.
3. Hover over each hidden neuron. The small square shows what that neuron computes over the whole input plane.
4. **Checkpoint 1:** with the tanh or ReLU activation, each hidden neuron in a one-layer network shows a pattern divided by a straight line (a soft half-plane). The output combines them. You will usually need three or four neurons for the circle (compare the chapter's figure of hidden units).
5. Switch to the **Spiral** dataset. Try to fit it with as few neurons as possible. Add a second hidden layer, and add the extra input features (squares, products, sines) if you get stuck.
6. **Checkpoint 2:** neurons in the second layer show curved patterns, combinations of the first layer's half-planes. Record one neuron whose pattern you can describe in words and one you cannot.

### Part B: attention (about 20 minutes)

7. Open the transformer explainer. Type the sentence `The nurse said that she` and look at the predicted next tokens.
8. Hover over the token `she` (or select it, depending on the version) and look at which earlier tokens it attends to. If the tool lets you choose a layer and a head, look at several and record which ones put weight on `nurse`.
9. Repeat with `The mechanic said that he` and with a sentence of your own that has two possible referents (for example, `The manager told the assistant that she`).
10. **Checkpoint 3:** you will find some heads that attend from the pronoun to a noun and many that attend mostly to the first token or to the token itself. This is normal: many heads put weight on positions that carry little information (the chapter's Deep box on attention shows why weight is not contribution).

## Expected results

Part A: three or four hidden neurons fit the circle; the spiral needs more neurons, usually two layers or extra input features. Part B: the patterns vary across heads; few if any heads give a clean, single link from pronoun to noun in every sentence.

## Questions

1. For your smallest circle network, describe in one sentence each what every hidden neuron computes. Was any neuron unnecessary?
2. For the spiral, could you describe every second-layer neuron in words? What does this suggest about naming the features of a network with millions of units?
3. For each of your three attention observations, mark it *untested* or *tested*. Nothing in this tool lets you edit internal values, so how would you test whether the head you saw actually drives the prediction? (Lab 4.4 does this on a tiny model.)

## What to hand in

A one-page log: the smallest working circle network with a sketch or description of each neuron, one spiral network, and three attention observations, each with the sentence, the layer and head if available, what you saw, and *tested* or *untested*.

## Self-check

If every one of your attention observations is marked *tested*, reread Question 3: looking is not testing.
