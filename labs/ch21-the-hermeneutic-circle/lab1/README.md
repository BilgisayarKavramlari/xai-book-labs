# Lab 21.1: Reading a Refusal as a Text

Chapter 21, The Hermeneutic Circle · No code · About 50 minutes · Last checked: 2026-11-24

## Goal

Carry out a part and whole reading of one refused credit applicant, in the five moves of Chapter 21, using only the printed packet below. You will treat every sentence of an explanation as a claim, look for evidence that could not exist, and record how your reading changes when you move from the part to the wholes.

## Tools

Paper or a text editor. Everything you need is in this README. The numbers in the packet were computed by the notebooks of Labs 21.2 and 21.3 (German Credit, a random forest of 200 trees, fixed seeds); you do not need to run them.

## Data and license

German Credit (Statlog), Hofmann (1994), UCI Machine Learning Repository, https://doi.org/10.24432/C5NC77, CC BY 4.0 as listed by UCI. 1,000 applicants from Germany, amounts in Deutsche Mark (DM), label good or bad credit risk. Old and coarse data: use them to learn a method, not to judge lending. See `data/german-credit.md`.

## The packet

**A. The applicant (we call him Kofi).** Age 33, male, single, skilled employee, at least 7 years in the current job, renting, 2 dependents, 2 existing credits at this bank, no telephone registered, foreign worker: yes. Request: 950 DM over 15 months for a new car, installment rate 4 (the highest band). Checking account: below 0 DM. Savings: below 100 DM. Credit history: "no credits taken / all credits paid back duly". Model output: probability of bad risk 0.668. Decision rule: refuse at 0.5 or more. Decision: refused.

**B. Explanation 1 (KernelSHAP, a Shapley value method; Chapter 8).** Largest contributions to the risk, relative to an average applicant: checking account below 0 DM, +0.161; credit history "no credits/all paid", +0.072; loan amount 950 DM, +0.043.

**C. Explanation 2 (LIME; Chapter 7).** Largest weights toward bad risk: checking account below 0 DM, +0.106; purpose new car, +0.039; credit history "no credits/all paid", +0.038.

**D. Explanation 3 (HermAI 0.1.8 narrative, as printed by the library).**

> Model predicted class '1' with 66.83% confidence.
> Key Feature Contributions (Local Importance):
> - Feature 'checking_status' decreases the probability.
> - Feature 'duration' increases the probability.
> - Feature 'purpose' decreases the probability.
> - Feature 'own_telephone' decreases the probability.
> - Feature 'credit_amount' decreases the probability.
> Counterfactual Analysis: To flip the prediction to class '0', one of the closest possibilities found is: change 'checking_status' from 1.00 to 0.00; 'duration' from 15.00 to 13.16; 'credit_history' from 4.00 to 3.00; 'purpose' from 4.00 to 2.00; 'credit_amount' from 950.00 to 800.80; 'savings_status' from 2.00 to 3.00; 'installment_commitment' from 4.00 to 3.98; 'residence_since' from 3.00 to 3.05; 'age' from 33.00 to 30.04; 'housing' from 2.00 to 1.00; 'existing_credits' from 2.00 to 2.13; 'num_dependents' from 2.00 to 1.96.

(Categories are integer codes in the library's input; for example `checking_status` 1 is "below 0 DM".)

**E. The whole, global.** A depth-four tree fitted to the forest's outputs explains Kofi's case with: checking account (raises the risk), purpose (raises), employment (lowers slightly). The same model, summarized by a depth-three decision tree, splits first on the checking account, then on purpose and loan amount.

**F. The whole, regional.** A tree fitted only to the quarter of training applicants most similar to Kofi explains his case with: checking account (raises), loan amount (raises), credit history (raises).

**G. On-horizon tests.** Replacing one feature at a time with the values of the 30 most similar training applicants changes Kofi's predicted risk on average by: checking account -0.130, credit history -0.073, loan amount -0.064, purpose -0.051, duration +0.015. (A minus sign means his own value had pushed the risk up.)

**H. The training data.** Bad-risk rate by credit history: critical account 0.152 (198 applicants); existing credits paid 0.313 (374); delayed previously 0.354 (65); all paid at this bank 0.641 (39); no credits taken or all paid back duly 0.625 (24). By loan amount: up to 1,000 DM 0.387 (75); 1,000 to 2,000 DM 0.262 (225); 2,000 to 4,000 DM 0.233 (232); 4,000 to 8,000 DM 0.339 (124); above 8,000 DM 0.591 (44). Overall: about 0.30.

## Steps

1. **Pre-understanding (5 minutes).** Before reading B to D, write three sentences: why do you expect Kofi was refused? What would a "good" reason look like to a credit officer?
2. **The part (10 minutes).** List every sentence in B, C and D as a claim in the form "Kofi's value of X pushed the risk up/down". **Checkpoint 1:** you should have nine direction claims (three per explainer) plus one counterfactual claim.
3. **Suspicion (10 minutes).** Use G to mark each claim verified or failed. A claim passes if the sign of its stated direction matches the measured effect (risk up means a negative number in G). **Checkpoint 2:** all three KernelSHAP claims pass; all three HermAI claims you can test (checking account, duration, purpose) fail.
4. **The horizon (5 minutes).** Go through the counterfactual in D. Which changed values could no applicant have? **Checkpoint 3:** at least four (3.98 installment rate, 3.05 years at residence, 2.13 existing credits, 1.96 dependents); also count how many features it asks Kofi to change (12).
5. **The wholes (10 minutes).** Compare B with E and with F. With how many features, and signs, does B agree with each whole? **Checkpoint 4:** one of three with E, three of three with F. Write two sentences on what this says about Kofi's case.
6. **The data and the setting (10 minutes).** Use H to explain the two reasons that look strange. Then decide: would you send the credit-history reason to Kofi? Why or why not?

## What to hand in

One page in five moves: your pre-understanding; the claims with their verdicts; the impossible evidence; the comparison with the two wholes; and what changed in your reading, ending with the two sentences you would send Kofi and the test each passed. This page is a draft of Dossier artifact 21 (part-and-whole reading of one decision).

## Self-check

If you marked HermAI's "checking_status decreases the probability" as verified, reread G: the measured effect is -0.130, so his checking status pushed the risk *up*. If you concluded that KernelSHAP is "the right explainer" in general, remember that this is one applicant on one dataset; Lab 21.3 measures 100.
