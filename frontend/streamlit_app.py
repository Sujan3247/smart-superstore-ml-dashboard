import streamlit as st
import requests
from recommendation_engine import get_recommendations

# Page setup
st.set_page_config(page_title="Smart Superstore Assistant", layout="wide")
st.title("🛍️ Welcome to Your Smart Superstore Assistant!")
st.caption("I’ll help you predict product prices and recommend top products in real time 🔍💡")

API_URL = "http://127.0.0.1:8000"  # FastAPI backend URL

# --- 👋 Interactive Input Area ---
st.markdown("### 🤔 What are you shopping for today?")

col1, col2, col3 = st.columns([2, 1, 1])

category = col1.selectbox("📂 Choose a product category", [
    "electronics", "jewelery", "men's clothing", "women's clothing"
])

rating_score = col2.slider("🌟 Minimum customer rating", 1.0, 5.0, 4.5, step=0.1)
rating_count = col3.slider("💬 Minimum number of reviews", 1, 500, 100)

# --- 🔮 Prediction Button & Response ---
if st.button("🔮 Predict Price & Suggest Products"):
    with st.spinner("Crunching numbers and browsing shelves..."):
        try:
            response = requests.get(f"{API_URL}/predict_price", params={
                "category": category,
                "rating_score": rating_score,
                "rating_count": rating_count
            })

            if response.status_code == 200:
                predicted_price = response.json()["predicted_price"]
                st.success(f"🎉 Based on your filters, the expected price is around **${predicted_price}**")
                st.balloons()
            else:
                st.error("⚠️ Oops! Couldn’t fetch prediction from backend.")
        except:
            st.error("🚫 Could not connect to backend. Is FastAPI running?")

    # --- 🧠 Recommendations ---
    st.markdown("## 🧠 Top Picks Just for You")

    recommended = get_recommendations(category, rating_score, rating_count)

    if recommended:
        for product in recommended:
            with st.expander(f"🛒 {product['title']}"):
                st.write(f"⭐ **Rating**: {product['rating']['rate']} ({product['rating']['count']} reviews)")
                st.write(f"💸 **Price**: ${product['price']}")
                st.image(product["image"], width=180)
    else:
        st.info("🤷 No great matches found. Try adjusting your rating filters or choose another category.")

# --- 🛍 Live Product Feed ---
st.markdown("---")
st.markdown("## 📦 Live Product Feed from FakeStoreAPI")

try:
    products = requests.get("https://fakestoreapi.com/products").json()

    for product in products:
        with st.expander(f"{product['title']}"):
            st.write(f"📂 **Category**: {product['category']}")
            st.write(f"⭐ **Rating**: {product['rating']['rate']} ({product['rating']['count']} reviews)")
            st.write(f"💰 **Price**: ${product['price']}")
            st.image(product["image"], width=150)
except:
    st.warning("⚠️ Could not fetch live products. Please check your internet or the API.")

# --- 📬 Footer ---
st.markdown("---")
st.markdown("🧾 _Thanks for shopping smart with us!_  📬 Feedback or ideas? Drop a message to the dev team anytime.")
