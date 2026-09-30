# VM0042 Methodology Note

**Version context checked 30 September 2026.** This note is a research crosswalk, not a validation opinion.

## Historical study framing

The 2025 project documents repeatedly frame the field study as generating evidence relevant to Verra VM0042. The September progress report discusses GHG measurements, tillage, AWD, fertilizer treatments, and eventual VM0042 verification documentation. That historical framing is retained.

However, a feasibility trial designed around a methodology is not the same thing as a VCS project satisfying the methodology. This repository therefore separates experimental evidence from carbon-accounting eligibility.

## Current VM0042 status

Verra lists **VM0042 Improved Agricultural Land Management v2.2** as active since 21 October 2025, while v2.1 also remains active. Verra released corrections and clarifications to v2.2 on 11 June 2026. The current methodology page should be checked again before any project filing because active versions and program rules can change.

Official page: https://verra.org/methodologies/vm0042-improved-agricultural-land-management-v2-2/

## Applicability is not established by a treatment name

VM0042 includes improved fertilizer management, improved water management/irrigation, reduced tillage/residue management, crop planting/harvesting, and grazing among potentially eligible practice categories. It also requires qualifying practice changes and imposes other applicability conditions.

The field trial's use of AWD or reduced tillage is therefore relevant to methodology scope, but the existence of those treatments does not by itself establish eligibility for a crediting project.

## Baseline

VM0042 v2.2 constructs the baseline as continuation of pre-project agricultural land-management practices and uses a minimum three-year historical look-back to build a schedule of activities. This is a project-level historical-evidence requirement. The 32-row trial dataset does not contain that baseline history.

For this reason the repository does not translate “IR1” or “L1” automatically into the VCS baseline scenario. They are experimental comparator codes, not a validated baseline.

## Additionality

Under VM0042 v2.2, additionality includes regulatory-surplus requirements, barrier analysis, and a common-practice test. The methodology defines common practice using a 20% adoption threshold before additional procedures where adoption exceeds that threshold or data are unavailable. A quantitative adjustment to a pre-existing practice must exceed 5% of the pre-existing value to qualify as a practice change under the methodology's applicability conditions.

Nothing in a one-season yield comparison demonstrates these conditions. A yield decrease can be relevant to agronomic viability and, under some circumstances, productivity/leakage concerns, but it is not an additionality test.

The repository therefore uses the wording:

> Reduced tillage showed poorer agronomic performance under the observed feasibility-study conditions and may therefore have been less viable as a candidate project intervention.

It does **not** use the wording “reduced tillage failed additionality.”

## Productivity and leakage

VM0042 v2.2 includes an applicability condition related to sustained productivity reductions and also addresses leakage associated with productivity declines. This makes yield an important feasibility variable, but the methodology question is not answered by one trial's marginal mean alone. The relevant assessment requires the methodology's procedures, appropriate regional evidence, and a defensible definition of the project activity.

## Quantification

VM0042 v2.2 provides multiple quantification approaches, including model-based and measurement-based elements. The exact requirements vary by emission/removal type. A chamber study can provide valuable empirical evidence, but raw field gas measurements do not automatically become VCUs. Model validation, parameter requirements, uncertainty, project/baseline accounting, leakage, and monitoring rules still apply.

## Monitoring

VM0042 requires a monitoring plan covering data/parameters, monitoring tasks, accounting boundaries, sampling design, QA/QC, and data management. The source project's 16 chambers, AWD monitoring, and field documentation are relevant building blocks. The supplied public package is incomplete for this purpose because it lacks the gas time series, calibration/QC evidence, chamber geometry/linkage, and water-depth series.

## Compliance language used in this repository

Allowed:

- “designed to generate evidence relevant to VM0042”;
- “practice categories overlap with those contemplated by VM0042”;
- “a methodology-alignment question remains”;
- “additional evidence is required.”

Avoided unless backed by formal documentation:

- “VM0042 compliant”;
- “verified carbon credits”;
- “additionality passed”;
- “validated by Verra”;
- “eligible credits generated.”
