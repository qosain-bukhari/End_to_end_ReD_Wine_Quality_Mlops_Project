import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from WineQuality_Project.entity.config_entity import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        # Load data
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

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
        model_path = os.path.join(
            self.config.root_dir,
            self.config.model_name
        )

        joblib.dump(model, model_path)

        return model
