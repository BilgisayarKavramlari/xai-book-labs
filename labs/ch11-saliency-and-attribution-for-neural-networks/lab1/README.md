# Lab 11.1: Spot the Shortcut

Chapter 11, Where the Network Looks · No code · About 45 minutes · Last checked: 2026-11-24

## Goal

Read a gallery of heat maps for two networks the way a validator would: decide which network relies on a source marker, say what the maps cannot tell you, and name the intervention that would settle the question.

## Tools

- `gallery.png` in this folder (open it in any image viewer or browser).
- Optional warm-up: CNN Explainer, a free browser tool that shows what each layer of a small convolutional network computes (https://poloclub.github.io/cnn-explainer/, reachable on 2026-11-24; Wang et al., IEEE TVCG, 2020). No account is needed.
- `make_gallery.py` documents how the gallery was computed. You do not need to run it.

## Data

Four synthetic, radiograph-like images (32 by 32 pixels). A "positive" image carries a faint round opacity in one lung. Some images carry an L-shaped token in the top-left corner, standing in for a source marker. Two networks with the same architecture were trained on different data; one of them saw a token that marked most positive images. The probability `p` above each map is that network's predicted probability of "positive" for the image. Maps show the absolute value of each method's score, scaled per map. Integrated Gradients uses the average healthy training image as its baseline.

## Steps

1. Warm-up (10 minutes, optional): in CNN Explainer, click through the layers for two example images and note what one convolutional feature map responds to. This is the kind of internal map that Grad-CAM weights.
2. Open `gallery.png`. For each image, note whether it shows a token and whether you can see an opacity.
3. **Checkpoint 1:** for each network, list the images where most of the Integrated Gradients map sits in the top-left corner.
4. **Checkpoint 2:** compare each network's probabilities for Image 2 (a positive without a token) and Image 3 (a healthy image with a token). Which network gets them wrong?
5. Decide which network relies on the token. Write down the evidence from at least two methods and from the probabilities.
6. Image 4 has no token, yet one network's Integrated Gradients map shows a small hot spot in the corner. Explain why. (Hint: what does the baseline contain?)
7. Name one intervention that would confirm your verdict, and what result would refute it.
8. List two things the maps cannot tell you.

## What to hand in

A one-page verdict: which network uses the shortcut, your evidence (maps and probabilities), the intervention you would run and its decisive result, and two limits of the maps.

## Self-check

If your verdict rests only on how the maps look, add the probabilities and the intervention: a map is a hypothesis about where to intervene, not proof. If you said a map "shows the model is fine", ask what a model that uses an unlocalized signal would look like in the same gallery.

## Answer key (read after you hand in)

Network B is the confounded one. Its Integrated Gradients maps concentrate on the corner for Images 1 and 3, its Grad-CAM maps show a hot region near the corner for the same images, and its probabilities follow the token: Image 3, healthy with a token, gets 0.81, while Image 2, positive without a token, gets 0.08. Network A gives 0.44 and 0.75 for those images and its maps sit in the lungs. For Image 4, the average healthy image used as Network B's baseline contains a faint token (half of the clean training images carry one), so the attribution records the token's absence: a reminder that Integrated Gradients explains a difference from the baseline. Interventions: paint the token into healthy images and out of positive images and compare the change in probability with the change for random patches; test on data where the token is independent of the label. In Lab 11.3 these interventions move Network B's mean probability from 0.03 to 0.76 (token added to healthy images) and from 0.92 to 0.12 (token removed from positives). Limits: the maps show where, not what (the network might respond to the token's brightness, its shape, or something correlated with it); Grad-CAM is coarse; and a network can rely on a signal with no location, which no map would show.
