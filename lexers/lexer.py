import yaml
from lexers.universal_lexer_checks import include_character

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
