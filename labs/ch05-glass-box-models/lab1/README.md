# Lab 5.1: Edit a Glass Box in the Browser

Chapter 5, Glass-Box Models: Accuracy You Can Read · No code · About 45 minutes · Last checked: 2026-11-24 (demo opened and the Lending Club model inspected in a desktop browser)

## Goal

Read the shape functions of an additive model (an Explainable Boosting Machine) trained on consumer loans, find shapes you would question, edit one, and see what the edit does to the model's accuracy. Then use a published clinical risk score, 2HELPS2B, by hand on five invented cases.

## Tools and versions

- GAM Changer, a free web demo from the InterpretML project (Wang et al., 2022, KDD), at https://interpret.ml/gam-changer/ . It runs entirely in the browser; nothing is uploaded and no account is needed. As of 2026-11-24 the demo offers four models: Iowa House Price, Lending Club, Census Income and "My Model" (your own file). This lab uses **Lending Club**.
- A wide browser window (at least about 1,200 pixels). In a narrow window the chart is cropped.
- Paper and pen, or a spreadsheet, for Part B.

If the demo has moved or changed, the book's tools page in `tools/` says what replaced it; the code in the GAM Changer repository (MIT license) can also be run in a notebook.

## Data

Part A: the demo's built-in Lending Club model (peer-to-peer consumer loans). As of the date above, the model has 18 single-feature terms (for example `fico_score`, `dti`, `annual_inc`, `loan_amnt`, `revol_util`, `term`, `home_ownership`, `purpose`) and 10 pairwise terms, and its panel reports metrics on 2,000 validation samples (ROC AUC 0.6933, accuracy 0.664 before any edit). The demo does not document the exact label definition on its main page; Step 2 asks you to work out what is predicted.

Part B: five invented EEG summaries (below). They are made up for teaching and describe no real patient.

## Part A: read and edit (about 30 minutes)

1. Open the demo and click **Lending Club** under "Choose a model". The chart shows one shape function at a time; the drop-down at its top left lists the terms with an importance number after each name. The right panel shows Metrics (accuracy, balanced accuracy, ROC AUC, confusion matrix), Feature (the distribution of the feature) and History (your edits).
2. **Checkpoint 1: what is predicted?** Select `fico_score`. The curve rises from left to right. A higher FICO score usually means lower credit risk. Decide whether the model's positive outcome is "good" (for example, loan paid) or "bad" (for example, charged off), and write one sentence with your reasoning. Check your guess against the confusion matrix: which class is the majority?
3. **Checkpoint 2: rank the terms.** From the drop-down, list the five terms with the highest importance numbers. As of the check date, `term`, `fico_score`, `dti`, `home_ownership` and `loan_amnt` were the top five.
4. **Checkpoint 3: question three shapes.** Look through the continuous terms (`dti`, `annual_inc`, `revol_util`, `loan_amnt`, `open_acc`, `revol_bal`, `earliest_cr_line`). For each, look at the density bars under the curve. Find three places where the curve does something you would not expect from credit knowledge, such as a dip in a region where higher values should mean higher risk, or a jump at the far end of the data. For each, note the feature, the range, how many applicants lie there (from the density bars), and whether you think it is real, noise or a sign of something else in the data.
5. **Checkpoint 4: make one edit.** Click **Select** at the top of the chart and drag a box around the region you questioned most. A small toolbar appears above the selection. Its buttons include making the selected region monotone increasing or monotone decreasing (the tool fits an isotonic regression weighted by the bin counts), interpolating between the ends, aligning, and deleting; you can also type a score. Apply the edit that matches your domain view.
6. **Checkpoint 5: measure it.** In the Metrics panel, compare the "origin", "last" and "current" values of ROC AUC and accuracy. Write down the change. Open the History panel and type a one-line reason for your edit. Use undo if you want to try a different edit.

## Part B: score five patients by hand (about 15 minutes)

2HELPS2B (Struck et al., 2017, *JAMA Neurology*) gives 1 point each for: a periodic or rhythmic pattern faster than 2 Hz; sporadic epileptiform discharges; lateralized periodic discharges, lateralized rhythmic delta activity or bilateral independent periodic discharges; "plus" features; a prior seizure (remote or recent). It gives 2 points for brief ictal rhythmic discharges (BIRDs). The published risk for each total is: 0 points about 5 percent, 1 point 12 percent, 2 points 27 percent, 3 points 50 percent, 4 points 73 percent, 5 points 88 percent, 6 or more above 95 percent.

This is a teaching exercise. The score is used by trained EEG readers with a standard terminology; nothing here is clinical advice.

| Case | Invented EEG and history summary |
|---|---|
| A | No seizure history. Sporadic epileptiform discharges. No periodic or rhythmic patterns. No BIRDs. |
| B | History of epilepsy. Lateralized periodic discharges at 1.5 Hz with superimposed fast activity ("plus"). No sporadic discharges. No BIRDs. |
| C | No seizure history. Diffuse slowing only. None of the score's findings. |
| D | No seizure history. Lateralized rhythmic delta activity at 2.5 Hz. BIRDs present. No sporadic discharges. |
| E | Recent suspected seizure. Sporadic epileptiform discharges. Bilateral independent periodic discharges at 2.5 Hz with "plus" features. BIRDs present. |

**Checkpoint 6:** for each case, write the items that score, the total and the risk band.

## Expected results

Part A: the edit you make will usually change the ROC AUC in the third decimal place or less; a large drop means the region you edited holds many applicants or the edit contradicted a strong pattern in the data. Part B: see the self-check below.

## What to hand in

1. Your answer to Checkpoint 1 (what is predicted, and how you know).
2. A table of the three questioned shapes (feature, range, number of applicants, your judgment).
3. Your edit: the region, the tool used, the metric change and the reason you recorded.
4. The five 2HELPS2B scores with their risk bands, and one sentence on which item you found hardest to score from a written summary.

## Questions

A. Your edit changed the model's behavior. Who in a lender should be allowed to make such an edit, and what should the record contain?

B. A shape function that dips in a region with very few applicants: would you edit it, constrain the whole feature to be monotone, or leave it and warn users? Give one reason for each choice.

## Self-check

Part B totals: A = 1 (12 percent); B = 3 (prior seizure, lateralized periodic discharges, plus; the 1.5 Hz pattern does not earn the frequency point; 50 percent); C = 0 (5 percent); D = 4 (lateralized rhythmic delta activity, faster than 2 Hz, BIRDs worth 2; 73 percent); E = 7 (all items; above 95 percent). If your B scored 4, check the frequency item.
