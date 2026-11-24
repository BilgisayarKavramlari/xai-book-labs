# Lab 1.2: Reason Codes from a Scorecard

Chapter 1, Why Explain a Machine? · Run-only notebook (no code to write) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run on OpenML credit-g with the versions in `env/requirements.txt`)

## Goal

Build a small points-based scorecard on a public credit dataset, then produce the top two reasons for five low-scoring applicants. You will see why reason codes are easy on an additive model, and what they leave out.

## Tools and versions

Python 3.10 or later, pandas, scikit-learn (see `env/requirements.txt`). Or open `reason_codes.ipynb` in a hosted notebook service.

## Data

German Credit (Statlog), 1,000 applicants, 20 attributes and a good or bad credit label, loaded from OpenML (`credit-g`). Data card: `data/german-credit.md`. The notebook uses seven attributes: checking account status, loan duration, credit history, credit amount, savings, employment length and age.

## Steps

1. Open `reason_codes.ipynb` and run the cells in order.
2. **Checkpoint 1:** the scorecard table lists points for each band of each feature; the worst band of every feature has 0 points.
3. **Checkpoint 2:** the notebook prints five applicants from the lowest 30 percent of total points (an invented cutoff for the lab), each with two reasons and the number of points below the maximum.
4. Copy the reasons for the five applicants into your write-up.

## Expected results

With the pinned versions and `random_state=0`, the scorecard gives the highest points to "no checking" account status (43), loan durations up to 12 months (32) and the credit history band "critical/other existing credit" (55). The five listed applicants have totals between 38 and 80 points, and their reasons come from checking account status, loan duration and credit history. Small differences in points can appear with other library versions; the pattern should hold.

Notice one oddity: the band labeled "critical/other existing credit" earns the most points and "all paid" earns none. This is a known feature of the German Credit data: the applicants in the file were already selected by the lender, so the labels reflect who was granted credit, not the whole population. A scorecard faithfully reproduces whatever its data say, including patterns a credit officer would call backwards. Keep this in mind for Question 4.

## Questions

1. For each reason, could the applicant change it? Which reasons describe something the applicant cannot change (for example age)? What does that mean for an adverse action notice?
2. The notebook ranks reasons by points below the best band. Another convention ranks by points below the average applicant. Would that change the ranking for any of your five applicants? Why might a lender prefer one convention? (Chapter 8 returns to this as the choice of a background.)
3. The scorecard uses age. Is that acceptable in your jurisdiction for credit decisions? Note what you find and its date.
4. The reason "credit_history" for an applicant whose history is "all paid" would be faithful to the scorecard. Would it be a sensible thing to tell the applicant? What does this say about the difference between faithful and useful?

## What to hand in

A one-page table of the five applicants' reasons, your answers to the three questions, and two sentences on what the reasons do not tell the applicant.

## Self-check

You should find at least one reason that the applicant cannot act on. If all your reasons are actionable, look again at the features in the scorecard.
