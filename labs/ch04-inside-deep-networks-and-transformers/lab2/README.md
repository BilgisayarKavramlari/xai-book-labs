# Lab 4.2: Occupations on a Gender Axis

Chapter 4, Inside Deep Networks and Transformers · No code · About 45 minutes · Last checked: 2026-11-24 (tool loaded in a desktop browser; the "Word2Vec All" dataset was listed with 71,291 words in 200 dimensions, and all twenty occupation words below were in its vocabulary)

## Goal

Repeat, in a public tool, the measurement at the heart of the chapter's opening story: define a direction from *she* to *he* in a word embedding, place occupation words along it, and check how much the result depends on the words you used to define the direction.

## Tool

Embedding Projector, https://projector.tensorflow.org/ (free, runs in the browser, no account; described in Smilkov et al., 2016, arXiv:1611.05469). It loads several demo embeddings and offers PCA, t-SNE, UMAP and **Custom** projections. A custom projection lets you define the horizontal axis by two words (or search patterns), one for the left end and one for the right end.

The projector's demo datasets include word2vec embeddings ("Word2Vec 10K" and "Word2Vec All"). The page does not document which text they were trained on, so treat the training corpus as unknown and say so in your write-up. Several words used in the 2016 paper (for example *homemaker* and *receptionist*) are not in this vocabulary.

If the tool has moved, check the tool landscape page in `tools/`. Any embedding viewer that lets you project words onto the difference of two word vectors will do.

## Steps

1. Open the projector. In the panel on the left, choose the dataset **Word2Vec All**. Wait until it loads.
2. In the projection panel at the bottom left, choose the **Custom** tab. For the horizontal axis, type `she` on one side and `he` on the other. (Use exact-word search if the tool offers a regex option: `^she$` and `^he$`.)
3. In the search box on the right, type each occupation in turn and note where it falls on the horizontal axis, from the *she* end to the *he* end. Use these twenty words: nurse, librarian, secretary, teacher, dancer, hairdresser, nanny, designer, cashier, accountant, lawyer, doctor, professor, manager, scientist, engineer, programmer, pilot, carpenter, mechanic.
4. **Checkpoint 1:** you can order all twenty from the *she* end to the *he* end. Record the order, or estimate each position on a scale from -1 (*she* end) to +1 (*he* end). Take a screenshot.
5. Change the axis to `woman` and `man`. Repeat for the same twenty words. Take a second screenshot.
6. **Checkpoint 2:** most words keep roughly the same side, but some move. Note every word whose side or rank changes by more than five places.
7. Optional: try `mother` and `father`, and a pair with no gender meaning, such as `summer` and `winter`, as a control. Do the occupations spread out along the control axis as well?

## Expected results

You should find a clear ordering in which some occupations (for example *nurse*, *hairdresser*, *nanny*) fall toward the *she* end and others (for example *mechanic*, *carpenter*, *engineer*) toward the *he* end. The exact order will differ from the 2016 paper, because the embedding, its corpus and its vocabulary differ. The order also changes, sometimes noticeably, when you define the axis with a different word pair: a direction defined by two words carries everything else that distinguishes those two words.

## Questions

1. Which occupations fall at each extreme of your *she* to *he* axis? Compare with the lists in the chapter's opening story. What could explain the differences?
2. How many of the twenty words changed side or rank substantially when you switched from *she/he* to *woman/man*? What does this say about the claim "the embedding places occupation X on the female side"?
3. Nissim and colleagues (2020) showed that the famous analogy was produced by code that could not return the question words. Your projection does not use analogies. Does that make your result stronger evidence of an association, weaker, or neither? Explain.
4. What did the control axis (if you tried it) show? Why is a control useful?

## What to hand in

A table of the twenty occupations with their positions on both axes, the two screenshots, and a paragraph (about 150 words) answering Question 3.

## Self-check

If your two orderings are identical, check that you really changed both ends of the axis. If every occupation sits exactly in the middle, check that you selected the Custom projection and the Word2Vec All dataset.
