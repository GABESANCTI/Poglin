import sys
from src.lexer.poglinParser import poglinParser
from src.lexer.poglinVisitor import poglinVisitor
from src.semantic.symbol_table import SymbolTable

class SemanticAnalyzer(poglinVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

        self.poglin_types_map = {
            'Int': 'Int',
            'String': 'String'
        }

    def report_error(self, message, line, column):
        error_msg = f"ERRO SEMÂNTICO [Linha {line}, Coluna {column}]: {message}"
        print(error_msg, file=sys.stderr)
        self.errors.append(error_msg)

    def get_errors(self):
        return self.errors

    def visitProgram(self, ctx: poglinParser.ProgramContext):
        self.symbol_table.enter_scope()
        self.visitChildren(ctx)

        # Captura o escopo global não joga fora as variáveis declaradas
        self.symbol_table.global_snapshot = self.symbol_table.scopes[-1].copy()

        # self.symbol_table.exit_scope()  # <- Comentado para preservar os símbolos
        return len(self.errors) == 0

    def visitStatement(self, ctx: poglinParser.StatementContext):
        if ctx.VAR():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column
            
            if self.symbol_table.is_declared_in_current_scope(var_name):
                self.report_error(f"Variável '{var_name}' já declarada no escopo atual.", var_line, var_column)
                return None
            
            declared_type_text = ctx.type_().getText()
            declared_poglin_type = self.poglin_types_map.get(declared_type_text, 'Unknown')

            self.symbol_table.declare(var_name, declared_poglin_type) 

            expr_type_info = self.visit(ctx.expression())
            
            if expr_type_info and expr_type_info['type'] != 'Error':
                expr_type = expr_type_info['type']
                
                if expr_type != declared_poglin_type:
                    self.report_error(
                        f"Tipo incompatível na inicialização de '{var_name}': esperado '{declared_poglin_type}', encontrado '{expr_type}'.",
                        expr_type_info['line'], expr_type_info['column']
                    )
            else:
                self.report_error(f"Expressão de inicialização inválida para '{var_name}'.", var_line, var_column)
            
            return None

        elif ctx.READLINE():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column

            if not self.symbol_table.is_declared(var_name):
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return None
            
            var_type = self.symbol_table.get_type(var_name)
            if var_type != 'String':
                self.report_error(f"Variável '{var_name}' do tipo '{var_type}' não pode receber entrada de 'readLine()'. Esperado 'String'.", var_line, var_column)
            
            return None

        elif ctx.ID() and ctx.ASSIGN() and ctx.expression():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column

            if not self.symbol_table.is_declared(var_name):
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return None
            
            var_type = self.symbol_table.get_type(var_name)
            expr_type_info = self.visit(ctx.expression())
            
            if expr_type_info and expr_type_info['type'] != 'Error':
                expr_type = expr_type_info['type']
                if expr_type != var_type:
                    self.report_error(
                        f"Atribuição inválida para '{var_name}': esperado '{var_type}', encontrado '{expr_type}'.",
                        expr_type_info['line'], expr_type_info['column']
                    )
            else:
                self.report_error(f"Expressão inválida ou com erro na atribuição para '{var_name}'.", var_line, var_column)
            
            return None

        elif ctx.PRINTLN():
            expr_type_info = self.visit(ctx.expression())
            if expr_type_info and expr_type_info['type'] == 'Error':
                pass
            return None
            
        elif ctx.IF():
            cond_type_info = self.visit(ctx.expression())
            if cond_type_info and cond_type_info['type'] != 'Int':
                self.report_error(f"Condição 'if' espera um valor Int (booleano), encontrado '{cond_type_info['type']}'.", cond_type_info['line'], cond_type_info['column'])

            self.symbol_table.enter_scope()
            in_current_block = False
            brace_count = 0
            for child in ctx.children:
                if child == ctx.LBRACE(0):
                    in_current_block = True
                    brace_count += 1
                    continue
                if child == ctx.RBRACE(0) and brace_count == 1:
                    in_current_block = False
                    brace_count -= 1
                    break 
                if in_current_block and isinstance(child, poglinParser.StatementContext):
                    self.visit(child)
            self.symbol_table.exit_scope()

            if ctx.ELSE():
                self.symbol_table.enter_scope()
                in_current_block = False
                brace_count = 0
                for child in ctx.children:
                    if child == ctx.LBRACE(1):
                        in_current_block = True
                        brace_count += 1
                        continue
                    if child == ctx.RBRACE(1) and brace_count == 1:
                        in_current_block = False
                        brace_count -= 1
                        break
                    if in_current_block and isinstance(child, poglinParser.StatementContext):
                        self.visit(child)
                self.symbol_table.exit_scope()
            return None

        elif ctx.WHILE():
            cond_type_info = self.visit(ctx.expression())
            if cond_type_info and cond_type_info['type'] != 'Int':
                self.report_error(f"Condição 'while' espera um valor Int (booleano), encontrado '{cond_type_info['type']}'.", cond_type_info['line'], cond_type_info['column'])

            self.symbol_table.enter_scope()
            in_current_block = False
            brace_count = 0
            for child in ctx.children:
                if child == ctx.LBRACE(0):
                    in_current_block = True
                    brace_count += 1
                    continue
                if child == ctx.RBRACE(0) and brace_count == 1:
                    in_current_block = False
                    brace_count -= 1
                    break
                if in_current_block and isinstance(child, poglinParser.StatementContext):
                    self.visit(child)
            self.symbol_table.exit_scope()
            return None
        
        elif ctx.POG():
            return None

        return self.visitChildren(ctx)


    def visitExpression(self, ctx: poglinParser.ExpressionContext):
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx: poglinParser.LogicalOrExpressionContext):
        left_type_info = self.visit(ctx.logicalAndExpression(0))
        
        # Acessa o token do operador de forma segura (verifica se a lista tem elementos)
        op_tokens = ctx.OR() # Retorna uma lista, pode ser vazia
        if op_tokens: # Se a lista não estiver vazia
            op_token_instance = op_tokens[0] # Pega a primeira instância do token
            right_type_info = self.visit(ctx.logicalAndExpression(1))
            
            if left_type_info and right_type_info:
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_token_instance.getText()}' (OR) espera operandos Int (booleanos), encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        
        return left_type_info

    def visitLogicalAndExpression(self, ctx: poglinParser.LogicalAndExpressionContext):
        left_type_info = self.visit(ctx.equalityExpression(0))
        op_tokens = ctx.AND() # Retorna uma lista
        if op_tokens:
            op_token_instance = op_tokens[0]
            right_type_info = self.visit(ctx.equalityExpression(1))

            if left_type_info and right_type_info:
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_token_instance.getText()}' (AND) espera operandos Int (booleanos), encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        return left_type_info

    def visitEqualityExpression(self, ctx: poglinParser.EqualityExpressionContext):
        left_type_info = self.visit(ctx.relationalExpression(0))
        op_token_instance = None
        if ctx.EQUALS(): op_token_instance = ctx.EQUALS()[0] # Acessa o primeiro elemento da lista
        elif ctx.NEQUALS(): op_token_instance = ctx.NEQUALS()[0] # Acessa o primeiro elemento da lista

        if op_token_instance:
            right_type_info = self.visit(ctx.relationalExpression(1))
            
            if left_type_info and right_type_info:
                if left_type_info['type'] != right_type_info['type']:
                    self.report_error(f"Operador '{op_token_instance.getText()}' espera operandos do mesmo tipo, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        return left_type_info

    def visitRelationalExpression(self, ctx: poglinParser.RelationalExpressionContext):
        left_type_info = self.visit(ctx.additiveExpression(0))
        op_token_instance = None
        if ctx.LT(): op_token_instance = ctx.LT()[0] # Acessa o primeiro elemento da lista
        elif ctx.LTE(): op_token_instance = ctx.LTE()[0] # Acessa o primeiro elemento da lista
        elif ctx.GT(): op_token_instance = ctx.GT()[0] # Acessa o primeiro elemento da lista
        elif ctx.GTE(): op_token_instance = ctx.GTE()[0] # Acessa o primeiro elemento da lista

        if op_token_instance:
            right_type_info = self.visit(ctx.additiveExpression(1))

            if left_type_info and right_type_info:
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_token_instance.getText()}' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        return left_type_info

    def visitAdditiveExpression(self, ctx: poglinParser.AdditiveExpressionContext):
        left_type_info = self.visit(ctx.multiplicativeExpression(0))
        op_token_instance = None
        if ctx.PLUS(): op_token_instance = ctx.PLUS()[0] # Acessa o primeiro elemento da lista
        elif ctx.MINUS(): op_token_instance = ctx.MINUS()[0] # Acessa o primeiro elemento da lista

        if op_token_instance:
            right_type_info = self.visit(ctx.multiplicativeExpression(1))

            if left_type_info and right_type_info:
                if op_token_instance.getText() == '+':
                    if (left_type_info['type'] == 'String' and right_type_info['type'] == 'String') or \
                       (left_type_info['type'] == 'String' and right_type_info['type'] == 'Int') or \
                       (left_type_info['type'] == 'Int' and right_type_info['type'] == 'String'):
                        return {'type': 'String', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_token_instance.getText()}' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        
        return left_type_info

    def visitMultiplicativeExpression(self, ctx: poglinParser.MultiplicativeExpressionContext):
        left_type_info = self.visit(ctx.unaryExpression(0))
        op_token_instance = None
        if ctx.MULT(): op_token_instance = ctx.MULT()[0] # Acessa o primeiro elemento da lista
        elif ctx.DIV(): op_token_instance = ctx.DIV()[0] # Acessa o primeiro elemento da lista

        if op_token_instance:
            right_type_info = self.visit(ctx.unaryExpression(1))

            if left_type_info and right_type_info:
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_token_instance.getText()}' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
                
                if op_token_instance.getText() == '/' and 'value' in right_type_info and right_type_info['value'] == 0:
                    self.report_error(f"Divisão por zero detectada.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                    return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}

                return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        return left_type_info

    def visitUnaryExpression(self, ctx: poglinParser.UnaryExpressionContext):
        op_tokens = ctx.NOT() # Retorna uma lista
        if op_tokens:
            op_token_instance = op_tokens[0] # Acessa o primeiro elemento da lista
            operand_type_info = self.visit(ctx.unaryExpression())
            if operand_type_info and operand_type_info['type'] != 'Int':
                self.report_error(f"Operador '{op_token_instance.getText()}' espera operando Int, encontrado '{operand_type_info['type']}'.", op_token_instance.symbol.line, op_token_instance.symbol.column)
                return {'type': 'Error', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
            return {'type': 'Int', 'line': op_token_instance.symbol.line, 'column': op_token_instance.symbol.column}
        
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: poglinParser.PrimaryContext):
        if ctx.INT():
            return {'type': 'Int', 'value': int(ctx.INT().getText()), 'line': ctx.INT().symbol.line, 'column': ctx.INT().symbol.column}
        elif ctx.STRING():
            string_value = ctx.STRING().getText()
            return {'type': 'String', 'value': string_value[1:-1], 'line': ctx.STRING().symbol.line, 'column': ctx.STRING().symbol.column}
        elif ctx.ID():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column
            
            var_type = self.symbol_table.get_type(var_name)
            
            if var_type is None:
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return {'type': 'Error', 'line': var_line, 'column': var_column}
            
            return {'type': var_type, 'line': var_line, 'column': var_column}

        elif ctx.expression():
            return self.visit(ctx.expression())
        
        self.report_error("Expressão primária não reconhecida ou inválida.", ctx.start.line, ctx.start.column)
        return {'type': 'Error', 'line': ctx.start.line, 'column': ctx.start.column}