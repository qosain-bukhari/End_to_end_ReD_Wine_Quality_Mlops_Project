import joblib
import pandas as pd

class PredictionPipeline:
    def __init__(self, model_path='artifacts/model_trainer/model.joblib'):
        # Load the trained model
        self.model = joblib.load(model_path)
        # Columns expected by the trained model
        self.expected_columns = [
            "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
            "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide",
            "density", "pH", "sulphates", "alcohol"
        ]

    def predict(self, data: pd.DataFrame):
        # 1️⃣ Standardize column names: remove spaces and replace with _
        data.columns = data.columns.str.strip().str.replace(" ", "_")

        # 2️⃣ Check for missing columns
        missing_cols = [c for c in self.expected_columns if c not in data.columns]
        if missing_cols:
            raise ValueError(f"Missing columns in input: {missing_cols}")

        # 3️⃣ Keep only expected columns in correct order
        data = data[self.expected_columns]

        # 4️⃣ Make prediction
        prediction = self.model.predict(data)
        return prediction
