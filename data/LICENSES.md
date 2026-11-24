# Data and model licenses

The labs download public datasets and pretrained models from their sources at run time; this repository does not store raw third-party data. The few derived files that are committed are listed at the end. Licenses were read on each source's own page on 2026-11-24. If you reuse a dataset, use the attribution line given here and check the source page, because terms can change.

## Datasets

| Dataset | License (as stated at source) | Source | Attribution line |
|---|---|---|---|
| Statlog (German Credit Data) | CC BY 4.0 (UCI); the OpenML copy `credit-g` that the notebooks fetch is listed as "Public" | https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data | Hofmann, H. (1994). Statlog (German Credit Data) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5NC77. Licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). |
| Diabetes 130-US Hospitals for Years 1999-2008 | CC BY 4.0 | https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008 | Clore, J., Cios, K., DeShazo, J., and Strack, B. (2014). Diabetes 130-US Hospitals for Years 1999-2008 [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5230J. Licensed under CC BY 4.0. |
| Default of Credit Card Clients | CC BY 4.0 | https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients | Yeh, I. (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H. Licensed under CC BY 4.0. |
| Online Retail II | CC BY 4.0 | https://archive.ics.uci.edu/dataset/502/online+retail+ii | Chen, D. (2012). Online Retail II [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D. Licensed under CC BY 4.0. |
| Breast Cancer Wisconsin (Diagnostic) (bundled with scikit-learn) | CC BY 4.0 | https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic | Wolberg, W., Mangasarian, O., Street, N., and Street, W. (1993). Breast Cancer Wisconsin (Diagnostic) [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B. Licensed under CC BY 4.0. |
| Optical Recognition of Handwritten Digits (scikit-learn `load_digits` is a copy of its test set) | CC BY 4.0 | https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits | Alpaydin, E., and Kaynak, C. (1998). Optical Recognition of Handwritten Digits [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C50P49. Licensed under CC BY 4.0. |
| freMTPL2freq | CC0 on OpenML (data_id 41214); the original source, the CASdatasets R package, is licensed GPL (>= 2) | https://www.openml.org/d/41214 ; https://github.com/dutangc/CASdatasets | freMTPL2freq, from Dutang, C., and Charpentier, A. CASdatasets: Insurance datasets (R package), https://doi.org/10.57745/P0KHAG; obtained from OpenML, data_id 41214. |
| BTS Reporting Carrier On-Time Performance (1987-present) and Airline On-Time Statistics and Delay Causes | Not stated on the data pages; US Government work (17 U.S.C. 105); the US DOT library states there are no copyright restrictions and asks users to cite | https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD | Bureau of Transportation Statistics, US Department of Transportation. Reporting Carrier On-Time Performance (1987-present), July 2024. |
| Bloomberg GPT resume-ranking data | Apache License 2.0 (repository LICENSE file) | https://github.com/BloombergGraphics/2024-openai-gpt-hiring-racial-discrimination | Derived from Bloomberg Graphics (2024), 2024-openai-gpt-hiring-racial-discrimination, Apache License 2.0; see `labs/ch14-why-language-models-are-hard-to-explain/lab3/NOTICE.md`. |
| VisA (Visual Anomaly), Candle subset (Lab 12.4) | CC BY 4.0 ("The data is released under the CC BY 4.0 license"; LICENSE-DATASET file in the repository) | https://github.com/amazon-science/spot-diff | Zou, Y., Jeong, J., Pemula, L., Zhang, D., and Dabeer, O. (2022). SPot-the-Difference Self-Supervised Pre-training for Anomaly Detection and Segmentation. ECCV 2022. https://doi.org/10.1007/978-3-031-20056-4_23. Data: VisA, licensed under CC BY 4.0. |

## Pretrained models and dictionaries

| Model | License (as stated at source) | Source | Attribution line |
|---|---|---|---|
| GPT-2 small (`gpt2`) | MIT (model card); OpenAI's repository uses a "Modified MIT License" that asks users to say when content was created with GPT-2 | https://huggingface.co/openai-community/gpt2 ; https://github.com/openai/gpt-2/blob/master/LICENSE | GPT-2 small, OpenAI (2019), via Hugging Face `openai-community/gpt2`, MIT license. |
| DistilBERT fine-tuned on SST-2 | Apache 2.0 (model card) | https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english | `distilbert-base-uncased-finetuned-sst-2-english`, Hugging Face, Apache License 2.0. |
| GPT-2 small sparse autoencoders | MIT (model card) | https://huggingface.co/jbloom/GPT2-Small-SAEs-Reformatted | `jbloom/GPT2-Small-SAEs-Reformatted`, Hugging Face, MIT license. |

The no-code labs also use hosted web tools (GAM Changer, LIT, Embedding Projector, Neuronpedia, CNN Explainer, Transformer Explainer). Their built-in data and models belong to the tools' owners, and nothing from them is stored here; for some (for example the Lending Club data in GAM Changer, SST-2 in LIT, the Word2Vec vectors in the Embedding Projector) no data license is stated at the source.

## Derived files committed to this repository

| File | Derived from | Changes |
|---|---|---|
| `labs/ch14-why-language-models-are-hard-to-explain/lab3/data/bloomberg_gpt_rankings.csv` | Bloomberg GPT resume-ranking data (Apache 2.0) | Selected and recomputed fields; see `NOTICE.md` and `build_runs_table.py` |
| `labs/ch25-explainability-in-production/lab1/weekly_monitor.csv` | Online Retail II (CC BY 4.0) | Weekly forecast and attribution statistics computed by Lab 25.2; no transaction rows |
| `labs/ch23-choosing-measuring-and-using-xai-tools/lab2/test_drive_results.json` | German Credit (CC BY 4.0) | Scores of explanation tools computed by Lab 23.2; no applicant rows |
| `labs/ch06-global-explanations/lab1/figures/*.png` | freMTPL2freq (CC0 on OpenML) | Charts of a model's results computed by Lab 6.2 |
| GPT-2 outputs and tables in Labs 15.1-15.3, 16.1, 16.2 and 18.1 | GPT-2 small (MIT) | Generated or computed with the lab notebooks; content created with GPT-2 |

All synthetic data are generated in the notebooks and carry no third-party license.
