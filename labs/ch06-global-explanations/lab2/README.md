# Lab 6.2: A Global Explanation Report for a Claims Frequency Model

Chapter 6, The Whole Model at a Glance: Global Explanations · Run-only notebook (one optional section to write) · About 75 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below, a few minutes on a laptop CPU)

## Goal

Train a Poisson gradient-boosted model on French motor insurance policies and produce its global explanation: permutation and leave-one-feature-out importance (with a correlated group), partial dependence and ICE, accumulated local effects, Friedman's H-statistic and a surrogate tree with fidelity overall and by leaf. This lab reproduces the data case study and all figures of Chapter 6.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, matplotlib 3.10.9 (see `env/requirements.txt`). Or open `global_report.ipynb` in a hosted notebook service. Other scikit-learn versions can move the third decimal of the numbers below; the patterns should hold.

## Data

freMTPL2freq, French motor third-party liability policies, OpenML data_id 41214 (https://www.openml.org/d/41214), 678,013 rows, licence listed on OpenML as CC0 (checked 2026-11-24). The original source is the CASdatasets R package by Dutang and Charpentier (https://github.com/dutangc/CASdatasets, GPL >= 2). A detailed actuarial case study on the same data: Noll, Salzmann and Wuthrich (2018), https://doi.org/10.2139/ssrn.3164764. The notebook downloads the data once (about 15 seconds) into a temporary folder. We cap claim counts at 4 and exposure at 1 year, which affects very few policies.

Known limitations: one insurer and period; frequency only (no claim amounts); a pocket of short, high-frequency policies for new vehicles of one brand whose origin the data do not explain. Use the data to learn methods, not to set real prices.

## Steps

1. Open `global_report.ipynb` and run the cells in order.
2. **Checkpoint 1:** 678,013 policies; 0.101 claims per policy-year; 95.0 percent of policies without a claim; test Poisson deviance 0.5710 for the model against 0.6220 for a constant rate.
3. **Checkpoint 2:** permutation importance (increase in deviance): bonus-malus 0.0409, vehicle age 0.0400, brand 0.0190, driver age 0.0119. LOFO: vehicle age 0.0214, bonus-malus 0.0189; population density 0.0000.
4. **Checkpoint 3:** area code and density together: permutation 0.0054, LOFO 0.0011; the crosstab shows each area code inside a narrow density band.
5. **Checkpoint 4:** PDP for driver age 0.231 at 18 and 0.108 at 30; for bonus-malus 0.091 at 50, 0.251 at 100, 0.452 at 150. Centered ICE at 18: 10th percentile about +0.01, 90th about +0.25.
6. **Checkpoint 5:** correlation of driver age and bonus-malus -0.48; of 11,253 drivers aged 18 to 21, 4.7 percent at bonus-malus 60 or below; young-driver effect at 18: ALE +0.059, PDP +0.116.
7. **Checkpoint 6:** H-statistic: brand x fuel 0.768 at the top; every one of the top four pairs involves brand; driver age x bonus-malus 0.263. Rerun with another sample as the notebook suggests.
8. **Checkpoint 7:** surrogate fidelity by depth 0.262, 0.467, 0.588, 0.678, 0.737, 0.781, 0.811, 0.831; the depth-3 tree splits on bonus-malus, vehicle age, brand B12 and driver age.
9. **Checkpoint 8:** leaf by leaf, the new-B12 leaf leaves the most variance (about 0.56 on the log scale), the leaf for new vehicles of other brands the least (about 0.06).
10. Optional: test whether your three main claims survive another split and a smaller model.

## Expected results

The numbers above come from scikit-learn 1.7.2 with `random_state=0` for the split and the model. The H-statistic is the least stable; a different sample of 300 policies changes the order of the weaker pairs.

## Questions

1. Why is LOFO for density zero while its permutation importance is not? Which number would you give an actuary who wants to drop a rating factor?
2. Where in the age and bonus-malus plane is the PDP evaluating the model on almost no data? What does ALE do instead?
3. What did the H-statistic lead you to find in the data, and what would you ask the data owners?
4. Would you quote the depth-3 surrogate's rules to a pricing committee? Under what conditions?

## What to hand in

A two- to three-page global explanation report: model and data, importance (with the density group), shape (PDP and ALE for driver age), interactions (with the B12 finding as an open question), surrogate with fidelity, and a section on what the report does not show. Use the numbers from your own run. This is the Chapter 6 artifact of your Explanation Dossier if you use the claims model as your system.

## Self-check

If your report says "density does not matter", reread Checkpoint 3. If it describes any effect as a cause, rewrite that sentence as a statement about the model.
