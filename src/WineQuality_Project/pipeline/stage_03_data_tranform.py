from WineQuality_Project import logger

import logging
from WineQuality_Project.config.configuration import ConfigManager
from WineQuality_Project.components.data_transformation import DataTransformation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

STAGE_NAME="Data Validation stage"
class DatatransformTrainingPipline():
    def __init__(self):
        pass

    def main(self):
            
        config = ConfigManager()
        
        data_transformation_config = config.get_data_transformation_config()
        
        data_transformation = DataTransformation(config=data_transformation_config)
        
        artifacts = data_transformation.initiate_data_transformation()

        print("✔ Data Transformation Completed Successfully!")
        return artifacts



      
if __name__=='__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=DatatransformTrainingPipline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
    except Exception as e:
        raise e