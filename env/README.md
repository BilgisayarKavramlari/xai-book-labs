# Environments

The labs use two Python environments, because the language model labs need older versions of some libraries than the other labs. Both were last run end to end on Python 3.10 on a laptop CPU (see the date at the top of each requirements file).

| File | For | Notes |
|---|---|---|
| `requirements.txt` | Chapters 1 to 13 and every non-language-model lab in later chapters | numpy 2.x; includes scikit-learn, shap, lime, interpret, dice-ml, PyTorch |
| `requirements-llm.txt` | Language model labs (Part V and the language model labs of Chapters 20 and 23) | TransformerLens 2.x (the `HookedTransformer` API), transformers 4.x, numpy 1.26 |

Each lab README says which file it uses.

## Setting up

Create one virtual environment per file, for example:

```
python3 -m venv .venv-xai
.venv-xai/bin/pip install -r env/requirements.txt
.venv-xai/bin/python -m ipykernel install --user --name xai-lab-venv

python3 -m venv .venv-xai-llm
.venv-xai-llm/bin/pip install -r env/requirements-llm.txt
.venv-xai-llm/bin/python -m ipykernel install --user --name xai-llm-venv
```

Then open a notebook and choose the kernel the lab README names (`xai-lab-venv` or `xai-llm-venv`). Hosted notebook services also work: install the packages from the same file in the first cell.

Do not install the language model packages into the first environment: they change the numpy and pandas versions the other labs were run with.
