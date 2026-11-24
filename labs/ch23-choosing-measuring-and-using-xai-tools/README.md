# Chapter 23 labs: Choosing, Measuring and Using XAI Tools

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Due diligence without code: a tool evaluation sheet for three tools | No code (browser and sheet) | about 60 minutes |
| [lab2](lab2/) | A test drive for explanation tools: correctness, stability, cost and agreement on a credit model | Run-only notebook | about 45 minutes |
| [lab3](lab3/) | The scored comparison: counterfactual checks, a weighted scorecard and a stress test (the chapter's case study) | Notebook, only weights edited | about 45 minutes |
| [lab4](lab4/) | Same model, two loaders: a cross-implementation check of GPT-2 small | Run-only notebook, language-model environment | about 30 minutes |

All notebooks were run end to end on 2026-11-24 with Python 3.10 on a laptop CPU.

- Labs 23.2 and 23.3 use the main environment in `env/requirements.txt` plus `hermai==0.1.8` and `seaborn==0.13.2`. Lab 23.2 runs in about four minutes; Lab 23.3 in under a minute and needs Lab 23.2's output file. Both fetch German Credit from OpenML on first use.
- Lab 23.4 uses the language-model environment in `env/requirements-llm.txt` (torch 2.6.0, transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4). It downloads GPT-2 small on first use and then runs in about 10 seconds.
- `lab1/tool-evaluation-sheet.md` is the tool evaluation sheet used throughout the chapter; copy it for your Explanation Dossier.

Disclosure: HermAI, one of the tools measured in Labs 23.2 and 23.3, is maintained by the book's author. It is tested with the same code and scored by the same rules as every other tool.
