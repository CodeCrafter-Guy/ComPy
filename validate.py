import yaml
import json
import glob
from jsonschema import validate, ValidationError, SchemaError

def load_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def load_json(json_file_path):
    with open(json_file_path, 'r') as file:
        schema = json.load(file)
    return schema

def validate_yaml(yaml_file_path, json_schema_path, error_list):
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
    files = glob.glob("./lexers/*.yaml")
    error_list = []
    for file in files:
        validate_yaml(file, './lexer_schema.json', error_list)
    if error_list:
        with open('validation_output.txt', 'w') as f:
            print('\n'.join(error_list))
    else:
        print("All lexers validated successfully.")
    return error_list

if __name__ == "__main__":
    validate_all()
