# Lab 6.3: Naming Customer Segments with a Surrogate Tree

Chapter 6, The Whole Model at a Glance: Global Explanations · Run-only notebook (one optional section) · About 45 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below, about one minute after the download)

## Goal

Cluster the customers of an online retailer into four segments, explain each segment with a small decision tree trained on the segment labels, and measure fidelity overall and segment by segment. The lab reproduces the segment figure in Chapter 6 and the point of the chapter's From the Field box: a surrogate gives a cluster a name, and fidelity tells you how much of the cluster the name covers.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, openpyxl 3.1.5 (to read the spreadsheet). Or open `segment_surrogate.ipynb` in a hosted notebook service.

## Data

Online Retail II, UCI Machine Learning Repository, donated by Daqing Chen, https://doi.org/10.24432/C5CG6D, license CC BY 4.0 (checked 2026-11-24). Transactions of a UK-based online retailer from December 2009 to December 2011; we use the sheet "Year 2010-2011" (541,910 invoice lines). The notebook downloads the 45 MB zip file once into a temporary folder. We keep lines with a customer number, a positive quantity and price, and no cancellation code.

Known limitations: one retailer, many wholesale customers, about a quarter of lines without a customer number, and a fixed reference date at the end of the sheet. Segments describe this dataset only.

## Steps

1. Open `segment_surrogate.ipynb` and run the cells in order.
2. **Checkpoint 1:** 541,910 lines in the sheet, 397,885 kept, 4,338 customers; median frequency 2 invoices.
3. **Checkpoint 2:** four segments of 652, 1,332, 1,423 and 931 customers. Medians: segment 0 bought 8 days ago, 11 invoices, about 3,983 in spending; segment 1 last bought 212 days ago, once; segment 2 bought 36 days ago, 4 invoices; segment 3 first bought only 49 days ago. Name them before you build a tree (the chapter uses loyal regulars, lapsed one-timers, steady occasional and newcomers).
4. **Checkpoint 3:** depth 2: overall fidelity 0.761, but 0.00 for segment 0; depth 3: 0.879 overall, every segment 0.85 or better; depth 4: 0.896.
5. **Checkpoint 4:** the depth-3 tree splits first on recency at about 104 days, then on tenure (about 90 days) and frequency.
6. Write one sentence per segment from the tree's rules, with its fidelity.
7. Optional: rerun KMeans with `random_state=1` and `2` and check whether names and first split survive.

## Expected results

With scikit-learn 1.7.2 and the seeds in the notebook you should reproduce the numbers above exactly. With other versions, segment numbers may be permuted; the pattern (depth 2 misses the smallest segment, depth 3 describes all four) should hold.

## Questions

1. Why can a tree with four leaves fail to describe one of four segments?
2. Overall fidelity rose from 0.76 to 0.88 between depth 2 and 3. Which number would have hidden the problem if you had reported only one?
3. A manager wants to use the tree's rules to assign new customers. What is the risk, and what would you put next to each rule?

## What to hand in

Four named segment descriptions, each with its rule and fidelity, and a short note on the depth-2 tree's missing segment. If your Dossier system uses clustering, repeat the exercise on it.

## Self-check

If any of your segment descriptions has no fidelity number next to it, add one. If your names changed when you changed the KMeans seed, say so in your note.
