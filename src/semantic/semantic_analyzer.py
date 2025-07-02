# src/semantic/semantic_analyzer.py
import sys
from src.lexer.poglinParser import poglinParser
from src.lexer.poglinVisitor import poglinVisitor
from src.semantic.symbol_table import SymbolTable

class SemanticAnalyzer(poglinVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.current_function_type = None 
        self.poglin_types = {
            poglinParser.INT_TYPE: 'Int',
            poglinParser.STRING_TYPE: 'String'
        }

    def report_error(self, message, line=None, column=None):
        if line is not None and column is not None:
            self.errors.append(f"ERRO SEMÂNTICO [Linha {line}, Coluna {column}]: {message}")
        else:
            self.errors.append(f"ERRO SEMÂNTICO: {message}")
        print(self.errors[-1], file=sys.stderr)

    def get_errors(self):
        return self.errors

    # Visitar a regra principal 'program'
    def visitProgram(self, ctx: poglinParser.ProgramContext):
        self.symbol_table.enter_scope() # Escopo global
        self.visitChildren(ctx)
        self.symbol_table.exit_scope()
        return len(self.errors) == 0 # Retorna True se nao houver erros

    # Visitar a regra 'statement'
    # Esta é uma regra multiplexada, entao precisamos verificar qual alternativa casou
    def visitStatement(self, ctx: poglinParser.StatementContext):
        if ctx.VAR(): # var ID : type = expression;
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column
            
            # Verificacao de declaracao duplicada
            success, error_msg = self.symbol_table.declare_symbol(var_name, None, var_line, var_column) # Tipo sera inferido/verificado
            if not success:
                self.report_error(error_msg, var_line, var_column)
                return None # Nao continua processando este statement para evitar erros em cascata
            
            # Obtem o tipo declarado
            declared_type_text = ctx.type_().getText()
            declared_poglin_type = self.poglin_types.get(getattr(poglinParser, declared_type_text + '_TYPE', None), declared_type_text)

            # Visita a expressao de inicializacao para obter seu tipo
            expr_type_info = self.visit(ctx.expression())
            if expr_type_info:
                expr_poglin_type = expr_type_info['type']
                expr_line = expr_type_info['line']
                expr_column = expr_type_info['column']
                
                # Verificacao de compatibilidade de tipos na inicializacao
                if declared_poglin_type != expr_poglin_type:
                    self.report_error(f"Incompatibilidade de tipos na inicialização de '{var_name}': esperado '{declared_poglin_type}', encontrado '{expr_poglin_type}'.", expr_line, expr_column)
                else:
                    # Atualiza o tipo na tabela de simbolos
                    self.symbol_table.lookup_symbol(var_name)['type'] = declared_poglin_type
            else:
                # Se a expressao de inicializacao teve erro, o tipo nao pode ser inferido
                self.report_error(f"Expressão de inicialização inválida para '{var_name}'.", var_line, var_column)
            
            return None # Retorna None pois ja processamos

        elif ctx.ASSIGN() and not ctx.READLINE(): # ID = expression; (reatribuição)
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column
            
            # Verificacao de declaracao previa
            symbol_info = self.symbol_table.lookup_symbol(var_name)
            if not symbol_info:
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return None
            
            # Visita a expressao do lado direito para obter seu tipo
            expr_type_info = self.visit(ctx.expression())
            if expr_type_info:
                expr_poglin_type = expr_type_info['type']
                expr_line = expr_type_info['line']
                expr_column = expr_type_info['column']
                
                # Verificacao de compatibilidade de tipos na atribuicao
                if symbol_info['type'] != expr_poglin_type:
                    self.report_error(f"Incompatibilidade de tipos na atribuição para '{var_name}': esperado '{symbol_info['type']}', encontrado '{expr_poglin_type}'.", expr_line, expr_column)
            else:
                self.report_error(f"Expressão inválida na atribuição para '{var_name}'.", var_line, var_column)
            return None

        elif ctx.PRINTLN(): # println(expression);
            expr_type_info = self.visit(ctx.expression())
            # println pode aceitar Int ou String, entao nao precisa de verificacao de tipo aqui.
            # Apenas garantimos que a expressao foi visitada.
            return None
            
        elif ctx.ASSIGN() and ctx.READLINE(): # ID = readLine();
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column
            
            # Verificacao de declaracao previa
            symbol_info = self.symbol_table.lookup_symbol(var_name)
            if not symbol_info:
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return None
            
            # readLine retorna String, entao a variavel deve ser String
            if symbol_info['type'] != 'String':
                self.report_error(f"Variável '{var_name}' do tipo '{symbol_info['type']}' não pode receber entrada de 'readLine()'. Esperado 'String'.", var_line, var_column)
            return None

        elif ctx.IF():
            self.visit(ctx.expression()) # Visita a condicao
            
            self.symbol_table.enter_scope() # Novo escopo para o bloco THEN
            # Lógica para visitar statements dentro do THEN block
            # (Reutiliza a lógica de iteração de blocos do ASTGenerator)
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
                    break # Importante sair aqui para não pegar statements do ELSE
                if in_current_block and isinstance(child, poglinParser.StatementContext):
                    self.visit(child)
            self.symbol_table.exit_scope() # Sai do escopo THEN

            if ctx.ELSE():
                self.symbol_table.enter_scope() # Novo escopo para o bloco ELSE
                # Lógica para visitar statements dentro do ELSE block
                in_current_block = False
                brace_count = 0
                for child in ctx.children:
                    if child == ctx.LBRACE(1): # LBRACE(1) para o ELSE
                        in_current_block = True
                        brace_count += 1
                        continue
                    if child == ctx.RBRACE(1) and brace_count == 1: # RBRACE(1) para o ELSE
                        in_current_block = False
                        brace_count -= 1
                        break
                    if in_current_block and isinstance(child, poglinParser.StatementContext):
                        self.visit(child)
                self.symbol_table.exit_scope() # Sai do escopo ELSE
            return None

        elif ctx.WHILE():
            self.visit(ctx.expression()) # Visita a condicao
            
            self.symbol_table.enter_scope() # Novo escopo para o bloco LOOP
            # Lógica para visitar statements dentro do LOOP block
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
            self.symbol_table.exit_scope() # Sai do escopo LOOP
            return None
        
        elif ctx.POG():
            return None # Nao faz verificacao semantica para 'pog;'

        return self.visitChildren(ctx) # Default: continua a visita para outras regras de statement


    # Métodos para visitar expressões e retornar seus tipos
    # Cada método de expressão deve retornar um dicionário: {'type': 'Int'/'String', 'line': int, 'column': int}
    
    def visitLogicalOrExpression(self, ctx: poglinParser.LogicalOrExpressionContext):
        left_type_info = self.visit(ctx.logicalAndExpression(0))
        if len(ctx.logicalAndExpression()) > 1: # Se tiver operador OR
            right_type_info = self.visit(ctx.logicalAndExpression(1))
            
            if left_type_info and right_type_info:
                # Operadores logicos esperam Int (para booleanos)
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '||' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", ctx.OR().symbol.line, ctx.OR().symbol.column)
                    return {'type': 'Error', 'line': ctx.OR().symbol.line, 'column': ctx.OR().symbol.column}
                return {'type': 'Int', 'line': ctx.OR().symbol.line, 'column': ctx.OR().symbol.column}
        return left_type_info

    def visitLogicalAndExpression(self, ctx: poglinParser.LogicalAndExpressionContext):
        left_type_info = self.visit(ctx.equalityExpression(0))
        if len(ctx.equalityExpression()) > 1: # Se tiver operador AND
            right_type_info = self.visit(ctx.equalityExpression(1))

            if left_type_info and right_type_info:
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '&&' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", ctx.AND().symbol.line, ctx.AND().symbol.column)
                    return {'type': 'Error', 'line': ctx.AND().symbol.line, 'column': ctx.AND().symbol.column}
                return {'type': 'Int', 'line': ctx.AND().symbol.line, 'column': ctx.AND().symbol.column}
        return left_type_info

    def visitEqualityExpression(self, ctx: poglinParser.EqualityExpressionContext):
        left_type_info = self.visit(ctx.relationalExpression(0))
        if ctx.EQUALS() or ctx.NEQUALS():
            right_type_info = self.visit(ctx.relationalExpression(1))
            op_symbol = ctx.EQUALS() if ctx.EQUALS() else ctx.NEQUALS()

            if left_type_info and right_type_info:
                # Igualdade pode ser entre Int e Int, ou String e String
                if left_type_info['type'] != right_type_info['type']:
                    self.report_error(f"Operador '{op_symbol.getText()}' espera operandos do mesmo tipo, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_symbol.symbol.line, op_symbol.symbol.column)
                    return {'type': 'Error', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                return {'type': 'Int', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column} # Retorna Int para booleanos
        return left_type_info

    def visitRelationalExpression(self, ctx: poglinParser.RelationalExpressionContext):
        left_type_info = self.visit(ctx.additiveExpression(0))
        if ctx.LT() or ctx.LTE() or ctx.GT() or ctx.GTE():
            right_type_info = self.visit(ctx.additiveExpression(1))
            op_symbol = None
            if ctx.LT(): op_symbol = ctx.LT()
            elif ctx.LTE(): op_symbol = ctx.LTE()
            elif ctx.GT(): op_symbol = ctx.GT()
            elif ctx.GTE(): op_symbol = ctx.GTE()

            if left_type_info and right_type_info:
                # Operadores relacionais esperam Int
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_symbol.getText()}' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_symbol.symbol.line, op_symbol.symbol.column)
                    return {'type': 'Error', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                return {'type': 'Int', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
        return left_type_info

    def visitAdditiveExpression(self, ctx: poglinParser.AdditiveExpressionContext):
        left_type_info = self.visit(ctx.multiplicativeExpression(0))
        if ctx.PLUS() or ctx.MINUS():
            right_type_info = self.visit(ctx.multiplicativeExpression(1))
            op_symbol = ctx.PLUS() if ctx.PLUS() else ctx.MINUS()

            if left_type_info and right_type_info:
                # Soma/Subtracao: Int com Int
                # Pode haver concatenacao de String com String ou String com Int
                if op_symbol == ctx.PLUS(): # Apenas o '+' pode ser usado para concatenacao
                    if left_type_info['type'] == 'String' and right_type_info['type'] == 'String':
                        return {'type': 'String', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                    if left_type_info['type'] == 'String' and right_type_info['type'] == 'Int':
                        return {'type': 'String', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                    if left_type_info['type'] == 'Int' and right_type_info['type'] == 'String':
                        return {'type': 'String', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                
                # Para Int, Int + Int ou Int - Int
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_symbol.getText()}' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_symbol.symbol.line, op_symbol.symbol.column)
                    return {'type': 'Error', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                return {'type': 'Int', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
        return left_type_info

    def visitMultiplicativeExpression(self, ctx: poglinParser.MultiplicativeExpressionContext):
        left_type_info = self.visit(ctx.unaryExpression(0))
        if ctx.MULT() or ctx.DIV():
            right_type_info = self.visit(ctx.unaryExpression(1))
            op_symbol = ctx.MULT() if ctx.MULT() else ctx.DIV()

            if left_type_info and right_type_info:
                # Multiplicacao/Divisao esperam Int
                if left_type_info['type'] != 'Int' or right_type_info['type'] != 'Int':
                    self.report_error(f"Operador '{op_symbol.getText()}' espera operandos Int, encontrado '{left_type_info['type']}' e '{right_type_info['type']}'.", op_symbol.symbol.line, op_symbol.symbol.column)
                    return {'type': 'Error', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
                
                # Verificacao de divisao por zero
                if ctx.DIV() and right_type_info['value'] == 0: # Isso requer que a expressao tenha um valor, o que eh dificil na fase semantica
                    # Para divisao por zero, precisaríamos do valor da expressão,
                    # o que só é possível em tempo de execução ou com avaliação constante.
                    # Por enquanto, apenas verificamos os tipos.
                    # Uma verificação mais robusta de divisão por zero virá na geração de código.
                    pass # Será feito mais adiante.
                
                return {'type': 'Int', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
        return left_type_info

    def visitUnaryExpression(self, ctx: poglinParser.UnaryExpressionContext):
        if ctx.NOT():
            operand_type_info = self.visit(ctx.unaryExpression())
            op_symbol = ctx.NOT()
            if operand_type_info and operand_type_info['type'] != 'Int':
                self.report_error(f"Operador '!' espera operando Int, encontrado '{operand_type_info['type']}'.", op_symbol.symbol.line, op_symbol.symbol.column)
                return {'type': 'Error', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
            return {'type': 'Int', 'line': op_symbol.symbol.line, 'column': op_symbol.symbol.column}
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: poglinParser.PrimaryContext):
        if ctx.INT():
            return {'type': 'Int', 'value': int(ctx.INT().getText()), 'line': ctx.INT().symbol.line, 'column': ctx.INT().symbol.column}
        elif ctx.STRING():
            return {'type': 'String', 'value': ctx.STRING().getText(), 'line': ctx.STRING().symbol.line, 'column': ctx.STRING().symbol.column}
        elif ctx.ID():
            var_name = ctx.ID().getText()
            var_line = ctx.ID().symbol.line
            var_column = ctx.ID().symbol.column
            symbol_info = self.symbol_table.lookup_symbol(var_name)
            if not symbol_info:
                self.report_error(f"Variável '{var_name}' não declarada.", var_line, var_column)
                return {'type': 'Error', 'line': var_line, 'column': var_column}
            return {'type': symbol_info['type'], 'line': var_line, 'column': var_column}
        elif ctx.expression():
            return self.visit(ctx.expression())
        return {'type': 'Error', 'line': ctx.start.line, 'column': ctx.start.column} # Fallback para expressao primaria invalida