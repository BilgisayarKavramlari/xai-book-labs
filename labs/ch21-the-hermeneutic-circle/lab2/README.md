# Lab 21.2: Auditing HermAI 0.1.8

Chapter 21, The Hermeneutic Circle · Run-only notebook (one written task at the end) · About 40 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below; under 10 seconds on a laptop CPU)

*Disclosure: the author of the book develops and maintains HermAI. The lab audits the released version exactly as published.*

## Goal

Apply to HermAI the checks you would apply to any explainer, on the refused applicant of the chapter's case study: which sampler an import gives you, whether its evidence could exist, whether its sentences pass the on-horizon claim test under the reading a credit officer would use, how many features its counterfactual changes, how it varies between runs, and how well its general explainer imitates the model.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9 (see `env/requirements.txt`), plus **hermai 0.1.8** (released on PyPI on 2025-10-02; MIT license; it installs seaborn, 0.13.2 in our run). Install with `pip install hermai==0.1.8`, then run `pip check`. The notebook `hermai_audit.ipynb` imports the helper module `../lab3/hct_mini.py` (data, model, horizon and claim test), so keep the folder structure.

## Data

German Credit (Statlog), from OpenML (`credit-g`); see `data/german-credit.md` for source, license (CC BY 4.0 as listed by UCI) and limitations. Categorical attributes are integer-coded (sorted labels) because HermAI 0.1.8 standardizes every column.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** test AUC 0.787; 0.92 of real test records inside the horizon.
3. **Checkpoint 2:** the package-level `TabularPerturbationGenerator` comes from `hermai.perturbations.tabular_generator` (independent noise of a quarter standard deviation), the README path from `hermai.perturbations.tabular` (noise from a quarter of the covariance); they are different classes, and neither takes a seed.
4. **Checkpoint 3:** predicted risk 0.668; the narrative says `checking_status` and `purpose` *decrease* the probability and `duration` *increases* it; the counterfactual changes 12 features, several to impossible values (13.16 months, 3.98 installment rate, 2.13 existing credits, 1.96 dependents).
5. **Checkpoint 4:** 0.946 of the evidence is close to real records by distance, none respects the integer scales, so Horizon Plausibility is 0.
6. **Checkpoint 5:** all three narrative sentences pass the literal slope reading and fail the natural (contribution) reading; for `checking_status` the on-horizon effect is +0.130.
7. **Checkpoint 6:** over five random states, mean Jaccard of the top-3 sets 0.65 and sign agreement 1.0.
8. **Checkpoint 7:** the depth-3 general explainer agrees with the forest on 0.807 of test decisions.
9. **Your turn:** rewrite the narrative (see the last cell).

## Expected results

The numbers above come from the versions listed and the seed 77 used for this applicant in Lab 21.3. HermAI 0.1.8 draws from NumPy's global random state, so another seed gives a different narrative and counterfactual; the pattern (fractional evidence, slope sentences that contradict contributions, counterfactuals that change most features) should hold. These findings agree with the self-audit in Seker (2026), *Machine Learning and Knowledge Extraction* 8(11), 381, https://doi.org/10.3390/make8110381, Section 5.9.

## Questions

1. Why does a slope on an integer code of a category (for example `purpose`) carry no meaning, and what should a narrative say instead?
2. The narrative is stable across runs for `checking_status` but wrong. What does that teach about stability as a test?
3. The narrative calls 66.83 percent the "confidence" of class 1. Read `LocalExplanation.narrative` in the library: what would it print for an applicant predicted class 0?

## What to hand in

Your rewritten three-sentence narrative (contributions, category names, each sentence passing the claim test) and one sentence describing a counterfactual you would accept for Kofi. Add both to Dossier artifact 21.

## Self-check

If your rewritten narrative says that Kofi's checking account "decreased" his risk, rerun Section 4: the measured effect is +0.130. If your counterfactual changes more than three features or uses fractional months, it fails the horizon.
