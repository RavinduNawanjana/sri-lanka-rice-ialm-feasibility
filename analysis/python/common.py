from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]

def read_plot_outcomes():
    path = ROOT / "data" / "derived" / "plot_outcomes_clean.csv"
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    numeric = [
        "plant_height_cm_early", "panicles_0_25m2", "productive_tillers_m2",
        "plant_height_cm_harvest", "fresh_weight_kg_plot", "ten_panicle_weight_g",
        "thousand_seed_weight_g", "filled_grain_count", "filled_grain_weight_g",
        "unfilled_grain_count", "unfilled_grain_weight_g", "dry_yield_kg_plot"
    ]
    for row in rows:
        for key in numeric:
            row[key] = float(row[key])
    return rows

def write_csv(path, fieldnames, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(records)
