# Chapter 13 labs: Beyond Tables and Images: Time Series, Graphs and Agents

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Why was my flight late? Reported delay causes versus model explanations | No code (browser and worksheet) | about 45 minutes |
| [lab2](lab2/) | Explaining a delay forecast (the chapter's case study, Part 1) | Run-only notebook | about 60 minutes |
| [lab3](lab3/) | Explaining a transaction graph (planted motifs and a synthetic payment network; the case study, Part 2) | Run-only notebook | about 60 minutes |
| [lab4](lab4/) | Why did the agent go around? Reward decomposition and counterfactual tests | Run-only notebook, one optional edit | about 45 minutes |

All notebooks were run end to end on 2026-11-24 with Python 3.10 on a laptop CPU, using numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, matplotlib 3.10.9, shap 0.49.1 (Lab 13.2) and torch 2.6.0 (Lab 13.3), the versions pinned in `env/requirements.txt`. Set the environment variable `XAI_DATA` to choose where downloaded data are cached.
