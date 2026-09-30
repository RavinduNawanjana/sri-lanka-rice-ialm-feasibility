# Methods

## Study context

The source materials describe a 2025 paddy-field feasibility study at a Sri Lankan rice research site. The study was designed to examine agricultural management practices relevant to greenhouse-gas mitigation and crop performance, with an intended connection to Verra's improved agricultural land-management framework.

This public repository is a secondary reconstruction from the supplied project files. It is not the primary field protocol and does not replace institutional records.

## Field factors

### Tillage

Two coded levels appear in the plot map and outcome workbook:

- L1: two ploughings, treated here as the conventional-intensity comparator.
- L2: one ploughing, treated here as reduced tillage.

The source proposal describes L1 as a multi-stage sequence involving ploughing, a waiting/decay interval, a second ploughing, another interval, and leveling. L2 is described as reduced soil disturbance. The final public analysis uses only the coded/intensity distinction because the exact operation timing should be confirmed from field logs before agronomic replication.

### Irrigation

- IR1: normal irrigation.
- IR2: alternate wetting and drying (AWD).

The September progress report states that AWD infrastructure was functional and daily water-level readings were maintained. The water-depth series itself was not supplied, so the realized drying intensity cannot be reconstructed.

### Nutrient management

Four nutrient codes F1-F4 were crossed with tillage and irrigation. Because the proposal, codebook, and application schedule disagree in limited but important ways, public treatment descriptions are conservative. Product-specific application details are withheld. See `treatment-definition-audit.md`.

## Replication and layout

The outcome table contains two R-coded observations in each L x IR x F cell. The proposal schematic visually organizes treatment plots within irrigation sections and irrigation sections within tillage sections. Therefore R1/R2 are treated as plot-level replicates, not automatically as independent replications of the tillage or irrigation assignment.

## Monitoring infrastructure

The September progress report describes 16 gas-monitoring chambers and continuing CO2 and CH4 measurement. The package contains photographs of chamber installations and a GHG data template with fields for CH4, N2O, CO2, temperature, chamber condition, and remarks. The measured gas records themselves are not in the supplied data package.

## Crop observations

The final outcome workbook reports:

- an earlier plant-height measure;
- panicle count from a nominal 50 cm x 50 cm sample;
- productive tillers/panicles per square metre;
- harvest-stage plant height;
- fresh weight per plot;
- ten-panicle weight;
- 1000-seed weight;
- filled and unfilled grain counts and weights;
- dry yield per plot.

Thirty-two additional longitudinal workbooks record plant height, number of tillers, leaf-area index, leaf length, and leaf width on 17 dates between 16 July and 12 September 2025. Because their filenames cannot be reliably mapped to final plot codes, they are analyzed only as unlinked source series.

## Data cleaning

The plot code is parsed deterministically into L, IR, F, and R components. Numeric outcome values are retained exactly as provided. No outlier is automatically removed or corrected. A public data-quality log identifies suspicious or unresolved records.

The public repository omits original progress reports, staff contacts, personal CVs, proprietary product dosing, and raw document metadata.

## Statistical analysis

The current analysis reports raw distributions, marginal means, standard deviations, relative mean differences, and L x IR x F cell means for dry yield. These statistics summarize the observed 32 plots but do not correct for a potentially hierarchical randomization design.

A full balanced plot-level factorial ANOVA is computed as an explicitly exploratory diagnostic. Confirmatory inference is deferred until block and assignment-unit identifiers are recovered. The preferred future approach is a split-plot or mixed model whose random-effects/error structure follows the actual field randomization.

## GHG analysis plan

No GHG flux calculations are performed. A future import must at minimum establish plot/chamber linkage, concentration units, closure times, chamber geometry, temperature, analytical method, calibration/QC, sampling dates, and water status. Only after those fields are verified should flux fitting, seasonal integration, treatment contrasts, and CO2e conversion be implemented.
