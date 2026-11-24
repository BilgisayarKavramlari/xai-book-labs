# Lab 13.1: Why Was My Flight Late?

Chapter 13, Beyond Tables and Images: Time Series, Graphs and Agents · No code (browser and worksheet) · About 45 minutes · Last checked: 2026-11-24

## Goal

Compare the delay causes that US airlines report to the Bureau of Transportation Statistics (BTS) with what a delay-forecasting model would explain, and write two explanations of the same delay pattern: one for a passenger and one for an airline operations controller.

## Tools

A web browser. The BTS page "Airline On-Time Statistics and Delay Causes": https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp (checked 2026-11-24: it lets you choose a carrier, an airport and a range of months from June 2003 onward, and shows the share of flights on time, delayed by air carrier, weather, National Aviation System, security or aircraft arriving late, canceled and diverted). A flight counts as delayed when it arrives 15 or more minutes after schedule. No account is needed.

## Data and license

BTS statistics are published by the US Department of Transportation and are in the public domain. You only read summary figures on the website.

## Steps

1. Open the page. Note the national figures for the most recent month shown. **Checkpoint 1:** the page lists eight categories (on time, five delay causes, canceled, diverted).
2. Choose one large airport you know and a carrier that serves it. Set the period to July 2024 to July 2024 and submit. Then set it to a calm month of your choice (for example October 2024). **Checkpoint 2:** you have two sets of percentages for the same airport and carrier.
3. Do the same for a second carrier at the same airport. If you choose Delta Air Lines, July 2024 includes the disruption that followed the faulty CrowdStrike software update of July 19, 2024 (Chapter 13 case study).
4. On the worksheet below, fill one row per airport, carrier and month: on-time share, each cause, canceled.
5. Look for how each cause is described on the page or in the notes and links next to it (if you cannot find a definition, write down your own reading of the category name and say so). Answer: in which category would you expect a delay to land when the inbound plane was itself late because of weather earlier in the day? (Hint: look at "aircraft arriving late".)
6. Write the two explanations (see What to hand in).

## Worksheet

| Airport | Carrier | Month | On time | Carrier | Weather | NAS | Security | Late aircraft | Canceled |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

## Questions

1. The reported causes are an explanation scheme. Who assigns a cause, at what moment, and with what incentives? What does that mean for their faithfulness to what really happened?
2. "Aircraft arriving late" is a cause that points to another delay. What is lost when a delay is explained by an earlier delay? Compare with a model that attributes a prediction to "inbound aircraft" (Chapter 13 case study).
3. A forecasting model would explain a prediction made two hours before departure. Which of the reported causes could it know about at that time, and which only afterwards?

## What to hand in

The filled worksheet; a three-sentence explanation of the July 2024 pattern for a passenger (plain words, what they can do); a five-sentence explanation for an operations controller (what drove delays, what the numbers cannot tell, what to watch next); and one paragraph on what the reported causes do not tell you.

## Expected results

Exact percentages depend on the airport and carrier you choose. In the national figures the largest delay categories are usually air carrier, National Aviation System and aircraft arriving late; weather and security are small. For a carrier hit by the July 2024 disruption, on-time shares and cancellations differ sharply from a calm month.

## Self-check

If your passenger explanation contains category names such as "NAS delay", rewrite it: the passenger needs what happened and what they can do, not the reporting scheme. If your controller explanation says "the outage caused late aircraft", check whether the data you looked at can show that, or only the categories airlines reported.
