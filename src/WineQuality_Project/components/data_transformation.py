import os
import pandas as pd
import numpy as np
import logging
from pathlib import Path
from sklearn.model_selection import train_test_split
from WineQuality_Project.entity.config_entity import DataTransformationconfig
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import logging

class DataTransformation:
    def __init__(self, config: DataTransformationconfig):
        self.config = config
        self.config.root_dir.mkdir(parents=True, exist_ok=True)

    def initiate_data_transformation(self):
        try:
            # 1️⃣ Load the validated data
            df = pd.read_csv(self.config.data_path)
            logging.info(f"Loaded data: {self.config.data_path}")

            # 2️⃣ Split into train and test
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Split data into train and test")

            # 3️⃣ Save the train and test CSVs
            train_path = self.config.root_dir / "train.csv"
            test_path = self.config.root_dir / "test.csv"
            train_df.to_csv(train_path, index=False)
            test_df.to_csv(test_path, index=False)

            logging.info(f"Saved train.csv at: {train_path}")
            logging.info(f"Saved test.csv at: {test_path}")

            # 4️⃣ Return paths for the next stage
            return train_path, test_path

        except Exception as e:
            logging.error(f"Data Transformation failed: {e}")
            raise e
