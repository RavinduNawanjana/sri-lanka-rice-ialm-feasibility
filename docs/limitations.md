# Limitations

## Design identification

The main limitation is not sample size alone. It is missing information about the randomization unit for tillage and irrigation. The available schematic suggests a hierarchical field arrangement, and the harvest workbook lacks block or whole-plot IDs. This prevents confident assignment of correct error terms to the higher-level factors.

## Small within-cell sample

Every coded L x IR x F cell has two plot observations. This is enough for a cell mean and one degree of freedom for a within-cell SD, but it provides little protection against local spatial heterogeneity and gives low power for interactions.

## Treatment-definition inconsistency

F1-F3 require reconciliation against a final field record. The repository consequently avoids product-specific causal attribution.

## Missing GHG measurements

Raw chamber concentration data are absent. No seasonal CH4, N2O, CO2, global warming potential, emission intensity, or carbon-credit quantity can be estimated.

## Missing AWD intensity data

Daily water-level monitoring is reported, but the underlying time series and target threshold are absent. The realized water stress cannot be categorized.

## Unlinked growth series

Thirty-two longitudinal crop-growth files exist but cannot currently be mapped to plot treatment codes. They are useful for data-quality review and overall growth trajectories but not treatment comparisons.

## Possible data-entry anomaly

One fresh-weight entry is 38 kg/plot. It is retained but flagged. Any analysis using fresh weight should run sensitivity analyses after checking the field sheet.

## Unit metadata

Several grain/panicle mass columns do not print units in the outcome workbook. The public data dictionary labels the likely agronomic unit but explicitly marks it for verification.

## Methodology evolution

The field study's 2025 methodology framing predates current VM0042 v2.2 and the July 2026 VM0051 v1.1 revision. Methodology conclusions must therefore be based on active documents at the time of any future filing, not frozen to the trial's original labels.
