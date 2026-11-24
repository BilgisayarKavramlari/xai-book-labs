# Lab 19.1: The Citation Audit

Chapter 19, Explaining LLM Applications: Citations, Traces and Agents · No code (browser and worksheet) · About 60 minutes · Last checked: 2026-11-24

## Goal

Audit the citations of two AI assistants that show their sources. For each cited sentence, decide whether the cited page supports it; compute citation recall and citation precision by hand (Gao et al., 2023); and label each answer grounded, ungrounded or misgrounded (Magesh et al., 2025).

## Tools

A web browser. Any two AI assistants or AI search tools that display sources next to their answers. Products change quickly: write down the product name, the date and, if shown, the model or mode you used. Use only services you are allowed to use; do not enter personal data.

## Data and license

You read public web pages only. Choose questions about public rules in a sector you know: for example, a city's rules for small businesses, a government benefit's eligibility, a parcel carrier's published refund policy, an airline's published baggage rules, or a bank's published fee schedule. Avoid questions whose answer depends on your personal situation.

## Steps

1. Write five questions. At least two should have a precise answer (a number, a deadline, a yes or no), and one should be a question where rules differ between places (a jurisdiction trap).
2. Ask each question to both assistants. Save each answer (copy the text, note the date).
3. Split each answer into sentences. For each sentence, record its citations (none, one or several).
4. Open every cited page. For each sentence, judge: **supported** (the cited pages together say this), **partly** (some of it), **not supported** (the pages do not say this, or say the opposite), **uncited** (no citation). **Checkpoint 1:** every sentence of every answer has one of the four labels.
5. For each citation in a sentence with several citations, ask: does this page support the sentence on its own, and do the other pages already support it without this one? If it does not support the sentence alone and the others suffice, mark it **irrelevant**.
6. Compute, per assistant: citation recall = supported sentences / all sentences; citation precision = citations that are not irrelevant and belong to a supported sentence / all citations. Count "partly" as not supported, and say so. **Checkpoint 2:** four numbers (two per assistant), each between 0 and 1.
7. Label each answer: **grounded** (all key statements cite supporting pages), **ungrounded** (a key statement has no citation), **misgrounded** (a key statement cites a page that does not support it or does not apply, for example another city's rule).
8. Pick the single failure that would matter most to a real user and describe it.

## Worksheet

| Q | Assistant | Sentence | Citations | Label (supported, partly, not supported, uncited) | Irrelevant citations |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

| Assistant | Sentences | Supported | Citation recall | Citations | Precise citations | Citation precision | Grounded / ungrounded / misgrounded answers |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |

## Questions

1. You were the judge. Where was judging hard (partial support, numbers, negation, outdated pages, another jurisdiction)? How would an automatic entailment judge do on those cases?
2. Your audit checks support, not use. Describe one answer where you suspect the citation was attached after the fact (a correct citation that the answer did not need). What experiment would test it? (Lab 19.2 runs one.)
3. Which explanation feature of the two products made checking easiest, and which made it hardest?

## What to hand in

The completed worksheet, the four scores, the answer labels, and one paragraph on the most serious failure, written for the product team.

## Expected results

Scores vary by product, date and question. Expect some sentences with no citation, some citations to pages that only partly support the sentence, and at least one jurisdiction or date problem if you included a jurisdiction trap. A perfect score on five questions does not show that the assistant is reliable; it shows that these answers were supported.

## Self-check

If your precision is higher than your recall, check that you scored citations of unsupported sentences as 0, as the definition requires. If every answer is "grounded", reread step 7: a key statement without a citation makes an answer ungrounded even if the rest is supported.

## References

Gao, T., Yen, H., Yu, J., and Chen, D. (2023). Enabling large language models to generate text with citations. *EMNLP 2023*. https://doi.org/10.18653/v1/2023.emnlp-main.398

Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., and Ho, D. E. (2025). Hallucination-free? Assessing the reliability of leading AI legal research tools. *Journal of Empirical Legal Studies, 22*(2), 216-242. https://doi.org/10.1111/jels.12413
