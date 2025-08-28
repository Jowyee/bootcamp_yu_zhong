# 1. Project Overview and Objectives
This project focuses on the core question: Can the new quantitative trading strategies of hedge funds still work next week?  Its primary objectives are to analyze the effectiveness and sustainability of the new quantitative trading strategies, predict their performance (e.g., yield, volatility) in the upcoming week, evaluate their ability to respond to market changes, and assess the controllability of potential risks. The project aims to provide data-driven insights for fund managers and investors, while organizing the research process into a standardized, reusable, and handoff-ready repository structure .


# 2. How to Rerun Scripts/Notebooks
## 2.1 Environment Preparation
- 1. Clone the project repository to your local machine using the following command:
```
git clone [Your GitHub Repository URL]
cd [Local Repository Path]
```
- 2. Ensure you are using Python 3.7 or a higher version. Install the required dependencies via the requirements.txt file (included in the repository root directory) with:
```
pip install -r requirements.txt
```
This file includes essential libraries such as pandas (for data processing), requests (for potential API calls), and other tools needed for strategy analysis and model operation .

## 2.2 Data Preparation
- 1. Data Source and Acquisition: The project uses GDP data from Wikipedia (https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)) as a key input for market environment analysis. Run the /notebooks/scraping_demo.ipynb notebook to legally scrape data using pandas.read_html() .
- 2. Data Storage Check: After running the scraping notebook, confirm that the raw data is saved as countries_gdp.csv in the /data/raw/ directory. If the file is missing, re-execute the data scraping cells in scraping_demo.ipynb.
- 3. Processed Data Generation: Run the relevant data cleaning notebook (e.g., /notebooks/data_cleaning.ipynb, to be created based on project needs) to clean and transform the raw data. The processed data will be saved to the /data/processed/ directory (e.g., as countries_gdp_clean.csv) for subsequent strategy analysis.

## 2.3 Rerun Sequence
- 1. First, execute /notebooks/scraping_demo.ipynb to acquire and store raw GDP data in /data/raw/.
- 2. Next, run the data cleaning notebook (e.g., /notebooks/data_cleaning.ipynb) to generate processed data in /data/processed/.
- 3. Then, execute the quantitative strategy analysis notebook (e.g., /notebooks/strategy_analysis.ipynb) to analyze the strategy’s effectiveness and predict next week’s performance using the processed data.
- 4. (If applicable) Run the API script (app.py in the repository root) via the terminal command python app.py to start the Flask service, enabling access to strategy prediction results through API endpoints .


# 3. Assumptions, Risks, and Lifecycle Mapping
## 3.1 Assumptions
- 1. Data Relevance: The GDP data from Wikipedia (used to analyze the macro market environment) is assumed to have a valid correlation with the performance of the hedge fund’s quantitative trading strategies. If this correlation is weaker than expected, the analysis results may deviate from actual strategy performance.
- 2. Data Availability: The Wikipedia page (https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)) is assumed to be accessible during data scraping, and its structure (e.g., table format, column names) remains unchanged. Changes to the page structure may cause pandas.read_html() to fail or scrape incorrect data.
- 3. Environment Consistency: The environment variables for data paths (e.g., RAW_PATH=./data/raw/countries_gdp.csv, PROCESSED_PATH=./data/processed/countries_gdp_clean.csv) are assumed to be correctly configured by referring to .env.example. Incorrect path configurations will prevent successful data loading .

## 3.2 Risks
- 1. Data Quality Risk: The scraped GDP data may contain missing values, outliers, or outdated information (e.g., unupdated 2024 GDP figures). This will affect the accuracy of market environment analysis and further distort strategy performance predictions.
- 2. Strategy Adaptability Risk: The quantitative trading strategy may be overly dependent on historical market patterns reflected in the current dataset. If the market undergoes sudden changes (e.g., policy adjustments, geopolitical events) next week, the strategy may fail to adapt, leading to inaccurate predictions.
- 3. Technical Risk: Dependencies in requirements.txt may have version conflicts (e.g., incompatible pandas and numpy versions), causing notebooks or scripts to crash during execution. Additionally, network issues during repository cloning or dependency installation may delay the rerun process .

## 3.3 Lifecycle Mapping

# 4. Instructions for Using APIs or Dashboards
## 4.1 API Usage (If Applicable)
### 4.1.1 API Endpoints

### 4.1.2 API Call Example (Python)
```
import requests

# Call POST /predict_strategy to get next-week strategy performance prediction
url = "http://localhost:5000/predict_strategy"
input_data = {"gdp_growth_rate": 2.5, "market_volatility_index": 18}
response = requests.post(url, json=input_data)
print("Prediction Result:", response.json())

# Call GET /plot_strategy_performance to save the performance chart
plot_url = "http://localhost:5000/plot_strategy_performance"
plot_response = requests.get(plot_url)
with open("./strategy_performance_chart.png", "wb") as f:
    f.write(plot_response.content)
print("Performance chart saved successfully")
```
### 4.1.3 Error Handling
- If the POST request is missing required input features (e.g., no "gdp_growth_rate" provided), the API will return a 400 error with JSON: {"error": "Missing required feature: gdp_growth_rate"}.
- If the input data type is invalid (e.g., "market_volatility_index" is a string like "high" instead of a number), the API will return a 400 error with JSON: {"error": "Invalid type for feature market_volatility_index: expected int/float"}.
- If the API service is not started (i.e., app.py is not run), a "Connection refused" error will occur. Ensure the Flask service is active before calling the API .

## 4.2 Dashboard Usage (Optional, If Developed)
If a Streamlit/Dash dashboard is built for the project:
- 1. Launch Method: For Streamlit, run streamlit run dashboard.py in the terminal; for Dash, run python dashboard.py. After successful launch, access the dashboard via the provided URL (e.g., http://localhost:8501).
- 2. Key Functions:
  - Input Area: Allow users to enter parameters such as GDP growth rate and market volatility index to customize prediction conditions.
  - Visualization Area: Display the strategy’s historical performance trends, next-week yield/volatility predictions, and risk level assessments.
  - Information Area: Show explanations of the strategy’s core logic and data sources for stakeholder reference.
- 3. Error Tips: If invalid inputs are entered (e.g., GDP growth rate < -10 or > 20), the dashboard will pop up a red warning box prompting users to correct the input range .


# 5. Stakeholder-Ready Summary Reference
The stakeholder-ready summary (in PDF/slide format, stored in /reports/stakeholder_summary.pdf) focuses on the following core content for different stakeholder personas:
- For Fund Managers: Highlight the predicted next-week performance of the new quantitative strategy (including yield range and volatility), analyze the strategy’s ability to respond to potential market changes (e.g., how it adjusts to GDP fluctuations), and provide risk control suggestions (e.g., setting stop-loss thresholds).
- For High-Net-Worth Individuals/Institutional Investors: Clarify the strategy’s expected return range, compare it with market benchmarks, explain the risk level of investments (e.g., maximum potential drawdown), and disclose key data sources (e.g., Wikipedia GDP data) and analysis methods to ensure information transparency .

# 6. Project File Structure
```
[Repository Root Directory]
├── data/                # Data directory (meets clean folder structure requirements)
│   ├── raw/             # Unmodified raw data from external sources
│   │   └── countries_gdp.csv  # Raw GDP data scraped from Wikipedia
│   └── processed/       # Cleaned, transformed data for analysis
│       └── countries_gdp_clean.csv  # Processed GDP data
├── notebooks/           # Jupyter notebooks directory
│   ├── scraping_demo.ipynb  # Notebook for data scraping (GDP data from Wikipedia)
│   ├── data_cleaning.ipynb  # Notebook for raw data cleaning/transformation
│   └── strategy_analysis.ipynb  # Notebook for quantitative strategy analysis and prediction
├── src/                 # Directory for reusable code (modularized functions)
│   └── strategy_utils.py  # Reusable functions (e.g., strategy performance calculation, data validation)
├── model/               # Directory for saved models (if strategy uses predictive models)
│   └── strategy_model.pkl  # Pickled model for strategy performance prediction
├── reports/             # Directory for reports
│   └── stakeholder_summary.pdf  # Stakeholder-ready summary (PDF)
├── app.py               # Flask API script (for exposing strategy prediction endpoints)
├── dashboard.py         # Optional: Streamlit/Dash dashboard script
├── requirements.txt     # Dependencies list for reproducibility
├── .env.example         # Example of environment variables (for data path configuration)
└── README.md            # Project description document (this file)
└── {insert\_element\_12\_}
```
