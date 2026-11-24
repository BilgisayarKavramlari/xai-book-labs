# Lab 25.2: Explanation Drift in a Demand Forecast

Chapter 25, Explainability in Production · Code notebook (run, read and answer; no code needs to be written) · About 45 minutes · Last checked: 2026-11-24 (executed end to end on a laptop CPU in under a minute with a local compressed copy of the data)

## Goal

Reproduce the chapter's case study: watch a weekly demand forecast for 64 weeks with three monitors (input drift, attribution drift, error), find a simulated stale feature with loss attribution, and compare the explanations of a retrained model with the launch model's. The notebook reproduces Figures 25.3 to 25.5.

## Tools and versions

`explanation_drift_demand_forecast.ipynb`, Python 3.10, the main environment in `env/requirements.txt`: numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, matplotlib 3.10.9, shap 0.49.1 (TreeExplainer), openpyxl 3.1.5 (to read the Excel file). Jupyter kernel used for the check run: `xai-lab-venv`.

## Data

Online Retail II, UCI Machine Learning Repository, Chen (2012), https://doi.org/10.24432/C5CG6D, license CC BY 4.0 (checked 2026-11-24). 1,067,371 invoice lines from a UK-based online retailer of gift items, many of whose customers are wholesalers, 1 December 2009 to 9 December 2011. The notebook downloads the zip file (about 45 MB) once into a temporary folder, or reads the file named in the environment variable `ONLINE_RETAIL_II` (`.xlsx` or a `.csv.gz` export).

**How the table is built.** Cancellations (invoices starting with "C"), zero quantities and zero prices are removed. Weeks run Monday to Sunday; the last, partial week is dropped. Products sold in at least 70 of the 105 full weeks are kept (1,061). Features at the end of week *t*: log(1 + units) last week and two weeks ago, 4-week and 12-week rolling means of log units, log(1 + distinct customers), median price over the 12-week rolling median, log of all store invoices that week, and the month of week *t* + 1. Target: log(1 + units) in week *t* + 1. Customers are counted only where the customer ID is known.

**Known limitations.** One retailer, 2009 to 2011, mostly wholesale; weekly demand of single products is noisy (training error 0.84 log units, a typical factor of about two). The stale-feature bug is simulated. Use the data to learn methods, not to judge the retailer.

## Steps

1. Run all cells in order.
2. **Checkpoint 1:** 1,061 products; 97,612 product-weeks.
3. **Checkpoint 2:** 28,647 training rows (forecast weeks 22 February to 23 August 2010); training MAE 0.839; reference shares: 4-week average 0.378, last week 0.165, customers 0.164, 12-week average 0.125, two weeks ago 0.068, store orders 0.052, month 0.033, price 0.014; alarm threshold 0.107.
4. **Checkpoint 3:** 12 of 64 weeks flagged; 9 with store orders below the training minimum (279); store-orders share 0.101 to 0.161 in flagged weeks; 14 weeks with at least one PSI alarm; MAE 1.126 in flagged weeks, 0.891 in the others, 0.787 in November 2010.
5. Answer Question A.
6. **Checkpoint 4:** with the stale feature, from October 2011: PSI 0.052, attribution share 0.349 (healthy 0.394), loss attribution 0.129 (healthy 0.311), MAE 0.971 (healthy 0.830).
7. Answer Question B.
8. **Checkpoint 5:** MAE 0.922 (launch) and 0.923 (retrained) on 18,037 product-weeks; 4-week average share 0.364 to 0.276, last week 0.157 to 0.229; top reason changed for 31.3 percent; the largest single move is from the 4-week average to last week's units (3,126 product-weeks).
9. Answer Question C.

## Expected results

All numbers above are reproducible with the pinned versions and seeds (the model uses `random_state=0`; the permutation loss uses NumPy seed 0). Small differences in the third decimal are possible with other library versions.

## What to hand in

The three monitoring results with answers to Questions A to C, and a half-page monitoring plan: which monitors, thresholds and how you set them, who is alerted, and what they do.

## Self-check

- Can you explain why the frozen feature does not change its PSI or its attribution share?
- Can you explain why two models with the same error give different top reasons, and why that is not a bug?
- Which of your monitors needs labels, and how long would it take to fire in a business with 90-day outcomes?
