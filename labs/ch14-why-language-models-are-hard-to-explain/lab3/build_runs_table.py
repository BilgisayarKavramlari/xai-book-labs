"""Rebuild data/bloomberg_gpt_rankings.csv from Bloomberg's published repository.

Optional: the lab ships the derived table, so you only need this to check it.

    git clone --depth 1 https://github.com/BloombergGraphics/2024-openai-gpt-hiring-racial-discrimination.git
    python build_runs_table.py 2024-openai-gpt-hiring-racial-discrimination data/bloomberg_gpt_rankings.csv

Source data: Bloomberg L.P., Apache License 2.0 (see NOTICE.md). For each of the 8,000 API calls the
script records which of the eight resumes GPT put first, at which position that resume had been shown,
which resume text it carried and which name group its name came from. The ranking is read the same way
as in Bloomberg's own analysis notebook: names are ordered by where they first appear in the reply.
"""
import glob
import json
import os
import re
import sys

import pandas as pd

repo, out = sys.argv[1], sys.argv[2]
templates = json.load(open(f"{repo}/data/intermediary/resumes_to_rank.json"))
rows = []
for model in ["gpt-3.5-turbo", "gpt-4"]:
    for fn in sorted(glob.glob(f"{repo}/data/intermediary/resume_ranking/{model}/*/1121/*.json")):
        r = json.load(open(fn))
        c = r["context"]
        job = c["job"]
        reply = r["choices"][0]["message"]["content"].lower()
        names = [n.lower() for n in c["default_order"]]
        where = {n: len(reply.split(n)[0]) for n in names}          # absent names sort last
        ranking = sorted(names, key=lambda n: where[n])
        body = c["inputs"].split(":\n\n", 1)[1]
        parts = [p for p in body.split("<hr>\n") if p.strip()]
        resume_ids = []
        for i, p in enumerate(parts):
            norm = lambda x: re.sub(r"\s+", "", x.replace(c["default_order"][i], "").replace("{name}", ""))
            match = [k for k, t in enumerate(templates[job]["resumes"]) if norm(t) == norm(p)]
            resume_ids.append(match[0] if match else -1)
        i = names.index(ranking[0])
        rows.append(dict(model=model, job=job, file=os.path.basename(fn), rebalance_run="rebalance" in fn,
                         top_pos=i, top_group=c["demo_order"][i], top_resume=resume_ids[i],
                         first_group=c["demo_order"][0], first_resume=resume_ids[0],
                         order_unchanged=ranking == names, names_found_in_reply=sum(n in reply for n in names)))
df = pd.DataFrame(rows)
df.to_csv(out, index=False)
print(df.shape, "unmatched resumes:", int((df.top_resume < 0).sum()))
