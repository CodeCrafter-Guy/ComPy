"""
A command-line tool for tokenizing an input file using a specified lexer configuration.

This script reads an input file and a YAML lexer configuration file, tokenizes the input
using the provided lexer, and prints the resulting tokens.

Usage:
    python main.py <input_file> <lexer_config>

Arguments:
    input_file     The path to the input file to be tokenized.
    lexer_config   The path to the YAML lexer configuration file.

Example:
    python main.py source_code.js lexers/javascript.yaml
"""

import argparse
import yaml

from lexers.lexer import process_tokens
from tokenizer.tokenizer import tokenize

def read_file(file_path):
    """
    Read the contents of a file and return it as a string.

    Parameters:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file.

    Raises:
        IOError: If the file cannot be opened or read.
    """
    with open(file_path, encoding="utf-8") as file:
        read_data = file.read()
    return read_data

def read_lexer_config(config_file_name):
    """
    Read a YAML configuration file for the lexer and return the configuration data.

    Parameters:
        config_file_name (str): The path to the YAML configuration file.

    Returns:
        dict: The lexer configuration data parsed from the YAML file.

    Raises:
        IOError: If the file cannot be opened or read.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    with open(config_file_name, 'r') as file:
        data = yaml.safe_load(file)
    return data

def main():
    """
    The main entry point of the script.

    Parses command-line arguments, reads the input file and lexer configuration,
    tokenizes the input text using the lexer, and prints the resulting tokens.
    """
    
    parser = argparse.ArgumentParser(description="Tokenize an input file using a lexer configuration.")
    
    parser.add_argument('input_file', type=str, help='The path to the input file to be tokenized.')
    parser.add_argument('lexer_config', type=str, help='The path to the YAML lexer configuration file.')
    
    args = parser.parse_args()
    
    input_text = read_file(args.input_file)
    lexer_config = read_lexer_config(args.lexer_config)
    
    tokens = tokenize(input_text, lexer_config, process_tokens)
    
    print(tokens)

if __name__ == "__main__":
    main()
