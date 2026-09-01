# Q3 revised workflow

## Chronological validation

The workflow uses three expanding-window rolling-origin validation folds:

1. train on 2017/18--2018/19 and validate on 2019/20;
2. train on 2017/18--2019/20 and validate on 2020/21;
3. train on 2017/18--2020/21 and validate on 2021/22.

Candidate models and hyperparameters are ranked using the mean weighted Total
Variation (TV) and mean weighted MAE across all three folds. TV measures the
probability mass assigned to the wrong parts of the four-category composition;
MAE gives the typical indoor/outdoor-rate error in percentage-point units. The model with
the lowest mean of the two metric ranks is selected. Only after selection is it
refitted through 2021/22 and evaluated once on the untouched 2022/23 test wave.

## Outcome definitions

The mutually exclusive outcome is: neither recorded, indoor only, outdoor only,
or both. "Neither recorded" does not mean physically inactive. It means that no
qualifying comparable activity had an indoor or outdoor location flag. The code
separates respondents with no qualifying activity from respondents who reported
a qualifying activity but had no recorded indoor/outdoor location.

Indoor exposure is `(indoor only + both) / (indoor only + outdoor only + 2*both)`.
It is an exposure-balance measure, not the proportion of people participating
indoors. A respondent in "both" contributes one indoor and one outdoor exposure.

## Missing values and valid zeroes

CSV blanks, non-numeric entries and codes outside each variable's legal set are
converted to pandas `NaN`; they are not converted to Python `None` and they are
not imputed. Legal zeroes remain zero. A zero in Months or Days therefore does
not satisfy the qualifying-participation rule, while zero in a location flag
means that location was not recorded for that activity.

## ALR and sensitivity analysis

The four probabilities are modelled through the additive log-ratio (ALR)
transform, using `both` as the reference component. Structural/sample zeroes are
replaced by epsilon before taking logarithms. The primary epsilon is 10^-6 to
minimise perturbation while keeping logarithms finite; 10^-4 and 10^-5 are
evaluated with the same model specification. Partial-pooling strengths are also
compared against weaker and stronger alternatives. Hyperparameters are treated
as candidate intensity parameters and are chosen only by rolling-origin CV.

## Forecast and COVID interpretation

The selected models are refitted on all observations from 2017/18--2022/23 and
produce recursive forecasts for every wave from 2023/24 through 2028/29. The
`persistent_legacy` and `legacy_recovery` scenarios quantify how future results
change when post-COVID controls continue or are set to zero. Their difference is
a scenario sensitivity range, not a causal estimate or confidence interval.
