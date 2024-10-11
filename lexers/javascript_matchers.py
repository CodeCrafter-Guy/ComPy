from lexers.universal_lexer_checks import include_numbers, is_whitespace, include_double_quote_strings, include_literal_strings, include_single_quote_strings, include_word
def paren_matcher(input, current_position):
    char = input[current_position]  
    if char == '(':
        return {'type': "paren", 'value': "("}, current_position + 1
    if char == ')':
        return {'type': "paren", 'value': ")"}, current_position + 1
    if is_whitespace(char):
        return
    
    string_input, new_position = include_double_quote_strings(input, current_position)
    if(string_input):
        return {'type': "string", 'value': string_input}, new_position
    
    string_input, new_position = include_single_quote_strings(input, current_position)
    if(string_input):
        return {'type': "string", 'value': string_input}, new_position
    
    string_input, new_position = include_literal_strings(input, current_position)
    if(string_input):
        return {'type': "string", 'value': string_input}, new_position
    
    string_input, new_position = include_word(input, current_position)
    if(string_input):
        return {'type': "name", 'value': string_input}, new_position
    
    numerical_input, new_position = include_numbers(input, current_position)
    print(numerical_input)
    if numerical_input:
        return {'type': "number", 'value': numerical_input}, new_position
    

    return None  # Return None if no match
