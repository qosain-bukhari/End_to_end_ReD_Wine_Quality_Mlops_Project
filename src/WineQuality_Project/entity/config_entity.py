from pathlib import Path

from dataclasses import dataclass
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

from dataclasses import dataclass

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path          # Base folder to store validation artifacts
    raw_data_file: Path     # CSV file produced by Data Ingestion
    status_file: Path       # Path to save validation status (success/fail)
    all_schema: dict 


@dataclass(frozen=True)
class DataTransformationconfig:
    root_dir:Path
    data_path:Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    n_estimators: int
    max_depth: int
    target_column: str