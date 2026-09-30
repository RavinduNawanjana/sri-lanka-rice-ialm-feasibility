# Data Management and Public Sanitization

## Included

The public repository includes numeric plot outcomes, treatment codes with conservative labels, a sanitized reconstruction of the harvest source layout, an unlinked tidy growth dataset, data dictionaries, quality flags, analysis scripts, derived figures, and selected field images.

## Public raw-source reconstruction

`data/raw_public/` exists so the cleaning logic can be inspected rather than hidden behind a pre-cleaned CSV. The `.xlsx` and companion `.csv` reconstruct only material already released in the portfolio: 32 plot codes, visually grouped tillage/irrigation labels, and agronomic measurements.

They are **not** represented as original RRDI/Kangara source files. The institutional originals remain outside the public repository.

## Excluded

The public package excludes personal email addresses, phone numbers, staff CVs, original reports containing personal details, raw proprietary fertilizer schedules, product-specific dosing, and unrelated internal files.

## Image sanitization

Selected field images are decoded and re-encoded as new JPEGs. This strips embedded EXIF and messenger metadata from the delivered files. Images with clearly identifiable project personnel or misleading treatment signage were not selected.

## Data transformations

The public harvest workflow is script-based:

1. visually grouped tillage and irrigation labels are forward-filled;
2. compact plot codes are parsed with a strict regular expression;
3. parsed codes are checked against the source labels;
4. numeric fields are validated;
5. the complete 32-code grid is checked;
6. the canonical clean table is written;
7. outcomes are reshaped to long form and joined to public treatment metadata.

Numeric outcome values are not normalized, winsorized, imputed, or corrected. The suspicious `38 kg/plot` fresh-weight value is retained and separately flagged.

Longitudinal growth records are reshaped from wide date columns to long rows. Source filenames are replaced by neutral series IDs while preserving a generic source group solely for traceability.

## Provenance

The public data are derived from project files supplied for this research portfolio. `data/metadata/source_register.csv` records provenance classes without redistributing source-sensitive files. `docs/reproducible-workflow.md` documents the public data lineage.

## Reuse

No open-source or open-data license is granted for the repository as a whole. Public visibility is intended to support academic review and reproducibility, not to authorize unrestricted reuse. Rights in institutional source material, field data, photographs, and third-party content remain with the relevant rights holders. See `DATA_USE.md`.
