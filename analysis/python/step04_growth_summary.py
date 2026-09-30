from collections import defaultdict
import csv, statistics
from common import ROOT, write_csv


def main():
    path=ROOT/"data/derived/growth_long_unlinked.csv"
    groups=defaultdict(list)
    with path.open(newline="",encoding="utf-8") as f:
        for r in csv.DictReader(f):
            groups[(r["date"],r["parameter"])].append(float(r["value"]))
    out=[]
    for (date,param),x in sorted(groups.items()):
        xs=sorted(x)
        q1=statistics.median(xs[:len(xs)//2])
        q3=statistics.median(xs[(len(xs)+1)//2:])
        out.append({"date":date,"parameter":param,"n":len(x),"median":round(statistics.median(x),6),
                    "q1":round(q1,6),"q3":round(q3,6),"min":min(x),"max":max(x)})
    write_csv(ROOT/"analysis/outputs/growth_unlinked_summary.csv",
              ["date","parameter","n","median","q1","q3","min","max"],out)

if __name__ == "__main__":
    main()
