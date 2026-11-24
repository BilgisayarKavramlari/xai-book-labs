# Lab 8.1: Shapley Values by Hand

Chapter 8, Shapley Values and SHAP · No code · About 45 minutes · Last checked: 2026-11-24

## Goal

Compute exact Shapley values for two small models from tables of coalition values, check that they add up to the gap they explain, and see what happens to them when the reference (the foil) changes.

## What you need

Paper and pencil, or any spreadsheet. Nothing to install. The models are invented for teaching.

## Background in one paragraph

A coalition is a set of features that take this person's values; all other features take the reference person's values. The table gives the model's output for every coalition. A feature's marginal contribution to a coalition is the change in output when it joins. Its Shapley value is the average of its marginal contributions over all orders in which the features can arrive. With three features there are six orders.

## Part A: A credit risk model (reference 1)

Features: L = a late payment in the last year, U = credit utilization above 80 percent, R = three or more recent credit applications. The applicant has all three. Reference 1 is an applicant with none of them. Outputs are predicted default risk in percent.

| Coalition (features at the applicant's value) | none | L | U | R | L,U | L,R | U,R | L,U,R |
|---|---|---|---|---|---|---|---|---|
| Risk (percent) | 5 | 17 | 9 | 7 | 27 | 19 | 13 | 31 |

1. Write down the six orders (L-U-R, L-R-U, U-L-R, U-R-L, R-L-U, R-U-L). For each order, write each feature's marginal contribution.
   *Checkpoint: in the order L-U-R, the contributions are L +12, U +10, R +4.*
2. Average each feature's six contributions.
3. Check efficiency: the three values must add up to 31 - 5 = 26.
4. Find the interactions in the table: which pairs add more together than the sum of their separate effects? How did the Shapley values share them?

## Part B: The same applicant, a different reference

Reference 2 is an applicant who also has utilization above 80 percent, but no late payment and no recent applications. The model is the same; only the table changes, because "missing" now means "set to reference 2's value".

| Coalition | none | L | U | R | L,U | L,R | U,R | L,U,R |
|---|---|---|---|---|---|---|---|---|
| Risk (percent) | 9 | 27 | 9 | 13 | 27 | 31 | 13 | 31 |

5. Compute the three Shapley values again and check that they add up to 31 - 9 = 22.
6. Which feature's value changed most, and why? Which property of the Shapley value explains U's new value?

## Part C: A hospital triage score with redundant signals

Features: O = oxygen saturation below 92 percent, H = heart rate above 120, A = age over 75. The patient has all three; the reference patient has none. Outputs are a deterioration score from 0 to 100.

| Coalition | none | O | H | A | O,H | O,A | H,A | O,H,A |
|---|---|---|---|---|---|---|---|---|
| Score | 10 | 40 | 25 | 18 | 45 | 48 | 33 | 53 |

7. Compute the Shapley values and check efficiency (53 - 10 = 43).
8. O and H together add less than the sum of their separate effects. How do the Shapley values handle this negative interaction? What would a clinician misread if shown only the three bars?

## Expected results

Part A: L 15, U 8, R 3. Part B: L 18, U 0, R 4. Part C: O 25, H 10, A 8. If yours differ, recheck one order at a time; the most common error is taking a contribution from the wrong column.

## What to hand in

Your three tables of contributions (one per part), the efficiency checks, and three sentences: what changed between Part A and Part B, why it changed, and which reference you would use if the applicant asked "why was I refused when my colleague with the same high utilization was approved?"

## Self-check

- Do your values in every part add up exactly to the gap? If not, one marginal contribution is wrong.
- In Part B, U gets zero because it never changes the output when it joins: the applicant and reference 2 have the same value. This is the dummy property. A feature that is very important to the model can still get zero when the foil shares its value.
- In Part C, the redundancy of -10 points (45 instead of 10 + 30 + 15 = 55) is split equally between O and H. Each bar is smaller than the feature's effect on its own.
