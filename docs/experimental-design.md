# Experimental Design Reconstruction

## Purpose

This note separates what can be reconstructed from the supplied files from what would be required to identify valid treatment effects. The distinction matters because a factorial **data table** is not necessarily a factorial **randomization design**.

## Observed coding structure

The outcome workbook has 32 unique plot codes matching the regular expression:

```text
L[12]IR[12]F[1-4]R[12]
```

Every combination occurs exactly once. This establishes a complete 2 x 2 x 4 x 2 coding grid:

- two tillage codes: L1 and L2;
- two irrigation codes: IR1 and IR2;
- four nutrient-treatment codes: F1-F4;
- two plot replicate codes: R1 and R2.

The code-mapping workbook defines L1 as two ploughings, L2 as one ploughing, IR1 as normal irrigation, and IR2 as AWD. It also maps F1-F4 to four nutrient-management treatments. The public representation of F1-F4 is conservative because the proposal and application schedule are not perfectly consistent; see `treatment-definition-audit.md`.

## What the proposal layout suggests

The proposal's experimental schematic depicts two large sections labelled conventional tillage and reduced tillage. Each section is divided into a normal-irrigation portion and an AWD portion. Within each tillage x irrigation portion are eight small treatment plots representing four nutrient treatments with two replicates in randomized order.

That structure is more consistent with a **hierarchical / split-plot-style field layout** than with a completely randomized 2 x 2 x 4 factorial experiment at the individual-plot level.

A conceptual reconstruction is shown in `../figures/design_schematic.svg`. It is not a surveyed plot map and should not be used to infer physical coordinates.

## Experimental unit versus observational unit

The 32 harvest rows are observational units. The experimental unit for a factor is the smallest independently randomized unit to which that factor was assigned.

If tillage was assigned to one large field section per level, there would be only one true assignment unit for L1 and one for L2. Two F-treatment plot replicates within a tillage section would not replicate tillage. Likewise, if irrigation was assigned to one sub-section within each tillage section, the eight nutrient plots inside it would not provide eight independent replications of irrigation.

This is the core reason the repository does not interpret a plot-level three-way ANOVA as confirmatory.

## What would resolve the design

The following records would determine the correct error structure:

1. A physical plot map with plot-code positions.
2. Block identifiers, if the field was blocked.
3. The exact units to which tillage and irrigation were independently randomized.
4. Randomization procedure or randomization list.
5. Chamber-to-plot mapping.
6. Confirmation of whether R1/R2 are true independent plot replicates, paired subplots, or repeated/adjacent measurements.

The template `../data/reconciliation/plot_randomization_map.csv` is prepared for this information.

## Candidate analysis after design recovery

If there are true replicated blocks and the allocation is block -> tillage whole plot -> irrigation subplot -> nutrient sub-subplot, an appropriate model would use error terms or random effects at those assignment levels. A generic mixed-model form would be:

```text
yield ~ tillage * irrigation * fertilizer
      + random(block)
      + random(block:tillage)
      + random(block:tillage:irrigation)
```

The exact random-effects structure must follow the actual allocation, not the labels in this illustrative equation.

If whole-plot replication is absent, the tillage and irrigation contrasts from this single trial should remain descriptive. Nutrient-treatment contrasts may still have within-section replication, but their interpretation also depends on the randomization and the unresolved treatment-definition audit.

## Design-level conclusion

The experiment is rich enough to support a useful feasibility analysis, data-quality audit, and formulation of a stronger follow-on trial. The source package is not yet rich enough to support unqualified causal statements about all three treatment factors. Preserving that distinction is part of the research result, not an analytical failure.
