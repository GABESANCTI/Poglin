class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def declare(self, name, var_type):
        self.scopes[-1][name] = var_type

    def is_declared(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return True
        return False

    def is_declared_in_current_scope(self, name):
        return name in self.scopes[-1]

    def get_type(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
