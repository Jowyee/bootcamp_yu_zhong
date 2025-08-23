def detect_outliers_iqr(series):
    """
    Detect outliers using IQR rule.
    Returns a boolean mask.
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (series < lower) | (series > upper)


def detect_outliers_zscore(series, threshold=3.0):
    """
    Detect outliers using Z-score rule.
    Returns a boolean mask.
    """
    mean = series.mean()
    std = series.std()
    z = (series - mean) / std
    return z.abs() > threshold


def winsorize_series(series, lower=0.05, upper=0.95):
    """
    Winsorize series by capping at quantiles.
    Returns a modified series.
    """
    low_val = series.quantile(lower)
    high_val = series.quantile(upper)
    return series.clip(low_val, high_val)
