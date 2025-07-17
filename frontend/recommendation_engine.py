import requests

def get_recommendations(category: str, min_rating: float = 4.0, min_reviews: int = 50, top_n: int = 5):
    try:
        response = requests.get("https://fakestoreapi.com/products")
        products = response.json()

        filtered = [
            p for p in products
            if p["category"] == category
            and p["rating"]["rate"] >= min_rating
            and p["rating"]["count"] >= min_reviews
        ]

        # Sort by rating + review count
        sorted_products = sorted(
            filtered,
            key=lambda p: (p["rating"]["rate"], p["rating"]["count"]),
            reverse=True
        )

        return sorted_products[:top_n]

    except Exception as e:
        return [{"error": str(e)}]
