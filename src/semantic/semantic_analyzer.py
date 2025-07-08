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
        self.symbol_table.exit_scope()
        return len(self.errors) == 0

    def visitBlockStatements(self, ctx, lbrace_idx=0, rbrace_idx=0):
        self.symbol_table.enter_scope()
        in_block = False
        brace_count = 0
        for child in ctx.children:
            if child == ctx.LBRACE(lbrace_idx):
                in_block = True
                brace_count += 1
                continue
            if child == ctx.RBRACE(rbrace_idx) and brace_count == 1:
                in_block = False
                brace_count -= 1
                break
            if in_block and isinstance(child, poglinParser.StatementContext):
                self.visit(child)
        self.symbol_table.exit_scope()

    def visitStatement(self, ctx: poglinParser.StatementContext):
        if ctx.VAR():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column

            if self.symbol_table.is_declared_in_current_scope(var_name):
                self.report_error(f"Variável '{var_name}' já declarada no escopo atual.", var_line, var_column)
                return

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

        elif ctx.READLINE():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column

            if not self.symbol_table.is_declared(var_name):
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return

            var_type = self.symbol_table.get_type(var_name)
            if var_type != 'String':
                self.report_error(f"Variável '{var_name}' do tipo '{var_type}' não pode receber entrada de 'readLine()'. Esperado 'String'.", var_line, var_column)

        elif ctx.ID() and ctx.ASSIGN() and ctx.expression():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column

            if not self.symbol_table.is_declared(var_name):
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return

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

        elif ctx.PRINTLN():
            expr_type_info = self.visit(ctx.expression())
            # Mesmo se for erro, a gente só processa e deixa quieto (já reportado)

        elif ctx.IF():
            cond_type_info = self.visit(ctx.expression())
            if cond_type_info and cond_type_info['type'] != 'Int':
                self.report_error(f"Condição 'if' espera um valor Int (booleano), encontrado '{cond_type_info['type']}'.", cond_type_info['line'], cond_type_info['column'])
            self.visitBlockStatements(ctx, 0, 0)
            if ctx.ELSE():
                self.visitBlockStatements(ctx, 1, 1)

        elif ctx.WHILE():
            cond_type_info = self.visit(ctx.expression())
            if cond_type_info and cond_type_info['type'] != 'Int':
                self.report_error(f"Condição 'while' espera um valor Int (booleano), encontrado '{cond_type_info['type']}'.", cond_type_info['line'], cond_type_info['column'])
            self.visitBlockStatements(ctx, 0, 0)

        return self.visitChildren(ctx)

    def visitExpression(self, ctx):
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        left = self.visit(ctx.logicalAndExpression(0))
        if ctx.OR():
            op = ctx.OR(0)
            right = self.visit(ctx.logicalAndExpression(1))
            if left['type'] != 'Int' or right['type'] != 'Int':
                self.report_error(f"Operador '{op.getText()}' espera operandos Int.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return left

    def visitLogicalAndExpression(self, ctx):
        left = self.visit(ctx.equalityExpression(0))
        if ctx.AND():
            op = ctx.AND(0)
            right = self.visit(ctx.equalityExpression(1))
            if left['type'] != 'Int' or right['type'] != 'Int':
                self.report_error(f"Operador '{op.getText()}' espera operandos Int.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return left

    def visitEqualityExpression(self, ctx):
        left = self.visit(ctx.relationalExpression(0))
        if ctx.EQUALS() or ctx.NEQUALS():
            op = ctx.EQUALS(0) if ctx.EQUALS() else ctx.NEQUALS(0)
            right = self.visit(ctx.relationalExpression(1))
            if left['type'] != right['type']:
                self.report_error(f"Operador '{op.getText()}' espera operandos do mesmo tipo.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return left

    def visitRelationalExpression(self, ctx):
        left = self.visit(ctx.additiveExpression(0))
        if ctx.LT() or ctx.LTE() or ctx.GT() or ctx.GTE():
            op = ctx.LT(0) or ctx.LTE(0) or ctx.GT(0) or ctx.GTE(0)
            right = self.visit(ctx.additiveExpression(1))
            if left['type'] != 'Int' or right['type'] != 'Int':
                self.report_error(f"Operador '{op.getText()}' espera operandos Int.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return left

    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.multiplicativeExpression(0))
        if ctx.PLUS() or ctx.MINUS():
            op = ctx.PLUS(0) if ctx.PLUS() else ctx.MINUS(0)
            right = self.visit(ctx.multiplicativeExpression(1))
            if op.getText() == '+' and ('String' in [left['type'], right['type']]):
                return {'type': 'String', 'line': op.symbol.line, 'column': op.symbol.column}
            if left['type'] != 'Int' or right['type'] != 'Int':
                self.report_error(f"Operador '{op.getText()}' espera operandos Int.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return left

    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.unaryExpression(0))
        if ctx.MULT() or ctx.DIV():
            op = ctx.MULT(0) if ctx.MULT() else ctx.DIV(0)
            right = self.visit(ctx.unaryExpression(1))
            if left['type'] != 'Int' or right['type'] != 'Int':
                self.report_error(f"Operador '{op.getText()}' espera operandos Int.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            if op.getText() == '/' and right.get('value') == 0:
                self.report_error("Divisão por zero detectada.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return left

    def visitUnaryExpression(self, ctx):
        if ctx.NOT():
            op = ctx.NOT(0)
            operand = self.visit(ctx.unaryExpression())
            if operand['type'] != 'Int':
                self.report_error(f"Operador '{op.getText()}' espera operando Int.", op.symbol.line, op.symbol.column)
                return {'type': 'Error', 'line': op.symbol.line, 'column': op.symbol.column}
            return {'type': 'Int', 'line': op.symbol.line, 'column': op.symbol.column}
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
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
        self.report_error("Expressão primária inválida.", ctx.start.line, ctx.start.column)
        return {'type': 'Error', 'line': ctx.start.line, 'column': ctx.start.column}
