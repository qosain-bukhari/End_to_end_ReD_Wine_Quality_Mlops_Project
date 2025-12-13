from WineQuality_Project import logger
from WineQuality_Project.config.configuration import ConfigManager

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        self.config_manager = ConfigManager()

    def main(self):
        try:
            logger.info(f">>> Stage {STAGE_NAME} started")
            
            # Get evaluation config
            eval_config = self.config_manager.get_model_evaluation_config()
            
            # Initialize evaluation
            from WineQuality_Project.components.model_evaluation import ModelEvaluation
            evaluator = ModelEvaluation(
                model_path=eval_config.model_path,
                test_data_path=eval_config.test_data_path,
                target_column="quality",
                metric_file_path=eval_config.metric_file_path  # ✅ pass metric_file_path
            )
            
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
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} Completed Successfully")
    except Exception as e:
        raise e
