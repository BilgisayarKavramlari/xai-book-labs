# Lab 7.3: Anchors, Ceteris Paribus Profiles and a Local Explanation Set

Chapter 7, One Decision at a Time: LIME, Anchors and Local Surrogates · Notebook with one cell to edit · About 75 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below; about 3 minutes on a laptop CPU after the first download)

## Goal

Explain the same retail customers as in Lab 7.2 with anchors and ceteris paribus profiles, check whether anchors depend on the random seed, and assemble a five-decision local explanation set with a stability check: the Chapter 7 artifact of your Explanation Dossier.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9 (see `env/requirements.txt`), plus:

- `anchor-exp==0.0.2.0` (the Anchors implementation by the method's authors, BSD license; last release September 2020; it installs `lime` and `spacy` as dependencies)
- `lime==0.2.0.1`
- `openpyxl==3.1.5`

Install with `pip install anchor-exp==0.0.2.0 lime==0.2.0.1 openpyxl==3.1.5`.

Alternative: Alibi also implements Anchors (`AnchorTabular`). As of 2026-11-24 its latest release, 0.9.6, requires numpy below 2.0 and is distributed under the Business Source License 1.1 (since version 0.9.5, January 2024); check the license terms before using it in a commercial setting.

## Data

Online Retail II (Chen, 2012), UCI Machine Learning Repository, https://doi.org/10.24432/C5CG6D, CC BY 4.0. The customer table and model are rebuilt exactly as in Lab 7.2; see that lab's README for the definitions and limitations. The download is cached, so if you ran Lab 7.2 on the same machine the data load in seconds.

## Steps

1. Open `anchors_profiles_explanation_set.ipynb` and run sections 1 and 2.
   *Checkpoint: 4,335 customers, AUC 0.784 and 0.787, as in Lab 7.2.*
2. **Section 3, anchors.** For customer 14203 the anchor grows from `recency_days > 212.75` (precision 0.686, coverage 0.242) to three conditions with precision 0.957 and coverage 0.081. For customer 16027 four conditions reach only 0.847: there is no anchor at the 0.95 threshold.
3. **Section 4, seeds.** Run the anchor search for customer 14203 with seeds 0 to 4. The first two conditions are always the same; the third is `products_12m <= 16.00` with seed 0 and `tenure_days <= 364.00` with seeds 1 to 4, with precision between 0.957 and 0.989.
4. **Section 5, profiles.** For customer 16027 the profiles span 0.300 to 0.873 (recency), 0.281 to 0.538 (products), 0.250 to 0.511 (return share) and 0.089 to 0.764 (orders). The customer's return share, 0.192, is above the 95th percentile of the training data (0.099).
5. **Section 6, your explanation set.** Replace the list `chosen` with five customers of your own, chosen by a rule you state in a markdown cell. Run the cell; it records each customer's probability, LIME top three, LIME fidelity, top-3 Jaccard over 20 seeds (2,500 samples each), and the anchor with its precision and coverage. With the default list, Jaccard ranges from 0.67 (customer 14203) to 1.00 (customer 12347).
6. Add one sentence per customer that an agent could say aloud, and mark it *safe to read* or *do not read*.

## Expected results

The numbers above come from the versions listed, the seeds in the notebook and the default customer list. Anchor precisions are estimated by sampling and can move by about 0.01 with other versions. The pattern should hold: short, precise anchors for confident predictions; long or failed anchors near the threshold; profiles that reveal effects LIME's bins understate.

## What to hand in

The explanation set table (saved by the notebook as `local_explanation_set.csv`) with your five agent sentences and safe or not-safe marks, plus one paragraph on where LIME, the anchor and the profiles agreed or disagreed for each customer. This is Dossier artifact 7 (see the Portfolio Assignment in Chapter 7 and `portfolio/`).

## Self-check

- Did you state your selection rule before looking at the explanations?
- For every sentence marked safe, is the reason in the top three in most seeds, consistent with the anchor or a profile, and something the customer would recognize?
- For every sentence marked not safe, did you say which test it failed?
