# Step 02 (R): descriptive analysis using the tidyverse.
#
# These are descriptive summaries.  They are not promoted as confirmatory
# treatment effects because the whole-plot/block structure remains unresolved.

suppressPackageStartupMessages({
  library(dplyr)
  library(ggplot2)
  library(readr)
})

d <- read_csv("data/derived/plot_outcomes_clean.csv", show_col_types = FALSE)

analysis_frame <- d |>
  select(
    plot_code, tillage_code, irrigation_code, fertilizer_code,
    replicate_code, dry_yield_kg_plot
  ) |>
  mutate(
    irrigation_group = if_else(
      irrigation_code == "IR2", "AWD", "normal irrigation"
    )
  )

marginal_summary <- analysis_frame |>
  group_by(tillage_code) |>
  summarise(
    n = n(),
    mean_kg_plot = mean(dry_yield_kg_plot),
    sd_kg_plot = sd(dry_yield_kg_plot),
    .groups = "drop"
  )

cell_summary <- analysis_frame |>
  group_by(tillage_code, irrigation_code, fertilizer_code) |>
  summarise(
    n = n(),
    mean_kg_plot = mean(dry_yield_kg_plot),
    sd_kg_plot = sd(dry_yield_kg_plot),
    .groups = "drop"
  )

flagged_source_record <- d |>
  filter(plot_code == "L2IR1F4R2") |>
  select(plot_code, fresh_weight_kg_plot, dry_yield_kg_plot)

print(marginal_summary)
print(cell_summary)
print(flagged_source_record)

p <- ggplot(
  analysis_frame,
  aes(x = fertilizer_code, y = dry_yield_kg_plot)
) +
  geom_point(position = position_jitter(width = 0.06, height = 0), alpha = 0.7) +
  stat_summary(fun = mean, geom = "point", shape = 18, size = 3) +
  facet_grid(tillage_code ~ irrigation_code) +
  labs(
    x = "Nutrient-treatment code",
    y = "Dry yield (kg/plot)",
    title = "Descriptive plot-level yield by treatment cell",
    subtitle = "Points are plots; diamonds are cell means. No causal error bars shown."
  ) +
  theme_minimal(base_size = 11)

ggsave(
  "figures/yield_cells_r.png",
  p,
  width = 7.4,
  height = 5.0,
  dpi = 220
)
