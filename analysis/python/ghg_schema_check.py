"""Validate a future GHG import without calculating fluxes.

Flux calculation is deliberately absent until concentration units, chamber geometry,
analyzer/lab method, and timing are verified.
"""
import csv, sys
from pathlib import Path
from common import ROOT

REQUIRED=[
    "plot_code","sampling_date","sampling_event_id","chamber_id","closure_time_min",
    "ch4_concentration","ch4_unit","co2_concentration","co2_unit","n2o_concentration","n2o_unit",
    "chamber_air_temperature_c","chamber_volume_m3","chamber_footprint_m2","water_depth_cm",
    "analyzer_or_lab_method","calibration_id","qc_flag","source_file"
]

def check(path):
    with Path(path).open(newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        missing=[c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("Missing required columns: "+", ".join(missing))
        rows=list(reader)
    print(f"Schema OK: {len(rows)} rows. No flux calculation performed.")

if __name__ == "__main__":
    path=sys.argv[1] if len(sys.argv)>1 else ROOT/"data/metadata/ghg_import_schema.csv"
    check(path)
