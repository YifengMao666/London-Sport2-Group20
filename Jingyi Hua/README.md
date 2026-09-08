# Physical Activity Forecasting by Age and Disability Group

This directory contains **Jingyi Hua's Research Question 2 contribution** to the London Sport 2 MSc Data Science dissertation project. It analyses eight waves of Sport England's Active Lives Adult Survey from **2015/16 to 2022/23** and examines how physical activity participation may change across age and disability groups in London.

The analysis covers overall physical activity composition, activity-specific participation, past-12-month participation and regular participation. Eight forecasting tasks are developed across the age and disability strands, with forecasts produced from **2023/24 to 2030/31**. The workflow also includes recursive backtesting, small-sample reliability checks and sensitivity analyses for longer-horizon forecasts.

## Research question

**How are physical activity levels and participation in specific activities expected to change across age and disability groups over the next eight years? Which activities are predicted to have the highest participation rates within each group?**

The analysis includes eight age groups from **16–24** to **85+**, three broad disability-status groups, 13 overlapping detailed disability indicators and **124 activities** that are comparable across all eight survey waves.

## Project structure

```text
Jingyi Hua/
├── README.md
├── data/
│   ├── codebook/
│   └── processed/
├── docs/
├── notebooks/
│   ├── 01_data_extraction.ipynb
│   ├── 02_RQ2_age_disability_aggregation.ipynb
│   ├── 03_RQ2_borough_disability_aggregation.ipynb
│   ├── 04_RQ2_borough_disability_days_months.ipynb
│   ├── 05_RQ2_pre_modeling_eda.ipynb
│   ├── 06_RQ2_modeling_pipeline_en.ipynb
│   ├── 06b_RQ2_disability_age_mixedlm.ipynb
│   ├── 06c_RQ2_smallsample_shrinkage.ipynb
│   ├── 07_RQ2_post_modeling_eda.ipynb
│   ├── 08_RQ2_disability_forecast.ipynb
│   ├── 08b_RQ2_age_forecast.ipynb
│   ├── 09_RQ2_recursive_backtesting.ipynb
│   ├── 10_RQ2_robustness_analysis.ipynb
│   └── build_125_activity_whitelist.py
└── outputs/
    ├── 05_RQ2_pre_modeling_eda/
    ├── 06_RQ2_modeling_pipeline/
    ├── 07_RQ2_post_modeling_eda/
    ├── 08_RQ2_forecasts/
    ├── 09_RQ2_recursive_backtesting/
    └── 10_RQ2_robustness_analysis/
```

## Analysis notebooks

| Notebook | Description |
|---|---|
| `01_data_extraction.ipynb` | Extracts and checks the required Active Lives variables and supporting metadata. |
| `02_RQ2_age_disability_aggregation.ipynb` | Constructs age and disability analysis inputs and checks variable availability and missingness. |
| `03_RQ2_borough_disability_aggregation.ipynb` | Builds borough-level disability activity-composition panels across survey years. |
| `04_RQ2_borough_disability_days_months.ipynb` | Constructs borough-level past-12-month and regular-participation panels. |
| `05_RQ2_pre_modeling_eda.ipynb` | Examines sample size, Kish effective sample size, temporal variation, activity concentration and subgroup sparsity before modelling. |
| `06_RQ2_modeling_pipeline_en.ipynb` | Compares Naive persistence, Ridge Regression, Random Forest and Gradient Boosting across the eight forecasting tasks using rolling-origin validation. |
| `06b_RQ2_disability_age_mixedlm.ipynb` | Provides a supplementary mixed-effects comparison for the overall age and disability outcomes. |
| `06c_RQ2_smallsample_shrinkage.ipynb` | Evaluates shrinkage for borough predictions with weaker historical sample support. |
| `07_RQ2_post_modeling_eda.ipynb` | Examines model performance by borough, age group, disability group, activity and effective sample size. |
| `08_RQ2_disability_forecast.ipynb` | Produces recursive forecasts for disability groups from 2023/24 to 2030/31. |
| `08b_RQ2_age_forecast.ipynb` | Produces age-group forecasts and predicted activity rankings. |
| `09_RQ2_recursive_backtesting.ipynb` | Evaluates historical recursive forecasting across horizons H1–H4 and compares performance with recursive Naive persistence. |
| `10_RQ2_robustness_analysis.ipynb` | Runs training-weight, ALR epsilon, COVID, residual-simulation and cross-model sensitivity analyses. |

## Forecasting tasks

RQ2 contains eight forecasting tasks. The age and disability strands each contain four outcomes: overall activity composition, activity-specific composition, past-12-month participation and regular participation.

Overall and activity-specific outcomes contain the three activity states **Inactive, Fairly Active and Active**. These are treated as compositional outcomes and evaluated using **Total Variation (TV)**. Past-12-month and regular participation are single-rate outcomes and are evaluated using **Mean Absolute Error (MAE)**.

The activity-specific analysis uses the 124 activities retained across all eight survey waves. Activity rankings are based on predicted past-12-month participation rates and therefore describe predicted participation rather than stated preferences.

## Methods

Respondent-level survey weights are used to construct annual borough and demographic panels. Raw respondent counts and the **Kish effective sample size** are retained as indicators of historical sample support. Missing or structurally unavailable responses are not automatically treated as zero participation, while valid zero values are retained when they represent genuine non-participation.

The overall and activity-specific activity-level outcomes are modelled using an **additive log-ratio (ALR) transformation**, with Active as the reference category. A zero-replacement value of `1e-6` is used in the primary analysis where a component equals zero, with `1e-4`, `1e-5` and `1e-6` compared in the numerical sensitivity analysis. Forecasts are transformed back to valid non-negative proportions that sum to one.

Four candidate forecasting approaches are compared: **Naive persistence, Ridge Regression, Random Forest and Gradient Boosting**. Naive persistence provides the benchmark for assessing whether additional model complexity improves forecasting performance.

Model family and hyperparameters are selected using four expanding-window rolling-origin validation folds. Data from 2015/16–2017/18 are used to validate on 2018/19, and the training window is then expanded one survey year at a time until validation on 2021/22. Performance is averaged across the four validation origins using the task-specific primary metric.

The **2022/23 survey wave is reserved for independent testing** and does not participate in model or hyperparameter selection. After testing, the selected specifications are refitted using the full observed history and used to generate forecasts from 2023/24 to 2030/31.

## Selected models

Rolling-origin validation selected different model families across the eight forecasting tasks.

| Task | Selected model |
|---|---|
| Age overall composition | Gradient Boosting |
| Disability overall composition | Gradient Boosting |
| Age activity composition | Random Forest |
| Disability activity composition | Gradient Boosting |
| Age past-12-month participation | Naive persistence |
| Disability past-12-month participation | Ridge Regression |
| Age regular participation | Naive persistence |
| Disability regular participation | Gradient Boosting |

Gradient Boosting was selected for four tasks, Naive persistence for two, Random Forest for one and Ridge Regression for one. The result shows that no single model was preferred across every outcome, while more complex models were retained only when rolling-origin validation supported them.

## Recursive forecasting and reliability checks

The final forecasts are generated recursively. Once observed lagged outcomes are no longer available, the prediction from one future survey year is reused to construct the inputs required for the following year.

Historical recursive backtesting evaluates this process over directly observable horizons **H1–H4**. These backtests provide direct evidence on multi-step forecast behaviour over the first four horizons, while H5–H8 extend beyond the historically testable range and depend more strongly on model-generated inputs and the continuation of historical relationships.

Small-sample reliability is examined using raw sample size and Kish effective sample size. A supplementary shrinkage analysis adjusts predictions with weaker historical support towards a leave-one-borough-out London reference. The shrinkage strength is selected from `{0, 2, 5, 10, 20}` using rolling validation while keeping the underlying forecasting specification fixed.

The robustness analysis also compares alternative training weights, ALR zero-replacement values and COVID-indicator specifications. Five hundred residual-based recursive simulation paths are used as an additional sensitivity check. Their 5th–95th percentile ranges are treated as indicative sensitivity bands.

A separate cross-model comparison examines longer-horizon trajectories under Ridge Regression, Random Forest, Gradient Boosting and Naive persistence. This analysis focuses on the 85+ Active-rate trajectory and the gap between the no-disability and limiting-disability groups.

## Selected findings

The largest independent-test improvement over Naive occurred for **disability activity composition**, where the primary test error was reduced by **29.1%**. Disability overall composition improved by **26.2%**, while age overall composition improved by **21.4%**. Age activity composition selected Random Forest and reduced the primary test error by approximately **15.4%** relative to Naive.

Both age single-rate tasks were best represented by Naive persistence under rolling-origin validation. This indicates that the available annual history did not provide enough additional predictive structure for the fitted alternatives to improve consistently on persistence for these outcomes.

Historical recursive backtesting showed controlled forecast error across the directly testable H1–H4 horizons for the main compositional tasks. The later forecast years remain less directly supported because they extend beyond the historical backtest range.

The production forecasts show relatively stable Active rates for most age groups, while the oldest age groups remain at lower predicted levels. The limiting-disability group also remains below the no-disability group in the selected production forecasts.

**Active Travel** and **Gardening** frequently appear among activities with high predicted past-12-month participation. These rankings are interpreted carefully when the two leading predicted participation rates are close.

Cross-model comparison shows that the exact longer-term direction of the 85+ Active-rate trajectory and the disability gap is sensitive to model specification. The longer-horizon results are therefore interpreted more carefully than the relative demographic patterns observed within the selected production forecasts.

## Outputs

The outputs are organised according to the notebooks.

`05_RQ2_pre_modeling_eda/` contains the pre-model exploratory analysis, including sample-size structure, Kish effective sample size, temporal volatility, activity concentration, disability co-occurrence, outcome relationships and borough-level variation.

`06_RQ2_modeling_pipeline/` contains the main model-selection outputs, including validation summaries, independent-test results and selected hyperparameters.

`07_RQ2_post_modeling_eda/` contains model diagnostics, including model comparisons, borough-level forecasting errors, error against effective sample size, subgroup-specific errors, residual distributions and feature-importance outputs.

`08_RQ2_forecasts/` contains the age and disability forecasts from 2023/24 to 2030/31, including overall activity composition, activity-specific composition, past-12-month participation, regular participation and predicted activity rankings.

`09_RQ2_recursive_backtesting/` contains the historical recursive evaluation across H1–H4, including results by forecast horizon and forecast origin, recursive Naive comparisons and supporting figures and tables.

`10_RQ2_robustness_analysis/` contains training-weight sensitivity, ALR epsilon sensitivity, COVID-indicator sensitivity, residual-based recursive simulation and cross-model longer-horizon comparisons.

## Environment setup

The notebooks were developed in Python using Jupyter.

The main packages used in the RQ2 workflow are:

- pandas
- NumPy
- SciPy
- scikit-learn
- statsmodels
- pyreadstat
- Matplotlib
- Seaborn
- openpyxl

A typical environment can be created with:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install jupyter pandas numpy matplotlib seaborn scipy scikit-learn statsmodels pyreadstat openpyxl
jupyter lab
```

## Running the analysis

The notebooks are intended to be run in numerical order because later stages use datasets or outputs produced by earlier stages.

Notebooks 01–04 prepare and aggregate the required age and disability datasets. Notebook 05 performs the pre-model exploratory analysis. Notebook 06 runs the main model-selection and independent-test pipeline, while Notebooks 06b and 06c provide supplementary mixed-effects and small-sample analyses.

Notebook 07 evaluates the fitted models in greater detail. Notebooks 08 and 08b generate the disability and age forecasts. Notebook 09 performs the historical recursive backtesting, and Notebook 10 contains the final robustness and sensitivity analyses.

Some notebooks contain local path-configuration cells. These paths should be checked after cloning or moving the repository. The model-selection, recursive-backtesting and robustness notebooks may take longer to run because they repeat model fitting across multiple tasks, validation origins and model specifications.

## Data access

The repository contains processed analysis files and Active Lives supporting documentation used by the RQ2 workflow.

The original respondent-level Active Lives survey files are not distributed in this directory. Access to the source data is subject to the original terms of Sport England and the UK Data Service. Users who wish to reproduce the full workflow from the original survey files should obtain the relevant datasets separately and update the corresponding input paths in the extraction notebooks.

## Limitations

The analysis uses eight annual survey waves and produces forecasts over a further eight survey years. Historical recursive backtesting directly evaluates only H1–H4, so empirical support is stronger for the earlier forecast horizons than for the final years of the projection.

Some borough-by-demographic cells have limited historical sample support, particularly among the oldest age groups and the detailed disability indicators. Kish effective sample size and supplementary shrinkage analyses help identify and assess these cases, but they cannot create additional information where the underlying sample is sparse.

Active Lives is a repeated cross-sectional and self-reported survey. The forecasts therefore describe population-level patterns across survey waves and should not be interpreted as individual longitudinal trajectories or causal effects.

Longer-horizon forecasts also become more dependent on the selected model family and recursively generated inputs. The projections should therefore be treated as **conditional model-based forecasts** and updated as new Active Lives survey waves become available.

## Author

**Jingyi Hua** — age and disability physical-activity forecasting, recursive evaluation, small-sample reliability analysis, activity ranking and robustness assessment for Research Question 2 of the London Sport 2 MSc Data Science dissertation project.