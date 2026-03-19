# =====================
# Random effects model.
# =====================

library(ggplot2)

ggplot() +
  stat_function(fun = dnorm, args = list(mean = -1, sd = 2), xlim = c(-8, 8)) +
  stat_function(fun = dnorm, args = list(mean = 2, sd = 2), xlim = c(-8, 8)) +
  annotate(
    "segment",
    x = -1, xend = -1,
    y = 0, yend = dnorm(-1, -1, 2),
    linetype = "dashed", color = "slategray"
  ) +
  annotate(
    "segment",
    x = 2, xend = 2,
    y = 0, yend = dnorm(2, 2, 2),
    linetype = "dashed", color = "slategray"
  ) +
  annotate("text", x = -4, y = -0.03, label = expression(hat(theta)[k]), size = 4) +
  annotate("text", x = -1, y = -0.03, label = expression(theta[k]), size = 4) +
  annotate("text", x = 2, y = -0.03, label = expression(mu), size = 4) +
  annotate(
    "segment",
    x = -3.9, xend = -1.1,
    y = -0.07, yend = -0.07,
    arrow = arrow(ends = "both", length = unit(0.1, "cm")), color = "steelblue"
  ) +
  annotate(
    "segment",
    x = -0.9, xend = 1.9,
    y = -0.07, yend = -0.07,
    arrow = arrow(ends = "both", length = unit(0.1, "cm")), color = "steelblue"
  ) +
  annotate("text", x = -2.5, y = -0.1, label = expression(epsilon[k]), size = 4) +
  annotate("text", x = 0.5, y = -0.1, label = expression(zeta[k]), size = 4) +
  coord_cartesian(ylim = c(-0.1, NA), clip = "off") +
  theme_classic() +
  theme(
    axis.line = element_blank(),
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    axis.title = element_blank(),
    aspect.ratio = 0.4,
  )

ggsave("random_effects.png", width = 4, height = 2)
