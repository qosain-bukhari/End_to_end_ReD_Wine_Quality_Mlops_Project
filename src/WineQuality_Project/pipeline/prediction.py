import pandas as pd
import joblib
from pathlib import Path

class PredictionPipeline:
    def __init__(self, model_path: str = "artifacts/model_trainer/model.joblib"):
        # Check if model exists
        if not Path(model_path).exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        # Load the trained model
        self.model = joblib.load(model_path)
        
        # Save the feature names used during training
        self.feature_names = self.model.feature_names_in_

    def predict(self, data: pd.DataFrame):
        # Standardize column names
        data = data.copy()
        data.columns = data.columns.str.strip().str.replace(" ", "_")

        # Ensure input columns match the training columns
        missing_cols = [c for c in self.feature_names if c not in data.columns]
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")

        # Keep only columns used during training
        data = data[self.feature_names]

        # Return predictions
        return self.model.predict(data)
