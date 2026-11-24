# Lab 3.2: A Leakage Hunt in Hospital Readmission Data

Chapter 3, The Machine Learning You Need · Run-only notebook (one optional cell to write) · About 60 minutes · Last checked: 2026-11-24 (end-to-end run on the UCI file with the versions below; about 1 minute on a laptop CPU)

## Goal

Train a 30-day readmission model on a public hospital dataset, plant the kind of leak that feature engineering often creates, and use a simple global explanation (permutation importance) to find it. This lab reproduces the data case study of Chapter 3.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2 (see `env/requirements.txt`). Or open `leakage_hunt.ipynb` in a hosted notebook service.

## Data

Diabetes 130-US Hospitals for Years 1999-2008, UCI Machine Learning Repository, https://doi.org/10.24432/C5230J, license CC BY 4.0 (checked 2026-11-24). 101,766 inpatient encounters of patients with diabetes at 130 US hospitals, 47 features, one row per encounter; `patient_nbr` identifies the patient (71,518 distinct patients). The target in this lab is `readmitted == "<30"` (readmitted within 30 days). Introduced by Strack et al. (2014), *BioMed Research International*, article 781670, https://doi.org/10.1155/2014/781670.

The notebook downloads the zip file from UCI once into a temporary folder. If you are offline, put `diabetic_data.csv` next to the notebook.

Known limitations: data from 1999-2008; some fields are mostly missing (weight, payer code); the readmission label only covers readmissions to hospitals in the same database; encounters that end in death can never be "readmitted". Use the data to learn methods, not to draw clinical conclusions.

## Steps

1. Open `leakage_hunt.ipynb` and run the cells in order.
2. **Checkpoint 1:** 101,766 encounters, 71,518 patients, 16,773 patients with more than one encounter, a 30-day readmission rate of 0.112.
3. **Checkpoint 2:** 1,652 encounters end in death, and none of them is followed by a readmission.
4. **Checkpoint 3:** with honest features, the random split gives a test AUC of 0.673 with 8,993 patients on both sides; the patient-grouped split gives 0.677 with none.
5. **Checkpoint 4:** adding the past-only count of earlier encounters gives 0.680; adding the count of the patient's encounters in the whole file gives 0.793.
6. **Checkpoint 5:** permutation importance ranks `encounters_in_file` first (a drop in AUC of about 0.21), far ahead of `number_inpatient` (about 0.05) and `discharge_disposition_id` (about 0.04).
7. **Checkpoint 6:** keeping first encounters only and excluding death and hospice discharges leaves 69,990 encounters (the paper reports 69,984), a readmission rate of 0.090 and a test AUC of 0.647.
8. Optional: build one more feature of your own and test it.

## Expected results

The numbers above come from scikit-learn 1.7.2 with `random_state=0`. Other versions can move the AUCs by about 0.01; the pattern (honest about 0.65 to 0.68, leaky about 0.79, the leaky feature at the top of the importance list) should hold.

## Questions

1. Why does the patient-grouped split not change the AUC much in this dataset? Name one kind of data where you would expect it to change a lot.
2. The leaky feature passed the grouped split. Which check caught it, and why could the test set not catch it?
3. Is "discharged as deceased, therefore not readmitted" leakage, a label problem or a population problem? Argue for one answer.
4. You must report one AUC to a hospital's quality committee. Which of the numbers in this lab would you report, with which population and split, and what caveat would you add?

## What to hand in

A half-page leakage log: each issue you found (the whole-file aggregate, the death discharges, the repeated patients), how you detected it, its effect on the test AUC, and the fix. Add your answers to the four questions. The log goes into the model card draft of your Explanation Dossier.

## Self-check

If your leakage log lists the whole-file aggregate but not the death discharges, reread Checkpoint 2. If you report 0.793 anywhere as the model's performance, start again from Checkpoint 4.
