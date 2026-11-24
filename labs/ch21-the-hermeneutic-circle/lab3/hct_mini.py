"""A small teaching re-implementation of the Hermeneutic Circle Test (HCT) for one tabular setting.

It follows the definitions published in Seker (2026), "Measuring the hermeneutic circle in explainable AI",
Machine Learning and Knowledge Extraction 8(11), 381, https://doi.org/10.3390/make8110381, Sections 3.1-3.6,
as far as the published text states them. It is NOT the reference implementation (that one is released with
the paper as supplementary code). Simplifications, all deliberate and listed in the lab README:
one dataset (German Credit), one model (a random forest), no meaning units (no feature pair in German Credit
reaches the 0.9 correlation the paper uses to group features; the code checks this), no HermAI-H explainer,
and the sign-flip control flips KernelSHAP rather than HermAI-H.

Positive class = "bad credit risk" (the refusal side). f(x) = predicted probability of bad risk.
"""
import contextlib, io, warnings
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

warnings.filterwarnings("ignore")
ALPHA, K_NOV, K_REP, EPS, SCALES = 0.05, 10, 30, 0.01, (1.0, 0.5, 0.25, 0.125)


# ---------------------------------------------------------------- data and model
def load_german():
    """German Credit (Statlog) from OpenML; categories are integer-coded (sorted labels), as in the paper."""
    df = fetch_openml("credit-g", version=1, as_frame=True).frame.copy()
    y = (df.pop("class").astype(str) == "bad").astype(int).values
    codebook = {}
    for c in df.columns:
        if str(df[c].dtype) in ("category", "object"):
            cats = sorted(df[c].astype(str).unique())
            codebook[c] = cats
            df[c] = df[c].astype(str).map({v: i for i, v in enumerate(cats)}).astype(int)
    return df.astype(float), y, codebook


def setup(seed=0):
    X, y, codebook = load_german()
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=seed, stratify=y)
    Xfit, Xcal = train_test_split(Xtr, test_size=0.25, random_state=seed, stratify=ytr)
    rf = RandomForestClassifier(n_estimators=200, min_samples_leaf=2, random_state=seed, n_jobs=-1)
    rf.fit(Xtr.values, ytr)
    f = lambda A: rf.predict_proba(np.asarray(A, float))[:, 1]
    return dict(X=X, y=y, Xtr=Xtr, Xte=Xte, ytr=ytr, yte=yte, Xfit=Xfit, Xcal=Xcal, rf=rf, f=f,
                codebook=codebook, cols=list(X.columns), cat=[c for c in X.columns if c in codebook])


def max_abs_corr(Xfit):
    c = np.abs(np.corrcoef(Xfit.values, rowvar=False)); np.fill_diagonal(c, 0)
    return float(c.max())


# ---------------------------------------------------------------- the horizon (HP)
class Horizon:
    """Split-conformal kNN novelty test in standardized space, plus the measurement-scale condition."""
    def __init__(self, Xfit, Xcal):
        self.mu, self.sd = Xfit.values.mean(0), Xfit.values.std(0) + 1e-12
        self.nn = NearestNeighbors(n_neighbors=K_NOV).fit(self.z(Xfit.values))
        self.cal = np.sort(self.score(Xcal.values))
        self.lo, self.hi = Xfit.values.min(0), Xfit.values.max(0)
        self.integer = np.all(np.isclose(Xfit.values, np.round(Xfit.values)), axis=0)

    def z(self, A):
        return (np.asarray(A, float) - self.mu) / self.sd

    def score(self, A):
        return self.nn.kneighbors(self.z(A))[0][:, -1]

    def pvalue(self, A):
        s = self.score(A)
        return (1 + len(self.cal) - np.searchsorted(self.cal, s, side="left")) / (len(self.cal) + 1)

    def parts(self, A):
        A = np.atleast_2d(np.asarray(A, float))
        dist_ok = self.pvalue(A) > ALPHA
        int_ok = np.all(np.isclose(A[:, self.integer], np.round(A[:, self.integer])), axis=1)
        rng_ok = np.all((A >= self.lo - 1e-9) & (A <= self.hi + 1e-9), axis=1)
        return dist_ok, int_ok & rng_ok

    def inside(self, A):
        d, t = self.parts(A)
        return d & t


# ---------------------------------------------------------------- explainers
class Recorder:
    """Wraps the model so that every point an explainer queries is kept as evidence."""
    def __init__(self, f):
        self.f, self.points = f, []
    def __call__(self, A):
        A = np.asarray(A, float); self.points.append(A); return self.f(A)
    def predict_proba(self, A):
        p = self(A); return np.c_[1 - p, p]
    def evidence(self, skip_first=False):
        pts = self.points[1:] if skip_first else self.points
        return np.vstack(pts) if pts else np.zeros((0, 0))


def make_explainers(S, seed=0):
    import shap, lime.lime_tabular
    from hermai.explainers import LocalExplainer
    from hermai.perturbations import TabularPerturbationGenerator as GenIndependent          # package level
    from hermai.perturbations.tabular import TabularPerturbationGenerator as GenCov           # README path
    Xfit, f, cols = S["Xfit"], S["f"], S["cols"]
    mu = Xfit.values.mean(0)
    bg = shap.kmeans(Xfit.values, 10)            # rounds centroids to observed values (shap default)
    cat_idx = [cols.index(c) for c in S["cat"]]
    lime_exp = lime.lime_tabular.LimeTabularExplainer(
        Xfit.values, feature_names=cols, categorical_features=cat_idx, discretize_continuous=True,
        mode="classification", random_state=seed)
    gens = {}
    with contextlib.redirect_stdout(io.StringIO()):
        for name, G in (("HermAI 0.1.8", GenIndependent), ("HermAI 0.1.8 (cov)", GenCov)):
            g = G(categorical_features=S["cat"]); g.fit(Xfit); gens[name] = g

    def kernelshap(x, i):
        rec = Recorder(f)
        np.random.seed(seed * 100000 + i)                  # KernelExplainer samples coalitions with np.random
        phi = shap.KernelExplainer(rec, bg).shap_values(x[None], nsamples=500, silent=True)
        return dict(a=np.asarray(phi).reshape(-1), E=rec.evidence(skip_first=True), cf=None)

    def lime_(x, i):
        rec = Recorder(f)
        e = lime_exp.explain_instance(x, rec.predict_proba, num_features=len(cols), num_samples=1000, labels=(1,))
        a = np.zeros(len(cols))
        for j, w in e.as_map()[1]:
            a[j] = w
        return dict(a=a, E=rec.evidence(), cf=None)

    def hermai_(name):
        def run(x, i):
            rec = Recorder(f)
            np.random.seed(seed * 100000 + i)              # the library has no seed argument
            inst = pd.Series(x, index=cols)
            with contextlib.redirect_stdout(io.StringIO()):
                ex = LocalExplainer(rec, gens[name]).explain(inst, n_samples=1000)
            E = rec.evidence(skip_first=True)              # first call is the instance itself
            coef = ex.feature_importances.set_index("feature").loc[cols, "importance"].values
            sd = E.std(0); slope_raw = np.where(sd > 0, coef / np.where(sd > 0, sd, 1), 0.0)
            a = slope_raw * (x - mu)                       # contribution relative to the training mean
            cf = None if ex.counterfactual is None else ex.counterfactual[cols].values.astype(float)
            claims = [(int(j), float(np.sign(coef[j]))) for j in top3(coef)]   # what the narrative says
            return dict(a=a, E=E, cf=cf, slope=coef, claims=claims, narrative=ex.narrative())
        return run

    return {"KernelSHAP": kernelshap, "LIME": lime_,
            "HermAI 0.1.8": hermai_("HermAI 0.1.8"), "HermAI 0.1.8 (cov)": hermai_("HermAI 0.1.8 (cov)")}


def pick_cases(S, n=100, seed=0):
    """Half from each predicted class where possible."""
    Xte, f = S["Xte"].values, S["f"]
    yhat = (f(Xte) >= 0.5).astype(int)
    rng = np.random.default_rng(seed)
    pos, neg = np.where(yhat == 1)[0], np.where(yhat == 0)[0]
    k = min(n // 2, len(pos))
    idx = np.r_[rng.choice(pos, k, replace=False), rng.choice(neg, n - k, replace=False)]
    return np.sort(idx)


def explain_all(S, idx, seed=0, verbose=True):
    ex = make_explainers(S, seed)
    out = {name: [] for name in ex}
    Xte = S["Xte"].values
    for name, fn in ex.items():
        for i in idx:
            out[name].append(fn(Xte[i], int(i)))
        if verbose:
            print(f"  explained {len(idx)} cases with {name}")
    rng = np.random.default_rng(seed + 7)
    d = Xte.shape[1]
    out["Random"] = [dict(a=rng.standard_normal(d), E=None, cf=None) for _ in idx]
    out["Sign-flip"] = [dict(a=-r["a"], E=r["E"], cf=None) for r in out["KernelSHAP"]]
    return out


# ---------------------------------------------------------------- claims (CVR)
def top3(a):
    nz = np.where(np.abs(a) > 1e-12)[0]
    return nz[np.argsort(-np.abs(a[nz]))][:3]


def claim_test(S, H, x, j, sigma, mode="horizon", rng=None):
    """On-horizon direction claim: replace feature j with the values of the K nearest comparable cases
    (distance on the other features). Delta = f(x) - mean f(x with j replaced). Pass if the sign matches
    the claim and |Delta| >= max(eps, 1.96 SE)."""
    Xf, f = S["Xfit"].values, S["f"]
    if mode == "horizon":
        keep = [k for k in range(len(x)) if k != j]
        zf, zx = H.z(Xf)[:, keep], H.z(x[None])[:, keep]
        nbr = np.argsort(((zf - zx) ** 2).sum(1))[:K_REP]
    else:                                                       # marginal variant
        nbr = rng.choice(len(Xf), K_REP, replace=False)
    R = np.repeat(x[None], K_REP, 0); R[:, j] = Xf[nbr, j]
    fr = f(R); delta = f(x[None])[0] - fr.mean(); se = fr.std(ddof=1) / np.sqrt(K_REP)
    return bool(np.sign(delta) == sigma and abs(delta) >= max(EPS, 1.96 * se)), float(delta)


def slope_test(S, H, x, j, sigma):
    """Literal (slope) reading: does increasing feature j raise the probability?"""
    f = S["f"]; diffs = []
    for h in (0.25, 0.5):
        up, dn = x.copy(), x.copy(); up[j] += h * H.sd[j]; dn[j] -= h * H.sd[j]
        diffs.append(f(up[None])[0] - f(dn[None])[0])
    d = float(np.mean(diffs))
    return bool(np.sign(d) == sigma and abs(d) >= EPS)


# ---------------------------------------------------------------- part and whole (PWA, HHR)
class Wholes:
    def __init__(self, S, H):
        import shap
        self.S, self.H, self.shap = S, H, shap
        Xf = S["Xfit"].values
        self.Xf, self.pf = Xf, S["f"](Xf)
        self.W1 = DecisionTreeRegressor(max_depth=4, random_state=0).fit(Xf, self.pf)
        self.T1 = shap.TreeExplainer(self.W1)

    def account(self, x, s):
        if s == 1.0:
            W, T = self.W1, self.T1
        else:
            n = int(round(s * len(self.Xf)))
            nb = np.argsort(((self.H.z(self.Xf) - self.H.z(x[None])) ** 2).sum(1))[:n]
            W = DecisionTreeRegressor(max_depth=3, random_state=0).fit(self.Xf[nb], self.pf[nb])
            T = self.shap.TreeExplainer(W)
        g = np.asarray(T.shap_values(x[None])).reshape(-1)
        return g, int(W.predict(x[None])[0] >= 0.5)


def sa3(a, g):
    ta, tg = set(top3(a)), set(top3(g))
    return sum(1 for u in ta & tg if np.sign(a[u]) == np.sign(g[u])) / 3.0


def pwa_profile(a, x, yhat, wholes, cache):
    vals = []
    for s in SCALES:
        key = (x.tobytes(), s)
        if key not in cache:
            cache[key] = wholes.account(x, s)
        g, yw = cache[key]
        vals.append(sa3(a, g) * (yw == yhat))
    ok = [s for s, v in zip(SCALES, vals) if v >= 2 / 3 - 1e-9]
    return vals, (max(ok) if ok else 0.0)


# ---------------------------------------------------------------- machine readers (HG)
def readers():
    return {"logistic": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
            "3-NN": lambda: make_pipeline(StandardScaler(), KNeighborsClassifier(3)),
            "tree": lambda: DecisionTreeClassifier(max_depth=3, random_state=0)}


def hermeneutic_gain(S, idx, A, seed=0, budgets=(10, 20, 40, 80), reps=10):
    """A: attributions (n_cases x d) for the explained cases idx. Readers learn the model's decisions
    from m explained cases using the 3 features the explanations favour (A) or 3 random features (B)."""
    Xte, f = S["Xte"].values, S["f"]
    yhat = (f(Xte) >= 0.5).astype(int)
    held = np.setdiff1d(np.arange(len(Xte)), idx)
    Xh, yh = Xte[held], yhat[held]
    Xe, ye = Xte[idx], yhat[idx]
    rng = np.random.default_rng(seed); d = Xte.shape[1]; res = {}
    lx = np.log2(budgets)
    for rname, make in readers().items():
        accA, accB = [], []
        for m in budgets:
            a_m, b_m = [], []
            for _ in range(reps):
                while True:
                    tr = rng.choice(len(idx), m, replace=False)
                    if len(set(ye[tr])) == 2:
                        break
                feats = top3(np.abs(A[tr]).mean(0))
                a_m.append((make().fit(Xe[tr][:, feats], ye[tr]).predict(Xh[:, feats]) == yh).mean())
                for _ in range(5):
                    rf_ = rng.choice(d, 3, replace=False)
                    b_m.append((make().fit(Xe[tr][:, rf_], ye[tr]).predict(Xh[:, rf_]) == yh).mean())
            accA.append(np.mean(a_m)); accB.append(np.mean(b_m))
        aucA = np.trapz(accA, lx) / (lx[-1] - lx[0]); aucB = np.trapz(accB, lx) / (lx[-1] - lx[0])
        res[rname] = (aucA - aucB) / (1 - aucB)
    return float(np.mean(list(res.values()))), float(min(res.values())), res


# ---------------------------------------------------------------- the profile
def hct_profile(S, idx, out, seed=0, verbose=True):
    H = Horizon(S["Xfit"], S["Xcal"]); W = Wholes(S, H)
    Xte, f = S["Xte"].values, S["f"]
    yhat = (f(Xte) >= 0.5).astype(int)
    rng = np.random.default_rng(seed + 11)
    rows, per_case, cache = [], {}, {}
    for name, R in out.items():
        hp, hpd, hpt, cvr, cvr_m, slope_ok, inv, pwa_s, hhr, empty, pgi = [], [], [], [], [], [], [], [], [], 0, []
        cvr_vec, cf_ok, cf_n = [], [], []
        cases = []
        for r, i in zip(R, idx):
            x, a = Xte[i], r["a"]
            if r["E"] is not None and len(r["E"]):
                dd, tt = H.parts(r["E"]); hp.append((dd & tt).mean()); hpd.append(dd.mean()); hpt.append(tt.mean())
            t3 = top3(a)
            claims = r.get("claims") or [(int(j), float(np.sign(a[j]))) for j in t3]
            if len(claims) == 0:
                empty += 1
            res = [claim_test(S, H, x, j, sg) for j, sg in claims]
            crng = np.random.default_rng(1000 + int(i))      # same marginal draws for every explainer
            if len(claims):
                cvr.append(np.mean([p for p, _ in res]))
                cvr_vec.append(np.mean([claim_test(S, H, x, j, np.sign(a[j]))[0] for j in t3]))
                cvr_m.append(np.mean([claim_test(S, H, x, j, sg, "marginal", crng)[0] for j, sg in claims]))
            if len(t3):
                Rm = np.repeat(x[None], K_REP, 0); nb = np.random.default_rng(2000 + int(i)).choice(len(S["Xfit"]), K_REP, replace=False)
                Rm[:, t3] = S["Xfit"].values[nb][:, t3]; pgi.append(np.abs(f(x[None])[0] - f(Rm)).mean())
            if "slope" in r and len(t3):
                st = top3(r["slope"])
                slope_ok.append(np.mean([slope_test(S, H, x, j, np.sign(r["slope"][j])) for j in st]))
                inv.append(np.mean([np.sign(r["slope"][j]) != np.sign(a[j]) for j in st]))
            if r.get("cf") is not None:
                cf = r["cf"]; cf_ok.append(int((f(cf[None])[0] >= 0.5) != yhat[i]) * bool(H.inside(cf)[0]))
                cf_n.append(int((~np.isclose(cf, x)).sum()))
            vals, h = pwa_profile(a, x, yhat[i], W, cache)
            pwa_s.append(vals); hhr.append(h)
            cases.append(dict(i=int(i), top3=t3, claims=claims, results=res, pwa=vals, hhr=h))
        per_case[name] = cases
        hg, hgmin, _ = hermeneutic_gain(S, idx, np.array([r["a"] for r in R]), seed)
        P = np.array(pwa_s); hhr = np.array(hhr)
        row = dict(explainer=name, HP=np.mean(hp) if hp else np.nan, HPdist=np.mean(hpd) if hpd else np.nan,
                   HPtype=np.mean(hpt) if hpt else np.nan, CVR=np.mean(cvr), CVR_vector=np.mean(cvr_vec),
                   CVR_marginal=np.mean(cvr_m),
                   PWA=P[:, 0].mean(), PWA_half=P[:, 1].mean(), PWA_quarter=P[:, 2].mean(), PWA_eighth=P[:, 3].mean(),
                   GI=(hhr == 1).mean(), AR=(hhr == 0).mean(), HG=hg, HGmin=hgmin, PGI_marginal=np.mean(pgi),
                   empty=empty, slope_CVR=np.mean(slope_ok) if slope_ok else np.nan,
                   inversion=np.mean(inv) if inv else np.nan,
                   CF_found=len(cf_ok) / len(R) if "slope" in R[0] else np.nan,
                   CF_valid=np.mean(cf_ok) if cf_ok else np.nan, CF_changed=np.mean(cf_n) if cf_n else np.nan)
        row["HCT"] = (row["HP"] * row["CVR"] * row["PWA"] * max(row["HGmin"], 0)) ** 0.25 if hp else np.nan
        rows.append(row)
        if verbose:
            print(f"  profile done: {name}")
    real_hp = H.inside(Xte).mean()
    return pd.DataFrame(rows).set_index("explainer"), per_case, H, W, real_hp
