from WineQuality_Project import logger

import logging
from WineQuality_Project.config.configuration import ConfigManager
from WineQuality_Project.components.Model_taining import ModelTraining
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

STAGE_NAME="Model taining stage"

class ModelTrainingPipeline:
    def main(self):
        try:
            logging.info(">>> Model Training Stage Started <<<")

            config_manager = ConfigManager()
            model_training_config = config_manager.get_model_training_config()

            model_trainer = ModelTraining(config=model_training_config)
            model_trainer.train()

            logging.info(">>> Model Training Stage Completed Successfully <<<")

        except Exception as e:
            logging.error(" Error occurred in Model Training Stage")
            logging.exception(e)
            raise e


      
if __name__=='__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
    except Exception as e:
        raise e