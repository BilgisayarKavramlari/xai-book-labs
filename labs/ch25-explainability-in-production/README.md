# Chapter 25 labs: Explainability in Production

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | A monitoring runbook and an explanation log | No code (browser, spreadsheet, worksheet) | about 60 minutes |
| [lab2](lab2/) | Explanation drift in a demand forecast (the chapter's case study) | Run-only notebook | about 45 minutes |
| [lab3](lab3/) | What explanations give away: model extraction, a coarsened defense and a membership check | Notebook, one setting edited | about 40 minutes |

All notebooks were run end to end on 2026-11-24 with Python 3.10 on a laptop CPU, with the main environment in `env/requirements.txt` (numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, shap 0.49.1, openpyxl 3.1.5). No package beyond that file is needed.

- Lab 25.2 reads Online Retail II (Chen, 2012; UCI, CC BY 4.0, DOI 10.24432/C5CG6D). It downloads the zip file (about 45 MB) once into a temporary folder, or uses a local copy named in the environment variable `ONLINE_RETAIL_II`. With a local compressed CSV it ran in under a minute; reading the Excel file adds about a minute.
- Lab 25.3 uses synthetic data and ran in under a minute.
- Lab 25.1 uses `lab1/weekly_monitor.csv`, the weekly monitoring results of Lab 25.2, so it needs no code.
