# Lab 16.1 Worksheet: Read a Patching Experiment Before You Run One

Name: ____________________  Date: ____________

## Part A: Predict (before opening any table)

Clean prompt: "When Mary and John went to the store, John gave a drink to" (answer: Mary).
Corrupted prompt: "When Mary and John went to the store, Mary gave a drink to" (answer: John).

A1. At which token positions do you expect the information that distinguishes the two prompts to sit in early layers? In late layers?

A2. Roughly in which layers do you expect it to move to the last position?

A3. What kinds of attention heads do you expect to matter? Do you expect any head to push *against* the correct answer?

A4. If the three most important heads were removed, what would happen to the model's preference for Mary?

## Part B: Look at attention

B1. Which earlier tokens does the last token attend to most, in two or three late-layer heads you inspected?

B2. Can you tell from the attention view alone whether those heads change the output? Why or why not?

## Part C: Read the results

C1. `residual_patching.csv`: describe the S2 and END columns in two sentences. What moves, and when?

C2. Why does patching the S2 position in layer 0 restore the full logit difference? Does that mean layer 0 computes the answer?

C3. `head_denoising.csv`: list the six heads with the largest absolute values and their signs. Which are negative, and what does a negative value mean here?

C4. Compare `head_denoising.csv` with `head_noising.csv`. Name one head whose rank changes clearly and suggest one structural reason (see the chapter's Deep box on AND and OR).

C5. Compare `head_denoising.csv` with `head_denoising_abc.csv`. What question does each corruption ask?

C6. `knockout_dla.csv`: which heads increase their direct contribution after the knockout, and what happens to head 10.7? What does this mean for judging a head by ablation alone?

C7. Compare your predictions in Part A with the results. What did you miss?

## Part D: Design your own patching experiment (one page)

| Item | Your answer |
|---|---|
| Behavior and model | |
| Clean prompt (and how you will generate at least 30 of them) | |
| Corrupted prompt, and why it is a fair control | |
| Metric (and how it is normalized) | |
| Direction(s): denoising, noising or both | |
| Granularity: residual stream, layers, heads, positions | |
| Expected result | |
| One test that could prove your conclusion wrong | |
| What the experiment will not show | |
