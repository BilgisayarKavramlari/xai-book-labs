# Lab 18.4: When the Monitor Becomes the Reward

Chapter 18, Steering, Editing and Monitoring Models · Run-only notebook with one editable cell · 30 to 45 minutes · Last checked: 2026-11-24 (end-to-end run in about 2 seconds)

## Goal

Train a three-strategy toy policy with and without a trace monitor in its reward, and see how a monitor that becomes a training signal teaches the policy to hide rather than to stop. Find the change that removes the incentive to hack.

## Tools and versions

Python 3.10, numpy 2.2.6 (`env/requirements.txt`). Notebook: `monitor_as_reward.ipynb`. No data.

## What the toy is and is not

A softmax policy chooses among solving honestly (passes 0.55 of the time), hacking with a visible plan in its trace (passes always, flagged 0.95 of the time) and hacking with an innocent trace (passes 0.97, flagged 0.05). It is trained by exact policy gradient. The toy mirrors the mechanism reported by Baker et al. (2025, arXiv:2503.11926) for a frontier reasoning model; it is not a reproduction, and its numbers describe only the toy.

## Steps and checkpoints

1. Run the cells in order.
2. **Checkpoint 1:** with the monitor only watching, the policy hacks in nearly every episode and the monitor catches 0.95 of hacks. With the flag subtracted from the reward, honest solving rises to 0.98 by step 300 and then collapses; by step 1,499 the policy hacks in nearly every episode and the monitor catches 0.05 of hacks.
3. **Checkpoint 2:** with 8,000 steps, every penalty from 0.25 to 2 ends with the hidden hack (it passes half of the episodes after 226 to 2,814 steps, depending on the penalty); a penalty of 4 delays it past the budget. Lowering the hack's pass rate to 0.6 makes honest solving win; at 0.8 it does not.
4. **Your turn:** change one assumption (a monitor that also catches hidden hacks half of the time, a costlier disguise, or a policy that hides more readily) and predict the result before running.

## Questions

1. If you could see only the monitor's flag rate, at which step would you have stopped training, and what would you have shipped?
2. Write two sentences for a model risk committee explaining why fewer flags after training is not evidence of fewer problems.
3. Which change removed the incentive to hack rather than the incentive to hide? What is its real-world counterpart?

## What to hand in

A half-page memo to a model risk committee answering Question 2, with the table from Checkpoint 2 as evidence.

## Self-check

If your memo recommends a bigger penalty, check Checkpoint 2 again: a larger penalty delayed hiding but did not remove the reason for it.
