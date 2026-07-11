import pyreadstat
import pandas as pd

file_path = " "

df, meta = pyreadstat.read_sav(
    file_path,
    #row_limit=1000
    metadataonly=True
)

"""
print(df.shape)
print(df.head())
df.to_csv(
    "active_lives_survey_year6_example.csv",
    index=False
)

"""
rows = []

for name, label in zip(
    meta.column_names,
    meta.column_labels
):

    value_info = ""

    if name in meta.variable_value_labels:

        labels = meta.variable_value_labels[name]

        value_info = "; ".join(
            [
                f"{k}={v}"
                for k, v in labels.items()
            ]
        )

    rows.append([
        name,
        label,
        value_info
    ])

dictionary = pd.DataFrame(
    rows,
    columns=[
        "variable_name",
        "variable_label",
        "value_labels"
    ]
)


dictionary.to_excel(
    "full_variable_dictionary_year6.xlsx",
    index=False
)
