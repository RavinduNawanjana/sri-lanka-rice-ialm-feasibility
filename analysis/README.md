# Analysis

The repository separates **data reconstruction**, **reshaping**, **descriptive analysis**, **exploratory inference**, and **figure generation**.

Run from the repository root:

```bash
python analysis/python/reproduce_all.py
python -m unittest discover -s tests -v
```

The pipeline executes in this order:

1. `step01_clean_harvest.py` rebuilds the clean 32-row harvest table from the public source-layout CSV.
2. `step02_reshape_join.py` creates tidy long outcomes and joins public treatment metadata.
3. `step03_descriptive_yield.py` creates marginal and treatment-cell summaries.
4. `step04_growth_summary.py` summarizes the still-unlinked longitudinal growth series.
5. `step05_exploratory_factorial.py` calculates a balanced plot-level ANOVA for transparency only.
6. `step06_figures.py` rebuilds the public figures.

`plot_codes.py` contains the strict regular-expression parser. `ghg_schema_check.py` validates the structure of future gas data but intentionally does not calculate fluxes.

## R

`analysis/r/` provides a second-language replication layer. It reads the public Excel reconstruction directly, uses tidyverse data manipulation and reshaping, and checks parity with the canonical CSV. See `analysis/r/README.md`.

## Notebook

`analysis/notebooks/reproducible_yield_walkthrough.ipynb` is a compact Pandas/Jupyter walkthrough suitable for local Jupyter or Google Colab.

## Inferential boundary

`analysis/outputs/exploratory_naive_anova.csv` is intentionally labelled **naive**. It assumes all 32 plot rows provide independent residual replication for the full factorial model. The design audit says that assumption may be false for tillage and irrigation. Do not cite its p-values as confirmatory effects unless the field randomization records establish the required independent units.
