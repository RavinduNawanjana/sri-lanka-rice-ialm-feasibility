"""Step 02: reshape outcomes to tidy long form and join treatment metadata."""
from __future__ import annotations

import csv
from pathlib import Path

from common import ROOT, write_csv

CLEAN = ROOT / "data" / "derived" / "plot_outcomes_clean.csv"
LONG = ROOT / "data" / "derived" / "plot_outcomes_long.csv"
ENRICHED = ROOT / "data" / "derived" / "plot_outcomes_with_treatment_metadata.csv"
CODEBOOK = ROOT / "data" / "metadata" / "treatment_codebook.csv"

OUTCOMES = {
    "plant_height_cm_early": "cm",
    "panicles_0_25m2": "count_per_0.25m2",
    "productive_tillers_m2": "panicles_per_m2",
    "plant_height_cm_harvest": "cm",
    "fresh_weight_kg_plot": "kg_per_plot",
    "ten_panicle_weight_g": "g",
    "thousand_seed_weight_g": "g",
    "filled_grain_count": "count",
    "filled_grain_weight_g": "g",
    "unfilled_grain_count": "count",
    "unfilled_grain_weight_g": "g",
    "dry_yield_kg_plot": "kg_per_plot",
}


def _read_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = _read_dicts(CLEAN)

    long_rows = []
    id_fields = [
        "plot_code",
        "tillage_code",
        "irrigation_code",
        "fertilizer_code",
        "replicate_code",
    ]
    for row in rows:
        for outcome, unit in OUTCOMES.items():
            long_rows.append(
                {
                    **{field: row[field] for field in id_fields},
                    "outcome": outcome,
                    "value": row[outcome],
                    "unit": unit,
                }
            )

    write_csv(
        LONG,
        [*id_fields, "outcome", "value", "unit"],
        long_rows,
    )

    nutrient = {
        row["code"]: row
        for row in _read_dicts(CODEBOOK)
        if row["factor"] == "nutrient"
    }
    enriched = []
    for row in rows:
        meta = nutrient[row["fertilizer_code"]]
        enriched.append(
            {
                **row,
                "nutrient_public_definition": meta["public_definition"],
                "nutrient_definition_status": meta["status"],
                "nutrient_definition_confidence": meta["confidence"],
            }
        )

    write_csv(
        ENRICHED,
        [*rows[0].keys(),
         "nutrient_public_definition",
         "nutrient_definition_status",
         "nutrient_definition_confidence"],
        enriched,
    )
    print(
        "Step 02: wrote tidy long outcomes "
        f"({len(long_rows)} rows) and treatment-metadata join ({len(enriched)} rows)."
    )


if __name__ == "__main__":
    main()
