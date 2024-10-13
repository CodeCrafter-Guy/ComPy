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

def process_tokens_old(input_text, current_position, lexer_config):
    value = ''
    token_type = ''
    new_position = current_position
    # print('analysing:', repr(input_text[current_position]))
    matched = False

    for token in lexer_config['tokens']:
        if 'value' in token:
            token_value = token['value']
            proposed_value = input_text[current_position:current_position + len(token_value)]
            if proposed_value == token_value:
                value = token_value
                token_type = token['type']
                current_position += len(token_value)
                matched = True
                break

        elif 'pattern' in token:
            slice_text, new_position = get_string_slice(input_text, current_position, lexer_config['delimiters'])
            match = re.match(token['pattern'], slice_text)
            if match:
                token_type = token['type']
                value = match.group(0)
                current_position = new_position
                matched = True
                break

    if not matched:

        if is_delimiter(input_text, current_position, lexer_config['delimiters']):
            # Skip over the delimiter without error
            current_position += 1
        else:
            print('Lexical analysis config could not determine character at position', current_position)
            current_position += 1
        ### print('nothing found...')
        return None, current_position

    return {'value': value, 'type': token_type}, current_position

def process_tokens(input_text, current_position, lexer_config):
    value = ''
    token_type = ''
    matched = False

    while is_in_bounds(input_text, current_position) and input_text[current_position] in lexer_config['delimiters']:
        current_position += 1  # Skip delimiters

    for token in lexer_config['tokens']:
        if 'value' in token:
            token_value = token['value']
            end_position = current_position + len(token_value)
            proposed_value = input_text[current_position:end_position]
            if proposed_value == token_value:
                # Check if the character after the matched value is a delimiter or end of input
                if end_position >= len(input_text) or is_delimiter(input_text, end_position, lexer_config['delimiters']):
                    value = token_value
                    token_type = token['type']
                    current_position = end_position
                    matched = True
                    break
        elif 'pattern' in token:
            slice_text, new_position = get_string_slice(input_text, current_position, lexer_config['delimiters'])
            match = re.match(token['pattern'], slice_text)
            if match:
                value = match.group(0)
                token_type = token['type']
                current_position += len(value)
                matched = True
                break

    if not matched:
        if is_in_bounds(input_text, current_position) and is_delimiter(input_text, current_position, lexer_config['delimiters']):
            # Skip over the delimiter without error
            current_position += 1
        else:
            print(f"Lexical analysis config could not determine character at position {current_position}")
            current_position += 1  # Skip the character

    return {'value': value, 'type': token_type} if matched else None, current_position
