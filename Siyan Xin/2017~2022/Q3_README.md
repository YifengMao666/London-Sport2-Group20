# Q3 Run Instructions

## Files

- `q3_indoor_outdoor_forecasting.ipynb`: Complete Jupyter Notebook execution code.
- `q3_outputs/`: All results obtained from re-running the workflow with the 6 full CSVs and `179.xlsx`.

## Input Files

Place the following files in the same input directory:

1. `2017_data_179_activities.csv`
2. `2018_data_179_activities.csv`
3. `1920_london32_stable179.csv`
4. `2021_london32_stable179.csv`
5. `year7_179activities.csv`
6. `year8_179activities.csv`
7. `179.xlsx`

## Specifications & Alignment

1. Three-fold expanding-window rolling-origin CV uses explicit wave years: 2017/18–2018/19 → 2019/20, 2017/18–2019/20 → 2020/21, and 2017/18–2020/21 → 2021/22; 2022/23 is reserved strictly for final testing.
2. Model selection is based on the average rank across the three folds of mean weighted Total Variation (TV) and indoor/outdoor weighted MAE; the final test set does not participate in model selection.
3. `algorithm_specifications.csv` and `METHODS_README.md` explain Naive, Ridge, Random Forest, Gradient Boosting, and their candidate hyperparameters.
4. The four-part compositional outcome is modelled via additive log-ratio (ALR) transformation, using a primary analysis epsilon of `1e-6` alongside comparative evaluations at `1e-4`, `1e-5`, and `1e-6`.
5. `alr_epsilon_sensitivity.csv` and `partial_pooling_sensitivity.csv` record numerical choices and sensitivity analyses; model intensity parameters are determined by rolling CV.
6. Outputs include yearly forecasts from 2023/24 through 2028/29, providing two distinct COVID scenarios: persistent legacy and legacy recovery.
7. `neither_recorded` is split into "no qualifying comparable activity" and "reported qualifying activity but no indoor/outdoor location recorded"; indoor exposure is not interpreted as the proportion of indoor participants.
8. CSV blanks, non-numeric entries, and illegal codes are converted to pandas `NaN` (not Python `None`) without imputation; legal zero values are retained and processed according to "no / did not occur" participation logic.

For detailed methodological explanations, refer to `q3_outputs/METHODS_README.md`; for the complete execution audit, see `q3_outputs/run_audit.json`.