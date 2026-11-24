# Lab 22.3: Numbers People Can Read

Chapter 22, Explanations for People · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in under 5 seconds on a laptop CPU)

## Goal

Compute natural frequencies for a deterioration alert at several prevalences and draw them as icon arrays; then show a flight-delay forecast as a point, an interval and a quantile dotplot, and write the message each display supports.

## Tools and versions

Python 3.10 with numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2 and matplotlib 3.10.9 (`env/requirements.txt`; Jupyter kernel `xai-lab-venv`). Notebook: `numbers_people_can_read.ipynb`. Nothing needs to be written, only cells run and outputs read; changing two numbers in one cell is optional.

## Data

Synthetic, generated in the notebook with seed 22: an alert with sensitivity 80 percent and specificity 90 percent; a history of 5,000 invented flights (inbound aircraft delay, departure hour, arrival delay). The forecast for one passenger's flight is the distribution of arrival delays of the 200 most similar past flights (nearest neighbors).

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** PPV 0.140 at 2 percent prevalence, 0.296 at 5 percent (135 alerts, 40 real), 0.471 at 10 percent, 0.667 at 20 percent (240 alerts, 160 real).
3. **Checkpoint 2:** median delay 19.8 minutes; 80 percent interval 12.2 to 32.6 minutes; 26.5 percent of similar flights past the 25-minute slack; 5 of 20 dots past the line. These match the chapter's figures.
4. Write one passenger message per display (examples are in the notebook).
5. Optional: change the inbound delay to 10 and to 40 minutes, rerun, and rewrite the dotplot message.

## Expected results

The checkpoints exactly. The point forecast says the passenger will make her connection; the dotplot says she will miss it about one time in four.

## Questions

1. A product sheet says the alert has "80 percent sensitivity". Write the one sentence a ward nurse should see instead, using natural frequencies for her ward.
2. Why does the interval display make a decision harder than the dotplot, although it contains similar information?
3. At what inbound delay would you advise the passenger to rebook, and what costs besides the chance of missing the connection did you weigh?

## What to hand in

Three icon arrays, the three delay displays, your passenger messages and your answers to the questions.

## Self-check

If your dotplot message contains a percentage with a decimal point, rewrite it as "about N in 20" or "about 1 in 4": people count dots more reliably than they read probabilities.
