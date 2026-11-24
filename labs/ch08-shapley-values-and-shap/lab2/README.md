# Lab 8.2: SHAP for a Credit Card Default Model

Chapter 8, Shapley Values and SHAP · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run on the UCI file with the versions below; about 30 seconds on a laptop CPU)

## Goal

Train a gradient-boosted default model on a public credit card dataset, explain flagged customers with exact interventional TreeSHAP values, and measure how much the choice of background (the foil) changes the reasons. This lab reproduces the data case study of Chapter 8.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, shap 0.49.1 (with numba 0.68.1), xlrd 2.0.2 (to read the .xls file). shap 0.49.1 is the last release for Python 3.10; newer releases need Python 3.11 or 3.12. Or open `shap_credit_default.ipynb` in a hosted notebook service and install shap and xlrd first.

## Data

Default of Credit Card Clients, UCI Machine Learning Repository, https://doi.org/10.24432/C55S3H, license CC BY 4.0 (checked 2026-11-24). Donated in 2016 by I-Cheng Yeh; introduced by Yeh, I.-C., and Lien, C.-H. (2009), *Expert Systems with Applications* 36(2), 2473-2480, https://doi.org/10.1016/j.eswa.2007.12.020. 30,000 credit card customers in Taiwan; payment history April to September 2005; 23 features; target `default payment next month` (22.12 percent positive).

The notebook downloads the zip file from UCI once into a temporary folder. If you are offline, put `default of credit card clients.xls` next to the notebook.

Known limitations: data from one country and one period (2005); the repayment status fields contain the values -2 and 0, which the documentation does not define (it documents -1 = paid duly and 1 to 9 = months of delay); demographic fields (sex, education, marital status, age) are coarse. Use the data to learn methods, not to draw conclusions about real lending.

The book plan first proposed the FICO HELOC dataset. Its usage terms require an agreement with FICO that could not be verified for redistribution or use without an account, so this openly licensed dataset is used instead.

## Steps

1. Open `shap_credit_default.ipynb` and run the cells in order.
2. **Checkpoint 1:** 30,000 rows, 25 columns, default rate 0.2212.
3. **Checkpoint 2:** test AUC 0.775; the riskiest 20 percent (threshold 0.332) are flagged: 1,500 customers, 56.2 percent of whom defaulted.
4. **Checkpoint 3:** for Mei (test row 7), base value -1.484 (risk 18.5 percent), her log-odds 0.560 (risk 63.7 percent); `PAY_0` contributes +1.932.
5. **Checkpoint 4:** setting her September status to "paid duly" lowers her log-odds by 2.395, not by 1.932.
6. **Checkpoint 5:** Daniel's (test row 75) top reason is `PAY_2` against all customers and `PAY_0` against customers who repaid.
7. **Checkpoint 6:** over 300 flagged customers, the top reason differs between the two backgrounds for 15.3 percent; top-three Jaccard 0.842 (A vs B) and 0.792 (A vs path-dependent); five random backgrounds give identical top-three sets in 73.9 percent of pairs.
8. **Checkpoint 7:** global ranking led by `PAY_0` (0.431); grouped repayment statuses 0.684.
9. **Checkpoint 8:** flag rates 0.215 for men and 0.190 for women, although sex is not an input.

## Expected results

The numbers above come from scikit-learn 1.7.2 and shap 0.49.1 with the fixed random seeds in the notebook. Other versions can move them slightly; the pattern (one feature dominating Mei, the top reason moving with the background for about one flagged customer in six) should hold.

## Questions

1. Which background would you use for the review officers, and which for a notice sent to a customer? Why?
2. Why is the SHAP value of `PAY_0` for Mei not equal to the change in her log-odds when `PAY_0` is set to -1?
3. The bill amounts are highly correlated. What happens to their individual SHAP values, and how would you report them?
4. Sex has a SHAP value of zero for every customer. What does that tell you about fairness, and what would you check instead?

## What to hand in

The output of the last cell (five flagged customers, top three reasons under backgrounds A and B), the share of flagged customers whose top reason changed, and one paragraph on the background you would use for an adverse-action style notice and why. This goes into the SHAP analysis of your Explanation Dossier (artifact 8).

## Self-check

If you report a SHAP value without naming its background, reread Section 4 of the notebook. If you wrote that Mei's risk would fall by 1.932 log-odds had she paid on time, reread Section 3.
