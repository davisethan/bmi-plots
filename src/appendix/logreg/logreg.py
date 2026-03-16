"""
Logistic regression vs. LDA decision boundaries.

References
----------
.. [1] https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
.. [2] https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


class LogisticRegressionPlot:
    def __init__(self):
        eigvecs = np.array([
            [np.cos(np.pi / 4), np.sin(np.pi / 4)],
            [np.cos(3 * np.pi / 4), np.sin(3 * np.pi / 4)]
        ])
        eigvals = np.diag([1, 3])
        cov = eigvecs @ eigvals @ eigvecs.T

        mean0 = np.array([-1, 1])
        mean1 = np.array([1, -1])

        rng = np.random.default_rng(seed=1)
        n_samples = 200
        self.X0 = rng.multivariate_normal(mean0, cov, n_samples)
        self.X1 = rng.multivariate_normal(mean1, cov, n_samples)

        n_outliers = 12
        self.outliers = rng.multivariate_normal([-10, 10], np.eye(2) * 0.3, n_outliers)

        self.X = np.vstack([self.X0, self.X1, self.outliers])
        self.y = np.array([0] * n_samples + [1] * n_samples + [1] * n_outliers)
        self.x1_range = np.linspace(self.X[:, 0].min() - 0.5, self.X[:, 0].max() + 0.5, 300)

        self.fig, self.ax = plt.subplots(figsize=(4, 4))

    def run(self):
        self._scatter()
        self._logreg()
        self._lda()
        self._cleanup()

    def _scatter(self):
        self.ax.scatter(
            *self.X0.T, color="tab:brown", label="Class 0", edgecolors="white", linewidths=0.4, zorder=2
        )
        self.ax.scatter(
            *self.X1.T, color="tab:cyan", label="Class 1", edgecolors="white", linewidths=0.4, zorder=2
        )
        self.ax.scatter(*self.outliers.T, color="tab:cyan", label="Outliers (class 1)", edgecolors="white", marker="*", s=100, linewidths=0.4, zorder=2)

    def _logreg(self):
        logreg = LogisticRegression()
        logreg.fit(self.X, self.y)
        logreg_acc = accuracy_score(self.y, logreg.predict(self.X))
        logreg_err = 1 - logreg_acc
        self.ax.plot(self.x1_range, self._boundary_line(logreg, self.x1_range), "k-", lw=2, label=f"LogReg  (err={logreg_err:.3f})")

    def _lda(self):
        lda = LinearDiscriminantAnalysis()
        lda.fit(self.X, self.y)
        lda_acc = accuracy_score(self.y, lda.predict(self.X))
        lda_err = 1 - lda_acc
        self.ax.plot(self.x1_range, self._boundary_line(lda, self.x1_range), "k--", lw=2, label=f"LDA  (err={lda_err:.3f})")

    def _boundary_line(self, model, x1):
        w = model.coef_[0]
        b = model.intercept_[0]
        return -(w[0] * x1 + b) / w[1]
    
    def _cleanup(self):
        self.ax.set_xlim(self.X[:, 0].min() - 0.5, self.X[:, 0].max() + 0.5)
        self.ax.set_ylim(self.X[:, 1].min() - 0.5, self.X[:, 1].max() + 0.5)
        self.ax.set_xlabel("$x_1$")
        self.ax.set_ylabel("$x_2$")
        self.ax.set_title("Logistic Regression vs. LDA under outliers")
        self.ax.legend(loc="upper right")
        plt.savefig("logreg")
