"""
Plot the LDA and QDA solutions.

References
----------
.. [1] https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis
.. [2] https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.patches import Ellipse
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis as LDA,
    QuadraticDiscriminantAnalysis as QDA,
)


class LDAPlot:
    def __init__(self):
        self.eigvecs = np.array(
            [[np.cos(np.pi / 4), np.sin(np.pi / 4)], [np.cos(3 * np.pi / 4), np.sin(3 * np.pi / 4)]]
        )
        self.eigvals = np.diag([1, 3])
        self.cov = self.eigvecs @ self.eigvals @ self.eigvecs.T

        self.mean0 = np.array([-1, 1])
        self.mean1 = np.array([1, -1])

        rng = np.random.default_rng(seed=1)
        self.n_samples = 200
        self.X0 = rng.multivariate_normal(self.mean0, self.cov, self.n_samples)
        self.X1 = rng.multivariate_normal(self.mean1, self.cov, self.n_samples)

        self.X = np.vstack([self.X0, self.X1])
        self.y = np.hstack([np.zeros(self.n_samples), np.ones(self.n_samples)])

        self.color0 = "tab:brown"
        self.color1 = "tab:cyan"

    def run(self):
        self._lda()
        self._qda()

    def _lda(self):
        _, ax = plt.subplots(figsize=(4, 4))

        lda = LDA()
        lda.fit(self.X, self.y)

        x1_vals = np.linspace(self.X[:, 0].min() - 1, self.X[:, 0].max() + 1, 200)
        w1, w2 = lda.coef_[0]
        b = lda.intercept_[0]
        x2_vals = -(w1 * x1_vals + b) / w2

        ax.scatter(
            *self.X0.T, color=self.color0, label="Class 0", edgecolors="white", linewidths=0.4, zorder=2
        )
        ax.scatter(
            *self.X1.T, color=self.color1, label="Class 1", edgecolors="white", linewidths=0.4, zorder=2
        )
        self._ellipse(ax, self.mean0, self.cov, self.color0)
        self._ellipse(ax, self.mean1, self.cov, self.color1)
        ax.plot(x1_vals, x2_vals, "k--", linewidth=2, zorder=4)

        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")
        ax.set_title("LDA Decision Boundary")
        ax.legend(loc="upper right")
        plt.tight_layout()
        plt.savefig("lda")

    def _qda(self):
        _, ax = plt.subplots(figsize=(4, 4))

        qda = QDA(store_covariance=True)
        qda.fit(self.X, self.y)

        x1_min, x1_max = self.X[:, 0].min() - 1, self.X[:, 0].max() + 1
        x2_min, x2_max = self.X[:, 1].min() - 1, self.X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max, 400), np.linspace(x2_min, x2_max, 400))

        Z = qda.predict(np.c_[xx1.ravel(), xx2.ravel()]).reshape(xx1.shape)

        ax.scatter(
            *self.X0.T, color=self.color0, label="Class 0", edgecolors="white", linewidths=0.4, zorder=2
        )
        ax.scatter(
            *self.X1.T, color=self.color1, label="Class 1", edgecolors="white", linewidths=0.4, zorder=2
        )
        self._ellipse(ax, self.mean0, qda.covariance_[0], self.color0)
        self._ellipse(ax, self.mean1, qda.covariance_[1], self.color1)
        ax.contour(xx1, xx2, Z, levels=[0.5], colors="k", linestyles="--", linewidths=2, zorder=4)

        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")
        ax.set_title("QDA Decision Boundary")
        ax.legend(loc="upper right")
        plt.tight_layout()
        plt.savefig("qda")

    def _ellipse(self, ax, mean, cov, color, n_std=3):
        eigvals, eigvecs = np.linalg.eigh(cov)
        width, height = 2 * n_std * np.sqrt(eigvals)
        theta = np.degrees(np.arctan2(eigvecs[1, 0], eigvecs[0, 0]))
        ellipse = Ellipse(
            mean,
            width=width,
            height=height,
            angle=theta,
            edgecolor=to_rgba(color, alpha=0.4),
            facecolor=to_rgba(color, alpha=0.2),
            zorder=3,
        )
        ax.add_patch(ellipse)
