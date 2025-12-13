import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from WineQuality_Project.entity.config_entity import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        try:
            # Load data
            train_df = pd.read_csv(self.config.train_data_path)
            test_df = pd.read_csv(self.config.test_data_path)

            # Drop any identifier column if exists (like 'Id')
            if 'Id' in train_df.columns:
                train_df = train_df.drop('Id', axis=1)
            if 'Id' in test_df.columns:
                test_df = test_df.drop('Id', axis=1)

            # Split features & target
            X_train = train_df.drop(self.config.target_column, axis=1)
            y_train = train_df[self.config.target_column]

            X_test = test_df.drop(self.config.target_column, axis=1)
            y_test = test_df[self.config.target_column]

            # Model
            model = RandomForestRegressor(
                n_estimators=self.config.n_estimators,
                max_depth=self.config.max_depth,
                random_state=42
            )

            # Train
            model.fit(X_train, y_train)

            # Save model
            os.makedirs(self.config.root_dir, exist_ok=True)
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(model, model_path)

            print(f"Model trained and saved at: {model_path}")
            return model

        except Exception as e:
            print(f"Error during training: {e}")
            raise e
