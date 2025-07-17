import pandas as pd
import requests
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

# Step 1: Fetch live product data from API
url = "https://fakestoreapi.com/products"
response = requests.get(url)
products = response.json()

# Step 2: Convert to DataFrame
df = pd.DataFrame(products)

# Step 3: Extract useful features
df["category"] = df["category"].astype("category")
df["rating_count"] = df["rating"].apply(lambda r: r["count"])
df["rating_score"] = df["rating"].apply(lambda r: r["rate"])
df = df[["category", "rating_score", "rating_count", "price"]]

# Step 4: One-hot encode category
df = pd.get_dummies(df, columns=["category"])

# Step 5: Define X and y
X = df.drop("price", axis=1)
y = df["price"]

# Step 6: Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Step 7: Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/live_price_predictor.pkl")
print("Model trained and saved from live API data!")
