import tokenizer
import argparse
import yaml;

# tokens = tokenizer.tokenize("function (test) { const a = 123; b = \"test\"}", javascript_matchers)

def read_file(file_path):
    """Reads the contents of a file and returns it as a string."""
    with open(file_path, encoding="utf-8") as f:
        read_data = f.read()
    return read_data

def read_lexer_config(config_file_name):
    """Reads a YAML configuration file for the lexer."""
    with open(config_file_name, 'r') as file:
        data = yaml.safe_load(file)
        return data

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Tokenize an input file using a lexer configuration.")
    
    # Add arguments
    parser.add_argument('input_file', type=str, help='The path to the input file to be tokenized.')
    parser.add_argument('lexer_config', type=str, help='The path to the YAML lexer configuration file.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Read input file and lexer config
    input_text = read_file(args.input_file)
    lexer_config = read_lexer_config(args.lexer_config)
    
    # Tokenize using the input and lexer configuration
    tokens = tokenizer.tokenize(input_text, lexer_config)
    
    # Print tokens
    print(tokens)

if __name__ == "__main__":
    main()