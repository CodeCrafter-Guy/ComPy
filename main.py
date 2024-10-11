import tokenizer
import lexers.javascript_matchers as javascript_matchers

tokens = tokenizer.tokenize("function (test) { const a = 123; }", javascript_matchers.paren_matcher)

print(tokens)