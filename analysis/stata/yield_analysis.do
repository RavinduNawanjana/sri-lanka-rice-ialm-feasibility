clear all
import delimited "data/derived/plot_outcomes_clean.csv", varnames(1) clear

summarize dry_yield_kg_plot
by tillage_code, sort: summarize dry_yield_kg_plot
by irrigation_code, sort: summarize dry_yield_kg_plot
by fertilizer_code, sort: summarize dry_yield_kg_plot

encode tillage_code, gen(tillage)
encode irrigation_code, gen(irrigation)
encode fertilizer_code, gen(fertilizer)

* Exploratory naive model only. Plot-level residual may be the wrong error term
* for tillage and irrigation if those factors were assigned to larger field units.
regress dry_yield_kg_plot i.tillage##i.irrigation##i.fertilizer

* Replace with a hierarchy matching the verified randomization, for example:
* mixed dry_yield_kg_plot i.tillage##i.irrigation##i.fertilizer || block_id: || tillage_whole_plot_id: || irrigation_subplot_id:
