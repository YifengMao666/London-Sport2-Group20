# RQ4: Frequent Sport Volunteering in London

**Research Question:**  
How will frequent sport-volunteering rates change over the next six years across London boroughs, age groups, and activity-level groups? Does the forecast gap between activity-level groups vary by age?

**Author: Shuhan Zhao**

This folder contains my main contributions to the London Sport 2 project.

My primary work is Research Question 4 (RQ4), which analyses and forecasts frequent sport volunteering across London boroughs, age groups, and activity-level groups.

The folder also contains data preprocessing work used in the wider project, especially for RQ2 and RQ4.

## Folder Structure

### `volunteer_analysis`

This folder contains the main analysis for RQ4.

#### `q4_volfreq_dataset.ipynb`

Prepares the datasets used in the RQ4 analysis.

Main tasks:
- combines six Active Lives survey waves from 2017/18 to 2022/23;
- harmonises the volunteering target, age groups, activity levels, boroughs, and survey weights;
- calculates survey-weighted frequent sport-volunteering rates;
- calculates Kish effective sample size and sample-support indicators;
- creates three complete historical panels:
  - borough × activity level;
  - borough × age;
  - borough × age × activity level.

Generated datasets and diagnostics are stored in `q4_dataset_outputs`.

#### `q4_historical_descriptive_analysis.ipynb`

Explores historical frequent sport-volunteering patterns before forecasting.

Main tasks:
- examines historical differences across age and activity-level groups;
- summarises annual borough-level volunteering rates;
- examines historical changes within boroughs;
- compares Active, Fairly Active, and Inactive groups;
- analyses age-specific activity-level gaps;
- produces historical tables and figures.

Outputs are stored in `q4_historical_outputs`.

#### `q4_model_comparison.ipynb`

Selects and evaluates forecasting models for RQ4.

Four model families are compared:
- Naive baseline;
- Ridge Regression;
- Random Forest;
- Gradient Boosting.

The notebook evaluates three forecasting tasks:
- borough × activity level;
- borough × age;
- borough × age × activity level.

Model and hyperparameter selection uses expanding rolling-origin validation.  
The final 2022/23 wave is kept as an independent test set.

The main evaluation measure is effective-sample-size-weighted MAE.

Model-selection results and diagnostics are stored in `q4_model_comparison_outputs`.

#### `q4_future_forecasting.ipynb`

Generates the final RQ4 forecasts and evaluates their robustness.

Main tasks:
- refits the selected models using all historical waves;
- produces recursive forecasts for 2023/24 to 2028/29;
- summarises forecasts by age and activity level;
- calculates age-specific Active–Inactive and Fairly Active–Inactive gaps;
- compares historical and forecast subgroup patterns;
- performs historical recursive backtesting;
- compares alternative model families as a sensitivity check;
- produces the final forecast tables and figures.

Outputs are stored in `q4_future_forecasting_outputs`.

### `code`

Contains data preprocessing scripts and notebooks used to prepare and harmonise Active Lives survey data for the project.

This work mainly supports RQ2 and RQ4, including variable selection, cross-year harmonisation, and construction of analysis-ready datasets.

### `docs`

Contains processed datasets and intermediate outputs created during data preprocessing.

These files support the later modelling and analysis stages.

## RQ4 Workflow

The main RQ4 notebooks should be read in the following order:

1. `q4_volfreq_dataset.ipynb`
2. `q4_historical_descriptive_analysis.ipynb`
3. `q4_model_comparison.ipynb`
4. `q4_future_forecasting.ipynb`

## Note

Some output files retain the earlier `q5` prefix from the development stage of the project. These files belong to the final RQ4 analysis.
