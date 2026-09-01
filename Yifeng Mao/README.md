# Physical Activity in London: Analysis and Forecasting

This directory contains **Yifeng Mao's Question 1 contribution** to the London Sport Group 20 project. It analyses eight waves of Active Lives survey data from **2015/16 to 2022/23** and examines physical activity across London, Inner/Outer London, the 32 London boroughs outside the City of London, and individual respondents.

The analysis covers historical trends, geographic differences, borough clustering and monthly, quarterly and annual forecasts for three activity states: **Inactive**, **Fairly Active** and **Active**.

## Research questions

1. How did physical activity change in London across the eight survey waves?
2. How do activity patterns differ between London, Inner/Outer London and individual boroughs?
3. Can boroughs be grouped into stable structural or activity-trajectory types?
4. Which forecasting method performs best at monthly, quarterly and annual frequencies?

## Project structure

```text
Yifeng Mao/
├── README.md
├── data/
│   ├── active_lives_1516_london_125.csv
│   ├── active_lives_1516_london_125_variables.csv
│   ├── active_lives_1617_london_125.csv
│   ├── active_lives_1617_london_125_variables.csv
│   └── preprocessing_code/
│       ├── prepare_london_1516.ipynb
│       └── prepare_london_1617.ipynb
└── Q1/
    ├── physical_activity_analysis/
    │   ├── 01_prepare_question1_data.ipynb
    │   ├── 02a_multilevel_descriptive_analysis.ipynb
    │   ├── 02b_borough_clustering_analysis.ipynb
    │   └── 03_monthly_quarterly_and_annual_forecasting.ipynb
    └── question1_outputs/
        └── prepared_data/
            ├── q1_respondents_8wave.csv
            ├── q1_annual.csv
            ├── q1_quarterly.csv
            ├── q1_monthly.csv
            └── q1_age_annual.csv
```

## Analysis notebooks

| Notebook | Description |
|---|---|
| [`01_prepare_question1_data.ipynb`](Q1/physical_activity_analysis/01_prepare_question1_data.ipynb) | Combines the eight survey waves, checks schema and missingness, applies survey weights, joins contextual data and creates the five analysis-ready datasets. |
| [`02a_multilevel_descriptive_analysis.ipynb`](Q1/physical_activity_analysis/02a_multilevel_descriptive_analysis.ipynb) | Examines London-wide trends, Inner/Outer differences, borough patterns and respondent-level participation. It includes seasonal decomposition, age standardisation, multilevel models and spatial analysis. |
| [`02b_borough_clustering_analysis.ipynb`](Q1/physical_activity_analysis/02b_borough_clustering_analysis.ipynb) | Builds structural and activity-trajectory borough typologies using PCA, K-means and Ward clustering, with bootstrap stability and membership-uncertainty checks. |
| [`03_monthly_quarterly_and_annual_forecasting.ipynb`](Q1/physical_activity_analysis/03_monthly_quarterly_and_annual_forecasting.ipynb) | Compares a naive baseline, Ridge Regression, Random Forest and Gradient Boosting using rolling-origin validation, then produces eight-year forecasts. |

## Prepared datasets

The files in [`Q1/question1_outputs/prepared_data/`](Q1/question1_outputs/prepared_data/) are the shared inputs for the descriptive, clustering and forecasting notebooks.

| File | Size | Content | Main use |
|---|---:|---|---|
| `q1_respondents_8wave.csv` | 135,497 rows × 275 columns | Respondent records, survey weights, activity status, 124 comparable activity measures, geography and eligibility flags | Individual-level analysis in Notebook 02a |
| `q1_annual.csv` | 280 rows × 397 columns | Eight annual observations for London, Inner/Outer London and 32 boroughs, with activity rates and contextual variables | Annual description, borough clustering and forecasting |
| `q1_quarterly.csv` | 1,120 rows × 401 columns | Thirty-two quarters for the same 35 geographies | Quarterly trends and forecasts |
| `q1_monthly.csv` | 3,360 rows × 402 columns | Ninety-six months for the same 35 geographies | Seasonality, monthly change and forecasts |
| `q1_age_annual.csv` | 1,120 rows × 15 columns | Annual activity rates for four age bands across all geographic levels | Age comparison and standardisation |

The three panel files use `geography_level` to distinguish `London`, `InnerOuter` and `Borough` observations. Activity outcomes are stored as proportions from 0 to 1, so a value of `0.664` represents 66.4%. `effective_n` is the Kish effective sample size and should be used when comparing the precision of different geographic or time cells.

Annual estimates use the final survey weight, while monthly and quarterly estimates use the time-based survey weight. The detailed activity columns describe participation in each of the 124 activity definitions shared across all eight waves.

## Methods

- Survey-weighted activity estimates at London, Inner/Outer London and borough levels
- Monthly time-series and seasonal decomposition
- Age standardisation and respondent-level adjusted models
- Multilevel borough analysis and spatial autocorrelation
- PCA and cluster analysis with bootstrap stability checks
- Rolling-origin forecast validation with a held-out eighth survey wave
- Eight-year monthly, quarterly and annual forecasting

## Selected findings

- London Active participation increased from **64.6% to 66.4%** between the first and eighth waves. Inactive also increased from **22.2% to 23.8%**, while Fairly Active fell by 3.4 percentage points.
- Borough differences are persistent: 75.8% of residual variation in the multilevel model is between boroughs, and Year 8 Active levels show positive spatial clustering.
- The structural analysis identifies two borough groups: 21 boroughs in a lower-activity structure and 11 in a higher-activity structure.
- The annual level-and-trajectory analysis also supports two groups: 17 boroughs with a persistent lower level and 15 with a persistent higher level.
- Annual forecasts are treated as the main forecasting result, with quarterly and monthly forecasts providing supporting higher-frequency evidence.

The notebooks contain the complete diagnostics, figures, uncertainty measures and interpretation supporting these summaries.

## Environment setup

The notebooks were developed with Python 3.12.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install jupyter numpy pandas matplotlib seaborn scipy scikit-learn statsmodels patsy geopandas
jupyter lab
```

## Running the analysis

The prepared datasets are already available, so the historical analysis and forecasting can be run directly:

1. Create and activate the Python environment.
2. Open `Yifeng Mao/Q1/physical_activity_analysis/` in Jupyter.
3. Check the path-configuration cell at the start of each notebook. The notebooks use `Path.cwd()`, so the prepared-data and borough-boundary paths must match the local clone location.
4. Run `02a_multilevel_descriptive_analysis.ipynb` for the descriptive and multilevel analysis.
5. Run `02b_borough_clustering_analysis.ipynb` for the borough clustering analysis.
6. Run `03_monthly_quarterly_and_annual_forecasting.ipynb` for model comparison and future forecasts.

Notebook 01 only needs to be rerun when the five prepared datasets need to be rebuilt. Notebooks 02a, 02b and 03 read the committed prepared files directly.

The clustering and forecasting notebooks take longer to run because they repeat model fitting across candidate specifications, geographic levels and resampling iterations.

## Author

**Yifeng Mao** — multilevel physical-activity analysis, borough clustering and forecasting for Question 1.
