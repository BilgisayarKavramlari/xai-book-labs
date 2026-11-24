# Lab 4.4: Inside a Tiny Transformer

Chapter 4, Inside Deep Networks and Transformers · Code notebook (run, read, and answer; no code needs to be written) · About 60 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in about 80 seconds with the versions below)

## Goal

Train a two-layer transformer on a lookup task, look at its attention patterns, and test whether an attention pattern is a faithful explanation by editing the input. This is the model behind the chapter's figure of attention patterns and editing results.

## Tools and versions

`tiny_transformer.ipynb`, Python 3.10, numpy 2.2.6, matplotlib 3.10.9, **torch 2.6.0** (CPU build). Install the extra library with `pip install torch==2.6.0` into the environment from `env/requirements.txt`. No GPU and no internet access are needed after installation.

## Data

Generated in the notebook: sequences of four (or six) distinct keys from A to H, each followed by a digit, then `?` and one of the keys. The correct output is the digit that followed that key. Training uses 800 batches of 256 random sequences; the test set is 2,000 new sequences.

## Steps

1. Open the notebook and run the cells in order. Training takes under a minute.
2. **Checkpoint 1:** test accuracy 1.000.
3. **Checkpoint 2:** for the example `B 9 E 0 C 2 D 3 ? C`, the prediction is `2`; in layer 2 the last row puts 0.97 (head 1) and 0.99 (head 2) of its attention on the token `2`; layer 1's last row is spread over several positions.
4. **Checkpoint 3:** averaged over heads and the test set, layer 2 puts 0.94 of the last position's attention on the correct value; layer 1 puts about 0.18.
5. **Checkpoint 4:** editing the attended value changes 100 percent of answers; editing another value changes 0 percent.
6. **Checkpoint 5:** weight and contribution (weight times the size of what the head writes) agree closely for layer 2. In layer 1 they are similar too in this model; note the largest difference you find.
7. **Checkpoint 6:** with six pairs, accuracy is again 1.000 and the edit rates are again 100 and 0 percent.

## Expected results

The numbers above, with the pinned versions and seeds. Small differences can appear with other versions of torch; the pattern (layer 2 retrieves, editing confirms it, layer 1 is hard to read) should hold.

## Questions

1. Which head would you trust as an explanation of the model's answer, and which would you not? Use the words *faithful* and *tested*.
2. Layer 1 must do something useful, because removing it would break the model (try it as an extra if you wish). Why can you not tell what it does from its heatmap? What experiment would you run to find out? (Chapter 16 covers such experiments.)
3. In a production language model with dozens of layers and many heads per layer, why is it unlikely that one head's attention will pass an editing test as cleanly as here?

## What to hand in

Two layer-2 heatmaps and one layer-1 heatmap, the edit rates for four and six pairs, and a paragraph answering Question 1.

## Self-check

If your edit rate for "another value" is high, the model is not doing the lookup you think it is: check accuracy first.
