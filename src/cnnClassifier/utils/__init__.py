import os
import sys
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# reading a yaml file

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    This function will read a yaml file and will return:
    
    Args: 
        path_to_yaml (str): path like input
    
    Returns: 
        ConfigBox: ConfigBox type
    
    Raises: 
        ValueError: if yaml file is empty
        e: empty file            
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logging.info("Error in performing read_yaml operation")
        raise CustomException(e,sys)
    
# create directories

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories:
    Args: 
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.          
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"created directory at: {path}")
    except Exception as e:
        logging.info("Error in performing create_directories operation")
        raise CustomException(e,sys)
    
# save json

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data:
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
            logging.info(f"json file saved at: {path}")
    except Exception as e:
        logging.info("Error in performing read_json operation")
        CustomException(e,sys)
        
# load json

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file data
    
    Args:
        path (Path): path to json file
        
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    try:
        with open(path) as f:
            content = json.load(f)
            logging.info(f"json file loaded successfully from: {path}")
            return ConfigBox(content)
    except Exception as e:
        logging.info("Error in performing operation load_json")
        raise CustomException(e,sys)
    
# save bin

@ensure_annotations
def save_bin(data: Any, path:Path):
    """
    save binary file
    
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    try:
        joblib.dump(value=data, filename=path)
        logging.info(f"binary file saved at: {path}")
    except Exception as e:
        logging.info("Error in performing save_bin operation")
        raise CustomException(e,sys)
    
# load bin

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data
    
    Args:
        path (Path): path to binary file
        
    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(path)
        logging.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        logging.info("Error in performing load_bin operation")
        raise CustomException(e,sys)
    
# get size

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB
    
    Args:
        path (Path): path of the file
        
    Returns:
        str: size in KB
    """
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        logging.info(f"The {path} has size: {size_in_kb} KB")
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logging.info("Error in performing operation get_size")
        raise CustomException(e, sys)
    
# decode image

@ensure_annotations
def decodeImage(imgstring, fileName):
    """
    to decode the binary string into normal form.
    
    Returns:
        Return the decoded string.    
    """
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, "wb") as f:
            f.write(imgdata)
            f.close()
            logging.info("image data decoded successfully using decodeImage function")
    except Exception as e:
        logging.info("Error in performing operation decodeImage")
        raise CustomException(e,sys)
    
# encode image into Base64

@ensure_annotations
def encodeImageintoBase64(croppedImagePath):
    """
    to encode the string into the binary form.
    
    Returns:
        Return the encoded string.    
    """
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
            logging.info("image data encoded successfully using encodeImageintoBase64 function")
    except Exception as e:
        logging.info("Error in performing encodeImageintoBase64 operation")
        raise CustomException(e,sys)