# Chapter 15 labs: Reading Representations: Probing and the Logit Lens

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Reading the lens, judging the probe | No code (worksheet with precomputed results) | about 45 minutes |
| [lab2](lab2/) | Watching a model change its mind: the logit lens and a fitted lens on GPT-2 small | Run-only notebook | about 45 minutes |
| [lab3](lab3/) | A truth probe with controls (the chapter's case study) | Run-only notebook | about 60 minutes |
| [lab4](lab4/) | Asking the right question: mine or theirs, decodable or used | Run-only notebook, synthetic data | about 30 minutes |

All notebooks were run end to end on 2026-11-24 with Python 3.10 on a laptop CPU.

- Labs 15.2 and 15.3 use the language-model environment in `env/requirements-llm.txt` (torch 2.6.0, transformer-lens 2.18.0 with the `HookedTransformer` API, transformers 4.57.6, numpy 1.26.4, scikit-learn 1.7.2). Lab 15.3 ran in about 2 minutes and Lab 15.2 in about 2.5 minutes. They download GPT-2 small (about 500 MB) from the Hugging Face Hub on first use; after that they run offline.
- Lab 15.4 uses the main environment in `env/requirements.txt` (numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2) and runs in about 10 seconds.
- Lab 15.1 needs only a browser or text viewer; its materials were produced by Labs 15.2 and 15.3.

TransformerLens 4.x removed `HookedTransformer`; keep 2.18.0 for these notebooks.
