import re

def is_delimiter(input, current_position, delimiters):
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
        True if current_position is within bounds, False otherwise.
    """
    return current_position < len(input)

def get_string_slice(input_text, current_position, delimiters):
    """
    Slice the input string until a delimiter is found.
    
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
    """
    slice_text = ''
    
    while is_in_bounds(input_text, current_position) and not is_delimiter(input_text, current_position, delimiters):
        slice_text += input_text[current_position]
        current_position += 1
    
    return slice_text, current_position
def process_tokens(input_text, current_position, lexer_config):
    """
    Process tokens from the input text starting at the current position.

    Parameters:
        input_text (str): The text to tokenize.
        current_position (int): The current index in the input text.
        lexer_config (dict): The lexer configuration dictionary.

    Returns:
        tuple: A tuple containing the matched token (dict) and the new current position (int).
    """
    value = ''
    token_type = ''
    matched = False

    # Skip over whitespace
    WHITESPACE = ' \t\n\r'
    while is_in_bounds(input_text, current_position) and input_text[current_position] in WHITESPACE:
        current_position += 1  # Skip whitespace

    if not is_in_bounds(input_text, current_position):
        return None, current_position

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
