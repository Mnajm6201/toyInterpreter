# Token name constants.
IDENTIFIER = "IDENTIFIER"
LITERAL = "LITERAL"
EQUALS = "EQUALS"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
LEFT_PARENTHESIS = "LEFT_PARENTHESIS"
RIGHT_PARENTHESIS = "RIGHT_PARENTHESIS"
SEMI_COLON = "SEMI_COLON"
EOF = "EOF"

# Operators dictionary matches constant name with appropraite char.
OPERATORS = {
    "=" : EQUALS,
    "+" : PLUS,
    "-" : MINUS,
    "*" : MULTIPLY,
}

# Punctuation dictionary matches constant name with appropraite char.
PUNCTUATION = {
    "(" : LEFT_PARENTHESIS,
    ")" : RIGHT_PARENTHESIS,
    ";" : SEMI_COLON  
}