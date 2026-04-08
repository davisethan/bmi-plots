import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm


class LogNormal:
    def run(self):
        mus = [0.0, 0.0, 0.0, 1.0]
        sigmas = [0.5, 1.0, 2.0, 1.0]

        x = np.linspace(0, 4, 500)

        _, ax = plt.subplots(figsize=(6, 4))

        for mu, sigma in zip(mus, sigmas):
            y = lognorm.pdf(x, s=sigma, scale=np.exp(mu))
            ax.plot(x, y, label=f"μ={mu}, σ={sigma}")

        ax.set_xlim(0, 4)
        ax.set_ylim(0)
        ax.set_xlabel("ℓ")
        ax.set_ylabel("Density")
        ax.set_title("Log-Normal PDF")
        ax.legend()
        plt.tight_layout()
        plt.savefig("log-normal")
