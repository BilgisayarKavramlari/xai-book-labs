# Lab 26.3: A Screening Score Is a Rank

Chapter 26, Casebook: Explainability Across Industries · Code notebook (run, read and answer; no code needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in a few seconds)

## Goal

Turn a synthetic screening model's probabilities into a 1 to 20 score in which each value holds 5 percent of child-referrals, show the maximum score per referral, apply a default screen-in above 17, and measure what the screener's number hides. The design follows the published description of the Allegheny Family Screening Tool, Version 2 (Vaithianathan et al., 2019), the chapter's public sector case.

## Tools and versions

`screening_score_rank.ipynb`, Python 3.10, the main environment in `env/requirements.txt`: numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2. Jupyter kernel used for the check run: `xai-lab-venv`.

## Data

12,000 synthetic referrals (about 30,000 child-referrals) generated in the notebook. Two synthetic groups, A and B, have the same distribution of unobserved need but differ in how often their households appear in public-system records. **The data are invented to illustrate a mechanism; they describe no real place, population or tool, and the group differences are a property of the simulation.**

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** group B households carry jail and public behavioral health records about twice as often as group A (about 0.31 and 0.61 against 0.15 and 0.30); outcome rates are about 0.108 and 0.096.
3. **Checkpoint 2 (Table 1):** score bands 1 to 19 are each under about 2 percentage points wide; score 20 spans about 23 points (predicted probability from about 0.18 to 0.41).
4. **Checkpoint 3 (Table 2):** share flagged for default screen-in, on each child's own score: about 0.12 (A) and 0.19 (B); on the maximum score per referral: about 0.16 (A) and 0.24 (B).
5. **Checkpoint 4 (Table 3):** for the highest-scoring referral, prior referrals contribute most to the log-odds, followed by a child under five and the two household records.

## Expected results

The tables above, reproducible with the fixed seeds. Note that the train and test split is by referral, so siblings never fall on both sides, the error the Allegheny Version 2 report corrected in Version 1.

## What to hand in

Tables 1 to 3 and a draft of the screen a call screener should see for the highest-scoring referral: the score, its probability band, the top reasons, and one sentence on what the reasons do not show.

## Self-check

- Why does taking the maximum over children raise the share flagged more for larger households?
- In this simulation need is identical across groups. Where does the gap in Table 2 come from, and could a screener see it from the score alone?
- Which local reasons in Table 3 can a family change, and which can it never change?
