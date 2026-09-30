import csv
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "analysis" / "python"))

from plot_codes import expected_plot_codes, parse_plot_code  # noqa: E402
from step01_clean_harvest import build_clean_rows  # noqa: E402


class TestSourceReconstruction(unittest.TestCase):
    def test_public_source_rebuild_matches_canonical(self):
        rebuilt = build_clean_rows()
        with (ROOT / "data" / "derived" / "plot_outcomes_clean.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            canonical = list(csv.DictReader(handle))
        self.assertEqual(rebuilt, canonical)

    def test_plot_code_parser(self):
        parsed = parse_plot_code("L2IR1F4R2")
        self.assertEqual(parsed.tillage_code, "L2")
        self.assertEqual(parsed.irrigation_code, "IR1")
        self.assertEqual(parsed.fertilizer_code, "F4")
        self.assertEqual(parsed.replicate_code, "R2")

    def test_plot_code_parser_rejects_malformed_code(self):
        for bad in ("L3IR1F1R1", "L1IR3F1R1", "L1IR1F5R1", "L1IR1F1R3", "L1-F1"):
            with self.subTest(code=bad):
                with self.assertRaises(ValueError):
                    parse_plot_code(bad)

    def test_expected_code_grid(self):
        self.assertEqual(len(expected_plot_codes()), 32)


class TestTidyDerivedData(unittest.TestCase):
    def test_long_outcome_shape(self):
        with (ROOT / "data" / "derived" / "plot_outcomes_long.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 32 * 12)
        self.assertEqual(len({r["plot_code"] for r in rows}), 32)
        self.assertEqual(len({r["outcome"] for r in rows}), 12)

    def test_treatment_metadata_join(self):
        with (
            ROOT / "data" / "derived" / "plot_outcomes_with_treatment_metadata.csv"
        ).open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 32)
        self.assertTrue(all(r["nutrient_public_definition"] for r in rows))
        self.assertTrue(all(r["nutrient_definition_status"] for r in rows))


class TestNotebook(unittest.TestCase):
    def test_notebook_code_cells_compile(self):
        path = ROOT / "analysis" / "notebooks" / "reproducible_yield_walkthrough.ipynb"
        notebook = json.loads(path.read_text(encoding="utf-8"))
        code_cells = [
            "".join(cell.get("source", []))
            for cell in notebook["cells"]
            if cell.get("cell_type") == "code"
        ]
        self.assertGreaterEqual(len(code_cells), 6)
        for index, source in enumerate(code_cells):
            with self.subTest(cell=index):
                compile(source, f"notebook-cell-{index}", "exec")


if __name__ == "__main__":
    unittest.main()
