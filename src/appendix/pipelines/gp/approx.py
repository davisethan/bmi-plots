"""
Show full inference GP vs. DTC side by side.

References
----------
.. [1] https://gpy.readthedocs.io/en/deploy/
"""

import GPy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.datasets import make_moons


class GPPlot:
    def run(self):
        X, y = make_moons(n_samples=300, noise=0.1)
        y = y.reshape(-1, 1) * 2 - 1
        Z = X[::10]

        full = GPy.models.GPClassification(X, y, kernel=GPy.kern.RBF(2))
        full.optimize()

        dtc = GPy.models.SparseGPClassification(X, y, kernel=GPy.kern.RBF(2), Z=Z)
        dtc.optimize()

        self._plot_gp_classification(full, "Full GP", X, y)
        self._plot_gp_classification(dtc, "Sparse DTC", X, y)

    def _plot_gp_classification(self, model, name, X, y):
        x0_min, x0_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
        x1_min, x1_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(
            np.linspace(x0_min, x0_max),
            np.linspace(x1_min, x1_max),
        )
        Xgrid = np.c_[xx.ravel(), yy.ravel()]

        _, ax = plt.subplots(figsize=(4, 3))

        scatter_colors = np.where(y.squeeze() == 1, "tab:red", "tab:blue")
        cmap = mcolors.LinearSegmentedColormap.from_list("br", ["tab:blue", "white", "tab:red"])

        mu, _ = model.predict_noiseless(Xgrid)
        prob = model.likelihood.gp_link.transf(mu)
        prob = prob.reshape(xx.shape)

        ax.contourf(xx, yy, prob, levels=50, cmap=cmap, alpha=0.6, vmin=0, vmax=1)
        ax.contour(xx, yy, prob, levels=[0.5], colors="k", linewidths=1.5)

        ax.scatter(X[:, 0], X[:, 1], c=scatter_colors, edgecolors="white", linewidths=0.4, zorder=3)

        if hasattr(model, "Z"):
            Z = model.Z.values
            ax.scatter(
                Z[:, 0], Z[:, 1], marker="x", s=60, c="k", linewidths=1.2, zorder=4, label="inducing pts"
            )
            ax.legend(fontsize=9, loc="upper right")

        ax.set_title(name)
        ax.set_xlim(x0_min, x0_max)
        ax.set_ylim(x1_min, x1_max)
        ax.set_aspect("equal")

        plt.tight_layout()
        plt.savefig(name.lower().replace(" ", "-"))
