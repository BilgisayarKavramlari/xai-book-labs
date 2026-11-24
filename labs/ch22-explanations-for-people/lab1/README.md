# Lab 22.1: Write for the Affected Person, Then Test It

Chapter 22, Explanations for People · No code · About 90 minutes · Last checked: 2026-11-24

## Goal

Turn a model's raw output and reasons for one decision into a layered explanation (headline, main reasons, what you can do, how to contest, details on request), then test it with three people using comprehension and action questions. You will see how much of what you wrote reaches a reader, and change the text because of it.

## What you need

This page, a word processor, and three people willing to spend about ten minutes each. No code. Both cases are invented; no real airline, hospital or person is described.

## Case A: a rebooked passenger (airline)

A flight from City P to City Q at 18:40 was cancelled for a technical fault. A rebooking model ranked the 168 passengers; the policy then filled the next morning's flight in ranked order and put the rest on a flight the day after. Raw output for one passenger:

```
passenger_id=PX-2214  rank=131/168  rebooked=FL214 next_day 07:10 (confirmed)
top_reasons (attribution, sorted):
  has_onward_connection = 0        -0.41
  waiting_since_hours  = 1.5       -0.22
  fare_class_flex      = 0         -0.09
  frequent_flyer_tier  = none      -0.07
  other features (8)               -0.04
policy: hotel voucher issued; refund available; standby on 21:55 possible
not used by the model: age, nationality, booking channel
```

## Case B: a follow-up call after discharge (hospital)

A readmission model flags patients for a nurse's call within two days of discharge. Raw output for one patient:

```
patient=H-0937  risk_30d=0.27 (flag threshold 0.20)  action=nurse_call_48h
top_reasons (attribution vs ward average):
  admissions_last_12m = 2           +0.07
  new_medications     = 5           +0.05
  lives_alone         = 1           +0.04
  age_years           = 71          +0.02
  other features (14)               +0.02
model performance on this ward (last year): of 100 flagged patients, about 32 were readmitted within 30 days
options: choose call time; clinic visit instead; decline
```

## Steps

1. **Pick one case** (or do both if you have time).
2. **List the questions** (15 minutes). Using the nine categories of the XAI question bank in the chapter (the table of question categories), write the five questions the passenger or patient is most likely to ask, in their words.
3. **Write the layered explanation** (25 minutes). At most 150 words for layers 1 to 3. Rules: use the person's facts, not feature names; say that other factors played a smaller part; separate the model's ranking or score from the decision; name a route to contest with a person. For Case B, state the performance figure as a natural frequency.
   *Checkpoint: no line of your text contains an underscore or a raw attribution number.*
4. **Write the test questions** (10 minutes): three comprehension questions with right answers (for example, "Why were you not on tonight's flight?" Right answer: passengers with onward connections and those who had waited longest were rebooked first) and one action question ("What would you do now?").
5. **Test with three people** (20 minutes). Give each person the text, then the questions, without help. Record answers verbatim. Ask for consent, collect no names, and say that the case is invented.
6. **Revise** (10 minutes). Change at least two things because of what you saw, and keep both versions.

## Expected results

Most first drafts fail on one of three points: a reason that names a model feature ("frequent flyer tier") without saying why it mattered, a missing or vague contest route, or (Case B) a probability that readers misread as "27 percent chance I will be readmitted, so I am probably fine". Readers usually answer the action question better than the "why" questions. Three people are far too few for conclusions; the point is to find what fails.

## What to hand in

Before and after texts, the five user questions from Step 2, the four test questions with right answers, the three participants' answers and two sentences on each change.

## Self-check

Did any reader answer a comprehension question with a reason the model did not use? If so, your text invited an inference you did not intend. A faithful explanation that is misread is not yet useful.
