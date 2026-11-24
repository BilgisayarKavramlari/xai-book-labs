# Chapter 21 labs: The Hermeneutic Circle

| Lab | Title | Time | Type |
|---|---|---|---|
| [21.1](lab1/README.md) | Reading a Refusal as a Text | about 50 minutes | No code (printed packet) |
| [21.2](lab2/README.md) | Auditing HermAI 0.1.8 | about 40 minutes | Run-only notebook |
| [21.3](lab3/README.md) | A Mini Hermeneutic Circle Test | about 60 minutes (8 minutes of computation) | Notebook with a few cells to edit |

*Disclosure: the author of the book develops and maintains the open-source HermAI library and designed the Hermeneutic Circle Test. These labs treat HermAI like any other explainer: the same checks, the same caveats, and its defects reported as found.*

Versions used for the end-to-end runs (2026-11-24): Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, shap 0.49.1, lime 0.2.0.1, hermai 0.1.8 (installs seaborn; 0.13.2 was used). `pip check` reported no broken requirements after installing hermai 0.1.8 into the environment of `env/requirements.txt`.

All three labs use the featured applicant of the chapter's case study (test row 77 of German Credit with `random_state=0`). Data: German Credit (Statlog), see `data/german-credit.md`.
