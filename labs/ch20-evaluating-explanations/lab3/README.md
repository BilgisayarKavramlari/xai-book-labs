# Lab 20.3: Comprehensiveness and Sufficiency for a Sentiment Classifier

Chapter 20, Is the Explanation Any Good? · Run-only notebook, language model environment · About 45 minutes · Last checked: 2026-11-24 (end-to-end run in about five minutes on a laptop CPU, after the model download)

## Goal

Score four token attribution methods for a small open sentiment classifier with the ERASER measures, comprehensiveness and sufficiency (DeYoung et al., 2020), and see how the way tokens are removed changes the verdict.

## Tools and versions

`comprehensiveness_sufficiency.ipynb`; Python 3.10, torch 2.6.0, transformers 4.57.6, numpy 1.26.4. Use the language model environment: `env/requirements-llm.txt`, kernel `xai-llm-venv`. No new package is needed. The methods are written out in about twenty lines of PyTorch.

## Model and data

- Model: `distilbert-base-uncased-finetuned-sst-2-english` from the Hugging Face hub (a DistilBERT model fine-tuned on the SST-2 movie-review sentiment data; Apache 2.0 license on its model card, checked 2026-11-24). About 270 MB, downloaded on first use.
- Data: forty short movie-review sentences written for this lab (in the notebook). No download and no personal data.

## Steps

1. Open the notebook with the `xai-llm-venv` kernel and run the cells in order. Run Part A first on a good connection; the model downloads once.
2. **Checkpoint 1 (Part A):** 20 of 40 sentences predicted positive; mean confidence 0.9997.
3. **Checkpoint 2 (Part B):** for sentence 1 ("The plot was predictable but the acting was wonderful."), predicted positive with probability 0.9998. Top three tokens: attention "wonderful", ".", "acting"; gradient x input "acting", "was", "but"; Integrated Gradients "wonderful", "acting", "but"; occlusion "wonderful", "but", ".".
4. **Checkpoint 3 (Part C):** comprehensiveness and sufficiency (area over the perturbation curve, bins of 1, 5, 10, 20 and 50 percent), deleting tokens / replacing them with `[MASK]`:

   | Method | Comp. (delete) | Suff. (delete) | Comp. (mask) | Suff. (mask) |
   |---|---|---|---|---|
   | Attention (last layer, CLS row) | 0.242 | 0.105 | 0.201 | 0.209 |
   | Gradient x input | 0.034 | 0.306 | 0.029 | 0.348 |
   | Integrated Gradients | 0.256 | 0.072 | 0.246 | 0.075 |
   | Occlusion | 0.249 | 0.053 | 0.238 | 0.073 |
   | Random | 0.069 | 0.266 | 0.052 | 0.292 |

5. **Checkpoint 4 (Part D):** the method with the highest comprehensiveness per sentence (delete): occlusion 19, Integrated Gradients 14, gradient x input 4, attention 3.

## Expected results

The numbers above with the pinned versions (seeded; another torch build or CPU may change the last digit). Lessons: occlusion and Integrated Gradients beat the random ranking on both measures; attention does well on comprehensiveness but its sufficiency nearly doubles, close to random, when tokens are masked instead of deleted; gradient x input is worse than random here (the classifier's outputs are saturated, and a single gradient at the input says little about what the model used); and no method is best on every sentence. Occlusion was itself computed with `[MASK]`, so the mask-based score shares its assumption.

## Questions

The notebook ends with five questions. Answer them in your hand-in.

## What to hand in

The score table under both removal methods and a paragraph on which method you would trust for which question, with its settings and caveats.

## Self-check

If your paragraph names a "best method" without saying how tokens were removed and how it compared with the random row, add both. A sufficiency score is only meaningful next to the random baseline and the removal method.
