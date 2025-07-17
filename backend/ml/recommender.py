from utils.sheets_utils import load_data


def get_recommendations(region: str, category: str):
    df = load_data()
    filtered = df[(df["Region"] == region) & (df["Category"] == category)]

    if filtered.empty:
        return ["No data available"]

    top_products = filtered["Product Name"].value_counts().head(5).index.tolist()
    return top_products
