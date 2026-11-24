# Chapter 27 labs: The Explanation Audit: Capstone and the Road Ahead

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Plan the Audit: scope, criteria, evidence index and finding register | No code (worksheet) | about 75 minutes |
| [lab2](lab2/) | The Reference Audit: re-performing the evidence for a credit model (the chapter's case study) | Run-only notebook (one optional edit) | about 60 minutes |
| [lab3](lab3/) | Ten Minutes, One Opinion: the audit presentation and peer review | No code (slides or paper, a timer, two reviewers) | about 90 minutes |

Lab 27.2 was run end to end on 2026-11-24 with Python 3.10 on a laptop CPU, with the main environment in `env/requirements.txt` (numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, shap 0.49.1; kernel `xai-lab-venv`). It ran in about 85 seconds after the data was cached, and it fetches German Credit from OpenML on first use. It uses the same data, model, seeds and code as the chapter's figures (`figures/scripts/ch27_figs.py` in the book repository), so its numbers match the chapter.

These labs close the Explanation Dossier (`portfolio/explanation-dossier-template.md`). Lab 27.1 turns your dossier into an audit plan, Lab 27.2 shows what re-performed evidence looks like, and Lab 27.3 turns the audit report into a ten-minute presentation.
