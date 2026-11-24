# Lab 6.1: Critique a Global Explanation Report

Chapter 6, The Whole Model at a Glance: Global Explanations · No code · About 45 minutes · Last checked: 2026-11-24

## Goal

Read a finished global explanation report for a motor insurance claims frequency model and decide, statement by statement, which conclusions the evidence supports. This is the reviewer's side of the Explanation Loop's Test step: a global explanation is only as good as the claims it can carry.

## Tools

A browser or any Markdown viewer. Everything you need is in this folder: `practice_global_explanation.md` and the figures in `figures/`. Nothing to install and no code to run. (The numbers come from the Lab 6.2 notebook; if you want to check one, run that lab.)

## Data behind the report

freMTPL2freq: 678,013 French motor third-party liability policies, OpenML data_id 41214 (listed there as CC0; original source the CASdatasets R package, GPL >= 2). The model is a gradient-boosted tree ensemble with a Poisson loss predicting claims per policy-year. Known limitations: one insurer, one period, no claim amounts in this file, and no information on why some groups of policies look unusual.

## Steps

1. Read `practice_global_explanation.md` once from top to bottom, including the figures. Do not judge yet.
2. **Checkpoint 1:** Without looking back, write down the two most important features and the one finding that surprised you. Compare with the report: if your surprise was not the B12 pocket or the density pair, read those sections again.
3. Go through the ten statements at the end of the report. For each, mark it **supported**, **unsupported** or **needs another check**, and write one sentence of evidence (which table or figure, which number).
4. **Checkpoint 2:** At least three statements confuse what the model does with what the world is like, and at least two ignore correlated features. Find them.
5. Rewrite the report's executive summary in at most 120 words so that every sentence is supported.
6. **Checkpoint 3:** Your summary must mention fidelity if it mentions the surrogate, and must not describe any effect as a cause.

## Expected results

Strong answers mark statements 2, 4, 6 and 9 as unsupported or in need of another check, explain the density pair as one factor in two encodings, and treat the B12 pocket as a question for the data owners rather than a finding about a car brand.

## Questions

1. The report's author computed permutation importance on held-out data with five repetitions. What would change if it had been computed on training data?
2. Which figure would you show a regulator first, and which one would you not show without a caveat?
3. Name one additional analysis the report should contain before the model is used for pricing.

## What to hand in

A one-page table (statement, verdict, evidence) and your rewritten executive summary. Add both to your Explanation Dossier as a review checklist you can reuse for your own report in Lab 6.2.

## Self-check

If you marked statement 4 as supported, reread the LOFO table. If your summary says that young age "causes" claims, reread the section on what a global explanation describes.
