# Lab 14.3: What Drove the Ranking?

Chapter 14, Why Language Models Are Hard to Explain (case study) · Code notebook (run, read and answer) · About 50 minutes · Last checked: 2026-11-24 (executed end to end in under 10 seconds)

## Goal

Audit a language model from the outside. Using the 8,000 replies Bloomberg published from its 2024 test of GPT-3.5 and GPT-4 as resume rankers, attribute the models' top picks to three input factors (position in the prompt, resume text and name group), test each for significance, and see how often the four-fifths check would raise a false alarm.

## Tools and versions

`what_drove_the_ranking.ipynb`, Python 3.10, main environment `env/requirements.txt`: numpy 2.2.6, pandas 2.3.3, scipy, matplotlib 3.10.9. No language model and no internet access are needed. Jupyter kernel used for the check: `xai-lab-venv`.

## Data and license

`data/bloomberg_gpt_rankings.csv` (8,000 rows, about 0.6 MB), derived from Bloomberg's repository https://github.com/BloombergGraphics/2024-openai-gpt-hiring-racial-discrimination (Apache License 2.0); see `NOTICE.md`. One row per reply: model, job, source file, whether it was a rebalancing run, and for the resume ranked first its position shown (`top_pos`, 0 = first), resume text (`top_resume`, 0 to 7) and name group (`top_group`: A, B, H, W for Asian, Black, Hispanic, White; M or W for men or women). To rebuild the table yourself (optional), clone the repository and run `python build_runs_table.py <repo folder> data/bloomberg_gpt_rankings.csv`; the result should be identical.

Known limits of the source: one prompt wording, models from late 2023 at temperature 1, eight resume texts per job, groups represented by names, and 11 percent of GPT-3.5 replies that do not mention all eight names (the ranking is read as Bloomberg's own notebook does, by the order in which names first appear).

## Steps

1. Run the notebook cells in order.
2. **Checkpoint 1:** 8,000 rows, 1,000 per model and job.
3. **Checkpoint 2:** in the factor table, GPT-3.5's largest position share ranges from 0.41 (financial analyst) to 0.83 (software engineer); for GPT-4 on HR one resume text takes 0.70 of top picks; name-group p-values are below 0.001 only for GPT-3.5 on HR specialist and financial analyst.
4. **Checkpoint 3:** GPT-3.5 put the first-shown resume first 56.1 percent of the time and returned the input order unchanged 11.7 percent; GPT-4, 28.3 and 3.3 percent.
5. **Checkpoint 4:** about 64 percent of simulated name-blind audits fall below four-fifths; 7 of 8 real cells fall below it, but only 2 have p below 0.05 (GPT-3.5 on HR, ratio 0.53, and financial analyst, 0.44).
6. **Checkpoint 5:** false alarms fall from about 98 percent of audits at 250 rankings to about 1 percent at 4,000.
7. **Checkpoint 6:** bootstrap intervals for the HR impact ratio are about 0.39 to 0.60 (GPT-3.5) and 0.53 to 0.78 (GPT-4), both below 0.8 although only GPT-3.5's name effect is significant; read the note in the notebook on why.

## Expected results

The numbers above. Simulation results vary in the last digit with the random seed.

## Questions

1. Rank the three factors by their effect for each model. Which is a legitimate basis for ranking, which is not, and which needs a recruiter to decide?
2. A vendor reports "passed four-fifths" on 500 rankings. What would you ask for before accepting the claim?
3. Bloomberg balanced which group was shown first. What would have gone wrong in the name analysis if it had not?
4. Write the three-sentence summary of this audit you would give an HR director, and the one you would give a candidate.

## What to hand in

A one-page audit note: the three factor effects for one job and both models, their tests, the four-fifths result read against the simulation, and one recommendation for an employer considering such a tool.

## Self-check

If your name-group p-values for GPT-4 are below 0.05, check that you are testing counts of top picks per group (eight numbers per model and job), not the 8,000 rows at once.

## Sources

- Bloomberg Graphics (2024), data and code repository (Apache License 2.0), linked above.
- Uniform Guidelines on Employee Selection Procedures, 29 CFR 1607.4(D), https://www.law.cornell.edu/cfr/text/29/1607.4
