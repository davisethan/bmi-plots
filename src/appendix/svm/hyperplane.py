"""
Plot an SVM hyperplane.

References
----------
.. [1] https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


class Hyperplane:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(4, 4))
        self.fig.tight_layout()
        self.fig.set_layout_engine(None)
        self.ax.axis("off")
        self.ax.set_aspect("equal")

    def run(self):
        self.boundary()
        self.points()
        self.w_vec()
        self.b_vec()
        self.origin()
        self.right_angle()
        self.save()

    def boundary(self):
        x = np.linspace(0, 2, 100)
        y = 2 - x
        self.ax.plot(x, y, linewidth=2, color="black")

    def points(self):
        self.ax.plot(0.8, 0.2, "o", color="tab:blue")
        self.ax.text(0.7, 0, "Negatve", va="center", fontsize=14)

        self.ax.plot(1.8, 1.2, "o", color="tab:green")
        self.ax.text(1.7, 1, "Positive", va="center", fontsize=14)

    def w_vec(self):
        self.ax.annotate(
            "",
            xy=(2, 2),
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color="tab:purple", lw=2, mutation_scale=20),
        )
        self.ax.text(2, 1.8, r"$\mathbf{w}$", va="center", fontsize=14)

    def b_vec(self):
        self.ax.annotate(
            "",
            xy=(0.95, 1.05),
            xytext=(-0.05, 0.05),
            arrowprops=dict(arrowstyle="<->", color="tab:purple", lw=2, mutation_scale=20),
        )
        self.ax.text(0.35, 0.65, r"$b$", va="center", fontsize=14)

    def origin(self):
        self.ax.plot(0, 0, "o", color="black")
        self.ax.text(0.1, -0.1, r"$\mathbf{0}$", va="center", fontsize=14)

    def right_angle(self):
        corners = [(1, 1), (1.1, 1.1), (1, 1.2), (0.9, 1.1)]
        diamond = mpatches.Polygon(corners, closed=True, facecolor="none", edgecolor="black", lw=2)
        self.ax.add_patch(diamond)

    def save(self):
        plt.tight_layout()
        plt.savefig("hyperplane.png")
