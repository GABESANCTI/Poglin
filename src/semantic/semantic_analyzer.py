from antlr4 import *
from src.lexer.poglinParser import poglinParser
from src.lexer.poglinVisitor import poglinVisitor
from src.semantic.symbol_table import SymbolTable

class SemanticAnalyzer(poglinVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def report_error(self, message, line, column):
        error_msg = f"ERRO SEMÂNTICO [Linha {line}, Coluna {column}]: {message}"
        print(error_msg)
        self.errors.append(error_msg)

    def visitProgram(self, ctx: poglinParser.ProgramContext):
        self.symbol_table.enter_scope()
        result = self.visitChildren(ctx)
        self.symbol_table.exit_scope()
        return len(self.errors) == 0

    def visitStatement(self, ctx: poglinParser.StatementContext):
        if ctx.VAR():
            var_name = ctx.ID().getText()
            declared_type_text = ctx.type_().getText()
            declared_type = declared_type_text.capitalize()

            if self.symbol_table.is_declared_in_current_scope(var_name):
                self.report_error(f"Variável '{var_name}' já declarada no escopo atual.", ctx.start.line, ctx.start.column)
            else:
                expr_type_info = self.visit(ctx.expression())
                expr_type = expr_type_info.get('type', 'Unknown')
                if expr_type != declared_type:
                    self.report_error(
                        f"Tipo incompatível para '{var_name}': esperado '{declared_type}', encontrado '{expr_type}'.",
                        ctx.start.line, ctx.start.column
                    )
                self.symbol_table.declare(var_name, declared_type)

        elif ctx.ID() and ctx.expression():
            var_name = ctx.ID().getText()
            if not self.symbol_table.is_declared(var_name):
                self.report_error(f"Variável '{var_name}' não declarada.", ctx.start.line, ctx.start.column)
            else:
                var_type = self.symbol_table.get_type(var_name)
                expr_type_info = self.visit(ctx.expression())
                expr_type = expr_type_info.get('type', 'Unknown')
                if expr_type != var_type:
                    self.report_error(
                        f"Atribuição inválida para '{var_name}': esperado '{var_type}', encontrado '{expr_type}'.",
                        ctx.start.line, ctx.start.column
                    )

        return self.visitChildren(ctx)

    def visitExpression(self, ctx: poglinParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitLogicalOrExpression(self, ctx: poglinParser.LogicalOrExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalAndExpression(0))

        left_type_info = self.visit(ctx.logicalAndExpression(0))
        right_type_info = self.visit(ctx.logicalAndExpression(1))

        if left_type_info['type'] != 'Bool' or right_type_info['type'] != 'Bool':
            self.report_error("Operador '||' requer operandos booleanos.", ctx.start.line, ctx.start.column)
        return {'type': 'Bool', 'line': ctx.start.line, 'column': ctx.start.column}

    def visitLogicalAndExpression(self, ctx: poglinParser.LogicalAndExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equalityExpression(0))

        left_type_info = self.visit(ctx.equalityExpression(0))
        right_type_info = self.visit(ctx.equalityExpression(1))

        if left_type_info['type'] != 'Bool' or right_type_info['type'] != 'Bool':
            self.report_error("Operador '&&' requer operandos booleanos.", ctx.start.line, ctx.start.column)
        return {'type': 'Bool', 'line': ctx.start.line, 'column': ctx.start.column}

    def visitEqualityExpression(self, ctx: poglinParser.EqualityExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpression(0))

        left_type_info = self.visit(ctx.relationalExpression(0))
        right_type_info = self.visit(ctx.relationalExpression(1))

        if left_type_info['type'] != right_type_info['type']:
            self.report_error("Operadores de igualdade requerem operandos do mesmo tipo.", ctx.start.line, ctx.start.column)
        return {'type': 'Bool', 'line': ctx.start.line, 'column': ctx.start.column}

    def visitRelationalExpression(self, ctx: poglinParser.RelationalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additiveExpression(0))

        left_type_info = self.visit(ctx.additiveExpression(0))
        right_type_info = self.visit(ctx.additiveExpression(1))

        if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
            self.report_error("Operadores relacionais requerem operandos inteiros.", ctx.start.line, ctx.start.column)
        return {'type': 'Bool', 'line': ctx.start.line, 'column': ctx.start.column}

    def visitAdditiveExpression(self, ctx: poglinParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        left = self.visit(ctx.multiplicativeExpression(0))
        right = self.visit(ctx.multiplicativeExpression(1))
        op_token = ctx.PLUS()[0] if ctx.PLUS() else ctx.MINUS()[0]

        if op_token.getText() == '+':
            if left['type'] == 'String' or right['type'] == 'String':
                return {'type': 'String', 'line': op_token.symbol.line, 'column': op_token.symbol.column}

        if left['type'] != 'Int' or right['type'] != 'Int':
            self.report_error("Operadores '+' e '-' requerem operandos inteiros.", op_token.symbol.line, op_token.symbol.column)
        return {'type': 'Int', 'line': op_token.symbol.line, 'column': op_token.symbol.column}

    def visitMultiplicativeExpression(self, ctx: poglinParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpression(0))

        left_type_info = self.visit(ctx.unaryExpression(0))
        right_type_info = self.visit(ctx.unaryExpression(1))
        op_token = ctx.MULT()[0] if ctx.MULT() else ctx.DIV()[0]

        if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
            self.report_error("Operadores '*' e '/' requerem operandos inteiros.", op_token.symbol.line, op_token.symbol.column)

        if op_token.getText() == '/' and 'value' in right_type_info and right_type_info['value'] == 0:
            self.report_error("Divisão por zero.", op_token.symbol.line, op_token.symbol.column)

        if 'value' in left_type_info and 'value' in right_type_info:
            left_val = left_type_info['value']
            right_val = right_type_info['value']
            result = 0
            if op_token.getText() == '*':
                result = left_val * right_val
            elif op_token.getText() == '/' and right_val != 0:
                result = left_val // right_val
            return {'type': 'Int', 'line': op_token.symbol.line, 'column': op_token.symbol.column, 'value': result}

        return {'type': 'Int', 'line': op_token.symbol.line, 'column': op_token.symbol.column}

    def visitPrimary(self, ctx: poglinParser.PrimaryContext):
        if ctx.INT():
            return {'type': 'Int', 'line': ctx.start.line, 'column': ctx.start.column, 'value': int(ctx.getText())}
        elif ctx.STRING():
            return {'type': 'String', 'line': ctx.start.line, 'column': ctx.start.column, 'value': ctx.getText()}
        elif ctx.ID():
            var_name = ctx.getText()
            if not self.symbol_table.is_declared(var_name):
                self.report_error(f"Variável '{var_name}' não declarada.", ctx.start.line, ctx.start.column)
                return {'type': 'Unknown', 'line': ctx.start.line, 'column': ctx.start.column}
            return {'type': self.symbol_table.get_type(var_name), 'line': ctx.start.line, 'column': ctx.start.column}
        elif ctx.READLINE():
            return {'type': 'String', 'line': ctx.start.line, 'column': ctx.start.column}
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            self.report_error("Expressão primária não reconhecida.", ctx.start.line, ctx.start.column)
            return {'type': 'Error', 'line': ctx.start.line, 'column': ctx.start.column}
