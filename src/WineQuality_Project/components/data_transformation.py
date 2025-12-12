import os
import pandas as pd
import numpy as np
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split
from WineQuality_Project.entity.config_entity import DataTransformationconfig
from sklearn.preprocessing import StandardScaler
import joblib

class DataTransformation:
    def __init__(self,config:DataTransformationconfig):
        self.config=config
    
    def initiate_data_transformation(self):
        logging.info(" Starting Data Transformation Stage...")

        try:
            df = pd.read_csv(self.config.data_path)
            logging.info(f"Loaded dataset: {self.config.data_path}")

            # --------------------------------------
            # 1️⃣ Separate features and target
            # --------------------------------------
            X = df.drop(columns=["quality"])
            y = df["quality"]

            # --------------------------------------
            # 2️⃣ Train–Test Split
            # --------------------------------------
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            logging.info("Train-test split completed")

            scalar=StandardScaler()
            X_train_scaled=scalar.fit_transform(X_train)
            X_test_scaled=scalar.transform(X_test)

            logging.info("Feature scaling completed")
            train_path = Path(self.config.root_dir, "train.npy")
            test_path = Path(self.config.root_dir, "test.npy")
            ytrain_path = Path(self.config.root_dir, "y_train.npy")
            ytest_path = Path(self.config.root_dir, "y_test.npy")
            scaler_path = Path(self.config.root_dir, "scaler.pkl")

            np.save(train_path, X_train_scaled)
            np.save(test_path, X_test_scaled)
            np.save(ytrain_path, y_train)
            np.save(ytest_path, y_test)
            

            # save scaler
            import joblib
            joblib.dump(scalar, scaler_path)

            logging.info(f"Artifacts saved inside: {self.config.root_dir}")

            return {
                "X_train": train_path,
                "X_test": test_path,
                "y_train": ytrain_path,
                "y_test": ytest_path,
                "scaler": scaler_path
            }
        except Exception as e:
             logging.error(f"Data Transformation failed: {e}")
             raise e