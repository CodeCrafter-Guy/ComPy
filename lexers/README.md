## Adding a lexer_config

-   Test the lexer against some common scenarios before raising a PR. Add these to the `sanity_tests/` folder
-   If a default lexer is not working for you, consider updating it and raising a PR!.

    Below are some gotchas and take aways that should be considered.

### Token Order

-   Comments First: Placing comment patterns at the top ensures that sequences starting with / are correctly identified as comments before potentially matching division operators.

-   String and Character Literals: These are placed before operators and punctuators because they can contain characters that might otherwise be misinterpreted as operators or punctuation.

-   Operators: Multi-character operators are listed before single-character ones to ensure the longest possible match is made. For example, == should be matched before =.

-   Punctuators: Multi-character punctuators (like ...) are listed before single-character ones to prevent partial matching.

-   Lifetimes (Rust) and language specfic elements: The pattern for lifetimes (e.g., 'a) is placed before identifiers to capture these correctly.

-   Keywords: Placed before identifiers to ensure that reserved words are matched as keywords and not as identifiers.

-   Identifiers: Placed after keywords and lifetimes.

-   Numeric Literals: Different types of numeric literals can be defined, with patterns for hexadecimal, octal, binary, floating-point, and integer literals.

-   Whitespace: Placed after other tokens since it generally doesn't conflict but is still important to capture.

-   Consider Unknown Tokens: The unknown token type is a catch-all to handle any unexpected characters, aiding in error detection.

### Patterns and Escaping

-   Regex Patterns: Backslashes in regex patterns are escaped with another backslash in YAML (e.g., \\s+).

-   String Literals: The pattern for raw string literals (in the case of rust) (r(#_)"(._?)"\1) uses backreferences to match the same number of # signs at the start and end of the string. This pattern handles raw strings with varying numbers of # signs, up to a certain complexity.

-   Character Literals: Patterns for character literals ensure that escape sequences are correctly handled within single quotes.

### Delimiters

-   Purpose: Delimiters are used in the lexer code to determine where to stop when matching pattern-based tokens. They include whitespace and symbols that separate tokens.

-   Definition: The delimiters string should includes common delimiters specific to the language, common ones include spaces, tabs, newlines, punctuation, and operator
