# Tools: what each one computes, versions, licenses and dates

This is the tool landscape page that the repository README and several labs point to. It lists the code libraries and the no-code web tools that the book and its labs use or name, with the facts a reader needs to choose between them: what each computes, what access to the model it needs, the version the labs were run with, its license and the date the facts were checked.

Tools change faster than books. Every fact below was read from the tool's own package page (the Python Package Index, PyPI), its repository, its documentation or its web page, or recorded when the labs were run. Where a fact was not checked, the table says "not recorded" rather than guessing. If a tool has moved or changed since the date shown, see "If a tool has moved" at the end of this page.

All tools are listed by the same rules and none is ranked. One of them, HermAI, is maintained by the book's author; it is tested and described exactly like the others. Chapter 23 of the book explains how to measure a tool on your own model before relying on it, and the [tool evaluation sheet](tool-evaluation-sheet.md) in this folder is the form it uses.

Last full check: 2026-11-24.

## Code libraries

Rows are grouped by family, in the order Chapter 23 uses: attribution libraries; glass-box and all-in-one toolkits; counterfactual and recourse libraries; data attribution; evaluation toolkits; language model interpretability; tracing and monitoring for applications. "Labs" means the pinned environments in `env/requirements.txt` and `env/requirements-llm.txt`. A library marked "not used in the labs" is named in the book as a dated example only.

| Library (package) | What it computes | Model access | Version in the labs | License | Checked |
|---|---|---|---|---|---|
| SHAP (`shap`) | Shapley-value attributions: model-agnostic estimators (Kernel SHAP, permutation) and exact TreeSHAP for tree ensembles; dependence and interaction plots | Agnostic (queries); specific for trees and networks | 0.49.1 (2025-10-14), the last release for Python 3.10. Latest: 0.54.1 (2026-10-16), requires Python 3.12 or newer; 0.50.0 (2025-11-11) and later require 3.11 or newer | MIT | 2026-11-24 |
| LIME (`lime`) | Local surrogate models fitted to perturbed samples weighted by proximity (defaults checked in source: quartile discretizer, kernel width 0.75 times the square root of the number of features, 5,000 samples) | Agnostic | 0.2.0.1 (2020-06-26); no later release | BSD | 2026-11-24 |
| Anchors (`anchor-exp`) | If-then rules with estimated precision and coverage | Agnostic | 0.0.2.0 (2020-09-10) | BSD | 2026-11-24 |
| Captum (`captum`) | Gradient and perturbation attributions for PyTorch models (Integrated Gradients, saliency, SmoothGrad, DeepLift, GradientShap), TCAV in its concept module, TracIn | Specific (PyTorch) | Not used in the labs (they implement the methods in plain PyTorch). Latest: 0.9.0 (2026-04-17), requires Python 3.10 or newer | BSD-3-Clause | 2026-11-24 |
| Zennit (`zennit`) | Rule-based attribution for PyTorch, with a focus on layer-wise relevance propagation (LRP) | Specific (PyTorch) | Not used in the labs. Latest: 1.0.0 (2025-07-31), requires Python 3.11.11 or newer | GPL-3.0-or-later and LGPL-3.0-or-later (PyPI license field) | 2026-11-24 |
| Zennit-CRP (`zennit-crp`) | Concept relevance propagation and relevance maximization | Specific (neural networks) | Not used in the labs. Latest: 0.6.0 (2023-04-03) | BSD 3-Clause Clear | 2026-11-24 |
| InterpretML (`interpret-core`) | Explainable Boosting Machines (glass-box additive models) and black-box explainers under one interface | Glass box; agnostic explainers | 0.7.8 (2026-03-17) | MIT (license file) | 2026-11-24 |
| dalex (`dalex`) | Permutation importance and partial dependence and accumulated local effects profiles | Agnostic | Not used in the labs. Latest: 1.8.0 (2026-01-20) | GPL-3.0 | 2026-11-24 |
| AI Explainability 360 (`aix360`) | A toolkit of explanation methods organized by the explanation type different audiences need | Not recorded | Not used in the labs. Latest: 0.3.0 (2023-07-31); repository still receiving commits in 2026, not archived | Apache 2.0 | 2026-11-24 |
| OmniXAI (`omnixai`) | Many explanation methods behind one interface | Not recorded | Not used in the labs. Latest: 1.3.1 (2023-07-16); repository still receiving commits in 2026, not archived | BSD-3-Clause | 2026-11-24 |
| HermAI (`hermai`) | A local surrogate (weighted Lasso on perturbations), a counterfactual (the closest perturbation that flips the decision; no option to fix features), a general surrogate tree and narrative summaries. **Maintained by the book's author.** | Agnostic | 0.1.8 (2025-10-02) | MIT | 2026-11-24 |
| DiCE (`dice-ml`) | Diverse counterfactual explanations, with an option to fix features that must not change | Agnostic; gradient methods for networks | 0.12 (2025-07-13), with its dependency `raiutils` 0.4.3 (MIT) | MIT | 2026-11-24 |
| Alibi Explain (`alibi`) | Counterfactuals, Anchors and other methods | Agnostic and specific | Not installed (0.9.6 requires numpy below 2.0). Latest: 0.9.6 (2024-04-18) | Business Source License 1.1 since 0.9.5 (2024-01-22); Apache 2.0 up to 0.9.4. The BSL permits non-production use; most production use needs a commercial license; each version converts to Apache 2.0 four years after release | 2026-11-24 |
| CARLA (`carla-recourse`) | A library of counterfactual recourse methods (its paper reports 11) | Not recorded | Not used in the labs. Latest: 0.0.5 (2022-05-30) | MIT | 2026-11-24 |
| Kronfluence (`kronfluence`) | Influence functions with eigenvalue-corrected Kronecker-factored curvature (EK-FAC) for PyTorch | Specific (PyTorch, gradients) | Not used in the labs. Latest: 1.0.1 | Apache 2.0 | 2026-11-24 |
| Quantus (`quantus`) | More than 30 metrics for evaluating neural network explanations in six categories (faithfulness, robustness, localisation, complexity, randomisation, axiomatic) | Agnostic (scores the explanations other methods produce) | Not used in the labs. Latest: 0.6.0 (2025-07-21) | GPL-3.0 (classifier) | 2026-11-24 |
| OpenXAI | Synthetic data with known ground truth, metrics and leaderboards for tabular attribution methods | Agnostic | Not used in the labs. Version not recorded; repository last updated in August 2024 | MIT | 2026-11-24 |
| TransformerLens (`transformer-lens`) | Caches and patches every activation of open-weight transformer models (`HookedTransformer`) | Specific (open weights) | 2.18.0 (2026-03-24). Latest: 4.4.0 (2026-11-12); 4.0.0 (2026-09-21) removed `HookedTransformer.from_pretrained`, which the labs use | MIT | 2026-11-24 |
| nnsight (`nnsight`) | Records interventions on a PyTorch model as a graph that runs locally or on the National Deep Inference Fabric (NDIF) | Specific (open weights) | Not used in the labs. Latest: 0.8.4 (2026-11-23) | MIT | 2026-11-24 |
| SAELens (`sae-lens`) | Trains and loads sparse autoencoders | Specific (open weights) | Not used in the labs (Lab 17.2 loads a sparse autoencoder with `huggingface_hub` 0.36.2 and `safetensors` 0.8.0). Latest: 6.56.1 (2026-11-20) | MIT | 2026-11-24 |
| circuit-tracer (`circuit-tracer`) | Attribution graphs for open models (released May 2025; Neuronpedia hosts a front end) | Specific (open weights) | Not used in the labs. Latest on PyPI: 0.5.4 | Not recorded | 2026-11-24 |
| tuned-lens (`tuned-lens`) | The tuned lens: trained per-layer translators that read a transformer's intermediate predictions | Specific (open weights) | Not used in the labs. Latest: 0.2.0 (2023-07-18) | MIT | 2026-11-24 |
| pyvene (`pyvene`) | Activation interventions for studying causal mechanisms, including causal abstraction | Specific (open weights) | Not used in the labs. Latest: 0.1.8 (2025-05-26) | Apache 2.0 | 2026-11-24 |
| Inseq (`inseq`) | Token attribution for sequence generation models | Specific (open weights) | Not used in the labs. Latest: 0.7.1 (2026-03-06) | Apache 2.0 | 2026-11-24 |
| LIT (`lit-nlp`) | The Learning Interpretability Tool: an interactive interface for inspecting models, including salience maps such as LIME; its hosted demo is used in Lab 7.1 | Not recorded | Not installed; the hosted demo is used instead (see the web tools table). Latest: 1.3.1 (2024-12-20) | Apache 2.0 | 2026-11-24 |
| Langfuse | Open-source tracing for LLM applications, built on OpenTelemetry | Application traces | Not used in the labs. Version not recorded | MIT, except folders marked `ee` | 2026-11-24 |
| Arize Phoenix | Tracing for LLM applications, built on OpenTelemetry | Application traces | Not used in the labs. Version not recorded | Elastic License 2.0 (source-available) | 2026-11-24 |
| Evidently | Open-source framework to evaluate, test and monitor machine learning and LLM systems | Model inputs and outputs | Not used in the labs. Version not recorded | Apache 2.0 | 2026-11-24 |
| Alibi Detect | Outlier, adversarial and drift detection | Model inputs and outputs | Not used in the labs. Version not recorded | Source-available; terms not recorded here | 2026-11-24 |

**The base environments.** `env/requirements.txt` (the tabular and vision labs; Python 3.10, CPU): numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, scipy 1.15.3, matplotlib 3.10.9, torch 2.6.0, seaborn 0.13.2, openpyxl 3.1.5, xlrd 2.0.2, nbclient 0.11.0, ipykernel 7.3.0, plus the explanation libraries above. `env/requirements-llm.txt` (Part V; Python 3.10, CPU): torch 2.6.0, transformer-lens 2.18.0, transformers 4.57.6, numpy 1.26.4 (TransformerLens 2.x needs numpy below 2), pandas 2.0.3, scikit-learn 1.7.2, scipy 1.15.3, einops 0.8.2, jaxtyping 0.3.7, tokenizers 0.22.2, matplotlib 3.10.9. Licenses of the pinned versions on PyPI: numpy, pandas, scipy, scikit-learn and torch 2.6.0 BSD; transformers 4.57.6 Apache 2.0; einops and jaxtyping MIT; matplotlib a license listed on PyPI as Python Software Foundation License. Newer releases exist for most of these and several require Python 3.11 or newer; the labs keep the pins so that every checkpoint number can be reproduced.

**Commercial platforms** are described by capability and dated, as in Chapter 23, and not ranked. As of November 24, 2026: Google Cloud's Vertex Explainable AI offers sampled Shapley, integrated gradients and XRAI attributions and example-based explanations, and has been deprecated since March 16, 2026, with access ending on or after March 16, 2027. Amazon SageMaker Clarify computes SHAP attributions and partial dependence plots and is no longer open to new customers; Amazon's guidance points to the open-source SHAP library on which Clarify is built, and SageMaker Model Monitor is also closed to new customers (the pages give no date for the change). Microsoft's Responsible AI dashboard in Azure Machine Learning assembles InterpretML, DiCE, EconML, Fairlearn and Error Analysis for tabular scikit-learn models. Lab 25.1 reads the Clarify and Vertex AI documentation on attribution drift monitoring.

## No-code web tools

These are the web tools used by the no-code labs. All are free and need no account for the steps the labs ask for. Never type real customer, patient or employee data into a public web tool.

| Tool | What it shows | Labs | Checked |
|---|---|---|---|
| TensorFlow Playground, https://playground.tensorflow.org | Trains a small fully connected network in the browser on four two-dimensional datasets (circle, exclusive or, Gaussian, spiral) with seven input features, and draws what every neuron computes | 3.1, 4.1 | 2026-11-24 |
| Transformer Explainer, https://poloclub.github.io/transformer-explainer/ | Runs GPT-2 small in the browser on your own text; shows next-token probabilities and attention weights on hover | 4.1, 16.1 (Part B, optional) | 2026-11-24 |
| Embedding Projector, https://projector.tensorflow.org/ | Projects word embeddings (demo sets "Word2Vec 10K" and "Word2Vec All", 71,291 words in 200 dimensions) with PCA, t-SNE, UMAP or a custom axis defined by two words; the training corpus is not documented on the page | 4.2 | 2026-11-24 |
| GAM Changer, https://interpret.ml/gam-changer/ | Lets you inspect and edit the shape functions of an additive glass-box model in the browser; four demo models (Iowa House Price, Lending Club, Census Income, your own file); nothing is uploaded | 5.1 | 2026-11-24 |
| Learning Interpretability Tool (LIT) hosted demo, https://pair-code.github.io/lit/demos/glue.html | Salience maps, including LIME with settable seed and sample size, for the `sst2-tiny` sentiment model on 872 SST-2 development sentences | 7.1 | 2026-11-24 |
| CNN Explainer, https://poloclub.github.io/cnn-explainer/ | What each layer of a small convolutional network computes on an image | 11.1 (optional warm-up) | 2026-11-24 |
| Teachable Machine, https://teachablemachine.withgoogle.com/ | Trains an image classifier in the browser tab from webcam or uploaded images; its FAQ says samples are not sent to a server unless you save the project to your own cloud drive | 12.1 | 2026-11-24 |
| BTS Airline On-Time Statistics and Delay Causes, https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp | Shares of flights on time and delayed by cause (air carrier, weather, National Aviation System, security, late-arriving aircraft), canceled and diverted, by carrier, airport and month from June 2003 | 13.1 | 2026-11-24 |
| Neuronpedia, https://www.neuronpedia.org/ | An open-source interpretability platform: sparse autoencoder dictionaries for open models (including GPT-2 small "res-jb", Gemma Scope, Gemma Scope 2, Llama Scope), feature pages with activating examples, a Test box for your own text, a Steer tool and the Circuit Tracer attribution graph viewer; generating new graphs, saving work and custom steering vectors may require signing in, and steering is rate-limited | 17.1, 18.1 (Option A) | 2026-11-24 |
| OpenXAI leaderboard, https://open-xai.github.io/ | Benchmark results for tabular attribution methods by dataset, model and metric | 20.1 (optional) | 2026-11-24 |
| Python Package Index, https://pypi.org/ | Package pages with versions, release dates, license fields and supported Python versions | 23.1 | 2026-11-24 |
| A general-purpose chat assistant, or AI assistants and AI search tools that show sources | Your own choice, used through its normal interface; record the product, the model or mode it reports and the date, because results change between versions | 14.1, 19.1 | Not applicable (reader's choice) |

The other no-code labs use worksheets and documents in this repository, public sources whose addresses are given in each lab's README (court judgments, regulations, regulators' pages and vendors' documentation), or, in Lab 10.1, the reader's own accounts on shopping or streaming services: Labs 1.1, 2.1, 2.2, 6.1, 8.1, 9.1, 10.1, 15.1, 20.1, 21.1, 22.1, 22.4, 24.1, 25.1, 26.1, 27.1 and 27.3.

## If a tool has moved

As of 2026-11-24 every tool above was reachable and no replacement was needed. If one has moved or changed, the labs name a fallback:

- TensorFlow Playground (Lab 3.1): a spreadsheet with a scatter chart covers the first two steps. Lab 4.1: any tool that trains a small network in the browser.
- Transformer Explainer (Labs 4.1 and 16.1): any viewer that shows a language model's attention for your own text; in Lab 16.1 Part B can be skipped.
- Embedding Projector (Lab 4.2): any embedding viewer that projects words onto the difference of two word vectors.
- GAM Changer (Lab 5.1): its source code (MIT license) can be run in a notebook.
- LIT (Lab 7.1): the LIT documentation lists the current demos; any tool that lets you set LIME's seed and number of samples will do.
- Neuronpedia steering (Lab 18.1): Option B uses the saved continuations in the lab's worksheet and needs no web tool.

When a replacement is confirmed, it will be added here with its date, and the old entry kept with a note.

## How to update this page

When you check a tool, change its row and its date together. Read versions and licenses from the package page or the license file itself, not from a badge. If a tool has changed in a way that alters a lab's checkpoints, update the lab's README in the same change. Keep the rows neutral: what the tool computes, what it needs and what is known about it, never a ranking.
