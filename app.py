import streamlit as st
import pandas as pd
from src.WineQuality_Project.pipeline.prediction import PredictionPipeline

st.set_page_config(page_title="Wine Quality Predictor", layout="wide")
st.title("🍷 Wine Quality Prediction App")

st.markdown("""
Upload a CSV file with the following columns:  
`fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol`
""")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Standardize column names (replace spaces with _)
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    st.subheader("Input Data Preview")
    st.dataframe(df.head())

    # Prediction
    try:
        predictor = PredictionPipeline()
        predictions = predictor.predict(df)
        df["Predicted_Quality"] = predictions

        st.subheader("Prediction Results")
        st.dataframe(df)

        # Option to download results
        csv = df.to_csv(index=False)
        st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")

    except KeyError as ke:
        st.error(f"Missing columns: {ke}")
    except Exception as e:
        st.error(f"Error: {e}")
