# Chapter 11 labs: Where the Network Looks: Saliency and Attribution

| Lab | Title | Kind | Time |
|---|---|---|---|
| [lab1](lab1/) | Spot the Shortcut | No code (browser, gallery image and worksheet) | about 45 minutes |
| [lab2](lab2/) | Six Maps, One Image | Run-only notebook (one optional edit) | about 60 minutes |
| [lab3](lab3/) | A Shortcut Hunt in Two Hospitals | Run-only notebook (one optional edit) | about 75 minutes |

All three labs use the same synthetic, chest-radiograph-like 32 by 32 images and the same small convolutional network as the chapter's figures (`figures/scripts/ch11_figs.py` in the book repository), with the same random seeds, so the numbers in the notebooks match the numbers in the chapter. The images are not medical data and the networks are not medical models.

Versions used for the end-to-end runs on 2026-11-24 (laptop CPU, Python 3.10): numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, matplotlib 3.10.9, torch 2.6.0 (all in `env/requirements.txt`). Lab 11.2 ran in about 30 seconds and Lab 11.3 in about 60 seconds. The attribution methods are written out in plain PyTorch so that every step can be read; Captum (0.9.0, checked 2026-11-24) and Zennit (1.0.0) implement them for any PyTorch model, and Chapter 23 compares toolkits.
