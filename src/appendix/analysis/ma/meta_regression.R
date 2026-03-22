# =========================================
# Random-effects model vs. meta-regression.
# =========================================

library(ggplot2)

set.seed(1)

n <- 10
x <- seq(1, 9, length.out = n)
beta0 <- -0.20
beta1 <- 0.09
y_true <- beta0 + beta1 * x + rnorm(n, 0, 0.15)
mu <- mean(y_true)

base_theme <- theme_classic(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 13),
    axis.title = element_text(size = 12),
    axis.ticks = element_blank(),
    axis.text = element_blank(),
    axis.line = element_line(arrow = arrow(length = unit(0.25, "cm"), type = "closed")),
    panel.grid = element_blank()
  )

y_lim <- c(min(y_true) - 0.1, max(y_true) + 0.15)
x_lim <- c(0, max(x) + 1.5)

p1 <- ggplot() +
  geom_segment(aes(x = x, xend = x, y = y_true, yend = mu), linetype = "dotted", color = "gray40") +
  geom_hline(yintercept = mu, color = "gray50", linewidth = 0.9) +
  annotate("text", x = -0.35, y = mu, label = expression(hat(mu)), size = 4.5, hjust = 1) +
  geom_point(aes(x = x, y = y_true), size = 3, color = "gray30") +
  scale_x_continuous(expand = expansion(add = c(0.2, 0.8))) +
  scale_y_continuous(expand = expansion(add = c(0.05, 0.15))) +
  coord_cartesian(xlim = x_lim, ylim = y_lim, clip = "off") +
  labs(title = "Random-Effects Model", x = "x", y = expression(hat(theta))) +
  base_theme +
  theme(axis.title.y = element_text(angle = 0, vjust = 1, hjust = 0))

p2 <- ggplot() +
  geom_segment(
    aes(x = x, xend = x, y = y_true, yend = beta0 + beta1 * x),
    linetype = "dotted", color = "gray40"
  ) +
  geom_abline(intercept = beta0, slope = beta1, color = "gray50", linewidth = 0.9) +
  annotate("text", x = -0.35, y = beta0, label = expression(theta), size = 4.5, hjust = 1) +
  geom_point(aes(x = x, y = y_true), size = 3, color = "gray30") +
  scale_x_continuous(expand = expansion(add = c(0.2, 0.8))) +
  scale_y_continuous(expand = expansion(add = c(0.05, 0.15))) +
  coord_cartesian(xlim = x_lim, ylim = y_lim, clip = "off") +
  labs(title = "Meta-Regression", x = "x", y = expression(hat(theta))) +
  base_theme +
  theme(axis.title.y = element_text(angle = 0, vjust = 1, hjust = 0))

ggsave("regression_left.png", p1, width = 4, height = 4, dpi = 200, bg = "white")
ggsave("regression_right.png", p2, width = 4, height = 4, dpi = 200, bg = "white")
