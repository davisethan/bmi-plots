# ====================
# Example forest plot.
# ====================

library(tidyverse)
library(dmetar)
library(meta)

data(ThirdWave)

m_gen <- metagen(
  TE = TE,
  seTE = seTE,
  studlab = Author,
  data = ThirdWave,
  sm = "SMD",
  common = FALSE,
  random = TRUE,
  method.tau = "REML",
  method.random.ci = TRUE,
  title = "Third Wave Psychotherapies"
)

png("forest.png", width = 2800, height = 1800, res = 300)
forest(
  m_gen,
  sortvar = TE,
  prediction = TRUE,
  print.tau2 = FALSE
)
dev.off()
