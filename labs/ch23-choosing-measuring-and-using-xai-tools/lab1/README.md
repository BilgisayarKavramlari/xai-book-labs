# Lab 23.1: Due Diligence Without Code

Chapter 23, Choosing, Measuring and Using XAI Tools · No code (browser and the evaluation sheet) · About 60 minutes · Last checked: 2026-11-24

## Goal

Fill in a tool evaluation sheet for three explanation tools from their public pages only, place each on the map of explanations, and find the facts that would knock a tool out before anyone writes code.

## What you need

A web browser and `tool-evaluation-sheet.md` in this folder (copy it three times, or use a spreadsheet with the same rows). Nothing to install.

## The scenario

A retail bank's credit team wants explanation tooling for a gradient-boosted credit model on tabular data. It needs (1) the principal reasons for each declined applicant, (2) a global view for model documentation, and (3) suggestions of what an applicant could change. The bank's production stack is pinned to Python 3.10 until next year. Software used in production must carry a license that permits commercial production use without a separate agreement.

## Steps

1. **Pick three tools.** One must come from each group:
   - attribution libraries: `shap`, `lime`, `captum`;
   - glass-box or all-in-one toolkits: `interpret` (InterpretML), `aix360`, `omnixai`, `dalex`, `hermai` (disclosure: maintained by the book's author);
   - counterfactual libraries: `dice-ml`, `alibi`.
2. **Read the package page** at `https://pypi.org/project/<name>/`. Record the latest version, its release date, the license field and classifiers, and the "Requires: Python" line. Then open the release history and count releases in the last 24 months.
   *Checkpoint: as of 2026-11-24, shap's latest release is 0.54.1 (2026-10-16) and requires Python 3.12 or newer; the last release that supports Python 3.10 is 0.49.1 (2025-10-14).*
3. **Read the source repository** linked from the package page. Record whether it is archived, the date of the latest commit, open issues, and whether there is a changelog or migration guide.
4. **Read the license file itself,** not only the badge. Write one sentence on what it allows for commercial production use.
   *Checkpoint: Alibi Explain moved from Apache 2.0 (version 0.9.4, July 2023) to the Business Source License 1.1 with version 0.9.5 (January 2024). That license allows non-production use; production use outside a narrow grant for non-profit educational institutions needs a commercial license. Each version converts to Apache 2.0 four years after its release.*
5. **Read the documentation for the method's assumptions.** For each tool, find what it computes (Shapley values, a local surrogate's coefficients, a glass-box model's own terms, counterfactual examples), its defaults (sample sizes, background data, kernel width, feature selection), and where randomness enters. Write the default you would most want to change.
   *Checkpoint: in shap 0.49.1, KernelExplainer's default `l1_reg` setting keeps only 10 features when explaining a model with more inputs (Chapter 23 shows the effect on a 20-feature model).*
6. **Place each tool on the map of explanations** (scope, access, timing, form) and mark which of the bank's three needs it covers.
7. **Apply the filter.** Using only what you recorded, mark each tool Keep, Keep with conditions, or Drop, and write the reason in one sentence.

## Expected results

Most groups drop at least one tool at step 7 without running it: on the Python constraint (current shap needs 3.12; pin 0.49.1 or upgrade), on the license (Alibi for a commercial production use), or on maintenance (lime's last release was 0.2.0.1 in June 2020; aix360's 0.3.0 and omnixai's 1.3.1 date from July 2023, although both repositories still receive commits). There is no single right answer for "Keep with conditions"; what matters is that the condition is written down.

## What to hand in

Three completed sheets and a half-page memo to the credit team: which tools go forward to a test drive, which do not, and the conditions attached.

## Self-check

- Did every fact on your sheet come from a page you opened, with the date you opened it?
- Did you separate what the tool computes from what its documentation says it reveals?
- Did you check the license file, not only the badge or the classifier?
- Could a colleague repeat your filter decision from your sheet alone?
