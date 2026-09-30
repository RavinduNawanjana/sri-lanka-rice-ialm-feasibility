# R workflows

The R scripts are a second-language replication layer rather than an alternative set of claims.

Run them from the repository root in order:

1. `step01_clean_harvest_excel.R` reads the public Excel reconstruction directly and checks that it reproduces the canonical 32-row clean CSV.
2. `step02_tidyverse_analysis.R` demonstrates `select`, `mutate`, `if_else`, `filter`, `group_by`, `summarise`, and `ggplot2` on the field data.
3. `step03_reshape_join.R` demonstrates `left_join`, `pivot_longer`, and `pivot_wider`.
4. `base_r_yield_analysis.R` keeps a compact base-R `read.csv` / `aggregate` / `aov` specification for transparent cross-checking.
5. `supplement_data_formats.R` is optional and covers URL ingestion plus Parquet/data-frame formats when the relevant packages are installed.

The Python pipeline remains the continuously tested reference implementation in GitHub Actions. The R layer exists to show that the data logic is portable across common environmental-data workflows, not to multiply analyses for their own sake.
