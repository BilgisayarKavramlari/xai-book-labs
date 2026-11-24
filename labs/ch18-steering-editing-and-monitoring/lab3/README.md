# Lab 18.3: Edit a Memory, Count the Ripples

Chapter 18, Steering, Editing and Monitoring Models · Run-only notebook · About 45 minutes · Last checked: 2026-11-24 (end-to-end run in about 2 seconds)

## Goal

Edit one fact in a toy key-value memory with a plain rank-one update and a covariance-weighted (ROME-style) update; measure efficacy, generalization, specificity and a ripple the edit misses; then apply 80 edits in sequence and watch earlier edits erode.

## Tools and versions

Python 3.10, numpy 2.2.6 (the main environment, `env/requirements.txt`). Notebook: `edit_a_memory.ipynb`. No data download: all keys and values are drawn from a seeded random generator.

## What the toy is and is not

The memory is a 128 by 128 matrix that stores 100 subjects' facts exactly (each fact is one of 20 value vectors). Keys are correlated, as real representations are, and a background sample of 20,000 keys gives the covariance used by the ROME-style update. It shows the mechanics of rank-one editing and the trade-offs to measure. It does not reproduce ROME or MEMIT results on real language models (Meng et al., 2022; Meng et al., 2023).

## Steps and checkpoints

1. Run the cells in order.
2. **Checkpoint 1:** both edits store the new fact (efficacy True) and every other subject still reads its old fact; the plain update generalizes to noisy paraphrases at 0.90 against 0.58 for the ROME-style update, while the ROME-style update disturbs the other subjects' stored values less (mean drift 0.137 against 0.198).
3. **Checkpoint 2:** when subject 1 is defined to depend on subject 0, editing subject 0 leaves subject 1 with its old fact: the edit misses the ripple.
4. **Checkpoint 3:** after 80 sequential edits, 0.45 of earlier plain edits still hold and untouched facts drop to 0.85; with the ROME-style update, 0.85 of earlier edits hold.

## Questions

1. Why can an edit be perfect on its target and still be a bad edit?
2. Where would dependencies like the one in Checkpoint 2 come from in a real language model, and how would you test for them?
3. A bank wants to correct one outdated product fact in its assistant. What do you advise, editing or retrieval at answer time, and why?

## What to hand in

An edit evaluation table (efficacy, generalization, specificity, drift, ripple, after 1 and after 80 edits, for both updates) and three sentences of advice to the bank.

## Self-check

If your advice recommends editing because "efficacy was 100 percent", look again at Checkpoints 2 and 3. Chapter 18 summarizes the real-model evidence (Hase et al., 2023; Cohen et al., 2024; Gupta et al., 2024).
