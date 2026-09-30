"""Step 01: rebuild the public clean harvest dataset from source-layout data.

The source-style table intentionally contains blank tillage/irrigation cells after
the first row of each visual group.  This script forward-fills those labels,
parses every compact plot identifier with a regular expression, checks that the
two representations agree, validates the complete 2 x 2 x 4 x 2 code grid, and
writes the canonical clean CSV.

No source value is imputed, winsorized, or silently corrected.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

from common import ROOT
from plot_codes import expected_plot_codes, parse_plot_code

SOURCE = ROOT / "data" / "raw_public" / "harvest_outcomes_source_layout.csv"
OUTPUT = ROOT / "data" / "derived" / "plot_outcomes_clean.csv"

OUTCOME_FIELDS = [
    "plant_height_cm_early",
    "panicles_0_25m2",
    "productive_tillers_m2",
    "plant_height_cm_harvest",
    "fresh_weight_kg_plot",
    "ten_panicle_weight_g",
    "thousand_seed_weight_g",
    "filled_grain_count",
    "filled_grain_weight_g",
    "unfilled_grain_count",
    "unfilled_grain_weight_g",
    "dry_yield_kg_plot",
]
FIELDNAMES = [
    "plot_code",
    "tillage_code",
    "irrigation_code",
    "fertilizer_code",
    "replicate_code",
    "tillage_label",
    "irrigation_label",
    *OUTCOME_FIELDS,
]

TILLAGE_LABEL = {
    "L1": "two_ploughings_conventional",
    "L2": "one_ploughing_reduced",
}
IRRIGATION_LABEL = {
    "IR1": "normal_irrigation",
    "IR2": "alternate_wetting_drying",
}


def _norm_label(value: str) -> str:
    return " ".join((value or "").split()).strip().lower()


def _validate_numeric(value: str, field: str, plot_code: str) -> None:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{plot_code}: {field} is not numeric: {value!r}") from exc
    if not math.isfinite(number):
        raise ValueError(f"{plot_code}: {field} is not finite: {value!r}")


def build_clean_rows(source: Path = SOURCE) -> list[dict[str, str]]:
    with Path(source).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))

    if len(rows) != 33:
        raise ValueError(f"Expected 1 header + 32 data rows; found {len(rows)} rows.")
    if any(len(row) != 15 for row in rows):
        widths = sorted({len(row) for row in rows})
        raise ValueError(f"Expected 15 source columns; observed widths {widths}.")

    current_tillage = ""
    current_irrigation = ""
    clean: list[dict[str, str]] = []

    for row_number, row in enumerate(rows[1:], start=2):
        if row[0].strip():
            current_tillage = row[0]
        if row[1].strip():
            current_irrigation = row[1]
        if not current_tillage or not current_irrigation:
            raise ValueError(
                f"Row {row_number}: cannot forward-fill source treatment labels."
            )

        parsed = parse_plot_code(row[2])

        # Independent consistency check against the labels visually carried down
        # in the source workbook.
        tlabel = _norm_label(current_tillage)
        ilabel = _norm_label(current_irrigation)
        if parsed.tillage_code == "L1" and "2 time ploughing" not in tlabel:
            raise ValueError(f"{parsed.plot_code}: L1 conflicts with {current_tillage!r}.")
        if parsed.tillage_code == "L2" and "1 time ploughing" not in tlabel:
            raise ValueError(f"{parsed.plot_code}: L2 conflicts with {current_tillage!r}.")
        if parsed.irrigation_code == "IR1" and ilabel != "irrigated":
            raise ValueError(f"{parsed.plot_code}: IR1 conflicts with {current_irrigation!r}.")
        if parsed.irrigation_code == "IR2" and ilabel != "awd":
            raise ValueError(f"{parsed.plot_code}: IR2 conflicts with {current_irrigation!r}.")

        values = row[3:15]
        for field, value in zip(OUTCOME_FIELDS, values, strict=True):
            _validate_numeric(value, field, parsed.plot_code)

        record = {
            "plot_code": parsed.plot_code,
            "tillage_code": parsed.tillage_code,
            "irrigation_code": parsed.irrigation_code,
            "fertilizer_code": parsed.fertilizer_code,
            "replicate_code": parsed.replicate_code,
            "tillage_label": TILLAGE_LABEL[parsed.tillage_code],
            "irrigation_label": IRRIGATION_LABEL[parsed.irrigation_code],
        }
        record.update(dict(zip(OUTCOME_FIELDS, values, strict=True)))
        clean.append(record)

    observed = {row["plot_code"] for row in clean}
    expected = expected_plot_codes()
    if observed != expected:
        missing = sorted(expected - observed)
        extra = sorted(observed - expected)
        raise ValueError(f"Incomplete code grid; missing={missing}, unexpected={extra}.")

    return clean


def main() -> None:
    rows = build_clean_rows()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Step 01: rebuilt {OUTPUT.relative_to(ROOT)} from {len(rows)} source rows.")


if __name__ == "__main__":
    main()
