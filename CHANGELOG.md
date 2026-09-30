# Changelog

## v1.1.0 - 2026-09-30

- Added a sanitized public reconstruction of the harvest source layout in Excel and companion CSV form so data cleaning can be reproduced rather than assumed.
- Added a strict regular-expression parser for compact plot identifiers and a tested source-to-clean reconstruction step.
- Added tidy long-form outcomes and an analysis-ready treatment-metadata join.
- Reorganized the Python workflow into explicit numbered steps while retaining one-command reproduction.
- Added direct Excel ingestion and tidyverse replication scripts in R, including joins and wide/long reshaping.
- Added an executed Pandas/Jupyter walkthrough and a CI notebook-execution check.
- Expanded the test suite from 6 to 13 checks, including malformed-code rejection, source reconstruction parity, long-data shape, treatment metadata, and notebook syntax.
- Added reproducibility workflow and computing-evidence documentation without changing the scientific interpretation or promoting exploratory p-values to confirmatory results.

## v1.0.1 - 2026-09-30

- Removed the MIT license so the public portfolio does not grant a blanket open-source or open-data reuse permission.
- Replaced licensing language with a rights-and-reuse statement appropriate for institutional field data, photographs, proprietary information, and derived research materials.
- Removed the license field from `CITATION.cff` and clarified that citation does not itself grant reuse permission.
- No analytical data, figures, statistical outputs, or research conclusions were changed in this refinement.

## v1.0.0 - 2026-09-30

- Reconstructed the complete 32-row L x IR x F x R coding grid.
- Recovered public-safe F1-F4 definitions and documented unresolved cross-source discrepancies.
- Added cleaned agronomic outcomes and unlinked longitudinal growth data.
- Added data-quality, provenance, claims, and statistical-identification audits.
- Added reproducible Python analysis, R/Stata equivalents, tests, and figures.
- Added current VM0042 / VM0051 methodology notes.
- Added metadata-scrubbed field photographs.
- Excluded personal contacts, unrelated CVs, proprietary dosing schedules, and original internal reports.
