# =========================
# Multilevel meta-analysis.
# =========================

library(ggplot2)

plot_curves <- function(p, rng, mu, sigma, chars, color) {
  p +
    stat_function(fun = dnorm, args = list(mean = mu[2], sd = sigma), xlim = c(rng[1], rng[2])) +
    annotate(
      "segment",
      x = mu[2], xend = mu[2],
      y = 0, yend = dnorm(mu[2], mu[2], sigma),
      linetype = "dashed", color = "slategray"
    ) +
    annotate("text", x = mu[1], y = -0.04, label = chars[1], size = 4) +
    annotate("text", x = mu[2], y = -0.045, label = chars[2], size = 4) +
    annotate(
      "segment",
      x = mu[1] + 0.1, xend = mu[2] - 0.1,
      y = -0.08, yend = -0.08,
      arrow = arrow(ends = "both", length = unit(0.1, "cm")), color = color
    ) +
    annotate("text", x = (mu[1] + mu[2]) / 2, y = -0.11, label = chars[3], size = 4) +
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
  c(-11, 1),
  c(-8, -5),
  2,
  c(
    expression(hat(theta)[ij]),
    expression(theta[ij]),
    expression(epsilon[ij])
  ),
  "darkolivegreen"
)
p <- plot_curves(
  p,
  c(-7, 3),
  c(-5, -2),
  1.5,
  c(
    expression(phantom(x)),
    expression(kappa[j]),
    expression(zeta[paste("(2)ij")])
  ),
  "darkolivegreen"
)
p <- plot_curves(
  p,
  c(-4, 6),
  c(-2, 1),
  1.8,
  c(
    expression(phantom(x)),
    expression(mu),
    expression(zeta[paste("(3)j")])
  ),
  "darkolivegreen"
)

ggsave("multilevel.png", width = 4, height = 2)
