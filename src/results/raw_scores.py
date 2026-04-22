import matplotlib.pyplot as plt
import numpy as np


class RawScores:
    def run(self):
        for bin_edges, counts1, counts2, marker, metric, output_file in self._params():
            self._plot(bin_edges, counts1, counts2, marker, metric, output_file)

    def _plot(self, bin_edges, counts1, counts2, marker, metric, output_file):
        width = bin_edges[1] - bin_edges[0]
        totals1 = counts1.sum()
        totals2 = counts2.sum()

        _, ax = plt.subplots(figsize=(8, 4))

        ax.bar(
            bin_edges[:-1],
            counts1 / (totals1 * width),
            width=width,
            align="edge",
            alpha=0.5,
            color="steelblue",
            label="Frequentist",
        )
        ax.bar(
            bin_edges[:-1],
            counts2 / (totals2 * width),
            width=width,
            align="edge",
            alpha=0.5,
            color="tomato",
            label="Bayesian",
        )
        if marker is not None:
            ax.axvline(x=marker, color="black", linestyle="--", linewidth=1.2, label="Null")

        ax.set_xlabel("Value")
        ax.set_ylabel("Density")
        ax.set_title(f"Overlapping Distributions: {metric}")
        ax.legend()

        plt.tight_layout()
        plt.savefig(output_file)

    def _params(self):
        yield (
            np.array([0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
            np.array([2.0, 22.0, 42.0, 45.0, 9.0]),
            np.array([3.0, 21.0, 42.0, 45.0, 9.0]),
            0.5,
            "AUROC",
            "raw_scores_auroc.png",
        )
        yield (
            np.array([-0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]),
            np.array([2.0, 15.0, 18.0, 38.0, 32.0, 14.0, 1.0]),
            np.array([4.0, 14.0, 16.0, 35.0, 37.0, 12.0, 2.0]),
            0,
            "MCC",
            "raw_scores_mcc.png",
        )
        yield (
            np.array([0.45, 0.65, 0.85, 1.05, 1.25, 1.45, 1.65]),
            np.array([32.0, 77.0, 7.0, 2.0, 1.0, 1.0]),
            np.array([39.0, 78.0, 3.0, 0.0, 0.0, 0.0]),
            -np.log(0.5),
            "NLL",
            "raw_scores_nll.png",
        )
        yield (
            np.array([0.16, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34]),
            np.array([7.0, 24.0, 57.0, 25.0, 5.0, 2.0]),
            np.array([6.0, 31.0, 64.0, 18.0, 1.0, 0.0]),
            0.25,
            "Brier score",
            "raw_scores_brier.png",
        )
        yield (
            np.array([0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]),
            np.array([10.0, 38.0, 33.0, 24.0, 11.0, 4.0]),
            np.array([13.0, 43.0, 37.0, 24.0, 3.0, 0.0]),
            None,
            "ECE",
            "raw_scores_ece.png",
        )
        yield (
            np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]),
            np.array([3.0, 15.0, 32.0, 29.0, 34.0, 6.0, 1.0]),
            np.array([6.0, 16.0, 32.0, 42.0, 22.0, 2.0, 0.0]),
            None,
            "MCE",
            "raw_scores_mce.png",
        )
