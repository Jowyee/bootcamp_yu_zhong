import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean DataFrame column names by:
    - Stripping leading/trailing whitespace
    - Converting to lowercase
    - Replacing spaces with underscores

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe with cleaned column names.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


# Example usage
if __name__ == "__main__":
    sample_df = pd.DataFrame({"First Name": [1, 2], " Age ": [25, 30]})
    print("Before:", sample_df.columns.tolist())
    clean_df = clean_column_names(sample_df)
    print("After:", clean_df.columns.tolist())
