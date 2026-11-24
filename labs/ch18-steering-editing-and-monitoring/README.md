# Chapter 18 labs: Steering, Editing and Monitoring Models

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Steer, then audit | No code (web steering tool or the saved-output worksheet) | 45 to 60 minutes |
| [lab2](lab2/) | Build a steering vector | Run-only notebook with one editable cell (GPT-2 small) | about 60 minutes |
| [lab3](lab3/) | Edit a memory, count the ripples | Run-only notebook (numpy) | about 45 minutes |
| [lab4](lab4/) | When the monitor becomes the reward | Run-only notebook (numpy) with one editable cell | 30 to 45 minutes |

Environments (checked 2026-11-24):

- Lab 18.2 uses the language-model environment in `env/requirements-llm.txt` (Python 3.10, torch 2.6.0, transformer-lens 2.18.0 with the HookedTransformer API, transformers 4.57.6, numpy 1.26.4). Jupyter kernel name used here: `xai-llm-venv`. It ran end to end in about 5.5 minutes on a laptop CPU, after a one-time download of GPT-2 small (about 550 MB) from the Hugging Face Hub.
- Labs 18.3 and 18.4 need only numpy (the main environment in `env/requirements.txt`, numpy 2.2.6; kernel `xai-lab-venv`). Each runs in a few seconds.

Labs 18.3 and 18.4 are toys built to show a mechanism, not reproductions of any published experiment. Their numbers describe the toy only. The GPT-2 numbers in Lab 18.2 are the ones quoted in Chapter 18.
