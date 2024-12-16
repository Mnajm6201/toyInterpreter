class SymbolTable:
    def __init__(self):
        self.variables = {}  

    def declare(self, var_name):
        if var_name not in self.variables:
            self.variables[var_name] = {"initialized": False, "value": None}

    def initialize(self, var_name):
        if var_name in self.variables:
            self.variables[var_name]["initialized"] = True

    def is_declared(self, var_name):
        return var_name in self.variables

    def is_initialized(self, var_name):
        return self.variables.get(var_name, {}).get("initialized", False)

    def get_value(self, var_name):
        return self.variables.get(var_name, {}).get("value", None)

    def set_value(self, var_name, value):
        self.variables[var_name]["value"] = value

    def get_uninitialized(self):
        return [var for var, state in self.variables.items() if not state["initialized"]]