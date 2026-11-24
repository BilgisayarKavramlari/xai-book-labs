# Lab 13.4: Why Did the Agent Go Around?

Chapter 13, Beyond Tables and Images: Time Series, Graphs and Agents · Run-only notebook, one optional edit · About 45 minutes · Last checked: 2026-11-24 (end-to-end run in about 2 seconds on a laptop CPU)

## Goal

Solve a small delivery task by value iteration, explain the agent's actions contrastively with decomposed rewards and a minimal sufficient explanation (Juozapaitis et al., 2019), summarize its policy by the states where the choice matters most (in the spirit of HIGHLIGHTS, Amir and Amir, 2018), and test the explanation by changing the environment.

## Tools and versions

Python 3.10, numpy 2.2.6. Notebook: `why_did_the_agent_go_around.ipynb`. No data download.

## The task

A van on a 5 x 7 grid starts at A (row 2, column 1) and must reach the depot D (row 2, column 6). A congested city block (rows 1 to 3, columns 2 to 4) lies on the direct road. In the block, 30 percent of moves fail (the van waits). Each step returns three rewards: time (-1), fuel (-0.4, or -0.6 in the block) and lateness risk (-1.2 per step in the block, 0 elsewhere). Discount 0.97.

## Steps

1. Run the cells in order.
2. **Checkpoint 1:** the route from A goes up two cells, right along the top row and down to D (10 cells), around the block.
3. **Checkpoint 2:** at A, "up" over "right": time -2.21, fuel -0.15, lateness risk +4.41, total +2.06; the minimal sufficient explanation is lateness risk alone. Two more states are explained the same way; at (1, 5) the explanation is time.
4. **Checkpoint 3:** the five most important states are four cells inside or at the edge of the block (importance about 5.1 to 5.3) and the cell (2, 5) next to the depot.
5. **Checkpoint 4:** with the risk removed, the van drives straight through the block (six cells), as the explanation predicts. With the congestion removed but the risk kept, it also drives straight through.

## Expected results

Exactly the numbers above (the computation is deterministic).

## Questions

1. Checkpoint 4 has a surprise. The explanation said "lateness risk"; why does removing only the congestion also change the route? (Hint: how many steps does the van expect to spend in the block, and how much risk does each step carry?)
2. What does reward decomposition tell you, and what does it not tell you, about the role of the environment's dynamics?
3. Would you show the policy summary of Checkpoint 3 to a dispatcher? What would you add?

## Optional edit

In `step`, change `risk=1.2` to `risk=0.6` and rerun. Does the action at A change? Compare the size of the lateness-risk advantage before and after, and write two sentences on explanations near a decision boundary.

## What to hand in

Three contrastive explanations in one sentence each, the policy summary with one sentence per state, the results of the counterfactual tests, and your answer to Question 1.

## Self-check

If your answer to Question 1 is "the explanation was wrong", look again: the explanation is faithful to the agent's values, but it is stated in reward kinds, and the risk the van avoids is risk per step in traffic. A complete explanation names both the reward kind and the dynamics that produce it.
