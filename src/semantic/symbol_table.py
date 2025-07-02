class SymbolTable:
    def __init__(self):
        self.scopes = [{}] 

    def enter_scope(self):
        self.scopes.append({})
    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def declare_symbol(self, name, symbol_type, line, column):
        current_scope = self.scopes[-1]
        if name in current_scope:
            return False, f"Erro Semântico [Linha {line}, Coluna {column}]: Variável '{name}' já declarada neste escopo."
        current_scope[name] = {'type': symbol_type, 'line': line, 'column': column}
        return True, None

    def lookup_symbol(self, name):
    
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name] 
        return None 