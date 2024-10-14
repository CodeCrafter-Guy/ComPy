"""
A script to validate YAML files against a JSON schema using the `jsonschema` library.

This script loads YAML lexer configuration files, validates them against a given
JSON schema, and logs any validation errors. If validation fails, errors are written
to a file called `validation_output.txt`.

Usage:
    python validate_yaml.py

Dependencies:
    - PyYAML
    - jsonschema
"""

import yaml
import json
import glob
from jsonschema import validate, ValidationError, SchemaError

def load_yaml(yaml_file_path):
    """
    Load a YAML file and return its data.

    Parameters:
        yaml_file_path (str): The path to the YAML file to load.

    Returns:
        dict: The loaded YAML data.

    Raises:
        IOError: If the file cannot be opened.
        yaml.YAMLError: If there is an error while parsing the YAML.
    """
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def load_json(json_file_path):
    """
    Load a JSON schema file and return its data.

    Parameters:
        json_file_path (str): The path to the JSON schema file to load.

    Returns:
        dict: The loaded JSON schema.

    Raises:
        IOError: If the file cannot be opened.
        json.JSONDecodeError: If there is an error while parsing the JSON.
    """
    with open(json_file_path, 'r') as file:
        schema = json.load(file)
    return schema

def validate_yaml(yaml_file_path, json_schema_path, error_list):
    """
    Validate a YAML file against a JSON schema.

    Parameters:
        yaml_file_path (str): The path to the YAML file to validate.
        json_schema_path (str): The path to the JSON schema file.
        error_list (list): A list to store error messages if validation fails.

    Returns:
        bool: True if the YAML file is valid, False if it is invalid.

    Raises:
        ValidationError: If the YAML file does not conform to the JSON schema.
        SchemaError: If the JSON schema is invalid.
    """
    data = load_yaml(yaml_file_path)
    schema = load_json(json_schema_path)
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as ve:
        error_message = f"Validation error in {yaml_file_path}: {ve.message}"
        error_list.append(error_message)
        return False
    except SchemaError as se:
        error_message = f"Schema error: {se.message}"
        error_list.append(error_message)
        return False

def validate_all():
    """
    Validate all YAML files in the 'lexers' directory against the JSON schema.

    This function searches for all YAML files in the './lexers/' directory,
    validates them using the provided JSON schema, and logs any validation
    errors.
    
    Returns:
        list: A list of error messages (empty if no errors are found).
    """
    files = glob.glob("./lexers/*.yaml")
    error_list = []
    for file in files:
        validate_yaml(file, './lexer_schema.json', error_list)
    if error_list:
        print('\n'.join(error_list))
    return error_list

if __name__ == "__main__":
    validate_all()
