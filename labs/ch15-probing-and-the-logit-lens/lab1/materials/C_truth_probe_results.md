# Material C: truth probe results

GPT-2 small; 72 cities; statements of the form "The city of X is in Y." (plain) and "The city of X is not in Y." (negated), one true and one false of each per city; residual stream at the final period; cities held out in five folds (lab3/). Paraphrase: "X is a city located in Y." Accuracy unless stated. Chance is 0.5.

| layer | logistic (plain, held-out cities) | mass-mean (plain, held-out cities) | logistic on random GPT-2 | plain probe tested on negated | plain probe tested on paraphrase (accuracy) | plain probe tested on paraphrase (AUROC) | logistic trained on plain + negated |
|---|---|---|---|---|---|---|---|
| 0 | 0.492 | 0.499 | 0.492 | 0.521 | 0.542 | 0.500 | 0.495 |
| 1 | 0.597 | 0.535 | 0.479 | 0.139 | 0.639 | 0.740 | 0.499 |
| 2 | 0.758 | 0.590 | 0.507 | 0.194 | 0.521 | 0.763 | 0.569 |
| 3 | 0.829 | 0.695 | 0.472 | 0.007 | 0.632 | 0.842 | 0.646 |
| 4 | 0.820 | 0.758 | 0.492 | 0.083 | 0.708 | 0.808 | 0.744 |
| 5 | 0.904 | 0.828 | 0.527 | 0.021 | 0.646 | 0.933 | 0.887 |
| 6 | 0.904 | 0.834 | 0.535 | 0.021 | 0.514 | 0.917 | 0.893 |
| 7 | 0.910 | 0.917 | 0.529 | 0.479 | 0.500 | 0.889 | 0.925 |
| 8 | 0.910 | 0.932 | 0.541 | 0.340 | 0.500 | 0.823 | 0.904 |
| 9 | 0.904 | 0.932 | 0.508 | 0.451 | 0.500 | 0.813 | 0.921 |
| 10 | 0.917 | 0.917 | 0.509 | 0.132 | 0.500 | 0.812 | 0.914 |
| 11 | 0.910 | 0.853 | 0.508 | 0.139 | 0.500 | 0.797 | 0.876 |
| 12 | 0.917 | 0.874 | 0.508 | 0.035 | 0.500 | 0.842 | 0.858 |

Other results from the same notebook:

- GPT-2 small gives the right country a higher probability than the wrong one for 71 of 72 cities after "The city of X is in".
- Mean log probability of the country after "is in": right -6.70, wrong -10.60. After "is not in": right -5.22, wrong -10.26.
- Correlation of the layer-8 probe score with the model's log probability of the country: 0.73 (plain statements), 0.82 (negated statements).
- Control task (a random bit for each country; the probe must predict the bit of the country named): accuracy 0.82 to 0.94 in layers 1 to 9.
