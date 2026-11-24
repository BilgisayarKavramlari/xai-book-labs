# Lab 25.1: A Monitoring Runbook and an Explanation Log

Chapter 25, Explainability in Production · No code (browser, spreadsheet and worksheet) · About 60 minutes · Last checked: 2026-11-24

## Goal

Turn 64 weeks of monitoring results for a demand forecast into alert rules, a specification for an explanation log record, and a release note for the people who read the forecast's reasons.

## Tools

- A spreadsheet program (any) to open `weekly_monitor.csv`.
- A web browser to read two vendors' documentation of attribution drift monitoring (both checked 2026-11-24; no account needed):
  - Amazon SageMaker Clarify, "Feature attribution drift for models in production": https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribution-drift.html (note the banner: SageMaker Clarify and Model Monitor have been closed to new customers since July 30, 2026, per the AWS service availability update of June 30, 2026).
  - Google Cloud Vertex AI, "Monitor feature attribution skew and drift": https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/monitor-explainable-ai
- Optionally, the OpenTelemetry generative AI conventions (status: Development) on what traces should and should not capture: https://github.com/open-telemetry/semantic-conventions-genai

## Data and license

`weekly_monitor.csv` holds one row per week from 30 August 2010 to 21 November 2011 for the chapter's case study, computed by Lab 25.2 from Online Retail II by Daqing Chen (Chen, D. (2012). Online Retail II [Data set]. UCI Machine Learning Repository, https://doi.org/10.24432/C5CG6D), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Changes: the file contains no transaction rows from the original; it holds weekly statistics of an invented forecasting system's errors and attributions, computed from the invoice lines by the Lab 25.2 notebook. The forecasting system is invented; the underlying transactions are real. See also `data/LICENSES.md` at the repository root. Columns:

| Column | Meaning |
|---|---|
| `week_starting` | Monday of the forecast week |
| `forecast_error_mae` | mean absolute error of next-week forecasts, log units (known a week later) |
| `attribution_shift_tv` | total variation distance between the week's attribution shares and the launch reference |
| `feature_that_moved_most` | feature whose attribution share changed most |
| `store_orders_below_training_range` | True if the store had fewer orders that week than in any training week (279) |
| `features_with_psi_above_0_25` | number of six product-level features with population stability index above 0.25 |

The alarm threshold for `attribution_shift_tv` is 0.107, the 95th percentile of weekly shifts inside the training period. Training error was 0.84.

## Steps

1. Open the CSV. Sort by `attribution_shift_tv`. **Checkpoint 1:** 12 weeks are above 0.107; the largest is 0.184 (17 January 2011).
2. Mark the weeks with at least one PSI alarm. **Checkpoint 2:** 14 weeks, 10 of them between October 2010 and January 2011. Compare their errors with the training error.
3. Find the week with the largest error. **Checkpoint 3:** 3.13 in the week of 20 December 2010; the week before (13 December, error 1.58) has no attribution alarm. Write one sentence on why.
4. Read the two vendor pages. Note for each: what is compared with what, which summary statistic or threshold is used, and what the vendor says you need to enable it.
5. Write three alert rules, one per rung of the monitoring ladder (input drift, attribution drift, loss attribution once labels arrive). For each: condition, window, who receives it, what they do in the first hour, and when the alert is closed.
6. Specify an explanation log record: field names, types, who may read each field, and how long it is kept. Include at least model version, explainer and library versions, a background data hash, the attributions, the reasons shown and the audience.
7. Fill the release-note template below for a retraining in which the top reason changed for 31 percent of product-weeks, mostly from the 4-week average to last week's units, with no change in error.

## Release-note template

| Field | Your text |
|---|---|
| What changed (model version, date) | |
| What did not change (accuracy, with numbers) | |
| What you will see differently (reasons) | |
| Why it changed, in one sentence | |
| What to do if a reason looks wrong | |
| Who to contact | |

## What to hand in

A one-page runbook (the three alert rules and their owners), the log record specification, and the filled release note.

## Expected results

Your alert rules will differ; good ones route input drift to a dashboard rather than a person, set the attribution threshold from measured variability, pre-register holiday weeks, and require labels for the loss-attribution rule. Good log specifications separate fields an outside party may see from fields only analysts may see.

## Self-check

- Would your attribution alarm have woken someone in the week of 13 December 2010? If not, what in your plan covers that week?
- Could an auditor reproduce, from your log record alone, the exact reason a store manager saw eighteen months ago?
- Does your release note say what did not change, with a number?
