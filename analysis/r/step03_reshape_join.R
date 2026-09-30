# Step 03 (R): tidy reshaping and metadata joins.

suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
  library(tidyr)
})

d <- read_csv("data/derived/plot_outcomes_clean.csv", show_col_types = FALSE)
codebook <- read_csv("data/metadata/treatment_codebook.csv", show_col_types = FALSE)

nutrient_meta <- codebook |>
  filter(factor == "nutrient") |>
  select(
    fertilizer_code = code,
    nutrient_public_definition = public_definition,
    nutrient_definition_status = status,
    nutrient_definition_confidence = confidence
  )

enriched <- d |>
  left_join(nutrient_meta, by = "fertilizer_code")

outcome_names <- c(
  "plant_height_cm_early", "panicles_0_25m2", "productive_tillers_m2",
  "plant_height_cm_harvest", "fresh_weight_kg_plot", "ten_panicle_weight_g",
  "thousand_seed_weight_g", "filled_grain_count", "filled_grain_weight_g",
  "unfilled_grain_count", "unfilled_grain_weight_g", "dry_yield_kg_plot"
)

long <- enriched |>
  pivot_longer(
    cols = all_of(outcome_names),
    names_to = "outcome",
    values_to = "value"
  )

yield_wide <- long |>
  filter(outcome == "dry_yield_kg_plot") |>
  group_by(tillage_code, irrigation_code, fertilizer_code) |>
  summarise(mean_kg_plot = mean(value), .groups = "drop") |>
  pivot_wider(
    names_from = fertilizer_code,
    values_from = mean_kg_plot
  )

print(long)
print(yield_wide)
