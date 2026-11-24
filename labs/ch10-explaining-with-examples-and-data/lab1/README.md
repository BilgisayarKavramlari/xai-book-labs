# Lab 10.1: Because You Bought: Auditing Example Explanations in the Wild

Chapter 10, Explaining with Examples and Training Data · No code · About 45 minutes · Last checked: 2026-11-24

## Goal

Collect five example-based explanations that real services show people ("because you bought", "customers who viewed this also viewed", "because you watched", "travelers like you chose") and judge each one with the questions of Chapter 10: which question it answers, whether it could be faithful to the system that made the recommendation, and what it reveals about other people.

## Tools

A web browser and your own accounts on shopping, streaming, music, travel or news services. Do not create new accounts for this lab and do not share screenshots that show your personal data; describe what you see in words instead. If you have no suitable accounts, use services that show "customers also bought" sections on public product pages without signing in.

## Steps

1. **Collect.** Find five explanations from at least three different services. For each, copy the exact wording, note where it appeared (product page, home page, email, cart) and what it recommended.
2. **Similarity or attribution?** For each, decide whether it points to similar items or people (similarity) or claims that particular data caused the recommendation (attribution). Checkpoint: almost every explanation you find will be a similarity explanation; attribution explanations are rarely shown to customers.
3. **Item-based or user-based?** Decide whether the wording refers to items ("because you bought X") or to people ("customers like you"). Write what kind of model would make that wording faithful (Chapter 10, "Testing an Example-Based Explanation").
4. **Faithful?** For each, write one way the explanation could be untrue for the system that actually decided, for example a "customers like you" sentence attached to a model that does not use similar customers, or a "because you watched X" that names only one of many inputs.
5. **What does it reveal?** Ask how many people could stand behind it. Could the explanation reveal another person's behavior if the group were small (a niche product, a small town, a small company account, a shared household account)?
6. **Persuade or inform?** Using Herlocker et al. (2000) as a reference point, say whether the explanation is designed to persuade, to inform, or both, and what would have to change for it to inform.
7. Fill in the worksheet below.

## Worksheet

| # | Service type | Exact wording | Similarity or attribution | Item- or user-based | One way it could be unfaithful | Who could it reveal? | Persuade or inform? |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

## Expected results

Most explanations will be item-based ("because you bought or watched X") or co-purchase statements ("customers who bought this also bought"). User-based "people like you" explanations are rarer, partly because of the disclosure risk discussed in the chapter. Few services state how many people stand behind a co-purchase statement.

## What to hand in

The completed worksheet and a two-sentence disclosure rule for one of your explanations: a minimum group size and a fallback wording when the group is too small.

## Self-check

If every row in your "Who could it reveal?" column says "nobody", look again at explanations about niche items or about people. If you marked an explanation as attribution, check that it really claims a causal role for particular data rather than resemblance.
