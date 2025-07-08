class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise Exception("Tentativa de sair do escopo global")

    def declare(self, name, var_type):
        if self.is_declared_in_current_scope(name):
            raise Exception(f"Variável '{name}' já declarada no escopo atual")
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

    def exists(self, name):
        return self.is_declared(name)

    def all(self):
        all_vars = set()
        for scope in self.scopes:
            all_vars.update(scope.keys())
        return all_vars
