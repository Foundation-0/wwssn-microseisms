# Historical microseism amplitude measurement

Status: preparation for review. No observational result is claimed.

Select ALQ and a coastal station only after the coverage screen, preferably with the same calendar month. Freeze the selection and list all expected days, including unreadable or missing records. Download only those station-months in small cached batches.

Every measurement row needs station, day, channel/component, scan IDs and hashes, digitizer/software version, pixel-to-time scale, pixel-to-trace scale, timing correction, clipping/saturation status, instrument-response source and validity interval, gain units, filter band, ground-motion quantity and unit, amplitude estimator and uncertainty.

A single scalar gain is not generally enough for a frequency-dependent long-period response. Reconstruct the response appropriate to station, component and date before integrating a chosen microseism band. State whether the final quantity is displacement, velocity or acceleration; do not mix them across stations.

Use a fixed robust daily estimator and explicit earthquake/transient masking. Preserve mask durations and reasons. Validate several days with an independent digitizer or manual measurement using a tolerance fixed before comparison. A failed response lookup or unreadable trace yields missing with a reason, not zero amplitude.

DigitSeis/Lee waveforms and Peterson–Hutt response material need versioned source verification. Scans, response calibration and independent measurements are unavailable here, so no physical amplitude is reported.
