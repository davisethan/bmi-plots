# ==================
# Subgroup analysis.
# ==================

library(ggplot2)

plot_curves <- function(p, rngs, mu, sigma, factor, chars, color) {
  rngs <- rngs + factor
  mu <- mu + factor
  p +
    stat_function(fun = dnorm, args = list(mean = mu[2], sd = sigma[1]), xlim = c(rngs[1], rngs[2])) +
    stat_function(fun = dnorm, args = list(mean = mu[3], sd = sigma[2]), xlim = c(rngs[3], rngs[4])) +
    annotate(
      "segment",
      x = mu[2], xend = mu[2],
      y = 0, yend = dnorm(mu[2], mu[2], sigma[1]),
      linetype = "dashed", color = "slategray"
    ) +
    annotate(
      "segment",
      x = mu[3], xend = mu[3],
      y = 0, yend = dnorm(mu[3], mu[3], sigma[2]),
      linetype = "dashed", color = "slategray"
    ) +
    annotate("text", x = mu[1], y = -0.04, label = chars[1], size = 4) +
    annotate("text", x = mu[2], y = -0.045, label = chars[2], size = 4) +
    annotate("text", x = mu[3], y = -0.04, label = chars[3], size = 4) +
    annotate(
      "segment",
      x = mu[1] + 0.1, xend = mu[2] - 0.1,
      y = -0.09, yend = -0.09,
      arrow = arrow(ends = "both", length = unit(0.1, "cm")), color = color
    ) +
    annotate(
      "segment",
      x = mu[2] + 0.1, xend = mu[3] - 0.1,
      y = -0.09, yend = -0.09,
      arrow = arrow(ends = "both", length = unit(0.1, "cm")), color = color
    ) +
    annotate("text", x = (mu[1] + mu[2]) / 2, y = -0.12, label = chars[4], size = 4) +
    annotate("text", x = (mu[2] + mu[3]) / 2, y = -0.12, label = chars[5], size = 4) +
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

p <- ggplot()
p <- plot_curves(
  p,
  c(-9, 3, -5, 5),
  c(-6, -3, 0),
  c(2, 1.5),
  -2,
  c(
    expression(hat(theta)[r]),
    expression(theta[r]),
    expression(hat(mu)[A]),
    expression(epsilon[r]),
    expression(zeta[r])
  ),
  "steelblue"
)
p <- plot_curves(
  p,
  c(2, 12, 4, 16),
  c(4, 7, 10),
  c(1.2, 1.7),
  2,
  c(
    expression(hat(theta)[s]),
    expression(theta[s]),
    expression(hat(mu)[B]),
    expression(epsilon[s]),
    expression(zeta[s])
  ),
  "firebrick"
)

ggsave("subgroup.png", width = 4, height = 2)
