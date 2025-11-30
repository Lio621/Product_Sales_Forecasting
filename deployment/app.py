from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

MODEL_PATH = "models/sales_forecast_model.pkl"
model = joblib.load(MODEL_PATH)

# Expected feature order and column names must match training
EXPECTED_FIELDS = ["Store_id","Store_Type","Location_Type","Region_Code","Discount","Holiday","#Order","Year","Month","Day"]

@app.route('/')
def home():
    return "Sales Forecast API. POST JSON to /predict"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Accept either single record dict or list of dicts
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    else:
        df = pd.DataFrame(data)

    # Fill missing cols
    for f in EXPECTED_FIELDS:
        if f not in df.columns:
            df[f] = 0 if f in ['Store_id','Holiday','#Order','Year','Month','Day'] else 'NA'

    # Ensure same column order
    df = df[EXPECTED_FIELDS]
    preds = model.predict(df)
    return jsonify({"predictions": preds.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
