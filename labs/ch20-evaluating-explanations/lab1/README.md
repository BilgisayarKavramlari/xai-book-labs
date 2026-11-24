# Lab 20.1: Grade the Evidence

Chapter 20, Is the Explanation Any Good? · No code · About 45 minutes · Last checked: 2026-11-24

## Goal

Judge three short evaluation write-ups, for a credit model, a radiology tool and a customer-service chatbot, against the evaluation report checklist of Chapter 20, and write the questions you would send back to each team.

## Tools

This worksheet and a pen, a document or a spreadsheet. Optional: a web browser to look at the public OpenXAI leaderboard pages (https://open-xai.github.io/, "Leaderboard"; the pages were online on 2026-11-24) and see how a benchmark reports results per dataset, model and metric.

## Data

None. The three write-ups below are **invented for this lab**. They describe no real company, product or study, and every number in them is fictional.

## The checklist

Score each write-up on the ten items, 2 (done well), 1 (partly) or 0 (missing):

1. The question the explanation must answer, and for whom, is stated.
2. The model, data and version tested are named.
3. At least one faithfulness test is matched to that question.
4. The test's settings are given (replacement value or reference, background, samples, seeds).
5. Every score is compared with a random baseline.
6. The result is checked under at least one alternative setting.
7. Stability is measured under the perturbations that matter in use.
8. Agreement with at least one other reasonable method is reported.
9. Manipulation risk is considered (who controls the model, the data and the explanation).
10. The verdict is given per intended use, with a date and a trigger for re-testing.

## Write-up A: reason codes for a credit model (fictional)

"Our gradient-boosted credit model produces four reason codes per declined applicant using SHAP. We validated the explanations by asking ten loan officers to rate 50 reason-code sets on a five-point clarity scale; the average was 4.4. The top reason matched the officers' expectation in 88 percent of cases. SHAP is the industry standard and is theoretically grounded in game theory, so its attributions are faithful by construction. Background: training data sample. Approved for production."

## Write-up B: heat maps for a radiology triage tool (fictional)

"The tool highlights the region of a chest radiograph that drove its 'urgent' flag. On 300 positive studies, the hottest pixel fell inside the radiologist-marked abnormality in 71 percent of cases. In a deletion test (top 10 percent of pixels set to black) the urgent probability fell by 0.42 on average. The heat maps were identical across three runs. We recommend showing the maps to radiologists to help them find the abnormality."

## Write-up C: citations in a customer-service chatbot (fictional)

"Each chatbot answer cites the help-center article it is based on. On 200 test questions, an automated judge found that 93 percent of cited articles support the sentence they are attached to. When we removed the cited article from the retrieved context, the answer changed in 61 percent of cases. We consider the citations faithful."

## Steps

1. Read Chapter 20, sections "Why 'It Looks Right' Is Not a Test" through "Benchmarks, Toolkits and the Evaluation Report".
2. **Checkpoint 1:** score write-up A on the ten items. Hint: clarity ratings are a usefulness proxy at best (Chapter 22), and "faithful by construction" is a claim about the method, not a test on this model.
3. **Checkpoint 2:** score write-up B. Hint: localization is not faithfulness (the Real Story box on Arun et al., 2021), black pixels are far from real radiographs, a deterministic method is always identical across runs, and there is no random baseline for the 0.42.
4. **Checkpoint 3:** score write-up C. Hint: support and use are different questions (Chapter 19), the judge itself needs validation, and "changed in 61 percent of cases" needs a baseline: how often does the answer change when an uncited article is removed?
5. Optional: open the OpenXAI leaderboard and note which metrics it reports for faithfulness and stability, and what it does not tell you about your own model.
6. Write three questions to send back to each team.

## Expected results

No write-up scores well. A typical grading gives A about 4 to 6 points of 20 (question and version partly stated; no faithfulness test, no baseline, no stability), B about 7 to 9 (a removal test is present but with an off-manifold replacement and no baseline; localization is reported instead of faithfulness; the stability claim is empty) and C about 8 to 10 (support and an ablation are both measured, but without a baseline, a validated judge or a verdict per use). Exact scores vary; what matters is the reasons.

## What to hand in

A one-page table: the three write-ups in columns, the ten items in rows, your scores, and the three questions you would send to each team.

## Self-check

For each question you wrote, ask: could the team answer it with a number from a test on their own model? If not, sharpen it. "Is SHAP reliable?" is a weak question; "What is the deletion area of your SHAP reason codes against a random ranking, with the background you used and with a second background?" is a strong one.
