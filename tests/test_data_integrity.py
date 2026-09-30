import csv
import unittest
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]

class TestPlotData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT/"data/derived/plot_outcomes_clean.csv").open(newline="",encoding="utf-8") as f:
            cls.rows=list(csv.DictReader(f))

    def test_32_unique_plots(self):
        self.assertEqual(len(self.rows),32)
        self.assertEqual(len({r["plot_code"] for r in self.rows}),32)

    def test_complete_factorial_code_grid(self):
        combos={(r["tillage_code"],r["irrigation_code"],r["fertilizer_code"],r["replicate_code"]) for r in self.rows}
        expected={(L,I,F,R) for L in ["L1","L2"] for I in ["IR1","IR2"] for F in ["F1","F2","F3","F4"] for R in ["R1","R2"]}
        self.assertEqual(combos,expected)

    def test_yield_complete(self):
        self.assertTrue(all(r["dry_yield_kg_plot"] != "" for r in self.rows))

    def test_reconstructed_means(self):
        def m(key,val):
            return mean(float(r["dry_yield_kg_plot"]) for r in self.rows if r[key]==val)
        self.assertAlmostEqual(m("tillage_code","L1"),9.4125,places=6)
        self.assertAlmostEqual(m("tillage_code","L2"),7.1625,places=6)
        self.assertAlmostEqual(m("irrigation_code","IR1"),8.83125,places=6)
        self.assertAlmostEqual(m("irrigation_code","IR2"),7.74375,places=6)

    def test_flagged_fresh_weight_retained(self):
        row=next(r for r in self.rows if r["plot_code"]=="L2IR1F4R2")
        self.assertEqual(float(row["fresh_weight_kg_plot"]),38.0)

class TestGrowthData(unittest.TestCase):
    def test_growth_shape(self):
        with (ROOT/"data/derived/growth_long_unlinked.csv").open(newline="",encoding="utf-8") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),2720)
        self.assertEqual(len({r["series_id"] for r in rows}),32)
        self.assertEqual(len({r["date"] for r in rows}),17)
        self.assertEqual(len({r["parameter"] for r in rows}),5)

if __name__ == "__main__":
    unittest.main()
