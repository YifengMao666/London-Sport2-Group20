# External COVID policy input

`OxCGRT_timeseries_StringencyIndex_v1.csv` is the final Oxford COVID-19
Government Response Tracker (OxCGRT) Stringency Index time-series file.

- Source: https://github.com/OxCGRT/covid-policy-dataset/blob/main/data/timeseries_indices/OxCGRT_timeseries_StringencyIndex_v1.csv
- Raw download: https://raw.githubusercontent.com/OxCGRT/covid-policy-dataset/main/data/timeseries_indices/OxCGRT_timeseries_StringencyIndex_v1.csv
- Publisher: Blavatnik School of Government, University of Oxford
- Licence: Creative Commons Attribution 4.0 (CC BY 4.0)
- Downloaded: 2026-08-04
- SHA-256: `C28B5BAB905286EC94DD5E0AB822C00A7FE4C471B70DC66BF225529B01460C69`

The COVID monthly sensitivity notebook selects the England `STATE_TOTAL` row
(`CountryCode=GBR`, `RegionCode=UK_ENG`) and converts the daily index to a
calendar-month mean. The index measures the number and strictness of recorded
government policy responses on a 0-100 scale; it does not measure whether the
response was appropriate or effectively implemented.
