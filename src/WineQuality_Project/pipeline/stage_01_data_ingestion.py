from WineQuality_Project import logger

import logging
from WineQuality_Project.config import configuration
from WineQuality_Project.config.configuration import ConfigManager
from WineQuality_Project.components.data_ingestion import  DataIngestion
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

STAGE_NAME="Data Ingestion stage"
class DataIngestionTrainingPipline():
    def __init__(self):
        pass
    def main(self):
            config = ConfigManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            csv_folder = data_ingestion.initiate_data_ingestion()
            logging.info(f"CSV files are ready in: {csv_folder}")
      
if __name__=='__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
    except Exception as e:
        raise e