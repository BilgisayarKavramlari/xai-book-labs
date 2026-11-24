# Material A: logit-lens tables for GPT-2 small

Computed with the notebook in lab2/ (GPT-2 small, TransformerLens 2.18.0, CPU). For each prompt: the top three guesses of the logit lens for the next token at the last position, layer by layer (0 = embeddings, 12 = the model's output), with their probabilities, and the rank of the model's final answer at each layer (0 = top).

## Prompt 1: "To reset your password, click the link we sent to your"

Final answer: `' email'`

| Layer | Guess 1 | Guess 2 | Guess 3 | Rank of final answer |
|---|---|---|---|---|
| 0 | `' your'` 0.83 | `'your'` 0.16 | `' mathemat'` 0.01 | 18053 |
| 1 | `' own'` 1.00 | `' favorite'` 0.00 | `' body'` 0.00 | 367 |
| 2 | `' own'` 1.00 | `' favorite'` 0.00 | `' personal'` 0.00 | 123 |
| 3 | `' own'` 1.00 | `' personal'` 0.00 | `' browser'` 0.00 | 20 |
| 4 | `' own'` 1.00 | `' favorite'` 0.00 | `' browser'` 0.00 | 7 |
| 5 | `' own'` 1.00 | `' respective'` 0.00 | `' browser'` 0.00 | 5 |
| 6 | `' own'` 0.94 | `' email'` 0.02 | `' respective'` 0.01 | 1 |
| 7 | `' email'` 0.58 | `' own'` 0.27 | `' inbox'` 0.03 | 0 |
| 8 | `' email'` 0.35 | `' mailbox'` 0.34 | `' inbox'` 0.23 | 0 |
| 9 | `' email'` 0.71 | `' inbox'` 0.26 | `' phone'` 0.01 | 0 |
| 10 | `' email'` 0.86 | `' inbox'` 0.12 | `' Gmail'` 0.00 | 0 |
| 11 | `' email'` 0.73 | `' inbox'` 0.19 | `' account'` 0.05 | 0 |
| 12 | `' email'` 0.68 | `' e'` 0.06 | `' account'` 0.02 | 0 |

## Prompt 2: "The Eiffel Tower is located in the city of"

Final answer: `' London'`

| Layer | Guess 1 | Guess 2 | Guess 3 | Rank of final answer |
|---|---|---|---|---|
| 0 | `' destro'` 0.60 | `' mathemat'` 0.26 | `' challeng'` 0.12 | 21746 |
| 1 | `' the'` 0.73 | `' course'` 0.05 | `' a'` 0.03 | 706 |
| 2 | `' the'` 0.83 | `' course'` 0.05 | `' a'` 0.02 | 443 |
| 3 | `' the'` 0.68 | `' course'` 0.17 | `' a'` 0.02 | 86 |
| 4 | `' the'` 0.63 | `' course'` 0.08 | `' a'` 0.01 | 167 |
| 5 | `' the'` 0.30 | `' La'` 0.07 | `' course'` 0.04 | 313 |
| 6 | `' England'` 0.08 | `' La'` 0.05 | `' the'` 0.04 | 56 |
| 7 | `' South'` 0.05 | `' Georgia'` 0.05 | `' East'` 0.05 | 44 |
| 8 | `' Ing'` 0.22 | `' San'` 0.06 | `' Chicago'` 0.04 | 17 |
| 9 | `' Chicago'` 0.11 | `' Rome'` 0.09 | `' London'` 0.08 | 2 |
| 10 | `' London'` 0.35 | `' Amsterdam'` 0.16 | `' Paris'` 0.15 | 0 |
| 11 | `' London'` 0.19 | `' Paris'` 0.14 | `' Amsterdam'` 0.12 | 0 |
| 12 | `' London'` 0.07 | `' Paris'` 0.07 | `' Amsterdam'` 0.04 | 0 |

## Prompt 3: "The capital of Japan is the city of"

Final answer: `' Tokyo'`

| Layer | Guess 1 | Guess 2 | Guess 3 | Rank of final answer |
|---|---|---|---|---|
| 0 | `' destro'` 0.65 | `' mathemat'` 0.26 | `' challeng'` 0.08 | 42622 |
| 1 | `' the'` 0.70 | `' course'` 0.06 | `' a'` 0.03 | 1783 |
| 2 | `' the'` 0.80 | `' course'` 0.06 | `' a'` 0.02 | 1104 |
| 3 | `' the'` 0.66 | `' course'` 0.20 | `' a'` 0.02 | 982 |
| 4 | `' the'` 0.71 | `' course'` 0.12 | `' a'` 0.01 | 949 |
| 5 | `' the'` 0.66 | `' its'` 0.05 | `' course'` 0.02 | 932 |
| 6 | `' the'` 0.39 | `' its'` 0.06 | `' course'` 0.02 | 1413 |
| 7 | `' the'` 0.21 | `' Ar'` 0.05 | `' Giants'` 0.04 | 262 |
| 8 | `' the'` 0.09 | `' Ar'` 0.05 | `' honor'` 0.05 | 345 |
| 9 | `' San'` 0.09 | `' Tokyo'` 0.07 | `' the'` 0.05 | 1 |
| 10 | `' Tokyo'` 0.86 | `' Osaka'` 0.06 | `' Japan'` 0.04 | 0 |
| 11 | `' Tokyo'` 0.68 | `' Osaka'` 0.10 | `' Kyoto'` 0.09 | 0 |
| 12 | `' Tokyo'` 0.10 | `' Kyoto'` 0.09 | `' Osaka'` 0.05 | 0 |

## Prompt 4: "I would like a refund because the package arrived"

Final answer: `' in'`

| Layer | Guess 1 | Guess 2 | Guess 3 | Rank of final answer |
|---|---|---|---|---|
| 0 | `' arrived'` 1.00 | `' mathemat'` 0.00 | `' arrive'` 0.00 | 30127 |
| 1 | `' arrived'` 0.36 | `' arrive'` 0.14 | `' arrives'` 0.10 | 5 |
| 2 | `' arrived'` 0.23 | `' upon'` 0.10 | `' at'` 0.09 | 4 |
| 3 | `' shipping'` 0.24 | `' here'` 0.16 | `' upon'` 0.08 | 6 |
| 4 | `' here'` 0.43 | `' shipping'` 0.09 | `' at'` 0.08 | 4 |
| 5 | `' here'` 0.33 | `' at'` 0.30 | `' in'` 0.03 | 2 |
| 6 | `' here'` 0.18 | `' at'` 0.17 | `' upon'` 0.06 | 3 |
| 7 | `' at'` 0.17 | `' here'` 0.06 | `' unexpectedly'` 0.06 | 6 |
| 8 | `' at'` 0.15 | `' properly'` 0.11 | `' unexpectedly'` 0.11 | 5 |
| 9 | `' safely'` 0.16 | `' promptly'` 0.14 | `' yesterday'` 0.11 | 17 |
| 10 | `' promptly'` 0.45 | `' unexpectedly'` 0.08 | `' sooner'` 0.06 | 20 |
| 11 | `' promptly'` 0.34 | `' yesterday'` 0.20 | `' late'` 0.12 | 16 |
| 12 | `' in'` 0.11 | `' on'` 0.06 | `' with'` 0.04 | 0 |
