# Results: Current Evidence

## Scope

This file reports what can be established from the supplied 32-row outcome table without treating unresolved randomization as known. All statements are descriptive unless explicitly marked exploratory.

## Dry yield per plot

The grand mean dry yield is **8.29 kg/plot** across 32 observations.

### Tillage-coded groups

- L1, two ploughings: n = 16, mean = 9.41 kg/plot, SD = 1.70, range = 6.70-12.40.
- L2, one ploughing / reduced tillage: n = 16, mean = 7.16 kg/plot, SD = 2.30, range = 3.10-10.10.
- Relative to the L1 mean, the L2 mean is approximately **23.9% lower**.

This supports the statement: **reduced tillage showed poorer descriptive agronomic performance under the observed feasibility-study conditions.** It does not establish why the difference occurred, whether it would generalize, whether the tillage assignment itself is statistically replicated, or whether reduced tillage fails any carbon-credit criterion.

### Irrigation-coded groups

- IR1, normal irrigation: n = 16, mean = 8.83 kg/plot, SD = 2.14.
- IR2, AWD: n = 16, mean = 7.74 kg/plot, SD = 2.38.
- Relative to IR1, the IR2 mean is approximately **12.3% lower**.

The supplied data do not include the water-depth trajectory or drying threshold, so this comparison cannot be classified as mild versus severe AWD. That distinction matters in the rice literature.

### Nutrient-treatment codes

- F1: n = 8, mean = 9.38 kg/plot, SD = 1.47.
- F2: n = 8, mean = 9.89 kg/plot, SD = 1.03.
- F3: n = 8, mean = 7.78 kg/plot, SD = 2.36.
- F4: n = 8, mean = 6.11 kg/plot, SD = 2.12.

These do not establish that any named fertilizer product caused the difference. F-treatment definitions remain partly unresolved, and each marginal mean pools across tillage and irrigation.

## Cell means

Every L x IR x F cell has two plot observations. The lowest cell mean is L2 x IR2 x F4 at 3.43 kg/plot; the highest is L1 x IR2 x F2 at 10.83 kg/plot. `analysis/outputs/yield_cell_summary.csv` contains all 16 cell means and within-cell SDs.

With n = 2 per cell, the within-cell SD is itself unstable and should not be overinterpreted.

## Data-quality flag

`L2IR1F4R2` has fresh weight = 38 kg/plot and dry yield = 4.75 kg/plot. The fresh-weight value is much larger than neighboring observations. The repository retains 38 exactly as supplied and flags it for verification; it is not changed to 3.8 on suspicion alone. The dry-yield endpoint used above is unaffected by that possible fresh-weight entry issue.

## Exploratory factorial ANOVA

The repository calculates a conventional balanced 2 x 2 x 4 factorial ANOVA only as a diagnostic exercise. The resulting model uses the plot-level residual as the common error term, which may be inappropriate for tillage and irrigation if the proposal schematic reflects the actual randomization hierarchy. Those p-values are therefore **not used as confirmatory results**.

See `statistical-identification.md` before using `analysis/outputs/exploratory_naive_anova.csv`.

## Growth time series

Thirty-two source workbooks contain complete observations on 17 dates from 2025-07-16 through 2025-09-12 for plant height, number of tillers, leaf-area index, leaf length, and leaf width. The treatment-to-series mapping could not be recovered. The data are included as `growth_long_unlinked.csv` with neutral series IDs, allowing quality inspection and overall temporal summaries without falsely assigning treatment exposure.

## GHG results

No GHG treatment result is reported because no measured gas series is present in the supplied spreadsheets. A report stating that CO2/CH4 measurement was ongoing is evidence of monitoring activity, not evidence of a treatment effect.
