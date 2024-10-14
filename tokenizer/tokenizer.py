"""
A simple tokenizer function that processes an input string and generates tokens
based on a given lexer configuration and lexer function.

The function iterates over the input string, applying the lexer function at each position
to identify tokens and their positions, then returns the tokens as a JSON array.

Usage:
    result = tokenize(input, lexer_config, lexer)

    input: A string of code or text to tokenize.
    lexer_config: The configuration defining the tokenization rules (typically from a YAML file).
    lexer: A function that processes the input text and returns tokens and their positions.
"""

import json

def tokenize(input, lexer_config, lexer):
    """
    Tokenizes an input string using a specified lexer and lexer configuration.

    Parameters:
        input (str): The input string to tokenize.
        lexer_config (dict): A lexer configuration that defines how tokens should be matched.
        lexer (function): A function that processes the input and returns a token and updated position.

    Returns:
        str: A JSON-formatted string representing the list of tokens.

    The function works by starting at position 0 and iterating over the input string. For each
    position, it applies the `lexer` function, which checks the current position in the input text
    for a matching token based on the lexer configuration. If a token is found, it is added to
    the `tokens` list, and the current position is updated. If no token is found, the position
    is incremented by one, and the function continues.

    At the end of the process, the list of tokens is returned as a JSON string.

    Example usage:
        tokens = tokenize("function test() { return 42; }", lexer_config, lexer_function)
        print(tokens)  # Outputs tokens in JSON format

    """
    current_position = 0
    tokens = []
    
    # Loop through the input until the end
    while current_position < len(input):
        # Apply the lexer function to get the next token and position
        result = lexer(input, current_position, lexer_config)
        
        if result:
            token, new_position = result
            if token:
                tokens.append(token)
            current_position = new_position
        else:
            current_position += 1
    
    # Return the tokens as a JSON-formatted string
    return json.dumps(tokens)
