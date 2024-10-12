import re

NUMBERS = r'\d'
WHITESPACE = r'\s'
LETTERS = r'[a-zA-Z]'

CARRIAGE_RETURN = r'\n'
TAB = r'\t'
EOL = r'\r'
ASTRIX = r'\*'
ASSIGNABLE_CHARACTERS = r'[^\s\n\t\r,;(){}[\]=]'
SPECIAL_CHARACTERS = r'[^a-zA-Z0-9_; \s\n\t\r]'


def includes(array, value):
    """
    Check if the given value is present in the array (list).
    
    Parameters:
    -----------
    array : list
        The list to search.
    value : any
        The value to look for in the array.

    Returns:
    --------
    bool
        True if the value is found in the array, otherwise False.
    """
    return value in array

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

def is_whitespace(char):
    return bool(re.match(WHITESPACE, char))

def is_numbers(char):
    return bool(re.match(NUMBERS, char))

def include_numbers(input, current_position):
    """
    Extracts a sequence of numerical characters from the input string, starting at the current position.
    
    This function reads characters from the input starting at the given position and continues reading 
    as long as the characters are numerical (e.g., digits). It stops when a non-numerical character is encountered 
    or the end of the input is reached. The function returns the extracted numerical string and the updated position.

    Parameters:
    -----------
    input : str
        The input string to parse.
    current_position : int
        The starting index in the input string from which to begin parsing numbers.

    Returns:
    --------
    tuple
        A tuple containing:
        - numerical_input (str): The extracted sequence of numeric characters.
        - current_position (int): The updated position after the last parsed character.
    """
    char = input[current_position]
    numerical_input = ''    
    while is_in_bounds(input, current_position) and is_numbers(char):
        numerical_input += char
        current_position += 1
        if current_position < len(input):
            char = input[current_position]
        else:
            break
    
    return numerical_input, current_position

def include_word(input, current_position):
    word = ''    
    while is_in_bounds(input, current_position) and re.match(LETTERS, input[current_position]):
        word += input[current_position]
        current_position += 1    
    return word, current_position

def include_double_quote_strings(input, current_position):
    return include_string(input, current_position, '"')

def include_single_quote_strings(input, current_position):
    return include_string(input, current_position, "'")

def include_keyword(input, current_position, keywords):
    // todo


def include_single_key_character(input, current_position, key):
    if input[current_position] == key:
        return input[current_position], current_position + 1
    return '', current_position

def include_character(input, current_position, key):
    """Check if the current characters match the multi-character key."""
    key_length = len(key)
    if input[current_position:current_position + key_length] == key:
        return input[current_position:current_position + key_length], current_position + key_length
    return '', current_position

def include_literal_strings(input, current_position):
    return include_string(input, current_position, '`')

def include_string(input, current_position, delimiter):
    """
    Extracts a sequence of characters enclosed within a specific delimiter 
    (e.g., ", ', `) starting at the current position.
    
    Parameters:
    -----------
    input : str
        The input string to parse.
    current_position : int
        The starting index in the input string from which to begin parsing.
    delimiter : str
        The string delimiter to look for (e.g., '"', "'", "`").
    
    Returns:
    --------
    tuple
        A tuple containing:
        - extracted_value (str): The string enclosed by the delimiter.
        - current_position (int): The updated position after the closing delimiter.
    """
    extracted_value = ''
    
    if input[current_position] == delimiter:
        current_position += 1
        while is_in_bounds(input, current_position) and input[current_position] != delimiter:
            extracted_value += input[current_position]
            current_position += 1
        if is_in_bounds(input, current_position) and input[current_position] == delimiter:
            current_position += 1
        else:
            raise ValueError(f"Unclosed {delimiter} found.")
    
    return extracted_value, current_position

def include_assignment_operator(input, current_position, assignment_operators):
    # Define valid assignment operators (single and multi-character)
    # assignment_operators = ['=', '+=', '-=', '*=', '/=', '%=', '//=', '**=']

    operator = ''
    char = input[current_position]
    while is_in_bounds(input, current_position) and includes(assignment_operators, char):
        operator += char
        current_position += 1


