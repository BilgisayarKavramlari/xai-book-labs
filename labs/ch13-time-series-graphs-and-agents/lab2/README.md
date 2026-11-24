# Lab 13.2: Explaining a Delay Forecast

Chapter 13, Beyond Tables and Images: Time Series, Graphs and Agents · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 4 minutes on a laptop CPU, including the 34 MB download and feature building)

## Goal

Reproduce Part 1 of the Chapter 13 case study: build a leak-free model that predicts, two hours before scheduled departure, whether a US flight will leave 15 or more minutes late; explain it with SHAP values for single features and for groups of features; measure how stable the explanations are across retrained models; and watch what the explanations do during the disruption that followed the faulty CrowdStrike software update of July 19, 2024.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, shap 0.49.1, matplotlib 3.10.9. Notebook: `explaining_a_delay_forecast.ipynb`. Set `XAI_DATA` to choose where the data are cached; by default the notebook uses a folder in your system's temporary directory.

## Data

US Bureau of Transportation Statistics (BTS), Reporting Carrier On-Time Performance (1987-present), July 2024: https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_2024_7.zip (34 MB zipped, 287 MB unzipped; checked 2026-11-24). A US government work in the public domain. One row per flight by a reporting carrier: scheduled and actual local times, delays, tail number, origin and destination, cancellation and diversion. Known limitations: only carriers that report to BTS; times are local (the notebook avoids time-zone leaks by using scheduled flight times); one month only, so seasonality across the year cannot be studied here.

## How the features avoid leakage

The prediction is made at p = scheduled departure minus 120 minutes. The airport's recent state is the mean delay of departures scheduled in each of the three hours before p, where a flight that has not yet left is counted only by the delay already known at p (a lower bound). The inbound aircraft feature is the previous leg of the same tail number: its known delay at p, whether it had departed, and the scheduled slack before this departure.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** 634,613 flights, 18,372 canceled; 394,541 modeling rows (operated departures at the 30 busiest airports); share delayed 0.32.
3. **Checkpoint 2:** test AUC 0.839 (train July 1-14, test July 15-31); without the schedule group 0.830, without the airport group 0.797, without the inbound aircraft group 0.729.
4. **Checkpoint 3:** mean absolute SHAP by group: inbound aircraft 1.13, airport last 3 hours 0.65, schedule and carrier 0.18 (log-odds). The single most important feature is the inbound aircraft's known delay.
5. **Checkpoint 4:** the three hourly windows correlate at 0.70 to 0.78. Across bootstrap retrains, the per-flight top hour agrees with run 0 for 0.73 to 0.79 of flights, while the group total correlates at 0.97 to 0.98.
6. **Checkpoint 5:** for Delta on July 19, actual share late 0.933 against predicted 0.610; mean SHAP for the inbound aircraft group 1.87; the schedule-and-carrier group stays negative all month. Delta's share late in the training weeks was 0.224 against 0.283 for other carriers. Delta recorded 5,737 cancellations from July 19 to 23.

## Expected results

The numbers above come from the versions listed. Another scikit-learn or SHAP version can move them in the second decimal; the ordering of the groups and the outage pattern should hold.

## Questions

1. Which explanation would you give an operations controller for a single flight: the top feature, the top hour, or the group totals? Use Checkpoint 4.
2. Why did the model underpredict Delta's delays on July 19 to 22? Name what the explanations reveal and what they cannot.
3. Propose one feature and one monitoring rule that would have made the problem visible on July 19.

## What to hand in

A one-page explanation report: what the model predicts and when; the three groups and their attributions; the stability result and the unit you recommend; one paragraph on the outage.

## Self-check

If your report says the outage "caused late inbound aircraft and therefore delays", check whether the model can know that. It can only report that inbound aircraft were late; the IT failure behind it is not an input.
