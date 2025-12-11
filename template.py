import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

Project_Name_root="End_to_end_ReD_Wine_Quality_Mlops_Project"

Project_Name = "WineQuality_Project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{Project_Name}/__init__.py",
    f"src/{Project_Name}/components/__init__.py",
    f"src/{Project_Name}/utils/__init__.py",
    f"src/{Project_Name}/config/__init__.py",
    f"src/{Project_Name}/config/configuration.py",
    f"src/{Project_Name}/pipeline/__init__.py",
    f"src/{Project_Name}/pipeline/training_pipeline.py",
    f"src/{Project_Name}/pipeline/prediction_pipeline.py",
    f"src/{Project_Name}/entity/__init__.py",
    f"src/{Project_Name}/constants/__init__.py",
    f"src/{Project_Name}/logger/__init__.py",
    f"src/{Project_Name}/exception/__init__.py",
    "params.yaml",
    "main.py",
    "app.py",
    "schema.yaml",
    "requirements.txt",
    "setup.py",
    "README.md",
    "Dockerfile",
    ".gitignore"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")