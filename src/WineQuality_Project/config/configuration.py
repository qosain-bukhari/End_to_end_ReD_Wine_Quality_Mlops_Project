import os
from WineQuality_Project.constants import *
from WineQuality_Project.utils.common import read_yaml,create_directories
from WineQuality_Project.entity.config_entity import DataIngestionConfig,ModelTrainingConfig
from WineQuality_Project.entity.config_entity import DataValidationConfig,DataTransformationconfig,ModelEvaluationConfig
class ConfigManager:
    def __init__(self,
                 config_filepath: Path = CONFIG_FILE_PATH,
                 params_filepath: Path = PARAMS_FILE_PATH,
                 schema_filepath: Path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([Path(self.config['artifact_root'])])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config['data_ingestion']
        create_directories([Path(config['root_dir'])])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config['root_dir']),
            source_url=config['source_url'],
            local_data_file=Path(config['local_data_file']),
            unzip_dir=Path(config['unzip_dir'])
        )
        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config['data_validation']
        create_directories([Path(config['root_dir'])])
        return DataValidationConfig(
            root_dir=Path(config['root_dir']),
            raw_data_file=Path(config['raw_data_file']),
            status_file=Path(config['status_file']),
            all_schema=self.schema
        )
    def get_data_transformation_config(self) -> DataTransformationconfig:
        config = self.config["data_transformation"]   # ← FIXED (dict access)

        root_dir = Path(config["root_dir"])
        data_path = Path(config["data_path"])

        create_directories([root_dir])  # ← FIXED

        data_transformation_config = DataTransformationconfig(
            root_dir=root_dir,
            data_path=data_path
        )
        return data_transformation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config['model_training']
        params = self.params['model_trainer']

        create_directories([Path(config['root_dir'])])

        return ModelTrainingConfig(
            root_dir=Path(config['root_dir']),
            train_data_path=Path(config['train_data_path']),
            test_data_path=Path(config['test_data_path']),
            model_name=config['model_name'],
            n_estimators=params['n_estimators'],
            max_depth=params['max_depth'],
            target_column=self.schema['target_column']
        )
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config['model_evaluation']
        Path(config['root_dir']).mkdir(parents=True, exist_ok=True)
        
        return ModelEvaluationConfig(
            root_dir=Path(config['root_dir']),
            test_data_path=Path(config['test_data_path']),
            model_path=Path(config['model_path']),
            metric_file_path=Path(config['metric_file_name'])
        )

    
    