# Lab 7.1: Will It Say the Same Thing Twice? LIME in a Browser

Chapter 7, One Decision at a Time: LIME, Anchors and Local Surrogates · No code · About 45 minutes · Last checked: 2026-11-24 (hosted demo opened, LIME settings panel and a LIME run checked in a browser)

## Goal

Run LIME on a text classifier in a hosted web tool, rerun it with different random seeds, sample counts and kernel widths, and decide whether its highlighted words are stable enough to be read aloud to a person.

## What you need

A web browser. The Learning Interpretability Tool (LIT), an open-source tool from Google's People + AI Research team, has a hosted demo with small sentiment models:

https://pair-code.github.io/lit/demos/glue.html

As of 2026-11-24 the demo opens with the model `sst2-tiny` on the Stanford Sentiment Treebank development set (872 movie-review sentences, labeled positive or negative). Hosted demos change; if this one has moved, the LIT documentation lists its current demos. Any tool that lets you set LIME's seed and number of samples will do.

The scenario: a retailer routes product reviews that a model scores as negative to its customer care team, and the care agent sees the words LIME highlights. Movie reviews stand in for product reviews here.

## Steps

1. **Open the demo and pick a sentence.** Click a sentence in the Data Table that is longer than about 12 words. Open the **Explanations** tab in the lower half and find the **Salience Maps** panel. Expand it with the maximize icon.
   *Checkpoint: you see several rows of the same sentence with colored words, one row per method, including one labeled LIME.*
2. **Open LIME's settings.** Click the gear icon on the LIME row. As of the check date the panel shows: class index to explain, mask token (`[MASK]`), kernel width (256), number of samples (256) and seed (empty).
   *Checkpoint: write down the default values you see. They are your record of what "LIME" meant in this run.*
3. **Five seeds, same settings.** Set the seed to 1, click Apply and expand the LIME row. Record the three most strongly colored words and whether each pushes toward or against the predicted class. Repeat with seeds 2, 3, 4 and 5.
   *Checkpoint: a table with five rows (one per seed) and three words per row.*
4. **Count agreement.** For each pair of seeds, count how many of the three words they share and divide by the number of distinct words in the pair (the Jaccard index, Chapter 2). Average over the ten pairs.
5. **More samples.** Set the number of samples to 1,024 (or the largest value the demo accepts in reasonable time) and repeat steps 3 and 4 with seeds 1 to 5.
   *Checkpoint: you have two average agreement scores, one at 256 samples and one at the larger setting.*
6. **Kernel width.** Return to 256 samples and seed 1. Run LIME with a much smaller kernel width (for example 8) and a much larger one (for example 2,048). Note what changes.
7. **Change the sentence.** In the Datapoint Editor, add or remove one word (for example insert "not" before an adjective), click "Add and compare", and run LIME on the new sentence with seed 1. Does the explanation move in the direction you expected?
8. **The read-aloud test.** For your sentence, write the one sentence a care agent would say to the customer ("Our system flagged your review because ..."). Mark it *safe to read* only if its words appear in the top three in at least four of the five seeds at the larger sample setting.

## Expected results

Results depend on the sentence. On most sentences of 15 or more words, some words stay in the top three across seeds and others swap in and out; agreement usually rises with more samples. Words that are frequent and strongly sentiment-laden tend to be stable; function words and subword pieces tend not to be. A very small kernel width makes the explanation depend on only the closest perturbations, and can make the colors fade or change.

## What to hand in

One page: the seed table at both sample sizes, the two agreement scores, one sentence on the kernel width, the edited-sentence result, and your agent sentence marked safe or not, with your reason.

## Self-check

- Did you record the settings (samples, kernel width, mask, seed) next to every result? An explanation without its settings cannot be reproduced.
- If all five seeds gave identical words, did you check that the seed was actually applied (for example by changing it to a very different number)?
- Did your agent sentence describe what the model did, not what the reviewer felt?
