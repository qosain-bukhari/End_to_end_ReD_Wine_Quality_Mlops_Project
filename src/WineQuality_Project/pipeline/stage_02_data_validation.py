from WineQuality_Project import logger

import logging
from WineQuality_Project.config.configuration import ConfigManager
from WineQuality_Project.components.data_validation import DataValidation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

STAGE_NAME="Data Validation stage"
class DatavalidationTrainingPipline():
    def __init__(self):
        pass
    def main(self):
            config = ConfigManager()
            data_ingestion_config = config.get_data_validation_config()
            data_ingestion = DataValidation(config=data_ingestion_config)
            csv_folder = data_ingestion.initiate_data_validation()
            logging.info(f"CSV files are ready in: {csv_folder}")
      
if __name__=='__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=DatavalidationTrainingPipline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
    except Exception as e:
        raise e