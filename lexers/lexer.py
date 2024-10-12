import yaml
import re
from lexers.universal_lexer_checks import include_character, is_in_bounds, is_not_delimiter
# when we search through the input, how do we know to "check" what we currently have? use a slice delimiter!
DEFAULT_SLICE_DELIMITER=" \t\n\r;(){}[]="

def get_string_slice(input_text, current_position, delimiters=DEFAULT_SLICE_DELIMITER):
    slice =''
    while is_in_bounds(input_text, current_position) and is_not_delimiter(input, current_position)
    slice += input[current_position]
    current_position += 1
    return slice, current_position

def match_token(input_text, current_position, token):
    if 'value' in token:
        key_length = len(token['value'])
        if input_text[current_position:current_position + key_length] == token['value']:
            return token['value'], current_position + key_length
    elif 'pattern' in token:
        # Handle regex pattern match (for tokens with 'pattern')
        pattern = token['pattern']
        match = re.match(pattern, input_text[current_position:])
        if match:
            return match.group(0), current_position + len(match.group(0))
    return '', current_position

def process_tokens(input_text, current_position, tokens):
    while current_position < len(input_text):
        for token in tokens:

            # check if we have a value
            if token['value']:
                token_value = token['value']

                # Check for matching key (single or multi-character)
                result, new_position = include_character(input_text, current_position, token_value)
                if result:
                    print(f"Matched: {result}")
                    current_position = new_position
                    break
            else
                # also need to check the pattern and check that


        # If no match was found, move to the next character
        current_position += 1

# Example YAML tokens (this would come from your YAML config)
yaml_tokens = """
tokens:
  - value: "="
  - value: "+"
  - value: "=="
  - value: "!="
"""
tokens_config = yaml.safe_load(yaml_tokens)['tokens']

# Example input
input_text = "a == b + c != d"

# Process the tokens
process_tokens(input_text, 0, tokens_config)
