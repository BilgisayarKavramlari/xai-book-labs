# Chapter 20 labs: Is the Explanation Any Good? Evaluating Faithfulness and Robustness

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Grade the Evidence | No code (worksheet; optional OpenXAI leaderboard pages in a browser) | about 45 minutes |
| [lab2](lab2/) | An Evaluation Suite for Five Explainers | Run-only notebook (one optional edit) | about 75 minutes |
| [lab3](lab3/) | Comprehensiveness and Sufficiency for a Sentiment Classifier | Run-only notebook, language model environment | about 45 minutes |

Lab 20.2 uses the same synthetic credit-style data, network, methods and seeds as the chapter's figures (`figures/scripts/ch20_figs.py` in the book repository), so its numbers match the chapter. The data is invented and contains no real person's information. Lab 20.3 uses a small open sentiment classifier and forty review sentences written for the lab.

Versions used for the end-to-end runs on 2026-11-24 (laptop CPU, Python 3.10):

- Lab 20.2: numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, matplotlib 3.10.9 (`env/requirements.txt`, kernel `xai-lab-venv`). Ran in about 50 seconds.
- Lab 20.3: torch 2.6.0, transformers 4.57.6, numpy 1.26.4 (`env/requirements-llm.txt`, kernel `xai-llm-venv`). Ran in about five minutes (275 seconds), after the model was downloaded.

The evaluation methods are written out in plain numpy and PyTorch so that every step can be read. Toolkits that implement many of them: Quantus 0.6.0 (released July 2025) and OpenXAI (repository last updated August 2024), both checked 2026-11-24; Chapter 23 compares toolkits.
