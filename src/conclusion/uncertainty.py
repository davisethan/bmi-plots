import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF


class UncertaintyPlot:
    def run(self):
        X_train = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]).reshape(-1, 1)
        y_train = np.cos(X_train.ravel()) * 1.5
        X_pred = np.linspace(0.5, 9.0, 300).reshape(-1, 1)

        # Polynomial fit
        degree = 6
        coeffs = np.polyfit(X_train.ravel(), y_train, degree)
        y_poly = np.polyval(coeffs, X_pred.ravel())

        # Gaussian process fit
        kernel = RBF(length_scale=1.0)
        gp = GaussianProcessRegressor(kernel=kernel, alpha=0.1, n_restarts_optimizer=10)
        gp.fit(X_train, y_train)
        y_mean, y_std = gp.predict(X_pred, return_std=True)

        _, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Plot ploynomial estimate
        axes[0].plot(X_pred, y_poly, color="blue", linewidth=2)
        axes[0].scatter(X_train, y_train, marker="x", color="black", s=80, zorder=5)
        axes[0].set_title("Prediction without uncertainty", fontsize=14)
        axes[0].set_xticks([])
        axes[0].set_yticks([])

        # Plot Gaussian process estimate
        axes[1].plot(X_pred, y_mean, color="blue", linewidth=2)
        axes[1].fill_between(
            X_pred.ravel(),
            y_mean - 1.96 * y_std,
            y_mean + 1.96 * y_std,
            color="blue", alpha=0.2
        )
        axes[1].scatter(X_train, y_train, marker="x", color="black", s=80, zorder=5)
        axes[1].set_title("Prediction with uncertainty", fontsize=14)
        axes[1].set_xticks([])
        axes[1].set_yticks([])

        plt.tight_layout()
        plt.savefig("uncertainty")
