# Cleaning Strategy

This project applies a three–step preprocessing workflow implemented in src/cleaning.py:

## 1.Handling Missing Values
  - Columns with more than 50% missing values are dropped using drop_missing(df, threshold=0.5).
    Rationale: highly sparse columns contribute little useful information and may distort analysis.
  - Remaining numeric columns with missing values are imputed with their median using fill_missing_median(df, columns).
    Rationale: the median is robust to outliers and provides a stable central tendency.

## 2.Normalization
  - Selected numeric columns are normalized to the [0, 1] range using normalize_data(df, columns).
  - Rationale: normalization ensures comparability across features, prevents features with large scales from dominating, and improves performance of models sensitive to feature magnitude.

## 3.Assumptions
  - Numeric fields (e.g., ages, counts, continuous measures) are assumed to be non–negative.
  - Categorical/text columns are left unchanged and not normalized.
  - Columns with more than 50% missingness are considered uninformative and removed.

# Folder Organization
  - Raw data: Stored in data/raw/ exactly as provided.
  - Processed data: Cleaned datasets are saved in data/processed/ in CSV or Parquet format, ensuring reproducibility and consistency for downstream analysis.