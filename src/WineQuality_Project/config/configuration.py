import os
from WineQuality_Project.constants import *
from WineQuality_Project.utils.common import read_yaml,create_directories
from WineQuality_Project.entity.config_entity import DataIngestionConfig
from WineQuality_Project.entity.config_entity import DataValidationConfig
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