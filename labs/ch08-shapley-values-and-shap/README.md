# Chapter 8 labs: Shapley Values and SHAP

| Lab | Title | Time | Type |
|---|---|---|---|
| [8.1](lab1/README.md) | Shapley Values by Hand | about 45 minutes | No code (paper or spreadsheet) |
| [8.2](lab2/README.md) | SHAP for a Credit Card Default Model | about 60 minutes | Run-only notebook |
| [8.3](lab3/README.md) | Backgrounds, Correlation and Estimators | about 75 minutes | Notebook with a few cells to edit |

Versions used for the end-to-end runs (2026-11-24): Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, shap 0.49.1 (with numba 0.68.1 and llvmlite 0.50.0), xlrd 2.0.2. shap 0.49.1 is the last release that supports Python 3.10; from 0.50 it needs Python 3.11, and from 0.52 Python 3.12 (as listed on PyPI, checked 2026-11-24). On Python 3.12, the current release (0.54.1, October 2026) should give the same values for TreeSHAP; check its defaults (see the notes in Lab 8.3).
