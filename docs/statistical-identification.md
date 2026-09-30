# Statistical Identification and Inference Strategy

## Identification before estimation

The central statistical question is not which model produces the smallest p-value. It is what randomization, replication, and measurement structure makes a treatment contrast identifiable.

The current data have two plot observations within every L x IR x F cell. That is enough to calculate means, variances, interactions, and a balanced plot-level ANOVA. It is not enough to establish that the residual variance from those 32 rows is the correct sampling variance for the tillage and irrigation assignments.

## Current inferential policy

The public results therefore use three levels of evidence.

**Level 1: directly descriptive.** Raw observations, marginal means, cell means, ranges, standard deviations, and plotted distributions can be reported from the 32 rows.

**Level 2: exploratory model output.** `analysis/outputs/exploratory_naive_anova.csv` shows what a conventional plot-level full-factorial ANOVA returns. It is preserved for transparency and training, but its p-values are not treated as confirmatory because the experimental-unit structure is unresolved.

**Level 3: confirmatory inference.** Deferred until block/whole-plot identifiers and randomization are recovered. At that point the model will be rewritten to use the correct split-plot or mixed-model error strata.

## Why pseudoreplication matters here

Suppose tillage was physically applied to a single 28 m section for L1 and a single 28 m section for L2. The 16 observations within each section then share the same tillage assignment. Treating all 16 as independent replications of tillage would inflate the apparent sample size from one assignment unit to sixteen observations. A small residual variance among subplots cannot substitute for missing replication of the whole-plot treatment.

The same logic applies to irrigation if the water treatment was assigned at a section level.

## What not to do

The analysis does not:

- declare reduced tillage statistically inferior using the naive plot-level p-value;
- use the reduced-tillage yield result as a proxy for Verra additionality;
- infer that AWD reduced methane because meta-analyses find average methane reductions elsewhere;
- infer that F2 is the best nutrient treatment because it has the highest marginal mean;
- drop the 38 kg fresh-weight value merely because it looks suspicious;
- force difference-in-differences into a dataset that does not provide an appropriate pre/post treated-control panel.

## Primary outcome

The current primary agronomic endpoint is `dry_yield_kg_plot`. It has complete data for all 32 plots and is the most interpretable current measure of productivity.

Secondary outcomes are harvest-stage plant height, panicle density, fresh weight, 1000-seed weight, filled-grain count/weight, and unfilled-grain count/weight. Several mass variables have unit labels that should be verified against the field sheet before formal manuscript analysis.

## Prospective GHG outcomes

When the raw gas series becomes available, the analysis plan should define before looking at treatment differences:

- chamber closure interval and concentration units;
- linear/nonlinear flux-fitting rule and diagnostics;
- chamber volume and footprint correction;
- temperature/pressure conversion where required;
- missing-event and below-detection rules;
- temporal integration from event fluxes to seasonal flux;
- CH4 and N2O primary seasonal endpoints;
- CO2 treatment according to the selected carbon-accounting methodology;
- yield-scaled GHG intensity as a secondary agronomic-climate outcome;
- QA/QC exclusions with a retained audit log.

No flux equation is hard-coded in this repository because the analyzer units, chamber geometry, and laboratory method are not documented in the supplied data package.

## Planned effect reporting

Once the assignment structure is known, report treatment contrasts with:

- point estimates in natural units;
- confidence intervals using the appropriate assignment-level variance;
- standardized effects only when they aid cross-outcome interpretation;
- cell means to make interactions visible;
- exact sample sizes at the independent-unit level;
- sensitivity analyses to documented data-quality decisions.

With only two plot observations per coded cell, higher-order interactions will be imprecise even if the design is valid. They should be reported as exploratory rather than mined for significance.
