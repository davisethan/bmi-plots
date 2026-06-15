import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm

class GPC:
    def run(self):
        RANDOM_SEED = 8888
        rng = np.random.default_rng(RANDOM_SEED)
        n = 100
        x = np.linspace(0, 10, n)

        # true covariance
        ell_true = 0.5
        eta_true = 1.0
        cov_func = eta_true**2 * pm.gp.cov.ExpQuad(1, ell_true)
        K = cov_func(x[:, None]).eval()

        # zero mean function
        mean = np.zeros(n)

        # sample from the gp prior
        f_true = pm.draw(pm.MvNormal.dist(mu=mean, cov=K, method="svd"), 1, random_seed=rng)

        # Sample the GP through the likelihood
        y = pm.Bernoulli.dist(p=pm.math.invlogit(f_true)).eval()

        fig = plt.figure(figsize=(5, 4))
        ax = fig.gca()
        ax.plot(x, pm.math.invlogit(f_true).eval(), "dodgerblue", lw=3)
        ax.plot(x, y + np.random.randn(n) * 0.01, "kx", ms=6)
        ax.tick_params(axis='both', which='major', labelsize=12)
        plt.tight_layout()
        plt.savefig("gpc.png")
