# Lab 10.2: Prototypes, Criticisms and Neighbors

Chapter 10, Explaining with Examples and Training Data · Run-only notebook · About 45 minutes · Last checked: 2026-11-24 (end-to-end run in about 5 seconds on a laptop CPU)

## Goal

Summarize two classes of handwritten digits with prototypes and criticisms (MMD-critic, Kim et al., 2016), then explain a neural network's predictions with nearest neighbors found in pixel space and in the network's hidden layer, and see which neighbors are more faithful to the model.

## Tools and versions

Python 3.10, numpy 2.2.6, scikit-learn 1.7.2, matplotlib 3.10.9. Notebook: `prototypes_and_neighbors.ipynb`. It also runs in a hosted notebook service.

## Data

The handwritten digits dataset bundled with scikit-learn (`load_digits`): 1,797 images of 8 x 8 pixels, digits 0 to 9, a copy of the test set of the UCI Optical Recognition of Handwritten Digits data (https://doi.org/10.24432/C50P49, CC BY 4.0). Nothing is downloaded.

## Steps

1. Open the notebook and run the cells in order.
2. **Checkpoint 1:** 1,257 training images and 540 test images (a stratified 70/30 split, `random_state=0`).
3. **Checkpoint 2:** the digit 1 class has 127 training images and the digit 7 class 125; three prototypes and three criticisms are shown for each. Prototypes look ordinary; criticisms look unusual.
4. **Checkpoint 3:** the network reaches a test accuracy of 0.978 with 12 wrong predictions. Pixel-space neighbors agree with the model on 0.976 of all test images and on 0.417 of the wrong ones (5 of 12); hidden-layer neighbors agree on 0.985 and 0.667 (8 of 12).
5. **Checkpoint 4:** four wrong predictions are shown with their five neighbors in each space.

## Expected results

The numbers above come from scikit-learn 1.7.2. Another version can change the network slightly and move the counts by one or two; the ordering (hidden-layer neighbors agree more with the model's wrong answers) should hold.

## Questions

1. Which kind of neighbor is the better explanation of the model, and which of the data? Use the Checkpoint 3 numbers.
2. Would you show the criticisms to a labeling team, to a customer, or to neither? Why?
3. A neighbor explanation shows real training images. Name one kind of data where that would be unacceptable, and one change that would make it acceptable.

## What to hand in

One prototype and criticism panel with a sentence on what the criticisms reveal, the agreement numbers with your interpretation, and your answers to the three questions.

## Self-check

If you concluded that pixel neighbors are "wrong", reread Chapter 10: they describe the data correctly; they are simply not the model's notion of similarity.
