"""Balanced plot-level factorial ANOVA for transparency only.

This is NOT the confirmatory model unless the field randomization map establishes
that the plot-level residual is a valid error term for tillage and irrigation.
"""
from collections import defaultdict
from statistics import mean
import warnings
import numpy as np
from scipy.stats import f as f_dist
from common import ROOT, read_plot_outcomes, write_csv


def ss_balanced(rows):
    # Fully balanced 2 x 2 x 4 with n=2 per cell.
    factors={
        "L":sorted({r["tillage_code"] for r in rows}),
        "IR":sorted({r["irrigation_code"] for r in rows}),
        "F":sorted({r["fertilizer_code"] for r in rows}),
    }
    y=np.array([r["dry_yield_kg_plot"] for r in rows],dtype=float)
    grand=float(y.mean())
    n=2; a=len(factors["L"]); b=len(factors["IR"]); c=len(factors["F"])

    def m(**conds):
        vals=[r["dry_yield_kg_plot"] for r in rows if all(r[k]==v for k,v in conds.items())]
        return mean(vals)

    Lm={L:m(tillage_code=L) for L in factors["L"]}
    Im={I:m(irrigation_code=I) for I in factors["IR"]}
    Fm={F:m(fertilizer_code=F) for F in factors["F"]}
    LIm={(L,I):m(tillage_code=L,irrigation_code=I) for L in factors["L"] for I in factors["IR"]}
    LFm={(L,F):m(tillage_code=L,fertilizer_code=F) for L in factors["L"] for F in factors["F"]}
    IFm={(I,F):m(irrigation_code=I,fertilizer_code=F) for I in factors["IR"] for F in factors["F"]}
    cell={(L,I,F):m(tillage_code=L,irrigation_code=I,fertilizer_code=F)
          for L in factors["L"] for I in factors["IR"] for F in factors["F"]}

    ss={}
    ss["tillage"] = b*c*n*sum((Lm[L]-grand)**2 for L in factors["L"])
    ss["irrigation"] = a*c*n*sum((Im[I]-grand)**2 for I in factors["IR"])
    ss["fertilizer"] = a*b*n*sum((Fm[F]-grand)**2 for F in factors["F"])
    ss["tillage:irrigation"] = c*n*sum((LIm[L,I]-Lm[L]-Im[I]+grand)**2 for L in factors["L"] for I in factors["IR"])
    ss["tillage:fertilizer"] = b*n*sum((LFm[L,F]-Lm[L]-Fm[F]+grand)**2 for L in factors["L"] for F in factors["F"])
    ss["irrigation:fertilizer"] = a*n*sum((IFm[I,F]-Im[I]-Fm[F]+grand)**2 for I in factors["IR"] for F in factors["F"])
    ss["tillage:irrigation:fertilizer"] = n*sum(
        (cell[L,I,F]-LIm[L,I]-LFm[L,F]-IFm[I,F]+Lm[L]+Im[I]+Fm[F]-grand)**2
        for L in factors["L"] for I in factors["IR"] for F in factors["F"])
    ss["error"] = sum((r["dry_yield_kg_plot"]-cell[r["tillage_code"],r["irrigation_code"],r["fertilizer_code"]])**2 for r in rows)
    df={
        "tillage":a-1,"irrigation":b-1,"fertilizer":c-1,
        "tillage:irrigation":(a-1)*(b-1),
        "tillage:fertilizer":(a-1)*(c-1),
        "irrigation:fertilizer":(b-1)*(c-1),
        "tillage:irrigation:fertilizer":(a-1)*(b-1)*(c-1),
        "error":a*b*c*(n-1),
    }
    mse=ss["error"]/df["error"]
    out=[]
    for effect in ["tillage","irrigation","fertilizer","tillage:irrigation","tillage:fertilizer","irrigation:fertilizer","tillage:irrigation:fertilizer"]:
        ms=ss[effect]/df[effect]
        F=ms/mse
        p=float(f_dist.sf(F,df[effect],df["error"]))
        out.append({"effect":effect,"sum_sq":round(ss[effect],6),"df":df[effect],"mean_sq":round(ms,6),
                    "F":round(F,6),"p_value":round(p,9),
                    "analysis_status":"exploratory_naive_only"})
    out.append({"effect":"error","sum_sq":round(ss["error"],6),"df":df["error"],"mean_sq":round(mse,6),
                "F":"","p_value":"","analysis_status":"plot_level_error_term_may_be_invalid_for_L_and_IR"})
    return out


def main():
    warnings.warn("Naive plot-level ANOVA: do not use as confirmatory evidence until experimental units are verified.")
    out=ss_balanced(read_plot_outcomes())
    write_csv(ROOT/"analysis/outputs/exploratory_naive_anova.csv",
              ["effect","sum_sq","df","mean_sq","F","p_value","analysis_status"],out)

if __name__ == "__main__":
    main()
