import os
from box.exceptions import BoxValueError
import yaml
import json
from WineQuality_Project import logger
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        file_path (Path): The path to the YAML file.        

    rasies:
        BoxValueError: If there is an error reading the YAML file.
    """
    try:
        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading YAML file: {file_path} - {e}")
        raise e

def create_directories(path_to_directories: list , verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list[Path]): List of directory paths to create.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

def save_json(file_path: Path, data: dict):
    """Saves a dictionary to a JSON file.

    Args:
        file_path (Path): The path to the JSON file.
        data (dict): The data to save.
    """
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at: {file_path}")

def  load_json(file_path: Path) -> ConfigBox:
    """Loads a JSON file and returns its contents as a dictionary.

    Args:
        file_path (Path): The path to the JSON file.
    Returns:
        dict: The contents of the JSON file.
        """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    logger.info(f"JSON file loaded from: {file_path}")
    return ConfigBox(data)

def save_bin(file_path: Path, data: any):

    """Saves binary data to a file.

    Args:
        file_path (Path): The path to the binary file.
        data (object): The binary data to save.
    """
    import joblib
    joblib.dump(data, file_path)
    logger.info(f"Binary file saved at: {file_path}")

def load_bin(file_path: Path) -> any:
    """Loads binary data from a file.

    Args:
        file_path (Path): The path to the binary file.
    Returns:
        object: The loaded binary data.
    """
    import joblib
    data = joblib.load(file_path)
    logger.info(f"Binary file loaded from: {file_path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    logger.info(f"File size for {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"