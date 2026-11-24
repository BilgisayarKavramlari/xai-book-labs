# Lab 9.1: From Reason Codes to Recourse

Chapter 9, What Would Have to Change? Counterfactuals, Causality and Recourse · No code · About 60 minutes · Last checked: 2026-11-24

## Goal

Take the sample list of denial reasons that United States Regulation B offers lenders, decide which of them tell an applicant something they can act on, and turn three of them into honest recourse statements. Then find recourse by hand on a small scorecard, first ignoring and then respecting what the applicant can actually change.

## What you need

A web browser, a pen or a spreadsheet. Nothing to install.

Source document: Regulation B (12 CFR part 1002), Appendix C, Sample Form C-1, part I, "Principal reason(s) for credit denial, termination, or other action taken concerning credit". It is published by the Consumer Financial Protection Bureau at https://www.consumerfinance.gov/rules-policy/regulations/1002/c/ (checked 2026-11-24; the form lists 23 reasons plus "Other, specify"). Regulation B's official interpretation of section 1002.9(b)(2) is at https://www.consumerfinance.gov/rules-policy/regulations/1002/interp-9/. These are public government texts.

## Part A: classify the sample reasons (25 minutes)

1. Open Form C-1 and copy its 23 reasons into a table.
2. For each reason, choose one label:
   - **Act now**: the applicant can do something about it within weeks (for example, supply missing information).
   - **Time only**: it changes only with time (for example, a length of employment).
   - **Not actionable**: it cannot be changed, or changing it would not be a reasonable request (for example, a past bankruptcy).
   - **Unclear**: the reason does not say what to change or in which direction.
3. For every reason labeled Act now, write the action in one sentence and ask: would the action change only the model's input, or also the risk the model is trying to predict?
   *Checkpoint: you have 23 labeled rows. Most readers find that only a minority are Act now, and that several are Unclear because they name a factor without a direction (the official interpretation, comment 9(b)(2)-3, allows "length of residence" instead of "too short a period of residence").*
4. Read comment 9(b)(2)-5 of the official interpretation. It describes ranking reasons by how far the applicant's score on each factor fell below an average. Note in one sentence why the factor that costs the most points is not always the easiest one to change.

## Part B: recourse by hand on a scorecard (25 minutes)

An invented points scorecard. An applicant is approved at 300 points or more.

| Factor | Bands and points |
|---|---|
| Missed payments in the last 2 years | 0: 110 · 1: 70 · 2 or more: 20 |
| Credit used, percent of limits | under 30: 90 · 30 to 60: 60 · over 60: 25 |
| Age of oldest account, years | under 2: 20 · 2 to 5: 50 · over 5: 75 |
| Requested amount, multiple of monthly income | under 2: 60 · 2 to 4: 40 · over 4: 15 |
| Applications in the last 6 months | 0 to 1: 45 · 2 to 3: 30 · 4 or more: 10 |

Applicants:

| Applicant | Missed payments | Credit used | Oldest account | Amount / income | Recent applications |
|---|---|---|---|---|---|
| Amara | 0 | 72% | 1.5 years | 4.5 | 2 |
| Kenji | 0 | 45% | 3 years | 3 | 5 |
| Lucia | 2 or more | 25% | 7 years | 1.5 | 1 |

5. Compute each applicant's score. *Checkpoint: Amara 200, Kenji 270, Lucia 290.*
6. **Unconstrained:** find, for each applicant, the change of the fewest bands that reaches 300, allowing any factor to change.
7. **Actionable:** repeat, but treat the age of the oldest account, past missed payments and recent applications as unchangeable today (the last two change only with time), and allow the requested amount and credit used to change. *Checkpoint: one of the three applicants has no actionable recourse at all today. Which one, and what is the earliest kind of change that could ever help?*
8. **Causal check:** reducing credit used is usually done by paying down a balance. Suppose paying down the balance uses savings that Amara would otherwise put toward the purchase, so the amount she must borrow rises one band. Does your recourse for Amara still work? What does this say about recommending two changes as if they were independent?

## Part C: write three recourse statements (10 minutes)

9. Pick three reasons from Part A labeled Act now or Time only. For each, write a statement an applicant could use, of the form "If [specific change], and nothing else changed, our model would have [outcome]. This would take about [time]." Add one honest caveat: what the statement does not promise.

## What to hand in

One page: the labeled table of Part A (or its counts by label, with three examples), your three recourse calculations from Part B, and the three statements of Part C. This feeds the recourse analysis in your Explanation Dossier (artifact 9).

## Self-check

- If every reason in your table is Act now, reread step 2: several reasons concern the past or the person.
- If your statements in Part C promise approval, rewrite them: a counterfactual describes the model's response to one change today, not a guarantee after the model is retrained or other facts change.
- If you found recourse for all three applicants in step 7, check Lucia again.
