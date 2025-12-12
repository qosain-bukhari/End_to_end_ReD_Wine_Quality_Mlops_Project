from WineQuality_Project import logger
from WineQuality_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline

STAGE_NAME="Data Ingestion stage"
try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
except Exception as e:
        raise e