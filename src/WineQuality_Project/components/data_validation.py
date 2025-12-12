import pandas as pd
import logging
from pathlib import Path
from WineQuality_Project.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.schema = self.config.all_schema

    def _write_status(self, message: str, success=True):
        self.config.status_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config.status_file, 'w') as f:
            if success:
                f.write(f"Validation Status: SUCCESS \n{message}\n")
            else:
                f.write(f"Validation Status: FAILED \n{message}\n")
        logging.info(f"Status written to {self.config.status_file}")

    def validate_file_existence(self):
        if not self.config.raw_data_file.exists():
            msg = f"File not found: {self.config.raw_data_file}"
            self._write_status(msg, success=False)
            raise FileNotFoundError(msg)
        logging.info(f"File exists: {self.config.raw_data_file}")

    def normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Replace spaces with underscores and strip column names."""
        df.columns = [col.strip().replace(" ", "_") for col in df.columns]
        return df

    def validate_columns(self, df: pd.DataFrame):
        df = self.normalize_columns(df)
        expected_columns = list(self.schema['columns'].keys())
        csv_columns = list(df.columns)

        missing_columns = [col for col in expected_columns if col not in csv_columns]
        extra_columns = [col for col in csv_columns if col not in expected_columns]

        if missing_columns:
            msg = f"Missing columns: {missing_columns}"
            self._write_status(msg, success=False)
            raise ValueError(msg)

        logging.info(f"All required columns exist. Extra columns ignored: {extra_columns}")
        return df

    def validate_missing_values(self, df: pd.DataFrame):
        missing_count = df.isnull().sum().sum()
        if missing_count > 0:
            msg = f"Dataset contains {missing_count} missing values"
            self._write_status(msg, success=False)
            raise ValueError(msg)
        logging.info("No missing values found.")

    def initiate_data_validation(self) -> pd.DataFrame:
        try:
            self.validate_file_existence()
            df = pd.read_csv(self.config.raw_data_file)
            logging.info(f"CSV loaded: {self.config.raw_data_file}")
            df = self.validate_columns(df)
            self.validate_missing_values(df)
            self._write_status("Data validation completed successfully ", success=True)
            return df
        except Exception as e:
            logging.error(f"Data validation failed: {e}")
            raise e
