# Data notice

`data/bloomberg_gpt_rankings.csv` is derived from the repository
https://github.com/BloombergGraphics/2024-openai-gpt-hiring-racial-discrimination
(published by the BloombergGraphics GitHub organization under the Apache License 2.0; the repository names no separate copyright holder), which accompanies the Bloomberg News investigation
"OpenAI's GPT Is a Recruiter's Dream Tool. Tests Show There's Racial Bias" (March 2024) by Leon Yin,
Davey Alba and Leonardo Nicoletti.

Changes: for each of the 8,000 model replies in `data/intermediary/resume_ranking/*/*/1121/`, the file
records only the model, job, source file name, whether the call was one of Bloomberg's rebalancing runs,
and, for the resume ranked first, its position in the prompt, its resume text index (in
`resumes_to_rank.json`) and its name group, plus the name group and resume index shown first, whether
the reply kept the input order, and how many of the eight names the reply mentioned. Names, resume texts
and replies are not copied. `build_runs_table.py` reproduces the file from the original repository.
The original license applies to the source data and to this derived file; a copy of the Apache License 2.0, taken from the source repository, is in `data/LICENSE-Apache-2.0.txt`.
