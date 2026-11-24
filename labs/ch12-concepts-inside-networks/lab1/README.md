# Lab 12.1: Teach a Machine a Shortcut, then Audit It with Concepts

Chapter 12, Concepts Inside Networks · No code · About 60 minutes · Last checked: 2026-11-24

## Goal

Build a small image classifier in the browser that learns a shortcut on purpose, catch the shortcut with a behavioral concept test, and then design (on paper) the TCAV test and the concept bottleneck that a team would use to catch the same shortcut in a real inspection or dermatology model.

## Tools

Teachable Machine (https://teachablemachine.withgoogle.com/, image project), a webcam or a phone camera, and this worksheet. Teachable Machine trains in your browser tab; its FAQ (checked 2026-11-24) says samples are not sent to any server unless you save the project to your own cloud drive. Do not photograph people or anything personal. If you have no camera, use the Upload option with photos you took yourself.

You need: about ten small objects of one kind that can be "good" or "defective" (for example coins, bottle caps, crackers or pens; "defective" = scratched, broken or marked with a thin pencil line), and a few small colored sticky notes or round stickers.

## Steps

1. **Plant the shortcut.** Create two classes, `good` and `defective`. Photograph each object several times (about 30 to 50 images per class, different angles). For every `defective` image, put a sticky note somewhere in the frame. Never use a sticky note in `good` images. This mirrors inspectors labeling rejected parts, or surgeons marking suspicious moles with ink (Winkler et al., 2019).
2. **Train** with the default settings. **Checkpoint 1:** in the preview, the model should separate your two classes almost perfectly.
3. **Behavioral concept test.** Hold up a *good* object with a sticky note next to it. Then a *defective* object with no sticky note. Record the class and confidence the preview shows, five tries each. **Checkpoint 2:** if the shortcut was learned, good objects with a note are called defective and defective objects without a note are often called good.
4. **Retrain clean.** Delete the note images (or make a new project), photograph the defective objects without notes, train again, and repeat step 3. Record the change.
5. **Design a TCAV test on paper** for the first model, as if you could see inside it. Fill in the TCAV table below: the concept example sets, the random sets, the layer, the class, the number of random runs, and what result would count as evidence of the shortcut. Add one control concept you expect to be unimportant.
6. **Design a concept bottleneck** for the inspection task: list four to six concepts an inspector could label (for the coins, say: scratch, dent, discoloration, missing edge), say who would label them, and how an inspector could correct a concept at the line. Name one factor that matters for the label but is not on your list, and say how it could leak into the concept scores (Chapter 12, "Leakage").

## Worksheet

| Test | Images shown | Prediction (5 tries) | Mean confidence | What it shows |
|---|---|---|---|---|
| Good + note, first model | | | | |
| Defective, no note, first model | | | | |
| Good + note, clean model | | | | |
| Defective, no note, clean model | | | | |

| TCAV design element | Your choice |
|---|---|
| Concept examples (what, how many) | |
| Random examples (what, how many sets) | |
| Layer (early, middle, late, and why) | |
| Class explained | |
| Control concept | |
| Result that would show the shortcut | |
| Result that would not settle it | |

## Expected results

Most first models call a good object with a sticky note "defective" most of the time; the clean model does not. Teachable Machine does not show internal activations, so steps 5 and 6 are a design exercise; Labs 12.2 to 12.4 run the same tests in code.

## What to hand in

The completed worksheet, the two design tables and a short paragraph: which test caught the shortcut, which would have caught it before deployment, and what a TCAV score alone could not tell you (Chapter 12, Myth vs. Reality).

## Self-check

If your clean model still reacts to sticky notes, check whether the notes appear in the background of other images, or whether lighting differed between classes. Shortcuts are not only the ones you plant.
