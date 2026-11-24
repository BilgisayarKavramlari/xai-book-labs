# Lab 16.1: Read a Patching Experiment Before You Run One

Chapter 16, Circuits and Causal Interventions · No code (web browser and worksheet) · About 60 minutes · Last checked: 2026-11-24

## Goal

Predict, then read, the results of an activation patching experiment on GPT-2 small, see why attention patterns alone could not have given the same answer, and design a patching experiment of your own for a different behavior.

## Tools

- A web browser. For Part B: Transformer Explainer (https://poloclub.github.io/transformer-explainer/, checked 2026-11-24), an interactive visualization from the Polo Club of Data Science that runs GPT-2 small in the browser and lets you type your own text and inspect attention. No account is needed. If the site is unavailable, skip Part B; the rest of the lab does not depend on it.
- The result tables in `results/` (plain CSV files; open them in any spreadsheet program or in the browser) and the figures in the chapter.
- `worksheet.md` (print it or copy it into a document).

## Data

The tables were computed with the notebook of Lab 16.2 on GPT-2 small (124 million parameters; the Hugging Face model card, openai-community/gpt2, lists the MIT license) and 48 generated prompts of the form "When Mary and John went to the store, John gave a drink to". No personal data is involved.

| File | What it contains |
|---|---|
| `results/residual_patching.csv` | Share of the logit difference restored by patching the residual stream, by layer (rows) and token position (columns) |
| `results/head_denoising.csv` | Share restored by copying one head's clean output into the corrupted run (12 layers by 12 heads) |
| `results/head_noising.csv` | Share lost by copying one head's corrupted output into the clean run |
| `results/head_denoising_abc.csv` | As `head_denoising.csv`, with a different corruption (a third name at the second mention of the subject) |
| `results/knockout_dla.csv` | Each head's direct contribution to the logit difference before and after knocking out heads 9.9, 9.6 and 10.0 |

## Steps

**Part A, predict (10 minutes).** Before opening any table, fill in Part A of the worksheet: where in the prompt, and in which layers, do you expect the information that decides between the two names to sit? Which kinds of heads do you expect to matter?

**Part B, look at attention (10 minutes).** In Transformer Explainer, type "When Mary and John went to the store, John gave a drink to" and look at the attention of the last token in a few heads of the late layers. Write down which earlier tokens get the most attention. **Checkpoint B:** you should be able to find heads that attend strongly to a name, but nothing on the screen tells you whether that attention changes the output.

**Part C, read the results (25 minutes).** Open the tables in order and answer Part C of the worksheet. **Checkpoint C1:** in `residual_patching.csv` the S2 column is close to 1 up to layer 7 and the END column is close to 1 from layer 9. **Checkpoint C2:** the heads with the largest absolute effect in `head_denoising.csv` are 10.7 (negative), 5.5, 8.6, 8.10, 9.9 and 7.9. **Checkpoint C3:** in `knockout_dla.csv`, the row "head 10.10" rises from about 0.46 to about 1.33 and the row "head 10.7" goes from about -2.38 to about 0.

**Part D, design (15 minutes).** Fill in the experiment design template in Part D for a behavior of your choice (examples: a model completing "The capital of France is" with Paris; a sentiment model's label flipping on "not"; a product category predicted from one key word). Name the clean and corrupted prompts, the metric, the direction(s), the granularity and one test that could break your conclusion.

## Expected results

Your predictions in Part A will probably miss something; most people do not predict the negative heads or the self-repair. That is the point of the exercise.

## What to hand in

The completed worksheet: predictions, the attention observation, answers to the reading questions, and the one-page experiment design.

## Self-check

Your reading of the residual stream table should say that the information *moves* from S2 to the final position in layers 7 and 8; it should not say that layers 0 to 7 *compute* the answer. If your design in Part D has no corruption that keeps the prompt a normal sentence, or no test that could prove you wrong, revise it.
