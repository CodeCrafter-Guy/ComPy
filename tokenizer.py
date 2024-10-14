import json
def tokenize(input, lexer_config, lexer):
    current_position = 0
    tokens = []
    while current_position < len(input):
        result = lexer(input, current_position, lexer_config)
        if result:
            token, new_position = result
            if token:
                tokens.append(token)
            current_position = new_position
        else:
            current_position += 1
    return json.dumps(tokens)