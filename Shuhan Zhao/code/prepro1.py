from pathlib import Path
import pandas as pd
import pyreadstat


LONDON_32_LA_2023_VALUES = [
    8, 9, 17, 30, 35, 44, 68, 78,
    91, 107, 109, 112, 114, 117, 122, 126,
    129, 135, 136, 139, 142, 147, 160, 171,
    196, 201, 241, 255, 272, 279, 280, 293
]


def build_keep_columns(all_columns):

    exact_vars = [
        "LA_2023",
        "Reg9",
        "LondInOut",
        "Age16plus",
        "Age9",
        "Disab3",
        "VolAny",
        "VolFrqB_Pop",
        "mode",
        "serial",
        "Number_Activities_150",
        "month",
    ]

    disty_vars = [f"disty{i}_POP" for i in range(1, 14)]

    volint_vars = [f"volint{i}" for i in range(1, 8)]

    activity_prefixes = [
        "MEMS7",
        "MEMS7GR",
        "INOUTA",
        "INOUTB",
        "DAYS10P60GR",
        "MONTHS_12",
    ]

    exact_keep = exact_vars + disty_vars + volint_vars

    activity_vars = [
        col for col in all_columns
        if any(col.startswith(prefix + "_") for prefix in activity_prefixes)
    ]

    weight_vars = [
        col for col in all_columns
        if col.startswith("wt_")
    ]

    target_vars = set(exact_keep + activity_vars + weight_vars)

    keep_columns = [
        col for col in all_columns
        if col in target_vars
    ]

    missing_exact_vars = [
        var for var in exact_keep
        if var not in all_columns
    ]

    return keep_columns, missing_exact_vars


def filter_london_32_boroughs(df):

    if "LA_2023" not in df.columns:
        raise ValueError("No LA_2023")

    df_london = df[df["LA_2023"].isin(LONDON_32_LA_2023_VALUES)].copy()

    return df_london


def preprocess_active_lives_sav(sav_path, output_path, survey_year):

    sav_path = Path(sav_path)
    output_path = Path(output_path)

    _, metadata = pyreadstat.read_sav(sav_path, metadataonly=True)
    all_columns = metadata.column_names

    keep_columns, missing_exact_vars = build_keep_columns(all_columns)

    if missing_exact_vars:
        print("No these variables in the sav file")
        for var in missing_exact_vars:
            print(f"  - {var}")

    print(f"raw variables：{len(all_columns)}")
    print(f"reserved variables：{len(keep_columns)}")

    df, metadata = pyreadstat.read_sav(
        sav_path,
        usecols=keep_columns,
        apply_value_formats=False
    )

    df = filter_london_32_boroughs(df)

    df["year"] = survey_year

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Saved：{output_path}")

    return df

df_19_20 = preprocess_active_lives_sav(
    sav_path = "/Users/zsh/Downloads/PROJECT/data/UKDA-8899-spss/spss/spss28/active_lives_survey_nov_19-20_data_year_5_shared_20250103.sav",
    output_path = "/Users/zsh/Downloads/PROJECT/code/1920_london32.csv",
    survey_year = "19_20"
)

print(df_19_20.shape)
print(df_19_20["LA_2023"].nunique())