# Step 01 (R): reconstruct the canonical harvest table directly from Excel.
#
# This script mirrors the continuously tested Python cleaning path but reads the
# public .xlsx reconstruction with readxl.  It demonstrates explicit sheet
# selection, removal of the report header row, forward-filling visually merged
# treatment labels, regular-expression parsing, and source/canonical checks.

suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
  library(readxl)
  library(stringr)
  library(tidyr)
})

source_path <- "data/raw_public/harvest_outcomes_source_layout.xlsx"
canonical_path <- "data/derived/plot_outcomes_clean.csv"

raw <- read_excel(
  source_path,
  sheet = "Harvest",
  col_names = FALSE,
  .name_repair = "minimal"
)

stopifnot(nrow(raw) == 33L, ncol(raw) == 15L)

raw <- raw[-1, ]
names(raw) <- c(
  "tillage_source", "irrigation_source", "plot_code",
  "plant_height_cm_early", "panicles_0_25m2", "productive_tillers_m2",
  "plant_height_cm_harvest", "fresh_weight_kg_plot", "ten_panicle_weight_g",
  "thousand_seed_weight_g", "filled_grain_count", "filled_grain_weight_g",
  "unfilled_grain_count", "unfilled_grain_weight_g", "dry_yield_kg_plot"
)

clean <- raw |>
  fill(tillage_source, irrigation_source, .direction = "down") |>
  mutate(
    plot_code = str_squish(as.character(plot_code))
  )

parsed <- str_match(
  clean$plot_code,
  "^(L[12])(IR[12])(F[1-4])(R[12])$"
)

if (any(is.na(parsed[, 1]))) {
  stop("At least one plot code falls outside L[12]IR[12]F[1-4]R[12].")
}

clean <- clean |>
  mutate(
    tillage_code = parsed[, 2],
    irrigation_code = parsed[, 3],
    fertilizer_code = parsed[, 4],
    replicate_code = parsed[, 5],
    tillage_label = if_else(
      tillage_code == "L1",
      "two_ploughings_conventional",
      "one_ploughing_reduced"
    ),
    irrigation_label = if_else(
      irrigation_code == "IR1",
      "normal_irrigation",
      "alternate_wetting_drying"
    )
  )

tillage_source_norm <- str_to_lower(str_squish(clean$tillage_source))
irrigation_source_norm <- str_to_lower(str_squish(clean$irrigation_source))

stopifnot(all(
  (clean$tillage_code == "L1" & str_detect(tillage_source_norm, "2 time ploughing")) |
  (clean$tillage_code == "L2" & str_detect(tillage_source_norm, "1 time ploughing"))
))
stopifnot(all(
  (clean$irrigation_code == "IR1" & irrigation_source_norm == "irrigated") |
  (clean$irrigation_code == "IR2" & irrigation_source_norm == "awd")
))

outcome_names <- c(
  "plant_height_cm_early", "panicles_0_25m2", "productive_tillers_m2",
  "plant_height_cm_harvest", "fresh_weight_kg_plot", "ten_panicle_weight_g",
  "thousand_seed_weight_g", "filled_grain_count", "filled_grain_weight_g",
  "unfilled_grain_count", "unfilled_grain_weight_g", "dry_yield_kg_plot"
)

clean <- clean |>
  mutate(across(all_of(outcome_names), as.numeric)) |>
  select(
    plot_code, tillage_code, irrigation_code, fertilizer_code, replicate_code,
    tillage_label, irrigation_label, all_of(outcome_names)
  ) |>
  arrange(plot_code)

canonical <- read_csv(canonical_path, show_col_types = FALSE) |>
  arrange(plot_code)

comparison <- all.equal(
  as.data.frame(clean),
  as.data.frame(canonical),
  check.attributes = FALSE
)

if (!isTRUE(comparison)) {
  stop(paste("R Excel reconstruction differs from canonical data:", comparison))
}

message("R Excel reconstruction matches the canonical 32-row clean dataset.")
