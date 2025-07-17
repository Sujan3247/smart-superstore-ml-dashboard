# 🛍️ Smart Superstore ML Dashboard

A real-time machine learning dashboard that predicts product prices and recommends top items using live data from the Fake Store API.

## 🔧 Tech Stack

- 🧠 Machine Learning: scikit-learn (RandomForestRegressor)
- 🧪 FastAPI backend for predictions
- 🎨 Streamlit frontend for interactive UI
- 🔌 FakeStore API for real-time product data

## 🚀 Features

- Predict product prices based on rating and popularity
- Real-time product recommendations
- Interactive UI with expandable cards
- Full integration of backend + frontend

## 📦 How to Run

### Backend

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
