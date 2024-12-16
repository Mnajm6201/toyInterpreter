# Import constants names from tokens.py and cfg_names.py and symbol table.
from tokens import IDENTIFIER, LITERAL, PLUS, MINUS, MULTIPLY, LEFT_PARENTHESIS, RIGHT_PARENTHESIS
from cfg_names import ASSIGNMENT, EXPRESSION, TERM, FACT

class Evaluator:
    def __init__(self, symbol_table):
        """
        Initializes symbol table.
        """
        self.symbol_table = symbol_table

    def evaluate(self, parse_tree):
        """
        Processes the program. Assignments get evaluated and printed immediately.
        """
        for node in parse_tree.children:
            self._evaluate_node(node)

    def _evaluate_node(self, node):
        """
        Decides what to do based on the node type.
        Assignment nodes update variables, expressions calculate values,
        and identifiers/literals return data.
        """
        if node.node_type == ASSIGNMENT:

            # Assignment → Identifier = Exp ;
            # Handle the left side and calculate the right side (Exp)
            var_name = node.children[0].value
            expression_result = self._evaluate_node(node.children[1])

            # Update symbol table, print result
            self.symbol_table.set_value(var_name, expression_result)
            print(f"{var_name} = {expression_result}")

        elif node.node_type == EXPRESSION:
            return self._evaluate_expression(node)

        elif node.node_type == TERM:
            return self._evaluate_term(node)

        elif node.node_type == FACT:
            return self._evaluate_fact(node)

        # Return variable
        elif node.node_type == IDENTIFIER:
            var_name = node.value
            return self.symbol_table.get_value(var_name)

        # Return literal
        elif node.node_type == LITERAL:
            return int(node.value)

    def _evaluate_expression(self, node):
        left_result = self._evaluate_node(node.children[0])
        operator = node.value
        right_result = self._evaluate_node(node.children[1])
        
        if operator == PLUS:
            return left_result + right_result
        elif operator == MINUS:
            return left_result - right_result

    def _evaluate_term(self, node):
        """
        Handles Term → Term * Fact | Fact.
        At this stage Term can only be Term * Fact.
        """
        left_result = self._evaluate_node(node.children[0])
        operator = node.value  
        right_result = self._evaluate_node(node.children[1])

        if operator == MULTIPLY:
            return left_result * right_result

    def _evaluate_fact(self, node):
        # Fact → + Fact or - Fact 
        if node.value in {PLUS, MINUS}:
            operator = node.value
            result = self._evaluate_node(node.children[0])
            return result if operator == PLUS else -result
            
        # Fact → ( Exp ) 
        if node.value == f'{LEFT_PARENTHESIS}{RIGHT_PARENTHESIS}':
            return self._evaluate_node(node.children[0])
            
        # Literal or identifier
        if len(node.children) == 1:
            return self._evaluate_node(node.children[0])