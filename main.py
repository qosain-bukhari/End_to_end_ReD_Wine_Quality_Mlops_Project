from WineQuality_Project import logger
from WineQuality_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from WineQuality_Project.pipeline.stage_02_data_validation import DatavalidationTrainingPipline
from WineQuality_Project.pipeline.stage_03_data_tranform import DatatransformTrainingPipline

STAGE_NAME="Data Ingestion stage"
try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=DataIngestionTrainingPipline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data validation stage"
try:
        logger.info(f'>> stage {STAGE_NAME} started')
        data_ingestion=DatavalidationTrainingPipline()
        data_ingestion.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data tranformation stage"  
try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=DatatransformTrainingPipline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
except Exception as e:
        logger.exception(e)
        raise e