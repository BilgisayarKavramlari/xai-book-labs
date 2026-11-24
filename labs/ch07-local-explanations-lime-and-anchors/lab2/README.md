# Lab 7.2: LIME for a Retail Churn Model, and How Far to Trust It

Chapter 7, One Decision at a Time: LIME, Anchors and Local Surrogates · Run-only notebook (one optional cell to edit) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run on the UCI file with the versions below; about 1.5 minutes on a laptop CPU after the first download)

## Goal

Build a customer churn model from public retail transactions, explain individual customers with LIME (by hand and with the `lime` package), and test those explanations for local fidelity, stability, sensitivity to the kernel width and off-manifold sampling. This lab reproduces the data case study of Chapter 7.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9 (see `env/requirements.txt`), plus:

- `lime==0.2.0.1` (the reference implementation by the method's authors, BSD license; last release June 2020, checked 2026-11-24)
- `openpyxl==3.1.5` (to read the Excel file once)

Note on the version pin: to count impossible samples (Checkpoint 6), the notebook calls the package's own tabular sampler through a private method (`_LimeTabularExplainer__data_inverse`). It works with lime 0.2.0.1; a future release could rename it, so keep the pin.

Install with `pip install lime==0.2.0.1 openpyxl==3.1.5`. Or open `lime_retail_churn.ipynb` in a hosted notebook service and install the same two packages in its first cell.

## Data

Online Retail II, UCI Machine Learning Repository, Chen (2012), https://doi.org/10.24432/C5CG6D, license CC BY 4.0 (checked 2026-11-24). 1,067,371 invoice lines from a UK-based, non-store online retailer of gift items, many of whose customers are wholesalers, from 1 December 2009 to 9 December 2011. Invoice numbers starting with "C" are cancellations; this lab treats them as returns.

The notebook downloads the zip file (about 45 MB) from UCI once into a temporary folder and caches a compressed CSV there. If you are offline, put `online_retail_II.xlsx` next to the notebook.

**How the churn table is built.** Cutoff date 2011-06-09. Customers: the 4,335 with at least one purchase in the 12 months before the cutoff (rows without a customer ID are dropped). Nine features from history before the cutoff: `recency_days`, `tenure_days` (days since first purchase in the data, so it is capped at about 550 days by the start of the data), `orders_12m`, `spend_12m`, `avg_order_value`, `products_12m`, `orders_90d`, `return_share` (value returned divided by value bought plus returned, 12 months) and `uk`. Label: `churn = 1` if no purchase in the 183 days after the cutoff.

Known limitations: one retailer, mostly wholesale customers, 2009 to 2011; "churn" is defined by us, not by the retailer; cancellations are not all customer returns; tenure is censored at the start of the data. Use the data to learn methods, not to draw conclusions about real customers.

## Steps

1. Open `lime_retail_churn.ipynb` and run the cells in order.
2. **Checkpoint 1:** 824,364 transaction lines with a customer ID, 4,335 customers, churn rate 0.427. Real data never has a last order before the first, or more orders in 90 days than in 12 months.
3. **Checkpoint 2:** test AUC 0.784 for boosted trees and 0.787 for a logistic regression on log-transformed features.
4. **Checkpoint 3:** LIME by hand for customer 16027 (model probability 0.511): the surrogate's intercept is about 0.30, and the largest slopes are on orders, products and spend.
5. **Checkpoint 4:** the `lime` package for the same customer: surrogate prediction 0.344, weighted R squared 0.125; top weights `orders_12m > 4.75` (-0.118) and `31.00 < recency_days <= 106.00` (-0.078), both toward staying.
6. **Checkpoint 5:** mean top-3 Jaccard over 30 seeds, at 250 / 1,000 / 5,000 samples: 16027: 0.47 / 0.72 / 0.91; 14933: 0.63 / 0.72 / 0.88; 17726: 0.56 / 0.77 / 0.91; 14203: 0.62 / 0.63 / 0.68.
7. **Checkpoint 6:** for customer 14203, 14.8 percent of LIME's 5,000 samples have a last order before the first, 21.9 percent have more orders in 90 days than in 12 months, 33.6 percent break at least one rule.
8. **Checkpoint 7:** kernel width 0.5 keeps the same three features but shrinks the weights to about a third and drops R squared to 0.06; widths from 1 to 20 give nearly identical results.
9. Optional: pick a customer near the threshold from the list in the last cell and repeat sections 4 to 7.

## Expected results

The numbers above come from scikit-learn 1.7.2 and lime 0.2.0.1 with the seeds in the notebook. Other versions may move individual weights in the third decimal and Jaccard values by a few hundredths; the pattern (low fidelity, agreement rising with samples except for the single-order buyer, a third of samples impossible) should hold.

## Questions

1. Customer 16027's top two LIME reasons point toward staying. Explain, using the bins and the surrogate's prediction, how that can happen when the model predicts churn.
2. Why does more sampling not fix customer 14203's instability? What would you change in the features to fix it?
3. Which of the four customers' explanations would you allow an agent to read aloud, and with what wording? Use your stability and fidelity numbers.
4. The logistic regression is as accurate as the boosted model. Argue for or against switching models in this setting.

## What to hand in

The stability table from Checkpoint 5, the off-manifold shares from Checkpoint 6, and a half-page judgment answering Question 3. This goes into the local explanation set of your Explanation Dossier.

## Self-check

If your judgment quotes a LIME weight without the model's prediction, the surrogate's prediction and the fidelity next to it, reread Checkpoint 4. If you allowed a reason that changed between seeds, reread Checkpoint 5.
