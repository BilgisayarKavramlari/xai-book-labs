# Material B: logit lens versus a fitted affine lens

GPT-2 small; affine translators fitted by least squares on 9,216 tokens of GPT-2-generated text, scored on 1,024 held-out tokens (lab2/). KL divergence from the model's output distribution in bits (lower is closer), and the share of tokens where the lens's top guess equals the model's.

| layer | KL bits, logit lens | same top token, logit lens | KL bits, affine lens | same top token, affine lens |
|---|---|---|---|---|
| 0 | 70.219 | 0.006 | 4.611 | 0.192 |
| 1 | 9.298 | 0.113 | 3.948 | 0.220 |
| 2 | 8.244 | 0.113 | 3.646 | 0.252 |
| 3 | 7.561 | 0.125 | 3.434 | 0.271 |
| 4 | 7.058 | 0.148 | 3.107 | 0.286 |
| 5 | 6.651 | 0.151 | 2.895 | 0.289 |
| 6 | 6.237 | 0.171 | 2.576 | 0.315 |
| 7 | 5.731 | 0.199 | 2.193 | 0.360 |
| 8 | 5.217 | 0.256 | 1.735 | 0.410 |
| 9 | 4.521 | 0.348 | 1.173 | 0.507 |
| 10 | 3.640 | 0.451 | 0.689 | 0.615 |
| 11 | 1.674 | 0.607 | 0.277 | 0.752 |
| 12 | 0.000 | 1.000 | -0.000 | 1.000 |
