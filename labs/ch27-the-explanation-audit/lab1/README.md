# Lab 27.1: Plan the Audit

Chapter 27, The Explanation Audit · No code · About 75 minutes · Last checked: 2026-11-24

## Goal

Turn an Explanation Dossier into an audit plan (scope, criteria, access, evidence index) and write the first three entries of a finding register, so that the audit can be re-performed by someone else.

## Tools

This worksheet and a document or spreadsheet. Your own Explanation Dossier if you have one; otherwise the fictional dossier excerpt below.

## Data

None. The dossier excerpt below is **invented for this lab**. It describes no real company, product or person, and every number in it is fictional.

## A fictional dossier excerpt: a claims triage model at a mid-sized insurer

- **Artifact 1 (system brief):** a gradient-boosted model scores incoming motor claims for fraud risk; claims above 0.7 go to a special investigations unit. Audiences named: claims handlers, investigators, the model validator, the regulator. The policyholder is not listed.
- **Artifact 2 (requirements):** "Explanations must be accurate and easy to understand." No foil, no number of reasons, no acceptance criteria.
- **Artifact 3 (model card):** test AUC 0.81 on a random split of 2021 to 2023 claims. No time-based split. A leakage log lists "investigator notes" as removed.
- **Artifact 7 (local explanations):** LIME reasons for five claims; stability "checked visually".
- **Artifact 8 (SHAP):** background = 100 random training claims; top three reasons shown to handlers on screen; library version not recorded.
- **Artifact 9 (recourse):** none; "not applicable to fraud".
- **Artifact 20 (evaluation):** deletion test with a random baseline: reasons first 0.31, random 0.52 (no interval).
- **Artifact 22 (affected person):** none.
- **Artifact 23 (tool memo):** shap chosen "because it is the industry standard".
- **Artifact 25 (monitoring):** monthly AUC; no explanation drift check.

## Steps

1. Read Chapter 27, sections "What an Explanation Audit Is" through "Writing Findings and the Opinion".
2. **Checkpoint 1, scope:** write the audit scope in three sentences: the system and version, the intended uses of its explanations (one per audience), and what is out of scope. Hint: the policyholder is missing from Artifact 1; decide whether the audit includes what a policyholder is told when a claim is delayed.
3. **Checkpoint 2, criteria and access:** for each use, write the criterion you will test against (from the requirements, from Chapter 20's triad, from a law or standard, or from the organization's own policy) and the access you need: black-box (query the model), white-box (weights and internals) or outside-the-box (documents, data, logs), in the terms of Casper et al. (2024).
4. **Checkpoint 3, evidence index:** build a table with one row per Loop step (Ask, Scope, Choose, Test, Tell, Record): the dossier artifact that gives evidence, its quality (re-performed, documented only, asserted only, missing) and the test you would re-perform.
5. **Checkpoint 4, finding register:** write three findings in the form criterion, condition, cause, effect, recommendation, each with a severity (high, medium, low) by the chapter's definitions.
6. Write the opinion you would expect to give for each use, marked as provisional: fit, fit with conditions, or not fit.

## Expected results

A plan of two to three pages. Typical findings for the excerpt: (a) requirements have no acceptance criteria, so faithfulness and stability cannot be passed or failed (medium; cause: requirements written without the validator); (b) the deletion test has no interval and no second replacement setting, and stability was "checked visually" (medium); (c) the library version and background are not recorded with the reasons shown to handlers, so no stated reason can be reproduced (high if handlers act on reasons; cause: no logging standard); (d) the policyholder audience and recourse were declared out of scope without a justification (medium to high, depending on what policyholders are told). Your wording and severities may differ; what matters is that each finding names its criterion and its evidence.

## What to hand in

The scope, the criteria and access table, the evidence index and three findings. This is the first part of your Chapter 27 Dossier artifact.

## Self-check

For each finding, ask: could the system owner disagree with the condition? If yes, name the evidence that would settle it. A finding that rests on "seems" or "appears" needs a test, not an adjective.
