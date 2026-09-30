# Source Provenance and Reconstruction Log

## Source package reviewed

The reconstruction used the following classes of source material supplied with the project:

1. a 32-row agronomic outcome workbook;
2. August-September 2025 progress report;
3. May-July 2025 progress report;
4. research proposal and experimental schematic;
5. plot-code mapping workbook;
6. fertilizer application schedule and summary image;
7. 32 longitudinal growth workbooks;
8. GHG/AWD data-record template;
9. field photographs;
10. methodology/SOP materials.

The public repository does not redistribute most originals because several contain personal contact information, institution-internal material, proprietary treatment details, or content unnecessary for reproducibility.

For the harvest outcomes only, `data/raw_public/` contains a **sanitized source-layout reconstruction** built from the same values already released in the clean dataset. This makes the source-to-clean transformation inspectable without presenting the reconstructed workbook as an institutional original.

## Reconstruction decisions

### Plot codes

The 32 final plot codes were taken directly from the outcome workbook and parsed into L, IR, F, and R factors. The set is complete and balanced at the code level.

### Treatment mapping

L1/L2 and IR1/IR2 are consistently interpretable across sources. F1-F4 are only partially reconciled; the public codebook preserves that uncertainty.

### Longitudinal growth files

All 32 files have five parameters and 17 dates with no missing values in the inspected cells. Their source filenames form two groups of 16 series, but no defensible file in the package links those names to the 32 final plot codes. They are therefore released as unlinked neutral series.

### GHG records

The package includes a data-record template, photographs, and progress-report statements about gas monitoring. It does not include the measured concentration/flux dataset. GHG effect estimates are therefore absent.

### Images

Only field images without clearly identifiable project personnel were selected. They were re-encoded to remove original EXIF/metadata and renamed with neutral filenames.

## Public-release rule

Where a source disagreement affects a scientific interpretation, the disagreement is recorded rather than harmonized silently. Where a source contains personal or proprietary information not needed for the research claim, that information is excluded rather than redacted into a partially recoverable original file.
