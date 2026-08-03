from pathlib import Path
import pandas as pd


ACTIVITY_PREFIXES = [
    "MEMS7",
    "MEMS7GR",
    "INOUTA",
    "INOUTB",
    "DAYS10P60GR",
    "MONTHS_12",
]

EXTRA_ACTIVITY_COLUMNS = [
    "MEMS7_ALL",
    "MEMS7GR_ALL",
]

def read_stable_suffixes(stable_path):
    stable_df = pd.read_excel(
        stable_path,
        sheet_name="Stable composites"
    )

    suffixes = (
        stable_df.iloc[:, 0]
        .dropna()
        .astype(str)
        .str.strip()
        .tolist()
    )

    return suffixes


def get_activity_prefix(column_name):
    for prefix in ACTIVITY_PREFIXES:
        if column_name.startswith(prefix + "_"):
            return prefix

    return None


def matches_stable_suffix(column_name, stable_suffixes):
    prefix = get_activity_prefix(column_name)

    if prefix is None:
        return False

    rest = column_name[len(prefix) + 1:]

    return rest in stable_suffixes


def filter_stable_activity_columns(input_path, stable_path, output_path):
    input_path = Path(input_path)
    stable_path = Path(stable_path)
    output_path = Path(output_path)

    df = pd.read_csv(input_path)

    stable_suffixes = read_stable_suffixes(stable_path)

    keep_columns = []

    for col in df.columns:
        prefix = get_activity_prefix(col)

        if prefix is None:
            keep_columns.append(col)
        elif col in EXTRA_ACTIVITY_COLUMNS:
            keep_columns.append(col)
        elif matches_stable_suffix(col, stable_suffixes):
            keep_columns.append(col)

    filtered_df = df[keep_columns].copy()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    filtered_df.to_csv(output_path, index=False)

    activity_kept = [
        col for col in filtered_df.columns
        if get_activity_prefix(col) is not None
    ]

    non_activity_kept = [
        col for col in filtered_df.columns
        if get_activity_prefix(col) is None
    ]

    print(
        f"Done: {len(filtered_df)} rows, "
        f"{len(activity_kept)} activity columns kept, "
        f"{len(filtered_df.columns)} columns total"
    )

    print(f"Non-activity columns kept: {len(non_activity_kept)}")
    for col in non_activity_kept:
        print(f"{col}")

    print("Activity columns kept by prefix:")
    for prefix in ACTIVITY_PREFIXES:
        count = sum(
            get_activity_prefix(col) == prefix
            for col in activity_kept
        )
        print(f"{prefix}: {count}")

    return filtered_df

df_19_20_stable = filter_stable_activity_columns(
    input_path="/Users/zsh/Downloads/PROJECT/code/2021_london32.csv",
    stable_path="/Users/zsh/Downloads/stable_activity_composites_year3_to_year8.xlsx",
    output_path="/Users/zsh/Downloads/PROJECT/code/2021_london32_stable179.csv"
)

print(df_19_20_stable.shape)