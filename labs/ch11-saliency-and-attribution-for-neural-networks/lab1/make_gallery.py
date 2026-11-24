"""Make gallery.png for Lab 11.1 (no code needed for the lab itself; this script documents how the
gallery was computed). Run: python make_gallery.py  (numpy, scipy, scikit-learn, matplotlib, torch)."""
import matplotlib
matplotlib.use("Agg")
import numpy as np, torch, torch.nn as nn, torch.nn.functional as F
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from sklearn.metrics import roc_auc_score
torch.set_num_threads(4)
print("numpy", np.__version__, "| torch", torch.__version__)

S = 32
yy, xx = np.mgrid[0:S, 0:S]
BODY = ((xx - 15.5) / 14.5) ** 2 + ((yy - 18) / 15) ** 2 < 1
LUNGS = (((xx - 9.5) / 4.8) ** 2 + ((yy - 17) / 9) ** 2 < 1) | (((xx - 21.5) / 4.8) ** 2 + ((yy - 17) / 9) ** 2 < 1)
MARK = np.zeros((S, S), bool); MARK[2:7, 2:4] = True; MARK[5:7, 2:6] = True   # the L-shaped token


def make_images(n, p_pos, p_mark_pos, p_mark_neg, rng, amp=0.22):
    """Synthetic radiograph-like images. Returns images, labels, token flags, opacity masks.
    p_mark_pos / p_mark_neg: chance that a positive / negative image carries the token."""
    X = np.zeros((n, S, S), np.float32); y = (rng.random(n) < p_pos).astype(np.float32)
    m = np.where(y == 1, rng.random(n) < p_mark_pos, rng.random(n) < p_mark_neg)
    les = np.zeros((n, S, S), bool)
    lung_pix = np.argwhere(LUNGS & (yy > 11) & (yy < 24))
    for i in range(n):
        img = np.where(BODY, 0.62, 0.05) - np.where(LUNGS, 0.36, 0.0)
        img = img + gaussian_filter(rng.normal(0, 0.18, (S, S)), 3) + 0.05 * (rng.random() - 0.5)
        if y[i] == 1:
            cy, cx = lung_pix[rng.integers(len(lung_pix))]
            blob = np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * 2.2 ** 2))
            img = img + amp * blob * LUNGS
            les[i] = blob > 0.3
        if m[i]:
            img = np.where(MARK, 0.95, img)
        X[i] = np.clip(img + rng.normal(0, 0.04, (S, S)), 0, 1)
    return X, y, m, les


class Net(nn.Module):
    def __init__(s):
        super().__init__()
        s.c1 = nn.Conv2d(1, 8, 3, padding=1); s.c2 = nn.Conv2d(8, 16, 3, padding=1)
        s.c3 = nn.Conv2d(16, 16, 3, padding=1); s.fc = nn.Linear(16, 1)
    def features(s, x):
        x = F.max_pool2d(F.relu(s.c1(x)), 2); x = F.max_pool2d(F.relu(s.c2(x)), 2)
        return F.relu(s.c3(x))
    def forward(s, x):
        return s.fc(s.features(x).mean((2, 3))).squeeze(-1)      # a logit


def train(X, y, seed=0, epochs=25):
    torch.manual_seed(seed); net = Net(); opt = torch.optim.Adam(net.parameters(), 3e-3)
    Xt, yt = torch.tensor(X[:, None]), torch.tensor(y); g = torch.Generator().manual_seed(seed)
    for _ in range(epochs):
        for idx in torch.randperm(len(X), generator=g).split(64):
            opt.zero_grad(); F.binary_cross_entropy_with_logits(net(Xt[idx]), yt[idx]).backward(); opt.step()
    return net.eval()


def predict(net, X):
    with torch.no_grad():
        return torch.sigmoid(net(torch.tensor(X[:, None]))).numpy()


def logit(net, x):
    with torch.no_grad():
        return net(torch.tensor(np.asarray(x, np.float32)[None, None])).item()

def _t(x):
    return torch.tensor(np.asarray(x, np.float32)[None, None])

def gradient(net, x):
    xt = _t(x).requires_grad_(True); net(xt).sum().backward(); return xt.grad[0, 0].numpy()

def grad_x_input(net, x):
    return gradient(net, x) * x

def smoothgrad(net, x, sigma=0.15, n=50, seed=0):
    rng = np.random.default_rng(seed)
    return np.mean([gradient(net, x + rng.normal(0, sigma, x.shape).astype(np.float32)) for _ in range(n)], 0)

def integrated_gradients(net, x, base=None, steps=64):
    base = np.zeros_like(x) if base is None else base
    alphas = (np.arange(steps) + 0.5) / steps                          # midpoint rule
    path = np.stack([base + a * (x - base) for a in alphas]).astype(np.float32)
    pt = torch.tensor(path[:, None]).requires_grad_(True); net(pt).sum().backward()
    return (x - base) * pt.grad[:, 0].numpy().mean(0)

def expected_gradients(net, x, refs, n=200, seed=0):
    rng = np.random.default_rng(seed)
    r = refs[rng.integers(len(refs), size=n)]; a = rng.random(n)[:, None, None]
    pt = torch.tensor((r + a * (x - r)).astype(np.float32)[:, None]).requires_grad_(True); net(pt).sum().backward()
    return ((x - r) * pt.grad[:, 0].numpy()).mean(0)

def gradcam(net, x):
    A = net.features(_t(x)); A.retain_grad(); net.fc(A.mean((2, 3))).sum().backward()
    w = A.grad[0].mean((1, 2)); cam = F.relu((w[:, None, None] * A[0]).sum(0))
    return F.interpolate(cam[None, None], size=(S, S), mode="bilinear", align_corners=False)[0, 0].detach().numpy()

def occlusion(net, x, size=4, stride=2):
    fill = x.mean(); base = logit(net, x); heat = np.zeros_like(x); cnt = np.zeros_like(x)
    for r in range(0, S - size + 1, stride):
        for c in range(0, S - size + 1, stride):
            z = x.copy(); z[r:r + size, c:c + size] = fill
            heat[r:r + size, c:c + size] += base - logit(net, z); cnt[r:r + size, c:c + size] += 1
    return heat / np.maximum(cnt, 1)

class GuidedReLU(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x); return x.clamp(min=0)
    @staticmethod
    def backward(ctx, g):
        x, = ctx.saved_tensors; return g * (x > 0) * (g > 0)

def guided_backprop(net, x):
    xt = _t(x).requires_grad_(True); r = GuidedReLU.apply
    h = F.max_pool2d(r(net.c1(xt)), 2); h = F.max_pool2d(r(net.c2(h)), 2); h = r(net.c3(h))
    net.fc(h.mean((2, 3))).sum().backward(); return xt.grad[0, 0].numpy()

def shares(a, lesion):
    """Share of total |attribution| on the token and on the opacity."""
    a = np.abs(a); a = a / (a.sum() + 1e-12); return a[MARK].sum(), a[lesion].sum()

def show(ax, a, title, lesion=None, cmap="magma"):
    ax.imshow(a, cmap=cmap); ax.set_title(title, fontsize=9); ax.set_xticks([]); ax.set_yticks([])
    if lesion is not None:
        ax.contour(lesion, levels=[0.5], colors=["cyan"], linewidths=1, linestyles="--")


rng = np.random.default_rng(1)
Xc, yc, mc, _ = make_images(3000, 0.5, 0.9, 0.1, rng)
Xk, yk, mk, _ = make_images(3000, 0.5, 0.5, 0.5, rng)
_ = make_images(1000, 0.5, 0.9, 0.1, rng)
Xe, ye, me, le = make_images(1000, 0.5, 0.5, 0.5, rng)
NETS = {"Network A": train(Xk, yk), "Network B": train(Xc, yc)}    # A clean, B confounded (the answer key)
MNEG = Xk[yk == 0].mean(0).astype(np.float32)
pick = [np.where((ye == 1) & me)[0][3], np.where((ye == 1) & ~me)[0][2],
        np.where((ye == 0) & me)[0][0], np.where((ye == 0) & ~me)[0][0]]
cols = [("Gradient", lambda n, x: np.abs(gradient(n, x))),
        ("Integrated Gradients", lambda n, x: np.abs(integrated_gradients(n, x, base=MNEG))),
        ("Grad-CAM", gradcam)]
fig, axes = plt.subplots(4, 7, figsize=(14, 8.6))
for r, i in enumerate(pick):
    x = Xe[i]
    axes[r, 0].imshow(x, cmap="gray"); axes[r, 0].set_xticks([]); axes[r, 0].set_yticks([])
    axes[r, 0].set_title(f"Image {r + 1}", fontsize=10)
    c = 1
    for name, net in NETS.items():
        p = predict(net, x[None])[0]
        for k, f in cols:
            ax = axes[r, c]; ax.imshow(f(net, x), cmap="magma"); ax.set_xticks([]); ax.set_yticks([])
            ax.set_title(f"{name}, p = {p:.2f}\n{k}", fontsize=8.5); c += 1
fig.suptitle("Lab 11.1 gallery: four synthetic radiograph-like images, two networks, three attribution methods", fontsize=12)
fig.tight_layout(rect=(0, 0, 1, 0.97))
fig.savefig("gallery.png", dpi=110)
print("saved gallery.png; images used:", pick)
