# Product Sales Forecasting

## Project Overview
Predict future product sales for stores using historical data, store metadata (type, location, region), and temporal features (date, holidays, discounts). This project contains EDA, hypothesis testing, machine learning models and a Flask API for prediction.

## Dataset
Source: Provided dataset (link given by course). Key columns: `Store_id`, `Store_Type`, `Location_Type`, `Region_Code`, `Date`, `Holiday`, `Discount`, `#Order`, `Sales`.

## Target Metric
Primary metrics used to evaluate models:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R²

## Repo Structure
product-sales-forecasting/
├─ notebooks/Product_Sales_Forecasting_Colab.ipynb
├─ deployment/app.py
├─ deployment/requirements.txt
├─ data/
├─ models/sales_forecast_model.pkl
├─ README.md


## How to run (Colab)
1. Open the notebook `Product_Sales_Forecasting_Colab.ipynb` in Google Colab.
2. Upload the training file.
3. Run cells sequentially. The notebook performs cleaning, EDA, hypothesis tests (t-tests, ANOVA), trains RandomForest and Linear Regression baselines, shows metrics, and saves the RF model to `models/sales_forecast_model.pkl`.

## Model & Results
- **RandomForestRegressor** (n_estimators=200) — best performing model during baseline testing.
- Example final metrics (your run may vary):  
  - MAE: *e.g.* 1932.78
  - RMSE: *e.g.* 2922.09  
  - R²: *e.g.* 0.97

## Deployment
1. Install dependencies: `pip install -r deployment/requirements.txt`.
2. Run API: `python deployment/app.py`.
3. POST sample JSON to `http://127.0.0.1:5000/predict`:
```json
{
  "Store_id": 1,
  "Store_Type": "TypeA",
  "Location_Type": "Urban",
  "Region_Code": "R1",
  "Discount": "No",
  "Holiday": 0,
  "#Order": 10,
  "Year": 2025,
  "Month": 2,
  "Day": 15
}
