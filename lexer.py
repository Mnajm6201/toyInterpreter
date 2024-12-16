# Import token name constants and dictionaries from token.py
from tokens import IDENTIFIER, LITERAL, OPERATORS, PUNCTUATION, EOF

# Function takes input string and cursor to start at in string, and returns
# a valid substring for the regular expression for Identifier.
# (Letter | Underscore)(Letter | Digit | Underscore)*
def match_identifier(input, cursor):

    # Check to see if input begins with letter or underscore (Letter| "_").
    # If not, or if cursor larger then or equal to input length return None.
    # (Pattern does not match or cursor is larger than input index).
    if cursor >= len(input) or not (input[cursor].isalpha() or input[cursor] == "_"):
        return None

    # If first char matched, move end one past first char,
    # and continue to include input in lexeme as long as it matches rest of pattern --
    # is either letter or digit (Letter| Digit)* and as long as end is less than length of input.
    end = cursor + 1
    while end < len (input) and (input[end].isalnum() or input[end] == "_"):
        end += 1

    # Return found valid substring (lexeme).
    return input [cursor: end]

# Function takes input string and cursor to start in string, and returns
# a valid substring for the regular expression for Literal.
# 0 | (NonZeroDigit)(Digit)*
def match_literal (input, cursor):
    
    # If cursor beyond input's index return None.
    if cursor >= len (input):
        return None

    # Check if input is single digit 0.
    if input [cursor] == '0':

        # Return None if 0 is not deliminated (leading 0s not allowed).
        if cursor + 1 < len (input) and input[cursor + 1].isalnum():
            return None
        
        # Return 0 as valid lexeme.
        return "0"
    
    # Check if first char is non zero digit. If it is increment end past cursor.
    if input[cursor].isdigit() and input[cursor] != '0':
        end = cursor + 1

        # Continue to accept characters into lexeme as long as they are digits.
        # (Increment end until non digit or end of input).
        while end < len (input) and input[end].isdigit():
            end += 1
        
        # Return None if next char is invalid to lexeme (prevent 123abc).
        if end < len (input) and not (
            input[end].isspace() or input[end] in OPERATORS or input[end] in PUNCTUATION
        ):
            return None

        # Return valid subsrting (lexeme).
        return input [cursor : end]
    
    # If no valid lexeme found, return None.
    return None

# Takes input string and cursor to begin in string and calls functions for
# identifier and literal matching and dictionaries for operators and punctuation
# to find valid lexeme. Returns found token and valid lexeme.
def scanner (input, cursor):

    # Check if identifier.
    lexeme = match_identifier (input, cursor)
    if lexeme:
        return IDENTIFIER, lexeme
    
    # Check if literal.
    lexeme = match_literal (input, cursor)
    if lexeme:
        return LITERAL, lexeme
    
    # Check if single character token.
    lexeme = input [cursor]

    # Operator.
    if lexeme in OPERATORS:
        return OPERATORS [lexeme], lexeme

    # Puncuation.
    if lexeme in PUNCTUATION :
        return PUNCTUATION  [lexeme], lexeme
    
    # If No token was found return None as token and lexeme.
    return None, None


# Central function, takes input and returns a list of token dicts with token and lexemes 
# for entire input string. Raises ValueError if invalid input found (unmatched input).
def tokenizer (input):

    # Initialize list for tokens and cursor to iterate through input.
    tokens = []
    cursor = 0

    # Iterate until cursor reaches length of input.
    while cursor < len (input):

        # If whitespace encountered, increase counter by one and exit loop iteration.
        if input[cursor].isspace():
            cursor += 1
            continue

        # Get the token and lexume returned from scanner function. (None if none found).
        token, lexeme = scanner (input, cursor)

        # If match found append token list with dict containin token and lexume values.
        # Move cursor past lexeme size for next input.
        if token:
            tokens.append ({"token": token, "lexeme": lexeme})
            cursor += len(lexeme)

        # If no match was found, (return was None) raise error. 
        else:
            raise ValueError (f"Unexpected character at position {cursor}: {input[cursor]}")

    # Return list of all token / lexume pairs.
    tokens.append ({"token": EOF, "lexeme": ""})
    return tokens


    
