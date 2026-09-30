from collections import defaultdict
from statistics import mean, median
import csv
import matplotlib.pyplot as plt
from common import ROOT, read_plot_outcomes


def strip_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def factor_plot(rows, factor, labels, filename, title):
    levels=list(labels)
    fig,ax=plt.subplots(figsize=(7.2,4.6))
    for i,level in enumerate(levels):
        vals=[r["dry_yield_kg_plot"] for r in rows if r[factor]==level]
        # deterministic horizontal offsets, not random jitter
        if len(vals)==1:
            offsets=[0]
        else:
            offsets=[(j-(len(vals)-1)/2)*0.018 for j in range(len(vals))]
        ax.scatter([i+o for o in offsets],vals,s=26,alpha=.7)
        ax.plot([i-.18,i+.18],[mean(vals),mean(vals)],linewidth=2.5)
    ax.set_xticks(range(len(levels)),[labels[x] for x in levels])
    ax.set_ylabel("Dry yield (kg/plot)")
    ax.set_title(title)
    ax.text(0.01,0.01,"Points are plots; horizontal line is the descriptive mean. No inferential error bar shown.",
            transform=ax.transAxes,fontsize=8,va="bottom")
    strip_axes(ax)
    fig.tight_layout()
    fig.savefig(ROOT/"figures"/filename,dpi=220,bbox_inches="tight")
    plt.close(fig)


def interaction_plot(rows):
    groups=defaultdict(list)
    for r in rows:
        groups[(r["tillage_code"],r["irrigation_code"],r["fertilizer_code"])].append(r["dry_yield_kg_plot"])
    fs=["F1","F2","F3","F4"]
    fig,ax=plt.subplots(figsize=(7.4,4.8))
    for L in ["L1","L2"]:
        for I in ["IR1","IR2"]:
            ys=[mean(groups[(L,I,F)]) for F in fs]
            ax.plot(fs,ys,marker="o",label=f"{L} x {I}")
    ax.set_ylabel("Cell mean dry yield (kg/plot)")
    ax.set_xlabel("Nutrient treatment code")
    ax.set_title("Descriptive L x IR x F cell means")
    ax.legend(frameon=False,ncol=2)
    strip_axes(ax)
    fig.tight_layout()
    fig.savefig(ROOT/"figures/yield_cell_means.png",dpi=220,bbox_inches="tight")
    plt.close(fig)


def growth_plot():
    path=ROOT/"data/derived/growth_long_unlinked.csv"
    bydate=defaultdict(list)
    with path.open(newline="",encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["parameter"]=="Plant Height":
                bydate[r["date"]].append(float(r["value"]))
    dates=sorted(bydate)
    med=[median(bydate[d]) for d in dates]
    q1=[];q3=[]
    for d in dates:
        xs=sorted(bydate[d]); n=len(xs)
        q1.append(median(xs[:n//2])); q3.append(median(xs[(n+1)//2:]))
    fig,ax=plt.subplots(figsize=(8.2,4.8))
    x=range(len(dates))
    ax.plot(x,med,marker="o",linewidth=1.8)
    ax.fill_between(x,q1,q3,alpha=.2)
    ax.set_xticks(list(x)[::2],[dates[i] for i in range(0,len(dates),2)],rotation=40,ha="right")
    ax.set_ylabel("Plant height (source units; nominally cm)")
    ax.set_title("Overall growth trajectory across 32 unlinked source series")
    ax.text(.01,.01,"Median and interquartile range; treatment mapping unavailable.",transform=ax.transAxes,fontsize=8)
    strip_axes(ax)
    fig.tight_layout()
    fig.savefig(ROOT/"figures/growth_height_unlinked.png",dpi=220,bbox_inches="tight")
    plt.close(fig)


def main():
    rows=read_plot_outcomes()
    factor_plot(rows,"tillage_code",{"L1":"L1: two ploughings","L2":"L2: one ploughing"},"yield_by_tillage.png","Dry yield by tillage code")
    factor_plot(rows,"irrigation_code",{"IR1":"IR1: normal","IR2":"IR2: AWD"},"yield_by_irrigation.png","Dry yield by irrigation code")
    factor_plot(rows,"fertilizer_code",{"F1":"F1","F2":"F2","F3":"F3","F4":"F4"},"yield_by_fertilizer.png","Dry yield by nutrient-treatment code")
    interaction_plot(rows)
    growth_plot()

if __name__ == "__main__":
    main()
