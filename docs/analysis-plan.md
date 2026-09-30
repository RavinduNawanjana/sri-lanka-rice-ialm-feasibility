# Analysis Plan

## Stage 1: current public reconstruction

Primary endpoint: dry yield per plot.

Current tasks:

- verify code completeness and balance;
- report raw observations, marginal means, SDs, and cell means;
- visualize yield distributions without inferential error bars that assume independent whole-plot replication;
- flag data-quality anomalies;
- keep nutrient treatments coded where operational definitions are disputed;
- maintain longitudinal growth series as unlinked.

## Stage 2: design reconciliation

Before confirmatory statistics:

- populate `data/reconciliation/plot_randomization_map.csv`;
- establish block count and assignment units;
- populate `treatment_definition_verification.csv` from a signed field source;
- verify units for outcome variables;
- verify harvest date and plot area.

Decision rule: if tillage or irrigation has no independent assignment-unit replication, do not report a frequentist treatment p-value for that factor from this trial.

## Stage 3: agronomic inference

If the design supports it:

- fit the appropriate split-plot/mixed model;
- estimate prespecified main effects and scientifically motivated interactions;
- report effect estimates and 95% CIs at the correct unit of inference;
- conduct residual and influence diagnostics;
- perform sensitivity analysis around any verified data corrections;
- interpret higher-order interactions cautiously given n = 2 per coded cell.

## Stage 4: GHG reconstruction

Required raw fields are defined in `data/metadata/ghg_import_schema.csv`.

Planned sequence:

1. validate chamber-plot linkage and sampling timestamps;
2. document instrument/lab method and concentration units;
3. validate chamber geometry and environmental corrections;
4. fit concentration-time slopes with predefined quality rules;
5. convert slopes to area-based flux with unit-audited formulas;
6. aggregate event fluxes to seasonal CH4 and N2O using a prespecified integration method;
7. estimate treatment contrasts using the actual assignment structure;
8. calculate climate metrics only after gas-specific units and GWP conventions are documented;
9. add yield-scaled emission intensity as a secondary outcome;
10. retain all exclusions and recalculations in an auditable QC table.

## Stage 5: methodology crosswalk

Only after experimental and GHG evidence is complete should the results be cross-walked to active Verra requirements. The sequence is intentionally evidence -> statistical inference -> methodology applicability, not methodology target -> selective evidence.
