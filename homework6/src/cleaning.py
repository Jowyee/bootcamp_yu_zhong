def fill_missing_median(df, columns):
    """
    Fill missing values in given columns with their median.
    """
    for col in columns:
        median = df[col].median()
        df[col] = df[col].fillna(median)
    return df

def drop_missing(df, threshold=0.5):
    """
    Drop columns where more than threshold fraction of values are missing.
    """
    return df.loc[:, df.isnull().mean() < threshold]

def normalize_data(df, columns):
    """
    Normalize given columns to [0,1] range.
    """
    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    return df
