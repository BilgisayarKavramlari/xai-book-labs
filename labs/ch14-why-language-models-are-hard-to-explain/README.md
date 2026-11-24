# Chapter 14 labs: Why Language Models Are Hard to Explain

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Ask it why, then check: counterfactual tests of a chat assistant's self-explanations | No code (browser and worksheet) | about 45 minutes |
| [lab2](lab2/) | Five attributions for one token (GPT-2 small) | Run-only notebook, one optional edit | about 60 minutes |
| [lab3](lab3/) | What drove the ranking? An output audit of Bloomberg's GPT resume experiment (the chapter's case study) | Run-only notebook | about 50 minutes |

Lab 14.2 uses the language model environment, `env/requirements-llm.txt` (Python 3.10, torch 2.6.0, transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4; Jupyter kernel `xai-llm-venv`). Lab 14.3 uses the main environment, `env/requirements.txt` (numpy 2.2.6, pandas 2.3.3, scipy, matplotlib 3.10.9). Both notebooks were run end to end on 2026-11-24 on a laptop CPU: Lab 14.2 in about 70 to 105 seconds after GPT-2 small was cached, Lab 14.3 in under 10 seconds.
