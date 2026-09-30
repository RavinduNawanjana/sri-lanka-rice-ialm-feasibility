# Public raw-source reconstruction

This folder contains a sanitized reconstruction of the harvest-outcome source layout used for the reproducibility workflow.

`harvest_outcomes_source_layout.xlsx` preserves the two-level spreadsheet structure needed to demonstrate direct Excel ingestion in R. `harvest_outcomes_source_layout.csv` contains the same `Harvest` values and is the input used by the continuously tested Python pipeline.

These are **public reproducibility inputs**, not copies of the institutional source-of-record. They contain the 32 public plot codes and agronomic measurements already released elsewhere in this repository. Personal information, proprietary nutrient formulations, application rates, and unrelated internal material are excluded.

The blank cells in the first two columns are intentional. They reproduce the source convention in which tillage and irrigation labels appeared once at the beginning of a group and were visually carried down. The cleaning code therefore has to forward-fill those labels and independently parse the compact plot codes rather than relying on manual spreadsheet edits.
