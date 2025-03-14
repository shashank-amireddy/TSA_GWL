import pandas as pd

def remove_all_nan_columns(df):
    return df.loc[:, (df != 'Nan').any(axis=0)]

def remove_all_nan_rows_from_third_col(df):
    non_nan_rows = (df.iloc[:, 2:] != 'Nan').any(axis=1)
    return df.loc[non_nan_rows]

df = pd.read_csv('GWMSL_Insitu.csv')

df_cleaned = remove_all_nan_columns(df)

df_cleaned = remove_all_nan_rows_from_third_col(df_cleaned)

df_cleaned = df_cleaned.applymap(lambda x: round(float(x), 2) if isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.', '', 1).isdigit()) else x)

df_cleaned.to_csv('cleaned_file.csv', index=False)
