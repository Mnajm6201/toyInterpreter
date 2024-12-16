class ParseTreeNode:
    """
    Class representing a node in the parse tree.
    """
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type  # Type of the node 
        self.value = value  # Value 
        self.children = children or []  # List of child nodes


