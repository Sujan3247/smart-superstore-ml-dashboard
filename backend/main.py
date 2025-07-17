from fastapi import FastAPI
from utils.sheets_utils import load_data
from ml.recommender import get_recommendations
from ml.predictor_live import predict_price


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Superstore API is live!"}

@app.get("/sales")
def get_sales():
    df = load_data()
    return df.to_dict(orient="records")

@app.get("/recommend")
def recommend(region: str, category: str):
    return {"recommended_products": get_recommendations(region, category)}

@app.get("/predict_price")
def predict_price_api(category: str, rating_score: float, rating_count: int):
    predicted = predict_price(category, rating_score, rating_count)
    return {
        "predicted_price": predicted,
        "input": {
            "category": category,
            "rating_score": rating_score,
            "rating_count": rating_count
        }
    }

