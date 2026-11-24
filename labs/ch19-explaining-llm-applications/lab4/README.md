# Lab 19.4: Is the Narrative Faithful to the Numbers?

Chapter 19, Explaining LLM Applications: Citations, Traces and Agents · Run-only notebook, optional chatbot part · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 2 seconds on a laptop CPU)

## Goal

Compute exact contributions for a small sales forecast, then check written narratives about them automatically: are the named factors in the model, are directions and numbers right, and is the largest factor named first? Find what such checks catch and what they miss.

## Tools and versions

Python 3.10 with numpy 2.2.6 and pandas 2.3.3 (`env/requirements.txt`; Jupyter kernel `xai-lab-venv`). Notebook: `is_the_narrative_faithful.ipynb`. For the optional part, a browser and any chatbot you are allowed to use (note its name and the date).

## Data

Synthetic: 60 months of sales for an invented importer, generated in the notebook from season, exchange rate (local currency per dollar), price change, promotion months and active customers, with a fixed seed.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** contributions to next January's forecast relative to an average month: fx_rate about -20.4, season about -9.1, promotion about +5.3, active_customers about +0.4, price_change about -0.35.
3. **Checkpoint 2:** of the six prepared narratives, N1 passes every check; N2 fails directions; N3 fails numbers and order; N4 fails "factors in model". N5 (a faithful paraphrase) and N6 (vague, with no checkable claim) both pass.
4. Optional: copy the printed table into a chatbot, ask for a three-sentence explanation for a small business owner using "units", paste two answers into the last cell and rerun it.

## Expected results

Checkpoints 1 and 2 exactly (deterministic). Chatbot narratives vary; record which errors the checker caught and which it missed.

## Questions

1. N6 passes every check. What does that tell you about what the checks measure? Add one check that would fail N6.
2. Which narrative errors are most dangerous for a business owner, and which do the four checks miss?
3. Write a rule of three or four lines for when an LLM-written narrative may be shown to a user without human review.

## What to hand in

The check grid for at least six narratives (the prepared ones, or four prepared and two from a chatbot), a list of the errors the checker missed, and your rule.

## Self-check

If your rule says "when all four checks pass", reread Question 1: a narrative that says nothing passes too. A good rule requires that the narrative makes the key claims, not only that it makes no wrong ones.
