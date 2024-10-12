def tokenize(input, token_matcher):
    current_position = 0
    tokens = []
    while current_position < len(input):
        result = token_matcher(input, current_position)
        if result:
            token, new_position = result
            tokens.append(token)
            current_position = new_position
        else:
            current_position += 1
    return tokens

tokens = tokenize("function (test) { const a = 123; b = \"test\"}", javascript_matchers)