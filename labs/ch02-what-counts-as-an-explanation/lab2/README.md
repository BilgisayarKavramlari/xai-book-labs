# Lab 2.2: Convincing or Correct? A Small User Check

Chapter 2, What Counts as an Explanation? · No code · About 60 minutes · Last checked: 2026-11-24 (fact sheet regenerated from Lab 2.3 with the pinned versions in `env/requirements.txt`)

## Goal

Rate six explanation cards for one flagged case on how convincing they are, check each against the model's facts, then run a short task with three people to see which cards are actually useful. You will see plausibility, faithfulness and usefulness come apart in your own ratings.

## What you need

This page (print it or keep it on screen), a pen, and three people willing to spend five minutes each. No code. The facts come from the synthetic model of Lab 2.3; nothing here describes a real person or agency.

## The case

Mariam (an invented name for a synthetic record) has been flagged by a welfare-style risk model. She is 45, has received benefit for 11 months, has had 2 income changes in the past year, does not share an address, has had no bank balance jump, has met the language requirement, and a caseworker has recorded a concern on her file. Her risk score is 0.19; the flag threshold is 0.13; an average resident scores 0.06.

## The six cards

**Card 1.** "Your file was selected by our risk model. The factors the model weighs most are caseworker assessments, shared addresses, time on benefit and sudden changes in bank balance."

**Card 2.** "Compared with an average resident, your score was raised most by a concern recorded on your file by a caseworker, and next by the 11 months you have received benefit. Other factors contributed less."

**Card 3.** "Compared with the most similar resident who was not selected, the main difference is the time on benefit: you have received benefit for 11 months, they for 2."

**Card 4.** "Your recent income changes and your household situation suggest a pattern consistent with undeclared cohabitation, which is what our model is designed to detect."

**Card 5.** "Contributions to your score compared with an average resident: caseworker concern +0.105; months on benefit +0.061; shared address -0.023; income changes +0.015; bank balance jump -0.012; language requirement -0.006; household size -0.005; age -0.002. Total above average: +0.133."

**Card 6.** "The model gives points to a set of risk indicators and selects any file whose total is above a fixed threshold. Your total was above the threshold."

## Fact sheet (computed in Lab 2.3)

- Exact Shapley values against a background of 100 residents: as in Card 5. They add up to her score minus the background mean.
- Against the most similar unflagged resident (age 48, 2 months on benefit, household of 3, same concern flag and income changes): months on benefit +0.107, household size -0.020, all others 0.
- Global permutation importance (whole model): caseworker concern 0.037, shared address 0.034, months on benefit 0.032, bank balance jump 0.028, language requirement 0.018, income changes 0.016, age 0.008, household size about 0.
- Replacing her concern flag and her months on benefit with typical values brings her score from 0.19 to about 0.03, below the average resident; replacing her shared-address value with typical values *raises* it to about 0.22, because she does not share an address.

## Steps

1. **Rate plausibility first (10 minutes).** Before reading the fact sheet, rate each card from 1 (not convincing) to 5 (very convincing). Write the ratings down.
2. **Check faithfulness (15 minutes).** Now read the fact sheet. For each card, mark every claim as *true of the model*, *false* or *not checkable*. A card is faithful only if all its claims about this case are true of the model.
   *Checkpoint: you should find at least one card that you rated 4 or 5 but that contains a false or uncheckable claim.*
3. **Judge stability (5 minutes).** Which cards would stay the same if the explanation method were rerun or the background sample changed? (Use the chapter's case study: the third reason of a sampled surrogate moves; the top two do not; Shapley values shift somewhat with a new background.)
4. **Run the user check (20 minutes).** Give each of three people one card (use Cards 1, 2 and 4 so that you compare a global list, a faithful local card and a plausible but unfaithful narrative). Do not show the fact sheet. Ask:
   - (a) "What raised this person's score the most?"
   - (b) "If the caseworker's concern were removed from the file, would the score drop a lot, a little, or not at all?"
   - (c) "What could this person do next?"
   - (d) "How convincing was the card, from 1 to 5?"
   Score (a) and (b) against the fact sheet (correct answers: the caseworker concern; a lot). For (c), note whether the answer is something Mariam can actually do (for example, ask what the concern is and contest it).
   Ask for consent, collect no names, and tell participants the case is invented.
5. **Compare (10 minutes).** Put the four numbers side by side for each card: your plausibility rating, your faithfulness verdict, the participant's correct answers, the participant's convincingness rating.

## Expected results

Card 4 is usually rated convincing and is unfaithful: shared living arrangements lower her score in this model, and income changes contribute little. Card 6 is true but uncheckable and useless for any decision, like the description the Dutch State gave of SyRI. Card 5 is faithful but long; Card 2 is faithful and selective; Card 3 is faithful for a different foil. Participants given Card 4 often answer (a) wrongly while rating it highly. Three participants are far too few for conclusions; the point is to see the gap with your own eyes.

## What to hand in

Your ratings before and after the fact check, the results table of the user check, and five sentences on where plausibility and faithfulness diverged and what that means for usefulness.

## Self-check

- Did you rate plausibility *before* reading the fact sheet? If not, your ratings are contaminated; say so in your write-up.
- Did you judge usefulness by what participants could answer and do, not by how much they liked the card?
- Did you note which foil each card uses?
