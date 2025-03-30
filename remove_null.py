# import pandas as pd

# def remove_all_nan_columns(df):
#     return df.loc[:, (df != 'Nan').any(axis=0)]

# def remove_all_nan_rows_from_third_col(df):
#     non_nan_rows = (df.iloc[:, 2:] != 'Nan').any(axis=1)
#     return df.loc[non_nan_rows]

# def only_all_nan_row(df):
#     return df.loc[(df == 'Nan').all(axis=1)]

# df = pd.read_csv('GWMSL_Insitu.csv')

# # df_cleaned = remove_all_nan_columns(df)

# df_cleaned = remove_all_nan_rows_from_third_col(df)

# df_cleaned = df_cleaned.applymap(lambda x: round(float(x), 2) if isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.', '', 1).isdigit()) else x)

# df_nan = only_all_nan_row(df)
# df_nan.to_csv('nan_rows.csv', index=False)

# df_cleaned.to_csv('cleaned_file.csv', index=False)


import pandas as pd


file_path = "GWMSL_Insitu.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Filter out rows where all cells (from 2nd column onward) are "Nan"
cleaned_df = df[~(df.iloc[:, 2:].eq("Nan").all(axis=1))]

# Save the cleaned data to a new CSV file
output_path = "Insitu_nan_row_removed.csv"  # Replace with desired output path
cleaned_df.to_csv(output_path, index=False)

print(f"Cleaned CSV saved to {output_path}")
