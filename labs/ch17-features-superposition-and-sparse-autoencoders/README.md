# Chapter 17 labs: Features, Superposition and Sparse Autoencoders

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Investigate a feature and a graph on Neuronpedia | No code (web tool and worksheet) | about 60 minutes |
| [lab2](lab2/) | Medical features in GPT-2 small | Run-only notebook, language model environment | about 50 minutes |
| [lab3](lab3/) | Superposition and dictionaries you can check | Run-only notebook, main environment | about 40 minutes |

Notebooks were run end to end on 2026-11-24 on a laptop CPU. Lab 17.3 uses `env/requirements.txt` (numpy 2.2.6, torch 2.6.0, matplotlib 3.10.9). Lab 17.2 uses `env/requirements-llm.txt` (torch 2.6.0, transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4; huggingface_hub 0.36.2 and safetensors 0.8.0 come with transformers) and downloads GPT-2 small and one openly licensed SAE (MIT) on first run.

The sparse autoencoder code in these labs is written out in a few lines of PyTorch so that every step is visible. For real projects, maintained libraries exist, for example SAELens for training and loading SAEs, TransformerLens or nnsight for hooking models, and circuit-tracer for attribution graphs (Chapter 23 compares tools). Neuronpedia hosts dictionaries, feature pages, steering and an attribution graph viewer; as a web service it changes over time, so the lab states the date it was checked.
