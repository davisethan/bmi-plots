# =====================================
# Meta-regression as subgroup analysis.
# =====================================

library(ggplot2)

plot_curve <- function(p, param, rng, text) {
  p +
    stat_function(fun = dnorm, args = list(mean = param[1], sd = param[2]), xlim = c(rng[1], rng[2])) +
    annotate(
      "segment",
      x = param[1], xend = param[1],
      y = 0, yend = dnorm(param[1], param[1], param[2]),
      linetype = "dashed", color = "slategray"
    ) +
    annotate("text", x = param[1], y = -0.04, label = text[1], size = 4) +
    annotate(
      "text",
      x = param[1], y = dnorm(param[1], param[1], param[2]) + 0.04,
      label = text[2], size = 4
    ) +
    coord_cartesian(ylim = c(-0.1, NA), clip = "off") +
    theme_classic() +
    theme(
      axis.line = element_blank(),
      axis.text = element_blank(),
      axis.ticks = element_blank(),
      axis.title = element_blank(),
      aspect.ratio = 0.4,
    )
}

plot_arrow <- function(p, rng, text, color) {
  p +
    annotate(
      "segment",
      x = rng[1] + 0.2, xend = rng[2] - 0.1,
      y = -0.04, yend = -0.04,
      arrow = arrow(ends = "both", length = unit(0.1, "cm")), color = color
    ) +
    annotate("text", x = (rng[1] + rng[2]) / 2, y = -0.09, label = text, size = 4)
}

p <- ggplot()
p <- plot_curve(
  p,
  c(-2, 1.7), c(-6, 2),
  c(expression(theta), expression(D[g] == 0))
)
p <- plot_curve(
  p,
  c(2, 1.3), c(-2, 6),
  c(expression(phantom(x)), expression(D[g] == 1))
)
p <- plot_arrow(p, c(-2, 2), expression(beta), "steelblue")

ggsave("subgroup_regression.png", width = 4, height = 2)
