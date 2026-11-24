# Chapter 19 labs: Explaining LLM Applications: Citations, Traces and Agents

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | The citation audit | No code (browser and worksheet) | about 60 minutes |
| [lab2](lab2/) | Which source did the model use? Context attribution on GPT-2 small | Run-only notebook (language-model environment) | about 60 minutes |
| [lab3](lab3/) | Audit an agent trace: a simulated parcel-support agent before and after an update | Run-only notebook | about 60 minutes |
| [lab4](lab4/) | Is the narrative faithful to the numbers? | Run-only notebook, optional chatbot part | about 60 minutes |

All notebooks were run end to end on 2026-11-24 on a laptop CPU with Python 3.10.
Labs 19.3 and 19.4 use the main environment (`env/requirements.txt`: numpy 2.2.6, pandas 2.3.3, matplotlib 3.10.9).
Lab 19.2 uses the separate language-model environment (`env/requirements-llm.txt`: torch 2.6.0, transformers 4.57.6, scikit-learn 1.7.2, scipy 1.15.3, numpy 1.26.4); it downloads GPT-2 small (about 500 MB) from the Hugging Face hub on first use.
No lab needs an API key or an account. The traces, policies, cities and firms in the labs are invented for teaching.
