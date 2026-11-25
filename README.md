# Explainable AI in Practice: Labs

Hands-on labs for the book *Explainable AI in Practice: Methods, Tools and Accountability, from Credit Scores to Language Models* by Sadi Evren Seker.

The book explains the ideas; this repository is where you try them. Every chapter has two to four labs. At least one lab per chapter needs no code: it uses a web tool or an interactive page you only read and click. The other labs are Jupyter notebooks that run on a laptop or in a free hosted notebook service.

## How the repository is organized

| Folder | What it holds |
|---|---|
| `labs/chNN-<slug>/labN/` | One lab: `README.md` (goal, time, tools, data, steps with checkpoints, expected results, what to hand in, self-check) and, for code labs, a notebook |
| `data/` | Data cards and `LICENSES.md`, the source and license of every dataset and pretrained model the labs use (labs download the data; the few small derived files kept in lab folders say where they come from) |
| `portfolio/` | Templates for the Explanation Dossier, the portfolio you build chapter by chapter |
| `tools/` | The tool landscape page (what each XAI tool does, dated), and the tool evaluation sheet used in Chapter 23 |
| `env/` | Pinned environments: `requirements.txt` for the tabular and vision labs, `requirements-llm.txt` for the language model labs |

## Getting started

1. Read the chapter first. Each lab starts where a Studio box in the book points to it.
2. For a no-code lab, open its `README.md` and follow the steps in your browser.
3. For a code lab, create the environment in `env/` (instructions in `env/README.md`) or open the notebook in a hosted notebook service. Run the cells from top to bottom; each checkpoint tells you what you should see.
4. Hand in what the lab asks for, or add it to your Explanation Dossier (`portfolio/`).

## Principles

- **Equal distance to tools.** Labs use several tools for the same job, so that you learn to compare them. One of the tools, HermAI, is maintained by the book's author; it is treated like every other tool.
- **Public data, stated licenses.** Every dataset's source and license is listed in `data/LICENSES.md`, and every lab names its data and license. Only datasets whose licenses allow commercial use and derived results are used.
- **Dated tools.** Web tools and libraries change. Every lab states the versions and the date it was last checked. If something has moved, the tool landscape page in `tools/` says what replaced it.

## License

This repository uses two licenses:

- **Code** (Python files, the code cells of the notebooks, and the environment files in `env/`) is under the MIT License. See `LICENSE`.
- **Text and templates** (the lab READMEs, the Markdown cells of the notebooks, the data cards, the tool pages and the portfolio templates) are under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See `LICENSE-CC-BY-4.0.txt`. To credit the material, write: "From the companion labs of *Explainable AI in Practice* by Sadi Evren Seker, https://github.com/BilgisayarKavramlari/xai-book-labs, CC BY 4.0."

Datasets, pretrained models and third-party files keep their own licenses, which are listed in `data/LICENSES.md` and in the files that come with them (for example `labs/ch14-why-language-models-are-hard-to-explain/lab3/NOTICE.md`). These licenses cover the companion repository only, not the book itself.
