# Problem Statement
Can the new quantitative trading strategies of hedge funds still work next week?

# Stakeholder Persona
Fund manager: Concerned about the actual performance of the new quantitative strategy next week (such as yield, volatility), whether it can respond to market changes, and whether potential risks are controllable.

High-net-worth individuals or institutional investors: Focus on whether the strategy can bring expected returns, the risk level of their own investments, and the information transparency of the fund.

# Data Acquisition
- Data source: Wikipedia (https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal))
- Method: Legal web scraping using pandas.read_html()
- Output: Saved as CSV in /data/raw/countries_gdp.csv
- Notebook: /notebooks/scraping_demo.ipynb

# Data Storage
- Data is organized into two folders:
  - /data/raw/: unmodified data from external sources
  - /data/processed/: cleaned and transformed data ready for analysis
- File formats:
  - CSV is used for portability
  - Parquet may also be used for efficient storage
- File access:
  - Paths are handled via environment variables (see .env.example)
  - Example variables:
      RAW_PATH=./data/raw/countries_gdp.csv
      PROCESSED_PATH=./data/processed/countries_gdp_clean.csv
- Code examples:
  - Load raw data:
    ```python
    import pandas as pd, os
    df = pd.read_csv(os.getenv("RAW_PATH"))
    ```
  - Load processed data:
    ```python
    df_clean = pd.read_csv(os.getenv("PROCESSED_PATH"))
    ```
