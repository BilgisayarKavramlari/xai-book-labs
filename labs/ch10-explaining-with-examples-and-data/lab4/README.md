# Lab 10.4: Customers Like You on Real Retail Data

Chapter 10, Explaining with Examples and Training Data · Run-only notebook · About 75 minutes · Last checked: 2026-11-24 (end-to-end run in about 15 seconds on a laptop CPU once the data are cached; the first run downloads 45 MB and converts the Excel file in about one minute)

## Goal

Reproduce the data case study of Chapter 10: build an item-based and a user-based recommender on public retail transactions, write the explanation each would show, and test the explanations for faithfulness (is the sentence true for the model that decided?), privacy (how many people stand behind it?) and influence (whose purchases shape everyone else's recommendations?).

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, openpyxl 3.1.5 (to read the Excel file once). Notebook: `customers_like_you.ipynb`. Set the environment variable `XAI_DATA` to choose where the data are cached; by default the notebook uses a folder in your system's temporary directory.

## Data

Online Retail II, UCI Machine Learning Repository, created by Daqing Chen, https://doi.org/10.24432/C5CG6D, license CC BY 4.0 (checked 2026-11-24). 1,067,371 transaction lines of a UK-based, non-store online retailer of all-occasion gift-ware, many of whose customers are wholesalers, from 1 December 2009 to 9 December 2011. Columns: invoice, stock code, description, quantity, invoice date, price, customer ID, country. The notebook removes cancellations (invoices starting with C), lines without a customer ID, non-positive quantities or prices, non-product stock codes and exact duplicate lines.

Known limitations: one retailer, mostly UK customers, many of them businesses rather than consumers; customer IDs are pseudonymous but behavioral records can still identify people and businesses (Chapter 10, Netflix Prize box). Use the data to learn methods; do not attempt to identify any customer.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** 1,067,371 rows from 2009-12-01 to 2011-12-09.
3. **Checkpoint 2:** in the training period (before 1 September 2011), 5,223 customers, 4,255 products bought by at least two customers, and 4,931 customers with at least five distinct products.
4. **Checkpoint 3:** three readable item-based explanations, and for the user-based recommender the distribution 0, 69, 420, 641, 730, 677, 603, 526, 475, 384, 406 of how many of the 10 nearest customers back the recommendation.
5. **Checkpoint 4:** 485 item-based recommendations (9.8 percent) are not bought by any of the customer's 10 nearest customers; 1,718 (34.8 percent) by at most two.
6. **Checkpoint 5:** 489 user-based explanations (9.9 percent) rest on one or two neighbors, 69 on exactly one; 21 countries have five or fewer customers (43 customers).
7. **Checkpoint 6:** removing one of the ten largest buyers changes the top recommendation of between 1.08 and 2.58 percent of other customers; the median for 30 random customers is 0.08 percent.
8. **Checkpoint 7:** for the 2,284 eligible customers who bought again after 1 September 2011, the item-based hit rate is 0.0884, 0.0876 when only product pairs bought by at least five customers are used, and 0.0797 for the user-based recommender.

## Expected results

The counts above are deterministic for the data file and versions listed. The random sample in Checkpoint 6 uses a fixed seed; the book's figure uses a larger sample of 110 random customers (median 0.08 percent).

## Questions

1. Write the explanation you would show customer `el[0]`, and one you would refuse to show. Why?
2. Is a "customers like you" sentence attached to the item-based recommender a lie, a simplification or acceptable marketing? Argue one position with the Checkpoint 4 numbers.
3. Should the largest wholesale buyers be told that their purchases shape other customers' recommendations? What would a data protection officer say?
4. Propose a suppression rule (threshold and fallback text) and state its cost using Checkpoints 5 and 7.

## What to hand in

A one-page disclosure rule for both explanations: thresholds, fallback wording, who may see individual records, and the measured cost of the rule. This page can go straight into the data attribution note of your Explanation Dossier.

## Self-check

If your rule only sets a threshold, add the fallback: a suppressed explanation should be replaced by a reason from the customer's own data, not by nothing.
