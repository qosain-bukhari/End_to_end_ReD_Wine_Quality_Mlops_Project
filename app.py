import streamlit as st
import pandas as pd
from src.WineQuality_Project.pipeline.prediction import PredictionPipeline

# Page config
st.set_page_config(page_title="Wine Quality Predictor 🍷", layout="wide")
st.title("🍷 Wine Quality Prediction App")

st.markdown("Enter the values for each feature to predict wine quality:")

# Input fields with default/example values
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, value=7.4, step=0.1)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, value=0.70, step=0.01)
citric_acid = st.number_input("Citric Acid", min_value=0.0, value=0.00, step=0.01)
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, value=1.9, step=0.1)
chlorides = st.number_input("Chlorides", min_value=0.0, value=0.076, step=0.0001)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, value=11.0, step=0.1)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, value=34.0, step=0.1)
density = st.number_input("Density", min_value=0.0, value=0.9978, step=0.0001)
pH = st.number_input("pH", min_value=0.0, value=3.51, step=0.01)
sulphates = st.number_input("Sulphates", min_value=0.0, value=0.56, step=0.01)
alcohol = st.number_input("Alcohol", min_value=0.0, value=9.4, step=0.1)

# Prepare input DataFrame
input_df = pd.DataFrame({
    "fixed_acidity": [fixed_acidity],
    "volatile_acidity": [volatile_acidity],
    "citric_acid": [citric_acid],
    "residual_sugar": [residual_sugar],
    "chlorides": [chlorides],
    "free_sulfur_dioxide": [free_sulfur_dioxide],
    "total_sulfur_dioxide": [total_sulfur_dioxide],
    "density": [density],
    "pH": [pH],
    "sulphates": [sulphates],
    "alcohol": [alcohol]
})

# Predict button
if st.button("Predict Wine Quality"):
    try:
        predictor = PredictionPipeline(model_path="artifacts/model_trainer/model.joblib")
        prediction = predictor.predict(input_df)
        st.success(f"Predicted Wine Quality: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
