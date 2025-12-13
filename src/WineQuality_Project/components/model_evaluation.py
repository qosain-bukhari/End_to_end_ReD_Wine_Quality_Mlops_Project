import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
import json
import os

class ModelEvaluation:
    def __init__(self, model_path, test_data_path, target_column, metric_file_path):
        self.model_path = model_path
        self.test_data_path = test_data_path
        self.target_column = target_column
        self.metric_file_path = metric_file_path

    def evaluate(self):
        # Load test data
        test_df = pd.read_csv(self.test_data_path)
        if "Id" in test_df.columns:
            test_df.drop("Id", axis=1, inplace=True)

        X_test = test_df.drop(self.target_column, axis=1)
        y_test = test_df[self.target_column]

        # Load model
        model = joblib.load(self.model_path)

        # Predict
        y_pred = model.predict(X_test)

        # Metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        metrics = {"MSE": mse, "R2": r2}

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.metric_file_path), exist_ok=True)

        # Save metrics
        with open(self.metric_file_path, "w") as f:
            json.dump(metrics, f, indent=4)

        print(f"Metrics saved successfully at: {self.metric_file_path}")
        return metrics
