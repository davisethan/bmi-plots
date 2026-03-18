library(ggplot2)

n <- seq(2, 100, by = 0.5)
d <- 0.2
hedges_g <- d * (1 - 3 / (4 * n - 9))

df <- data.frame(
  n = rep(n, 2),
  value = c(rep(d, length(n)), hedges_g),
  estimator = rep(c("Uncorrected SMD", "Hedges' g"), each = length(n))
)

ggplot(df, aes(x = n, y = value, linetype = estimator, color = estimator)) +
  geom_line(linewidth = 1) +
  scale_linetype_manual(values = c("Uncorrected SMD" = "dotted", "Hedges' g" = "solid")) +
  scale_color_manual(values = c("Uncorrected SMD" = "black", "Hedges' g" = "grey40")) +
  scale_x_continuous(breaks = c(25, 50, 75, 100)) +
  scale_y_continuous(limits = c(0.10, 0.20)) +
  labs(
    x = "Sample Size",
    y = NULL,
    linetype = NULL,
    color = NULL
  ) +
  theme_classic(base_size = 14) +
  theme(
    legend.position = c(0.7, 0.3),
    legend.background = element_blank(),
    legend.key.width = unit(1.5, "cm")
  )

ggsave("hedges_g.png", width = 4, height = 4)
