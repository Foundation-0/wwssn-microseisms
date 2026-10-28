# Archive inventory acceptance

Status: preparation for review. No observational result is claimed.

The input is a normalized metadata CSV with station, date (ISO calendar day) and scan_id. Multiple components or scans can occur on one station-day; report both scan count and unique days. The script downloads no images and rejects conflicting reuse of a scan identifier.

Obtain the current access route from the USGS data-release metadata for DOI 10.5066/P13PHZMA. Record the Globus collection identifier, listing command, metadata schema, UTC time and file-list hash. Use only listing/metadata access for this stage; do not transfer millions of scans.

Run `python3 tools/inventory.py listing.csv station-months.json`. Preserve the normalization mapping from source fields and filenames to station and date. Unparseable entries must be counted and quarantined, not silently excluded.

Reconcile total unique scans with the approximate published figure and report the actual minimum/maximum metadata dates, including any records outside the summary interval. The actual listing, adapter for its schema and produced inventory are pending. No archive coverage is inferred from the synthetic fixture.
