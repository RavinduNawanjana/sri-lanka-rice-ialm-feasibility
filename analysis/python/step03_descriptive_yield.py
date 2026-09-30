from collections import defaultdict
from statistics import mean, stdev
from common import ROOT, read_plot_outcomes, write_csv


def summarize(rows, factor):
    groups = defaultdict(list)
    for r in rows:
        groups[r[factor]].append(r["dry_yield_kg_plot"])
    result=[]
    for level in sorted(groups):
        x=groups[level]
        result.append({
            "factor":factor,
            "level":level,
            "n":len(x),
            "mean_kg_plot":round(mean(x),6),
            "sd_kg_plot":round(stdev(x),6),
            "min_kg_plot":min(x),
            "max_kg_plot":max(x),
        })
    return result


def main():
    rows=read_plot_outcomes()
    out=[]
    for factor in ["tillage_code","irrigation_code","fertilizer_code"]:
        out.extend(summarize(rows,factor))
    write_csv(ROOT/"analysis/outputs/yield_marginal_summary.csv",
              ["factor","level","n","mean_kg_plot","sd_kg_plot","min_kg_plot","max_kg_plot"], out)

    cells=defaultdict(list)
    for r in rows:
        key=(r["tillage_code"],r["irrigation_code"],r["fertilizer_code"])
        cells[key].append(r["dry_yield_kg_plot"])
    cell_out=[]
    for key in sorted(cells):
        x=cells[key]
        cell_out.append({"tillage_code":key[0],"irrigation_code":key[1],"fertilizer_code":key[2],
                         "n":len(x),"mean_kg_plot":round(mean(x),6),"sd_kg_plot":round(stdev(x),6)})
    write_csv(ROOT/"analysis/outputs/yield_cell_summary.csv",
              ["tillage_code","irrigation_code","fertilizer_code","n","mean_kg_plot","sd_kg_plot"],cell_out)

if __name__ == "__main__":
    main()
