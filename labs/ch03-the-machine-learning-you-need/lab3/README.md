# Lab 3.3: Metrics, Base Rates and Calibration

Chapter 3, The Machine Learning You Need · Run-only notebook · About 50 minutes · Last checked: 2026-11-24 (end-to-end run with the versions below; under 1 minute on a laptop CPU)

## Goal

Read a readmission model's performance the way a validator would: with a metric that respects the base rate, at a threshold someone would actually use, with a calibration check, and by group. The last cell prints the validation section of a model card draft.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, matplotlib 3.10.9 (see `env/requirements.txt`). Or open `metrics_calibration.ipynb` in a hosted notebook service.

## Data

The same Diabetes 130-US Hospitals file as Lab 3.2 (UCI, https://doi.org/10.24432/C5230J, CC BY 4.0). The population follows Strack et al. (2014): first encounter per patient, encounters ending in death or hospice discharge removed (69,990 encounters, 9.0 percent readmitted within 30 days).

## Steps

1. Run the notebook from top to bottom.
2. **Checkpoint 1:** boosted trees reach a test AUC of 0.647 and an average precision of 0.171; logistic regression reaches 0.643 and 0.157. The test prevalence is 0.090.
3. **Checkpoint 2:** at a threshold of 0.5 the model flags 25 of about 21,000 test patients. Flagging the riskiest 10 percent (threshold about 0.148) gives a precision of 0.204 and a recall of 0.227.
4. **Checkpoint 3:** the decile calibration curves follow the diagonal; mean predicted risk equals the observed rate (0.090) for both models.
5. **Checkpoint 4:** after removing half of the readmitted test patients, the base rate is 0.048, the mean predicted risk is still 0.089, and the AUC is 0.649. Ranking survived; calibration did not.
6. **Checkpoint 5:** the AUC by age band ranges from about 0.63 (70 and over) to about 0.66 (50 to 69).
7. Copy the printed validation section into your model card draft.

## Expected results

As listed in the checkpoints, with `random_state=0`. Other library versions may move the numbers in the third decimal.

## Questions

1. Why does the notebook not print accuracy? What accuracy would a model that never predicts readmission achieve here?
2. A care team can call 10 percent of discharged patients. What does a precision of about 0.2 mean for their week? What does a recall of about 0.23 mean for the patients they do not call?
3. Checkpoint 4 changed the base rate but not the model. Which number in a model card would have warned a new hospital, and which would not?
4. The model's AUC is lowest for patients aged 70 and over, who also have the highest readmission rate. Name two possible reasons and one check you would run next.

## What to hand in

The printed validation section, completed by hand with one line on intended use and one on known gaps, plus your answers to the four questions (one page).

## Self-check

Your validation section should name the population, the split, the prevalence, at least two metrics, a calibration statement and at least one gap. If it has only an AUC, it is not yet a validation section.
