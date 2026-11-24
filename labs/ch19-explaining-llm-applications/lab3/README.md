# Lab 19.3: Audit an Agent Trace

Chapter 19, Explaining LLM Applications: Citations, Traces and Agents · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in about 3 seconds on a laptop CPU)

## Goal

Read traces from a simulated parcel-support agent before and after an update, locate the steps that changed, and confirm which change mattered by replaying the same conversation with one component restored at a time.

## Tools and versions

Python 3.10 with pandas 2.3.3 and matplotlib 3.10.9 (`env/requirements.txt`; Jupyter kernel `xai-lab-venv`). Notebook: `audit_an_agent_trace.ipynb`. No model download: the agent's "model" is a set of scripted rules, so every run is reproducible.

## Data

None to download. The agent, its tools, queue names and conversation are invented for teaching. The simulation is not the system of any real company, including the DPD case discussed in Chapter 19, whose design has not been published. Span and attribute names follow the OpenTelemetry semantic conventions for generative AI where they exist (for example `gen_ai.operation.name`, `gen_ai.tool.name`; status: development, checked 2026-11-24); application-specific attributes start with `app.`.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** version 1 produces 6 spans and hands the customer to a person on the first turn. Version 2 produces 11 spans over three turns; its handoff span has status ERROR ("queue not found") and its last reply contains `[profanity]`.
3. **Checkpoint 2:** the trace comparison shows three differences: the handoff error, zero `output_guardrail` spans in version 2 (one in version 1), and a new prompt version (p-8 instead of p-7).
4. **Checkpoint 3:** replays: restoring the guardrail alone stops the profanity but nobody is handed over (3 turns); fixing the handoff queue alone ends the conversation on turn 1 with a handoff; restoring the old prompt version changes nothing.
5. Optional: the last cell writes the spans to `traces_ch19_lab3.jsonl` (17 lines). Think about which attributes you would remove before sharing a real trace.

## Expected results

Exactly the results above (the simulation is deterministic).

## Questions

1. Which of the three differences would you have suspected first from the customer's screenshots alone? Which did the replay show to matter?
2. Is "no guardrail span" evidence that the guardrail did not run, or only that it was not recorded? What design rule removes the ambiguity?
3. Write the public explanation you would give after this incident, using only what the traces and replays support.

## What to hand in

A one-page trace audit: the two timelines, the list of differences, the replay table with your reading of it, the decisive step for the customer, and two design changes (one to the agent, one to its tracing).

## Self-check

If your audit names the prompt version as the cause, look at the replay table again: changing it back alone changes nothing. A difference in the trace is a candidate cause, not a cause, until a replay tests it.
