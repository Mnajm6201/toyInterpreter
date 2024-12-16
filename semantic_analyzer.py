# Import names for CFG and token constants rather than hard coding it.
from cfg_names import ASSIGNMENT, EXPRESSION, TERM, FACT
from tokens import IDENTIFIER

class SemanticAnalyzer:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def analyze(self, parse_tree):
        
        # Iterate through assignment nodes analyzing each.
        for assignment in parse_tree.children:  
            self._analyze_node(assignment)


    def _analyze_node(self, node):
        if node.node_type == ASSIGNMENT:
            var_name = node.children[0].value  # Identifier

            # Declare the variable if not already declared
            if not self.symbol_table.is_declared(var_name):
                self.symbol_table.declare(var_name)

            # Analyze expression
            self._analyze_node(node.children[1])

            # Mark variable as initialized
            self.symbol_table.initialize(var_name)

        elif node.node_type in {EXPRESSION, TERM, FACT}:
            for child in node.children:
                self._analyze_node(child)

        elif node.node_type == IDENTIFIER:

            # Check if variable declared
            var_name = node.value
            if not self.symbol_table.is_declared(var_name):
                raise Exception(f"Semantic Error: Variable '{var_name}' not declared.")
            
            # Check if variable initialized
            if not self.symbol_table.is_initialized(var_name):
                raise Exception(f"Semantic Error: Variable '{var_name}' used before initialization.")



