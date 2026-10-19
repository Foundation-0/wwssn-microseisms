# wwssn-microseisms

**Did ocean wave energy, as recorded in seismic microseisms, change between 1962–78 and today?**

Ocean waves shake the sea floor and make the whole Earth hum faintly. Seismometers, the instruments that record
ground motion, pick up this hum as microseisms. Modern records show wave energy rising. From the 1960s the
World-Wide Standardized Seismographic Network (WWSSN) recorded ground motion on photographic paper and film. The US
Geological Survey (USGS) has released scans of part of that archive. Measuring microseisms on those scans would
extend the record of ocean wave energy back by decades.

Part of Foundation0's physics and Earth science work ([physics0](https://github.com/Foundation-0/physics0)), which
keeps inventories of the seismic and climate archives. It follows the pattern of
[plate-eclipses](https://github.com/Foundation-0/plate-eclipses): an old photographic archive joined to modern data.
It began in Foundation0's [scouting](https://github.com/Foundation-0/f0/tree/main/deep-fields) of 18–19 October 2026.

**Status: not started.**

## What is known

Checked against the source on 19 Oct 2026:

- On 14 July 2025 the USGS released "World-Wide Standardized Seismographic Network film chip scans"
  ([data release](https://www.usgs.gov/data/world-wide-standardized-seismographic-network-film-chip-scans),
  DOI 10.5066/P13PHZMA). It holds about 3.7 million single-day records from 1962–78, about 5% of the archive. It is
  marked CC0 1.0 Universal, so anyone may use it for any purpose.

From the scouting report, not yet re-checked:

- Aster et al. found wave energy rising by 0.27% a year at 52 stations since the late 1980s. They wrote that
  extending the record into the analog era, before digital recording, "offers an opportunity"
  ([Nature Communications 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620394/)).
- The USGS says "few researchers have utilized large numbers of these records"
  ([Nagle-McNaughton 2022](https://pubs.usgs.gov/publication/70231381)).
- The scans are reached through Globus, a service for moving large files.
- Tools that may help:
  - DigitSeis, software that turns scanned records into digital traces;
  - Lee (2022), digitised waveforms;
  - Peterson and Hutt 2014, instrument responses (how each instrument turned ground motion into a trace);
  - the ERA5 wave reanalysis, a reconstruction of past ocean waves;
  - EarthScope's FDSN service, for modern seismic data.
- Risks:
  - the 5% may have been chosen around earthquakes, so it may not be a fair sample of days;
  - the metadata gives 1961–1996, while the summary says 1962–78;
  - instrument gains changed over time.

The full list, with every source, is in [notes/scouting-2026-10-19.md](notes/scouting-2026-10-19.md). The complete scouting reports behind it are in [notes/reports/](notes/reports/README.md).

## Who else is working on this

From the scouting report, not yet re-checked:

- Studies of single stations' old paper records exist: Bromirski 2023 (Berkeley, 1931–2021) and Lecocq et al. 2020
  (Belgium, the 1953 storm).
- The scouts found no study of microseisms at many stations using the WWSSN scans since their release.
- The USGS authors (Aster, Ringler, Lee) are the likeliest competitors and collaborators. A person tells them about
  this project before any result is published.

## How a result is checked

- Every measurement names the scan files it used, and can be regenerated from the committed code.
- Amplitudes are converted to ground motion with the instrument response for that station and date, because gains
  changed over time.
- Before any trend is claimed, the daily amplitudes must track ERA5 swell (long waves that have travelled from
  distant storms) for the same days.
- The project stops if no station has about 3 years of near-continuous days, or if the amplitudes don't track ERA5.

## How to contribute

Take an [open issue](https://github.com/Foundation-0/wwssn-microseisms/issues). AI agents start with
[AGENTS.md](AGENTS.md) and Foundation0's [JOIN.md](https://github.com/Foundation-0/f0/blob/main/JOIN.md). Agents
coordinate in [st0a](https://github.com/Foundation-0/st0a). Questions and ideas go to the
[forum](https://github.com/Foundation-0/f0/discussions). The lead is to be named. A person signs for every result.

## Files

| path | what |
|---|---|
| `README.md` | this page |
| `AGENTS.md` | the guide for AI agents |
| `CLAUDE.md` | makes Claude Code read AGENTS.md |
| `notes/scouting-2026-10-19.md` | the research so far, with sources |
| `notes/reports/` | the complete scouting reports, kept as written, and the fact-check |
| `.github/` | the pull request template and the task issue form |
| `LICENSE` | Apache License 2.0 |

## Licence

Apache License 2.0 ([LICENSE](LICENSE)), as for Foundation0's other repositories.
