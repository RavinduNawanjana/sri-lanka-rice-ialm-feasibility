# Reproducible Research-Computing Workflow

## Problem definition

The computational problem is narrower than the scientific problem.

The current public workflow asks:

1. Can the 32 harvest rows be reconstructed from a source-style table without manual spreadsheet edits?
2. Do compact plot identifiers encode a complete `2 x 2 x 4 x 2` grid?
3. Do the source labels and encoded factors agree?
4. What descriptive patterns are present in the agronomic outcomes?
5. Which inferential questions must remain unanswered because the experimental assignment units or GHG series are missing?

This definition prevents the code from quietly solving a different problem, such as treating every plot row as an independent replicate for every treatment factor.

## Pipeline pseudocode

```text
READ public source-layout harvest table
FORWARD-FILL visually grouped tillage and irrigation labels
FOR each plot row:
    PARSE plot_code with a strict regular expression
    CHECK parsed L and IR against the source labels
    CHECK every agronomic outcome is numeric
CHECK that the exact 32-code factorial grid is present
WRITE canonical clean plot table

RESHAPE the clean outcomes to tidy long form
JOIN public nutrient-treatment metadata by treatment code

CALCULATE descriptive marginal and cell summaries
CALCULATE a mechanically valid but explicitly naive plot-level ANOVA
    LABEL it exploratory because the correct whole-plot error structure is unresolved
GENERATE figures from the clean data

RUN automated tests
FAIL on malformed codes, missing plots, changed benchmark means, or lost flagged source values
```

## Data lineage

```text
data/raw_public/harvest_outcomes_source_layout.xlsx
        │
        ├── R: analysis/r/step01_clean_harvest_excel.R
        │       └── verifies the canonical clean table
        │
        └── companion CSV
                │
                ▼
analysis/python/step01_clean_harvest.py
                │
                ▼
data/derived/plot_outcomes_clean.csv
                │
                ├── step02_reshape_join.py
                │       ├── plot_outcomes_long.csv
                │       └── plot_outcomes_with_treatment_metadata.csv
                │
                ├── step03_descriptive_yield.py
                ├── step05_exploratory_factorial.py
                └── step06_figures.py
                        │
                        ▼
              analysis/outputs/ + figures/
```

The longitudinal growth series have a separate path because their source filenames cannot yet be linked defensibly to the final plot codes.

## Failure should be visible

The cleaning workflow is designed to stop rather than guess when:

- a plot identifier falls outside `L[12]IR[12]F[1-4]R[12]`;
- a source tillage or irrigation label conflicts with the encoded identifier;
- a numeric harvest field contains a non-numeric value;
- the expected 32-code grid is incomplete or duplicated.

By contrast, the suspicious `38 kg/plot` fresh-weight observation at `L2IR1F4R2` is **not** automatically rejected. It is retained because it is a source value and separately flagged in the data-quality log. Reproducibility does not justify silently changing inconvenient measurements.

## Raw versus derived data

The institutional originals are intentionally not placed in this public repository. `data/raw_public/` contains a sanitized source-layout reconstruction restricted to values already released in the portfolio. It is treated as immutable input.

Derived files can be regenerated. A user should never have to open the raw workbook and manually copy, fill, sort, or correct cells to reproduce the public analysis.

## Language roles

Python is the continuously tested reference pipeline. R provides a direct Excel-ingestion and tidyverse replication layer. Stata contains a compact alternative specification for the yield model. Multiple languages are included only where they demonstrate portability of the research logic; they are not treated as separate evidence streams.

## What is intentionally not automated

No script fills absent GHG measurements with literature values. No script invents block identifiers, chamber-to-plot links, AWD thresholds, or fertilizer definitions. The pipeline automates transformations that are documented by the available evidence and leaves unresolved scientific inputs unresolved.
