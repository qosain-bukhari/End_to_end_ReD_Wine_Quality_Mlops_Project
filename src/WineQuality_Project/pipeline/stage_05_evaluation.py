from WineQuality_Project import logger
from WineQuality_Project.config.configuration import ConfigManager

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        self.config_manager = ConfigManager()

    def main(self):
        try:
            logger.info(f">>> Stage {STAGE_NAME} started")
            
            # Get config
            eval_config = self.config_manager.get_model_evaluation_config()
            
            # Initialize evaluation
            from WineQuality_Project.components.model_evaluation import ModelEvaluation
            evaluator = ModelEvaluation(config=eval_config, target_column="quality")
            
            # Run evaluation
            metrics = evaluator.evaluate()
            
            logger.info(f">>> Stage {STAGE_NAME} completed successfully ✅")
            return metrics

        except Exception as e:
            logger.exception(f"{STAGE_NAME} failed: {e}")
            raise e

     
if __name__=='__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME} started')
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
    except Exception as e:
        raise e