# Tool evaluation sheet

One sheet per tool. Fill every row from a page you opened; write the URL and the date. Leave a row empty rather than guess.

| Section | Item | Entry | Source and date |
|---|---|---|---|
| Identity | Tool name, package name, version evaluated | | |
| | Maintainer (person, lab, company); disclosure of any tie to you | | |
| Map placement | Scope: local, global, or both | | |
| | Access: model-agnostic or model-specific (which model families) | | |
| | Timing: interpretable by design or post hoc | | |
| | Form: attribution, rule, example, counterfactual, concept, mechanism, narrative | | |
| What it computes | The quantity, in one sentence (for example "interventional Shapley values with a background set") | | |
| | Inputs it needs (model access, background data, gradients, activations) | | |
| | Defaults that change the result (sample size, background, kernel width, feature selection, baselines) | | |
| | Where randomness enters, and how to fix the seed | | |
| Fit to the need | Which of the requirements it covers, and which it does not | | |
| | Audience it serves best (developer, validator, operator, affected person) | | |
| Engineering | Supported Python and framework versions | | |
| | Runtime class (per explanation, per batch), if documented | | |
| | Install footprint and heavy dependencies | | |
| Governance | License, read from the license file; commercial production use allowed? | | |
| | Latest release and date; releases in the last 24 months | | |
| | Repository status (archived? latest commit; changelog; migration guides) | | |
| | Documentation quality: method, assumptions, limits | | |
| | Known issues or published critiques of the method | | |
| Decision | Keep, keep with conditions, or drop; one-sentence reason | | |
| | What the test drive must measure before approval | | |
