import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta as beta_dist


class Beta:
    def run(self):
        alphas = [1.0, 2.0, 4.0, 8.0]
        betas = [1.0, 2.0, 4.0, 8.0]
        x = np.linspace(0, 1, 500)
        _, ax = plt.subplots(figsize=(6, 4))

        for a, b in zip(alphas, betas):
            dist = beta_dist(a, b)
            y = dist.pdf(x)
            ax.plot(x, y, label=f"α={a}, β={b}")

        ax.set_xlim(0, 1)
        ax.set_ylim(0)
        ax.set_xlabel("x")
        ax.set_ylabel("Density")
        ax.set_title("Beta PDF")
        ax.legend()
        plt.tight_layout()
        plt.savefig("beta")
