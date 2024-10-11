import re

NUMBERS = r'\d'

def is_whitespace(char):
    return char.isspace()

def is_numbers(char):
    return bool(re.match(NUMBERS, char))

def maybe_include_numbers(input, current_position):
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
    while is_numbers(char):
        numerical_input += char
        current_position += 1
        if current_position < len(input):
            char = input[current_position]
        else:
            break
    
    return numerical_input, current_position
