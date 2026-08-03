# External context data

The preparation notebook reads the large user-supplied source files from
`Y:/afinal/extradata` by default. Set `LONDON_SPORT_EXTRA_DATA_DIR` to override
that directory.

Included in the prepared panels:

- ONS mid-year population estimates and migration components from
  `myebtablesenglandwales20112024.xlsx`;
- residence-based ASHE median weekly earnings from
  `earnings-residence-borough.xlsx`;
- ONS Annual Population Survey economic inactivity rates from
  `economic-inactivity.csv`, downloaded from the London Datastore;
- daily historical London weather data from the user-supplied Open-Meteo file,
  supplemented for 2015–2016 by `open-meteo-2015-2016.csv`.

Reviewed but deliberately excluded:

- GLA population projections, because actual ONS estimates cover the study;
- climate-model projections for 2024–2030, because they are outside the study
  period and are future scenarios rather than historical data;
- MPS crime data, because it begins only in June 2020 and offence definitions
  change inside the file;
- two Nomis workbooks that contain only a title and no observations.

Downloaded files are retained locally so notebook execution does not depend on
live network access. The preparation notebook exports a machine-readable source
inventory, coverage audit and variable dictionary with the six analysis panels.
