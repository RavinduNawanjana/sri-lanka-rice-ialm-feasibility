# Optional supplement: URL input, Parquet, tibble, and data.table.
#
# The local CSV path remains the canonical public input.  Once this repository
# is online, set RICE_REPO_RAW_CSV to the raw GitHub URL if you want to verify
# remote ingestion without hard-coding a personal GitHub account here.

suppressPackageStartupMessages({
  library(readr)
  library(tibble)
})

local <- read_csv("data/derived/plot_outcomes_clean.csv", show_col_types = FALSE)

remote_url <- Sys.getenv("RICE_REPO_RAW_CSV")
if (nzchar(remote_url)) {
  remote <- read_csv(remote_url, show_col_types = FALSE)
  stopifnot(isTRUE(all.equal(local, remote, check.attributes = FALSE)))
  message("Remote URL input matches local canonical CSV.")
}

base_frame <- as.data.frame(local)
tibble_frame <- as_tibble(base_frame)
stopifnot(nrow(base_frame) == nrow(tibble_frame))

if (requireNamespace("data.table", quietly = TRUE)) {
  dt <- data.table::as.data.table(base_frame)
  stopifnot(nrow(dt) == nrow(base_frame))
}

if (requireNamespace("arrow", quietly = TRUE)) {
  tmp <- tempfile(fileext = ".parquet")
  arrow::write_parquet(tibble_frame, tmp)
  parquet <- arrow::read_parquet(tmp)
  stopifnot(nrow(parquet) == nrow(tibble_frame))
  unlink(tmp)
}
