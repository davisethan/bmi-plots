"""
Plot a margin of an SVM hyperplane.

References
----------
.. [1] https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


class Margin:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(4, 4))
        self.fig.tight_layout()
        self.fig.set_layout_engine(None)
        self.ax.axis("off")
        self.ax.set_aspect("equal")

    def run(self):
        self.boundary()
        self.w_vec()
        self.origin()
        self.right_angle()
        self.primary_point()
        self.primary_vec()
        self.projection_point()
        self.projection_vec()
        self.distance()
        self.distance_right_angle()
        self.save()

    def boundary(self):
        x = np.linspace(0, 2, 100)
        y = 2 - x
        self.ax.plot(x, y, linewidth=2, color="black")

    def w_vec(self):
        self.ax.annotate(
            "",
            xy=(2, 2),
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color="tab:purple", lw=2, mutation_scale=20),
        )
        self.ax.text(2, 1.8, r"$\mathbf{w}$", va="center", fontsize=14)

    def origin(self):
        self.ax.plot(0, 0, "o", color="black")
        self.ax.text(0.1, -0.1, r"$\mathbf{0}$", va="center", fontsize=14)

    def right_angle(self):
        corners = [(1.1, 0.9), (1.2, 1), (1.1, 1.1), (1, 1)]
        diamond = mpatches.Polygon(corners, closed=True, facecolor="none", edgecolor="black", lw=2)
        self.ax.add_patch(diamond)

    def primary_point(self):
        self.ax.plot(1, 2, "o", color="black")
        self.ax.text(1.1, 1.9, r"$\mathbf{x}_p$", va="center", fontsize=14)

    def primary_vec(self):
        x = np.linspace(0, 1, 100)
        y = 2 * x
        self.ax.plot(x, y, linewidth=2, color="tab:orange")

    def projection_point(self):
        self.ax.plot(0.5, 1.5, "o", color="black")
        self.ax.text(0.2, 1.4, r"$\mathbf{x}_p'$", va="center", fontsize=14)

    def projection_vec(self):
        x = np.linspace(0, 0.5, 100)
        y = 3 * x
        self.ax.plot(x, y, linewidth=2, color="tab:orange")

    def distance(self):
        x = np.linspace(0.5, 1, 100)
        y = 1 + x
        self.ax.plot(x, y, linewidth=2, color="tab:red", linestyle="--")
        self.ax.text(0.65, 1.8, r"$r$", va="center", fontsize=14)

    def distance_right_angle(self):
        corners = [(0.5, 1.5), (0.6, 1.6), (0.5, 1.7), (0.4, 1.6)]
        diamond = mpatches.Polygon(corners, closed=True, facecolor="none", edgecolor="black", lw=2)
        self.ax.add_patch(diamond)

    def save(self):
        plt.tight_layout()
        plt.savefig("margin.png")
