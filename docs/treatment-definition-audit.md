# Nutrient-Treatment Definition Audit

## Why this audit exists

The source package contains enough information to decode F1-F4, but three source types do not align perfectly: the research proposal, the plot-code mapping workbook, and the operational application schedule. A public research repository should preserve that disagreement instead of silently choosing the most convenient version.

## Public-safe reconstruction

| Code | Public interpretation used here | Source agreement |
|---|---|---|
| F1 | Full recommended mineral fertilizer plus organic manure | Moderate |
| F2 | Reduced recommended mineral fertilizer plus organic manure and a proprietary organic input | Moderate |
| F3 | Full recommended mineral fertilizer; residue component unresolved | Moderate |
| F4 | No-fertilizer control | High |

## F1 discrepancy

The plot-code mapping identifies F1 as full recommended mineral fertilizer plus organic manure. An application schedule appears to record the proprietary liquid input on F1 as well as F2 plots. That is not consistent with the simplest reading of the code-mapping workbook. The public repository therefore does not publish a product-specific formula for F1.

## F2 status

The code-mapping workbook and proposal both support a reduced-mineral treatment combined with organic inputs. The public repository deliberately omits the proprietary product name, exact proportion, concentration, and dose schedule. The analytical dataset uses only `F2` and a generic treatment label.

## F3 discrepancy

The proposal specifies full recommended mineral fertilizer plus previous-season straw. The plot-code mapping workbook describes F3 only as full inorganic fertilizer. The final operational status of residue retention/incorporation is therefore unresolved.

## F4 status

F4 is consistently described as a no-fertilizer control.

## What will close the audit

The authoritative resolution should come from a signed final treatment sheet or contemporaneous field book, not from post hoc inference. `../data/reconciliation/treatment_definition_verification.csv` provides fields for that confirmation.

Until then, statistical output should reference F1-F4 codes and the conservative public labels above. It should not interpret a difference between F1 and F2 as the effect of any single proprietary product, because more than one input dimension may differ and the operational schedule is not fully reconciled.
