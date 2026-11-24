# Chapter 16 labs: Circuits and Causal Interventions

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Read a patching experiment before you run one | No code (browser tool, result tables and worksheet) | about 60 minutes |
| [lab2](lab2/) | Activation patching on GPT-2 small (the chapter's case study) | Run-only notebook | about 60 minutes |
| [lab3](lab3/) | Find and knock out induction heads | Run-only notebook, one optional edit | about 40 minutes |
| [lab4](lab4/) | Attribution patching versus real patching | Run-only notebook | about 40 minutes |

The notebooks use the separate language-model environment of this repository, `env/requirements-llm.txt` (Python 3.10, torch 2.6.0, transformer-lens 2.18.0 with the `HookedTransformer` API, transformers 4.57.6, numpy 1.26.4, pandas 2.0.3, matplotlib 3.10.9). Do not install it into the main lab environment: TransformerLens 2.x needs numpy below 2. TransformerLens 4.x (4.4.0 as of 2026-11-24) removed `HookedTransformer`; these labs pin 2.18.0.

All notebooks were run end to end on 2026-11-24 on a laptop CPU that was also running other jobs. Measured run times: Lab 16.2 about 6 minutes (several hundred forward passes; expect 3 to 10 minutes), Lab 16.3 under 1 minute, Lab 16.4 about 1 minute, each after a one-time download of GPT-2 small (about 500 MB) from the Hugging Face Hub. The model card (openai-community/gpt2) lists the MIT license.

Every patching step is written out with the library's hook functions so that you can see what is overwritten and when. Comparable open libraries for the same experiments include nnsight (0.8.4) and pyvene (0.1.8), both checked on 2026-11-24; Chapter 23 compares tools.
