# Import token names as constants rather than hardcoding them.
from tokens import IDENTIFIER, LITERAL, PLUS, MINUS, MULTIPLY, EQUALS, LEFT_PARENTHESIS, RIGHT_PARENTHESIS, SEMI_COLON, EOF
from cfg_names import *
from ParseTree import ParseTreeNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current_token(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return {"token": EOF, "lexeme": ""}

    def next_token(self):
        tok = self.current_token()
        self.index += 1
        return tok

    def match(self, expected):
        tok = self.current_token()
        if tok["token"] == expected:
            self.next_token()
            return tok
        raise SyntaxError(f"Expected {expected}, found '{tok['lexeme']}'")

    def parse_program(self):
        # Program -> Assignment*
        children = []
        while self.current_token()["token"] != EOF:
            children.append(self.parse_assignment())
        return ParseTreeNode(PROGRAM, children=children)

    def parse_assignment(self):
        # Assignment -> Identifier = Exp ;
        ident = self.current_token()
        if ident["token"] != IDENTIFIER:
            raise SyntaxError(f"Expected IDENTIFIER, found '{ident['lexeme']}'")
        self.next_token() # consume identifier

        eq = self.match(EQUALS)
        expr_node = self.parse_exp()
        self.match(SEMI_COLON)

        return ParseTreeNode(ASSIGNMENT,
                             value=eq["lexeme"],
                             children=[
                                 ParseTreeNode(IDENTIFIER, value=ident["lexeme"]),
                                 expr_node
                             ])

    # Exp -> Term Exp'
    def parse_exp(self):
        term_node = self.parse_term()
        return self.parse_exp_prime(term_node)

    # Exp' -> + Term Exp' | - Term Exp' | ε
    def parse_exp_prime(self, left_node):
        tok = self.current_token()
        if tok["token"] in (PLUS, MINUS):
            op = self.next_token()
            right_term = self.parse_term()
            new_node = ParseTreeNode(EXPRESSION,
                                     value=op["token"],
                                     children=[left_node, right_term])
            return self.parse_exp_prime(new_node)
        # ε (no more + or -)
        return left_node

    # Term -> Fact Term'
    def parse_term(self):
        fact_node = self.parse_fact()
        return self.parse_term_prime(fact_node)

    # Term' -> * Fact Term' | ε
    def parse_term_prime(self, left_node):
        tok = self.current_token()
        if tok["token"] == MULTIPLY:
            op = self.next_token()
            right_fact = self.parse_fact()
            new_node = ParseTreeNode(TERM,
                                     value=op["token"],
                                     children=[left_node, right_fact])
            return self.parse_term_prime(new_node)
        # ε (no more * )
        return left_node

    # Fact -> ( Exp ) | - Fact | + Fact | Literal | Identifier
    def parse_fact(self):
        tok = self.current_token()

        if tok["token"] == LEFT_PARENTHESIS:
            self.next_token()  # consume '('
            exp_node = self.parse_exp()
            self.match(RIGHT_PARENTHESIS)
            return ParseTreeNode(
                FACT,
                value=f'{LEFT_PARENTHESIS}{RIGHT_PARENTHESIS}',
                children=[exp_node]
            )

        elif tok["token"] in (PLUS, MINUS):
            op = self.next_token()
            fact_node = self.parse_fact()
            return ParseTreeNode(
                FACT,
                value=op["token"],
                children=[fact_node]
            )

        elif tok["token"] in (LITERAL, IDENTIFIER):
            self.next_token()
            return ParseTreeNode(tok["token"], value=tok["lexeme"])

        else:
            raise SyntaxError(f"Unexpected token '{tok['lexeme']}' in Fact")

