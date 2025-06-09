import streamlit as st
import joblib
import pandas as pd
import xgboost
from feature_extraction import extract_features  # <-- you'll write this module

# Load model
model = joblib.load("Model/xgb_model.pkl")

st.title("🕵️‍♂️ Phishing URL Classifier")
st.write("Paste a URL below to check if it's potentially phishing.")

url_input = st.text_input("Enter URL here:")

if url_input:
    try:
        features_df = extract_features(url_input)  # ➜ your function
        prediction = model.predict(features_df)[0]
        prediction_label = "🔒 Legitimate" if prediction == 0 else "⚠️ Phishing"

        st.subheader("Prediction:")
        st.success(prediction_label)
    except Exception as e:
        st.error(f"Something went wrong during prediction: {e}")