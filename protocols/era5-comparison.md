# ERA5 comparison before trend work

Status: preparation for review. No observational result is claimed.

Choose each ocean region by geography and a physical propagation argument before seeing correlations. Freeze the ERA5 product/version, wave variable, units, grid aggregation, time convention and treatment of missing days. Do not optimize the region or lag on the same month used to judge agreement.

Join daily amplitudes and swell by UTC day, keeping unpaired days in an exclusion log. The kernel rejects duplicate days and constant series. Pearson correlation is association, not evidence that a trend is climatic or that amplitude is proportional to wave energy.

A proposed tracking rule is positive correlation with a positive lower confidence bound under a seven-day block bootstrap, after a minimum paired-day requirement agreed before analysis. With only one month the uncertainty may be large; do not replace block resampling with independent-day errors. The bootstrap and sensitivity analysis still need implementation and review.

No tracking verdict or trend is claimed. Acceptance needs real response-calibrated amplitudes, frozen ERA5 extracts, a committed comparison table and plot, uncertainty and independent rerun. If the frozen tracking rule fails, the project stop rule applies before trend claims.
