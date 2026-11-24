# Lab 15.1: Reading the Lens, Judging the Probe

Chapter 15, Reading Representations: Probing and the Logit Lens · No code · About 45 minutes · Last checked: 2026-11-24

## Goal

Read precomputed logit-lens tables and probe results for GPT-2 small and decide, claim by claim, what the evidence supports. The skill practiced is the Test step of the Explanation Loop: telling a reading of a representation apart from a finding about what the model uses.

## Tools

A web browser or any text viewer. The materials are Markdown files in `materials/`:

- `A_logit_lens_tables.md`: the logit lens on four prompts, layer by layer.
- `B_lens_comparison.md`: the logit lens against a fitted affine lens on held-out text.
- `C_truth_probe_results.md`: truth probes on 288 city statements, with baselines and transfer tests.

All numbers were computed by the notebooks in `../lab2/` and `../lab3/` (GPT-2 small, TransformerLens 2.18.0). If you can run those notebooks, you will get the same numbers.

## Data

Prompts and statements written for this lab; GPT-2 small (OpenAI, 2019), as distributed on the Hugging Face Hub; see its model card for the license terms. No personal data.

## Steps

1. Read Material A. **Checkpoint 1:** for Prompt 1 the top guess is `' own'` from layer 1 to 6 and `' email'` from layer 7 on.
2. Read Material B. **Checkpoint 2:** at layer 6 the logit lens is 6.24 bits from the output and the affine lens 2.58 bits.
3. Read Material C. **Checkpoint 3:** the logistic probe on plain statements scores 0.910 at layer 8; the same probe scores 0.340 on negated statements at layer 8.
4. Fill in the worksheet below.

## Worksheet

For each claim, write a verdict (supported, partly supported, not supported) and one sentence of evidence that cites a number from the materials.

1. "GPT-2 small knows the Eiffel Tower is in Paris."
2. "In Prompt 1, the model has decided on 'email' by layer 7."
3. "The logit lens is a reliable reading of GPT-2 small's early layers."
4. "A fitted lens reads every layer better than the logit lens on held-out text."
5. "GPT-2 small has a truth direction at layer 8."
6. "The truth probe works because of the probe's capacity, not because of anything training built."
7. "The truth probe would work as a hallucination flag for a support assistant."
8. "A probe trained on plain and negated statements has found how GPT-2 small represents truth."

## Expected results

Reasonable verdicts: 1 partly (Paris is a close second, London wins; the lens shows London leading from layer 10). 2 partly (email leads from layer 7 but with 0.58 and 0.35 at layers 7 and 8; "decided" claims more than a lens shows). 3 not supported (70 bits at layer 0; low agreement). 4 supported (lower KL and higher agreement at layers 0 to 11). 5 partly (0.91 on held-out cities, random network near 0.5, but negations and paraphrases fail, so it reads plausibility as much as truth). 6 not supported (the random network and layer 0 stay near 0.5), though the control task shows how much a probe can read from country identity. 7 not supported (negation, paraphrase threshold failure, no test on the team's own data). 8 not supported (decodable on these two forms; use not tested; a third form not tested).

## What to hand in

The completed worksheet (one page) and, in three sentences, the one experiment you would run next and what result would change your verdict on claim 5.

## Self-check

If any of your verdicts rests on a single number without a baseline or a transfer test, revisit it: the chapter's point is that probe and lens readings mean little without them.
