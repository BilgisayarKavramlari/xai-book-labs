# Lab 13.3: Explaining a Transaction Graph

Chapter 13, Beyond Tables and Images: Time Series, Graphs and Agents · Run-only notebook · About 60 minutes · Last checked: 2026-11-24 (end-to-end run in 75 to 130 seconds on a laptop CPU; nothing is downloaded)

## Goal

Part A: check two edge explainers (single-edge occlusion and a GNNExplainer-style learned mask, Ying et al., 2019) against a planted ground truth and a random baseline. Part B: reproduce Part 2 of the Chapter 13 case study on a synthetic payment network with planted money-laundering schemes: train random forests and a two-layer graph convolutional network (GCN), score single-edge explanations against the schemes you planted, and see why "remove every edge" is a misleading test.

## Tools and versions

Python 3.10, numpy 2.2.6, pandas 2.3.3, scikit-learn 1.7.2, torch 2.6.0 (CPU). Notebook: `explaining_a_transaction_graph.ipynb`.

## Data

All data in this lab are **synthetic**, generated in the notebook with fixed seeds. They are not real payments, not a sample of any institution's data, and carry no third-party license.

- Part A: a small graph (300 base nodes grown by preferential attachment, 40 planted five-node "house" motifs, 50 random extra edges); the only node feature is the node's number of links.
- Part B: 30 time windows, each with about 1,000 accounts (15 percent businesses) making ordinary payments (purchases, transfers between people, salaries, supplier payments, a few large legitimate transfers), plus 10 planted laundering schemes per window. The schemes use three of the eight shapes that Altman et al. (2023) list from IBM's AMLSim simulator: fan-out (a hub pays 4 to 7 mules), fan-in (4 to 7 mules pay one hub) and scatter-gather (a hub pays mules who pass the money to a second hub). Most mules are existing customers recruited into the scheme, so they keep their ordinary activity; 30 percent of schemes keep amounts just under 10,000. Each account has nine features of its own (payments in and out, amounts in and out, share of amounts just under 10,000, pass-through ratio, spread of outgoing amounts, account age, business flag). Laundering accounts are about 6.6 percent of all accounts, far more than in real data; the generator is built to teach, not to estimate how well any method works in practice.

Why not a real dataset? The Elliptic Data Set used in the first draft of this lab is licensed CC BY-NC-ND 4.0 (non-commercial, no derivatives), which the book's data policy does not allow. Realistic synthetic data exist: IBM's *Transactions for Anti Money Laundering* (Altman et al., 2023; https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml) is licensed under the Community Data License Agreement - Sharing 1.0, which allows commercial use, places no obligations on results computed from the data, and requires that the data, if you republish them (modified or not), be published under the same agreement with attributions kept. Its smallest set has about 5 million transactions (a file of about 475 MB), too large for a one-hour lab on a laptop, so this lab does not use it. See "Going further".

## Steps

1. Run the cells in order.
2. **Checkpoint A1:** the three-layer GCN flags house nodes with held-out accuracy 0.95.
3. **Checkpoint A2:** over 43 correctly flagged held-out house nodes, the share of each explainer's top-k edges that are house edges (k = number of house edges in the node's computation graph): occlusion 0.76, learned mask 0.65, random 0.55. Both beat the random baseline; neither is perfect.
4. **Checkpoint B1:** 30,791 accounts, 107,488 payments, 104,582 edges (pairs of accounts that paid each other), 2,035 laundering accounts (390 hubs, 1,645 mules), 2,148 scheme payments.
5. **Checkpoint B2:** with windows 1-20 for training and 21-30 for testing, a random forest on the nine own features reaches laundering-class F1 0.576 (recall: hubs 0.77, mules 0.43); with neighbor summaries added (mean and maximum of each feature over the account's neighbors), F1 0.673 (precision 0.882).
6. **Checkpoint B3:** the GCN, which sees only the own features plus the edges, reaches precision 0.650, recall 0.709, F1 0.678; it catches 0.70 of mules and 0.73 of hubs. Training takes about 15 seconds.
7. **Checkpoint B4:** of the correctly flagged test accounts, 0.64 of hubs (95) and 0.92 of mules (382) stay flagged when every edge in the graph is removed.
8. **Checkpoint B5:** for 40 hubs and 80 mules, single-edge occlusion over the edges within two steps: share of the top-k edges that are scheme edges, hubs 0.55 (random 0.16), mules 0.71 (random 0.17). Cutting only the account's scheme edges reverses 0.60 of hub flags and 0.61 of mule flags; cutting every edge around the account reverses 0.28 and 0.08.
9. **Checkpoint B6:** for mules, the sum of single scheme-edge drops differs from the joint drop by a median of 0.24 (largest 1.35). Example: account 23204 has probability 0.82; cutting its scheme's 4 edges lowers it to 0.03, while cutting all 83 edges around it raises it to 1.00.

## Expected results

Data, forest and Part A numbers are deterministic with the versions listed. GCN numbers can move slightly with another PyTorch version or CPU; the pattern (occlusion well above chance; cutting the scheme reverses most flags while cutting everything does not) should hold.

## Questions

1. Why is the random baseline in Part A so high (0.55) and in Part B so low (about 0.17)? What does that tell you about how to report an explainer's accuracy?
2. Checkpoint B4 alone suggests that the GCN flags mules from their own features. Why is that conclusion wrong, and which checkpoint shows it?
3. Explain in your own words why removing every edge can raise the GCN's probability while removing four edges lowers it.
4. Weber et al. (2019) found that a random forest beat a GCN on the Elliptic Data Set, whose transactions already carry 72 features summarized from their neighbors. Compare that with Checkpoint B2: what does putting the graph inside the table do?

## Optional edit

In the last cell, pick one flagged hub from `R`, list its five most important edges by single-edge occlusion, then cut all five together. Compare the joint drop with the sum of the single drops, and write the explanation you would give an investigator.

## What to hand in

The edge-removal results (B4 to B6), one explained account with its occlusion list and the joint test, and a paragraph on what such an explanation would let an investigator do, and not do.

## Going further

If you have time and disk space, try the same tests on IBM's HI-Small set (about 5 million transactions over 10 days; Altman et al., 2023). Subsample by day or by bank before building a graph on a laptop, keep the chronological split the authors recommend, and use the patterns file as partial ground truth (the authors note that not all laundering in the data follows one of the eight patterns). This extension was not run for the book.

## Self-check

If you concluded that "the graph does not matter" from Checkpoint B4, reread Checkpoint B5: an account with no payments at all is an input the model never saw, so its answer there says little about the real graph.

## References

Altman, E., Blanusa, J., von Niederhausern, L., Egressy, B., Anghel, A., and Atasu, K. (2023). Realistic synthetic financial transactions for anti-money laundering models. *Advances in Neural Information Processing Systems 36* (Datasets and Benchmarks Track).

Weber, M., Domeniconi, G., Chen, J., Weidele, D. K. I., Bellei, C., Robinson, T., and Leiserson, C. E. (2019). Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks for financial forensics. KDD Workshop on Anomaly Detection in Finance.

Ying, R., Bourgeois, D., You, J., Zitnik, M., and Leskovec, J. (2019). GNNExplainer: Generating explanations for graph neural networks. *NeurIPS 32*.
