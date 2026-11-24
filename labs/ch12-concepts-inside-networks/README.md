# Chapter 12 labs: Concepts Inside Networks

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Teach a machine a shortcut, then audit it with concepts | No code (browser tool and worksheet) | about 60 minutes |
| [lab2](lab2/) | Dissect a small network, then test a concept | Run-only notebook | about 45 minutes |
| [lab3](lab3/) | Concept bottlenecks, interventions and leakage | Run-only notebook, one optional edit | about 40 minutes |
| [lab4](lab4/) | Stickers on rejected parts (the chapter's case study, VisA Candle subset, CC BY 4.0) | Run-only notebook | about 60 minutes |

All notebooks were run end to end on 2026-11-24 on a laptop CPU with Python 3.10, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, matplotlib 3.10.9, torch 2.6.0 and pillow 12.3.0 (pillow is installed with matplotlib). Run times: Lab 12.2 about 20 seconds, Lab 12.3 about 15 seconds, Lab 12.4 about 5 minutes plus a one-time download of about 130 MB.

Every concept method in these labs is written out in plain numpy, scikit-learn and PyTorch so that you can see each step. For real projects, maintained implementations exist, for example the TCAV class in Captum (version 0.9.0, checked 2026-11-24) and Concept Relevance Propagation in zennit-crp (version 0.6.0); Chapter 23 compares tools.
