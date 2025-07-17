import pandas as pd
import requests

def load_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    return df[["title", "price", "category", "rating"]]
