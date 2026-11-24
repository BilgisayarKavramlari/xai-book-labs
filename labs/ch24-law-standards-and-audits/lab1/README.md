# Lab 24.1: Map the Rules

Chapter 24, Law, Standards and Audits · No code (browser and the template in this folder) · About 75 minutes · Last checked: 2026-11-24

## Goal

Build a regulatory and standards map for one credit or insurance system from the primary legal texts, place each duty on the seven jobs of the chapter's obligation matrix, and turn each duty into an evidence item for an evidence pack.

## What you need

A web browser and `obligation-matrix-template.md` in this folder. Nothing to install. You will read primary texts only: regulations, statutes, judgments and supervisors' own documents. Law firm notes may help you find a provision, but every cell you fill must cite the primary text.

## The scenario

Choose one:

- **A.** A consumer lender uses a gradient-boosted model to decide personal loan applications in Germany and in Colorado. A few applications are reviewed by a loan officer; most are decided automatically.
- **B.** A life insurer uses a predictive model with external consumer data (purchasing and property data) to underwrite and price term life policies in the EU (Ireland) and in Colorado.
- **C.** Your own Explanation Dossier system, if it is used in at least one jurisdiction covered below.

## Primary texts (open these; record the date you opened each)

| Rule | Where to read it |
|---|---|
| GDPR Articles 13-15, 22, 35 | https://eur-lex.europa.eu/eli/reg/2016/679/oj |
| CJEU C-203/22 (Dun & Bradstreet Austria), Feb 27, 2025 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62022CJ0203 |
| CJEU C-634/21 (SCHUFA), Dec 7, 2023 | https://curia.europa.eu/juris/liste.jsf?num=C-634/21 |
| EU AI Act, Articles 6, 12, 13, 14, 26, 27, 43, 86, Annex III point 5, Annex IV | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| Digital Omnibus on AI (dates in amended Article 113) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj |
| Consumer Credit Directive, Article 18 | https://eur-lex.europa.eu/eli/dir/2023/2225/oj |
| Regulation B, 12 CFR 1002.9 and 1002.12 with Supplement I | https://www.consumerfinance.gov/rules-policy/regulations/1002/9/ |
| FCRA, 15 U.S.C. 1681m and 1681g(f) | https://www.law.cornell.edu/uscode/text/15/1681m |
| Colorado SB26-189 (automated decision-making technology) | https://leg.colorado.gov/bills/sb26-189 |
| Colorado SB21-169 (insurers' external consumer data) | https://leg.colorado.gov/bills/sb21-169 |
| Turkey KVKK Law No. 6698, Article 11 (official English translation) | kvkk.gov.tr, "Personal Data Protection Law" |
| SR 26-2 / OCC Bulletin 2026-13 (model risk) | https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm |
| NIST AI RMF 1.0, section 3.5 and MEASURE 2.9 | https://doi.org/10.6028/NIST.AI.100-1 |

## Steps

1. **Scope (10 minutes).** Write two sentences: what the system decides, for whom, where, and whether a human formally decides. Decide which rules can apply at all. *Checkpoint: for scenario A, GDPR, the AI Act (Annex III point 5(b)), the Consumer Credit Directive, Colorado SB26-189 and, if the lender is a United States creditor for Colorado applicants, Regulation B and the FCRA. For scenario B, the AI Act (Annex III point 5(c)), the GDPR and Colorado SB21-169 with its regulations.*
2. **Read and extract (35 minutes).** For each rule, find the provision that asks an explanation to do each of the seven jobs: tell before, reasons after, what would change it, human review or contest, records for authorities, logs and versions, impact or risk assessment. Fill `yes`, `partly` or blank in the template, and write the article or section in the cell. *Checkpoint: Regulation B gives "reasons after" in 1002.9(b)(2) and record retention of 25 months in 1002.12(b)(1); AI Act Article 26(6) requires deployers to keep logs at least six months; Article 27 requires a fundamental rights impact assessment from deployers of Annex III 5(b) and 5(c) systems.*
3. **Date it (5 minutes).** For each rule, write when it applies to your system. *Checkpoint: after Regulation (EU) 2026/1744, Chapter III obligations for Annex III systems apply from December 2, 2027; Consumer Credit Directive Article 18 applies from November 20, 2026; Colorado SB26-189 duties from January 1, 2027.*
4. **Turn duties into evidence (20 minutes).** In the second table of the template, write for each filled cell one evidence item an auditor could inspect (a document, a log field, a test result) and the step of the Explanation Loop it belongs to.
5. **Flag what moves (5 minutes).** Mark every entry that rests on guidance rather than on a statute or regulation, and every entry with a pending amendment (for example the GDPR Digital Omnibus proposal, COM(2025) 837, under negotiation as of November 2026).

## Expected results

A filled 7-by-N matrix with a citation in every filled cell, a list of application dates, and an evidence table of 15 to 30 items. Two students mapping the same scenario should agree on most cells; disagreements usually involve the "partly" cells (for example whether GDPR Article 15(1)(h), as read in C-203/22, requires "what would change it" or only allows it). Write down your reason for each "partly".

## What to hand in

The filled template (matrix, dates and evidence table) and a one-page evidence pack outline with one section per step of the Explanation Loop. Add the line "Not legal advice; as of <date>."

## Self-check

- Does every filled cell cite an article or section of a primary text you opened?
- Did you record when each rule applies, not only whether it applies?
- Could an auditor start from any of your obligations and find an evidence item in your outline?
- Which of your entries would break if a piece of guidance were withdrawn tomorrow?
