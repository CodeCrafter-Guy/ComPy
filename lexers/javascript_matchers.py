from lexers.universal_lexer_checks import maybe_include_numbers, is_whitespace
def paren_matcher(input, current_position):
    char = input[current_position]  
    if char == '(':
        return {'type': "paren", 'value': "("}, current_position + 1
    if char == ')':
        return {'type': "paren", 'value': ")"}, current_position + 1
    if is_whitespace(char):
        return
    
    numerical_input, new_position = maybe_include_numbers(input, current_position)
    print(numerical_input)
    if numerical_input:
        return {'type': "number", 'value': numerical_input}, new_position
    

    return None  # Return None if no match
