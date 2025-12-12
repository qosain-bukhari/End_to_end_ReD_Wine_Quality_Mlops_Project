# src/WineQuality_Project/components/data_ingestion.py

import urllib.request
import zipfile
from pathlib import Path
from WineQuality_Project.config import configuration
from WineQuality_Project.utils.common import create_directories
import logging
from WineQuality_Project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def download_data(self):
        # local_data_file is a Path object; use its exists() method
        if not self.config.local_data_file.exists():
            filename, headers = urllib.request.urlretrieve(
                url=self.config.source_url,
                filename=str(self.config.local_data_file)
            )
            logging.info(f"File downloaded successfully and saved to {filename} with headers {headers}")
        else:
            logging.info(f"File already exists at {self.config.local_data_file}")

    def extract_zip_file(self):
        """
        Extracts the zip file to the specified directory.
        """
        unzip_path = Path(self.config.unzip_dir)
        unzip_path.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logging.info(f"Extracted zip file to {unzip_path}")

    def initiate_data_ingestion(self):
        self.download_data()
        self.extract_zip_file()
        return self.config.unzip_dir