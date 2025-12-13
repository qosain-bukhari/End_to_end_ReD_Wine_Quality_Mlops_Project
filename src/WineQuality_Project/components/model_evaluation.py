import pandas as pd
import joblib
import json
import logging
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from WineQuality_Project.entity.config_entity import ModelEvaluationConfig
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig, target_column: str):
        self.config = config
        self.target_column = target_column

    def evaluate(self):
        try:
            # Load test data
            df_test = pd.read_csv(self.config.test_data_path)
            logging.info(f"Test data loaded from: {self.config.test_data_path}")

            X_test = df_test.drop([self.target_column], axis=1)
            y_test = df_test[self.target_column]

            # Load trained model
            model = joblib.load(self.config.model_path)
            logging.info(f"Model loaded from: {self.config.model_path}")

            # Make predictions
            y_pred = model.predict(X_test)

            # Calculate metrics
            metrics = {
                "r2_score": r2_score(y_test, y_pred),
                "mse": mean_squared_error(y_test, y_pred),
                "mae": mean_absolute_error(y_test, y_pred)
            }

            # Save metrics to JSON
            self.config.metric_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config.metric_file_path, 'w') as f:
                json.dump(metrics, f, indent=4)

            logging.info(f"Metrics saved at: {self.config.metric_file_path}")
            logging.info(f"Model evaluation metrics: {metrics}")

            return metrics

        except Exception as e:
            logging.error(f"Model evaluation failed: {e}")
            raise e
