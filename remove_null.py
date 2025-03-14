import pandas as pd

def remove_all_nan_columns(df):
    """Remove columns where all values are the string 'Nan'."""
    return df.loc[:, (df != 'Nan').any(axis=0)]

def remove_all_nan_rows_from_third_col(df):
    """Remove rows where all values are 'Nan' starting from the 3rd column (1-indexed)."""
    non_nan_rows = (df.iloc[:, 2:] != 'Nan').any(axis=1)  # Check from the 3rd column onward
    return df.loc[non_nan_rows]

# Load your data into a DataFrame
df = pd.read_csv('GWMSL_Insitu.csv')

# Remove columns where all values are "Nan"
df_cleaned = remove_all_nan_columns(df)

# Remove rows where all values are "Nan" starting from the 3rd column
df_cleaned = remove_all_nan_rows_from_third_col(df_cleaned)

# Save the cleaned DataFrame to a new file
df_cleaned.to_csv('cleaned_file.csv', index=False)


#final code