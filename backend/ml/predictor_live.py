import pandas as pd
import joblib
import os

model_path = os.path.join("ml", "models", "live_price_predictor.pkl")
model = joblib.load("ml/models/live_price_predictor.pkl")

# Use the same feature columns used during training
FEATURE_COLUMNS = [
    "rating_score",
    "rating_count",
    "category_electronics",
    "category_jewelery",
    "category_men's clothing",
    "category_women's clothing"
]

def predict_price(category: str, rating_score: float, rating_count: int) -> float:
    # Create a row with dummy columns
    input_data = {col: 0 for col in FEATURE_COLUMNS}
    input_data["rating_score"] = rating_score
    input_data["rating_count"] = rating_count

    category_col = f"category_{category}"
    if category_col in FEATURE_COLUMNS:
        input_data[category_col] = 1

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    return round(float(prediction), 2)
