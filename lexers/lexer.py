"""
A set of utility functions to tokenize an input string based on a lexer configuration.

This module includes functions for determining delimiters, checking bounds, slicing
strings, and processing tokens based on a given lexer configuration.

Functions:
    - is_delimiter: Check if a character at a position in the input string is a delimiter.
    - is_in_bounds: Check if the current position is within bounds of the input string.
    - get_string_slice: Extract a slice of the input string until a delimiter is found.
    - process_tokens: Tokenize the input string by matching tokens based on the lexer config.
"""

import re

def is_delimiter(input, current_position, delimiters):
    """
    Check if the character at the current position in the input string is a delimiter.

    Parameters:
    -----------
    input : str
        The input string to check.
    current_position : int
        The current index in the input string.
    delimiters : str
        A string containing characters that should be considered as delimiters.

    Returns:
    --------
    bool
        True if the character at the current position is a delimiter, False otherwise.

    Example:
        is_delimiter("function test() {}", 13, " (){}")  # Returns True for "("
    """
    return input[current_position] in delimiters

def is_in_bounds(input, current_position):
    """
    Check if the current position is within the bounds of the input string.

    Parameters:
    -----------
    input : str
        The input string to check.
    current_position : int
        The current index in the input string.

    Returns:
    --------
    bool
        True if the current_position is within bounds, False otherwise.

    Example:
        is_in_bounds("function test() {}", 5)  # Returns True if 5 is a valid index
    """
    return current_position < len(input)

def get_string_slice(input_text, current_position, delimiters):
    """
    Slice the input string starting at the current position until a delimiter is found.

    Parameters:
    -----------
    input_text : str
        The full input string being tokenized.
    current_position : int
        The current position in the input string from which to start slicing.
    delimiters : str
        A string containing all characters that should be treated as delimiters.

    Returns:
    --------
    tuple
        A tuple containing:
        - slice (str): The slice of the input text up to the first delimiter.
        - current_position (int): The updated position after the slice.

    Example:
        get_string_slice("function test() {}", 9, " (){}")  # Returns ('test', 13)
    """
    slice_text = ''
    
    while is_in_bounds(input_text, current_position) and not is_delimiter(input_text, current_position, delimiters):
        slice_text += input_text[current_position]
        current_position += 1
    
    return slice_text, current_position

def process_tokens(input_text, current_position, lexer_config):
    """
    Process tokens from the input string starting at the given current position.

    The function loops through the lexer configuration to match tokens based on
    specified patterns or values. It checks for delimiters to correctly parse the
    input text into tokens and returns the matched token and updated position.

    Parameters:
    -----------
    input_text : str
        The input string to tokenize.
    current_position : int
        The current index in the input string.
    lexer_config : dict
        The lexer configuration dictionary which defines token types, patterns, and values.

    Returns:
    --------
    tuple
        A tuple containing:
        - token (dict): A dictionary containing the matched token with 'value' and 'type' keys.
        - current_position (int): The updated position in the input text after tokenization.

    Example:
        lexer_config = {
            'tokens': [
                {'type': 'keyword', 'value': 'function'},
                {'type': 'identifier', 'pattern': r'[a-zA-Z_][a-zA-Z0-9_]*'}
            ],
            'delimiters': ' (){};'
        }
        process_tokens("function test()", 0, lexer_config)
        # Returns ({'value': 'function', 'type': 'keyword'}, 8)
    """
    value = ''
    token_type = ''
    matched = False

    # Skip over whitespace characters
    WHITESPACE = ' \t\n\r'
    while is_in_bounds(input_text, current_position) and input_text[current_position] in WHITESPACE:
        current_position += 1  # Skip whitespace

    if not is_in_bounds(input_text, current_position):
        return None, current_position

    # Retrieve the list of types that should check for delimiters
    delimiter_check_for_types = lexer_config.get('delimiter_check_for_types', [])

    for token in lexer_config['tokens']:
        if 'value' in token:
            token_value = token['value']
            end_position = current_position + len(token_value)
            proposed_value = input_text[current_position:end_position]
            if proposed_value == token_value:
                # Decide whether to check for delimiter based on token type
                if token['type'] in delimiter_check_for_types:                    
                    if end_position >= len(input_text) or input_text[end_position] in lexer_config['delimiters']:
                        value = token_value
                        token_type = token['type']
                        current_position = end_position
                        matched = True
                        break
                else:                    
                    value = token_value
                    token_type = token['type']
                    current_position = end_position
                    matched = True
                    break
        elif 'pattern' in token:
            match = re.match(token['pattern'], input_text[current_position:])
            if match:
                value = match.group(0)
                token_type = token['type']
                current_position += len(value)
                matched = True
                break

    if not matched:
        print(f"Lexical analysis config could not determine character at position {current_position}: '{input_text[current_position]}'")
        current_position += 1  # Skip the character

    return {'value': value, 'type': token_type} if matched else None, current_position
