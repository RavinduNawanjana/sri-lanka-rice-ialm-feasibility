# Public reconstruction: descriptive and exploratory only.
# Do not treat plot-level p-values for tillage/irrigation as confirmatory until
# block and whole-plot assignment units are recovered.

d <- read.csv("data/derived/plot_outcomes_clean.csv", stringsAsFactors = TRUE)

aggregate(dry_yield_kg_plot ~ tillage_code, data=d, FUN=mean)
aggregate(dry_yield_kg_plot ~ irrigation_code, data=d, FUN=mean)
aggregate(dry_yield_kg_plot ~ fertilizer_code, data=d, FUN=mean)

# Naive plot-level factorial model retained only for transparent comparison.
naive <- aov(dry_yield_kg_plot ~ tillage_code * irrigation_code * fertilizer_code, data=d)
print(summary(naive))

# After randomization recovery, use the actual field hierarchy. Example only:
# d$block_id <- ...
# fit <- aov(dry_yield_kg_plot ~ tillage_code * irrigation_code * fertilizer_code +
#            Error(block_id / tillage_whole_plot_id / irrigation_subplot_id), data=d)
# summary(fit)
