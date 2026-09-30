# Research Skills Demonstrated by This Repository

This file describes what the **portfolio reconstruction itself** demonstrates. It does not imply that every listed method was part of the original field trial.

## Experimental-design reasoning

The project distinguishes observational rows from treatment-assignment units, identifies pseudoreplication risk, reconstructs a hierarchical field design from independent source records, and defers confirmatory inference when the randomization map is missing. See `docs/statistical-identification.md`.

## Reproducible data engineering

A sanitized source-layout reconstruction is preserved under `data/raw_public/`. The tested Python pipeline rebuilds the 32-row canonical harvest table without manual spreadsheet edits, forward-fills visually grouped source labels, validates all numeric outcomes, parses compact experimental identifiers with a strict regular expression, and fails if the expected `2 x 2 x 4 x 2` code grid is incomplete.

The same public Excel workbook is independently ingested in R using `readxl`, `tidyr`, `stringr`, and `dplyr`. See `docs/reproducible-workflow.md`.

## Quantitative analysis

The executable workflow performs descriptive statistics, factorial cell summaries, explicit exploratory ANOVA, data-quality checks, tidy reshaping, treatment-metadata joins, and reproducible figure generation. It is designed to be extended to mixed/split-plot models once block identifiers are recovered.

## Programming and reproducibility

Python is the continuously tested reference workflow. R provides a tidyverse/Excel replication layer, while Stata retains a compact alternative yield specification. A Jupyter notebook demonstrates the same data logic with Pandas. Tests verify code balance, source reconstruction, parsing, completeness, key numerical results, and preservation of flagged values. GitHub Actions rebuilds derived outputs on push.

Concrete evidence is indexed in `docs/computing-competency-evidence.md`.

## Carbon-methodology analysis

The methodology notes separate field evidence from VM0042 concepts such as applicability, baseline, additionality, quantification, leakage, and monitoring. They also recognize the later emergence of VM0051 as a rice-specific methodology without retroactively rewriting the 2025 study.

## Data governance

The public release removes personal contacts and proprietary dosing, strips image metadata, preserves a source register, and uses a claims register to identify which conclusions are observed, source-reported, inferred, or unresolved. The public raw workbook is explicitly a sanitized reconstruction rather than an institutional source-of-record.

## Research judgement

Several techniques could be mechanically applied but are deliberately not used as headline evidence. Difference-in-differences is not forced onto a dataset without a suitable pre/post treated-control structure. A naive factorial p-value is not elevated above the unresolved experimental-unit problem. Missing GHG data are not filled with literature averages. These exclusions are methodological choices, not missing ambition.
