from src.lexer.poglinParser import poglinParser
from src.lexer.poglinVisitor import poglinVisitor
from src.intermediario.tac_classes import TACOperand, TACInstruction

class TACGenerator(poglinVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_counter = 0
        self.label_counter = 0
        self.symbol_table = None # Será injetada do SemanticAnalyzer para info de tipos

    def set_symbol_table(self, symbol_table):
        self.symbol_table = symbol_table

    def new_temp(self):
        temp = f"_t{self.temp_counter}"
        self.temp_counter += 1
        return TACOperand(temp, is_temp=True)

    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return TACOperand(label, is_label=True)

    def emit(self, opcode, dest=None, src1=None, src2=None):
        instr = TACInstruction(opcode, dest, src1, src2)
        self.instructions.append(instr)
        return instr

    def get_tac(self):
        return self.instructions

    # Regras principais (visitam filhos e emitem TAC conforme a estrutura)
    def visitProgram(self, ctx: poglinParser.ProgramContext):
        program_start_label = self.new_label() # Etiqueta de inicio do programa
        self.emit("LABEL", program_start_label)
        self.visitChildren(ctx)
        self.emit("EXIT") # Instrução para finalizar o programa
        return None

    def visitStatement(self, ctx: poglinParser.StatementContext):
        if ctx.VAR(): # var ID : type = expression;
            var_name = ctx.ID().getText()
            expr_operand = self.visit(ctx.expression()) # Resultado da expressão de inicialização
            self.emit("ASSIGN", TACOperand(var_name), expr_operand)
            return None

        elif ctx.READLINE(): # ID = readLine();
            var_name = ctx.ID().getText()
            self.emit("READ", TACOperand(var_name))
            return None

        elif ctx.ID() and ctx.ASSIGN() and ctx.expression(): # ID = expression; (reatribuição)
            var_name = ctx.ID().getText()
            expr_operand = self.visit(ctx.expression()) # Resultado da expressão do lado direito
            self.emit("ASSIGN", TACOperand(var_name), expr_operand)
            return None

        elif ctx.PRINTLN(): # println(expression);
            expr_operand = self.visit(ctx.expression()) # Resultado da expressão a ser impressa
            self.emit("PRINT", expr_operand)
            return None
            
        elif ctx.IF(): # if (expression) { statements } else { statements }
            cond_operand = self.visit(ctx.expression()) # Resultado da condição (booleano, 0/1)
            
            then_label = self.new_label()
            else_label = self.new_label()
            end_if_label = self.new_label()

            self.emit("IF_TRUE", cond_operand, then_label) # Se condicao verdadeira, salta para THEN
            self.emit("GOTO", else_label) # Se condicao falsa, salta para ELSE (ou fim se nao tiver ELSE)
            
            # Bloco THEN
            self.emit("LABEL", then_label)
            # A lógica de iteração sobre filhos para blocos é a mesma usada no SemanticAnalyzer e ASTGenerator
            in_then_block = False
            brace_balance = 0
            for child in ctx.children:
                if child == ctx.LBRACE(0): # Início do bloco THEN
                    in_then_block = True
                    brace_balance += 1
                    continue
                if child == ctx.RBRACE(0) and brace_balance == 1: # Fim do bloco THEN
                    in_then_block = False
                    brace_balance -= 1
                    break
                if in_then_block and isinstance(child, poglinParser.StatementContext):
                    self.visit(child)
            
            self.emit("GOTO", end_if_label) # Após o bloco THEN, salta para o fim do IF

            # Bloco ELSE (se presente)
            self.emit("LABEL", else_label) # Etiqueta para o inicio do bloco ELSE
            if ctx.ELSE():
                in_else_block = False
                brace_balance = 0
                for child in ctx.children:
                    if child == ctx.LBRACE(1): # Início do bloco ELSE
                        in_else_block = True
                        brace_balance += 1
                        continue
                    if child == ctx.RBRACE(1) and brace_balance == 1: # Fim do bloco ELSE
                        in_else_block = False
                        brace_balance -= 1
                        break
                    if in_else_block and isinstance(child, poglinParser.StatementContext):
                        self.visit(child)
            
            self.emit("LABEL", end_if_label) # Etiqueta de fim para toda a estrutura IF
            return None

        elif ctx.WHILE(): # while (expression) { statements }
            loop_start_label = self.new_label()
            loop_body_label = self.new_label()
            loop_end_label = self.new_label()

            self.emit("LABEL", loop_start_label) # Início do loop, verifica a condição aqui
            
            cond_operand = self.visit(ctx.expression()) # Resultado da condição do while
            
            self.emit("IF_TRUE", cond_operand, loop_body_label) # Se TRUE, entra no corpo do loop
            self.emit("GOTO", loop_end_label) # Se FALSE, sai do loop

            self.emit("LABEL", loop_body_label) # Etiqueta para o corpo do loop
            # Lógica para visitar statements dentro do corpo do WHILE
            in_loop_body = False
            brace_balance = 0
            for child in ctx.children:
                if child == ctx.LBRACE(0):
                    in_loop_body = True
                    brace_balance += 1
                    continue
                if child == ctx.RBRACE(0) and brace_balance == 1:
                    in_loop_body = False
                    brace_balance -= 1
                    break
                if in_loop_body and isinstance(child, poglinParser.StatementContext):
                    self.visit(child)
            
            self.emit("GOTO", loop_start_label) # Após o corpo, volta para reavaliar a condição

            self.emit("LABEL", loop_end_label) # Etiqueta de fim para o loop
            return None
        
        elif ctx.POG(): # pog;
            self.emit("POG_OP") # Operação simples para 'pog'
            return None

        return self.visitChildren(ctx) # Default para outros statements, se houver

    # Métodos para visitar expressões: retornam o TACOperand que contém o resultado
    def visitLogicalOrExpression(self, ctx: poglinParser.LogicalOrExpressionContext):
        left_operand = self.visit(ctx.logicalAndExpression(0))
        if ctx.OR():
            right_operand = self.visit(ctx.logicalAndExpression(1))
            temp = self.new_temp()
            self.emit("OR", temp, left_operand, right_operand)
            return temp
        return left_operand

    def visitLogicalAndExpression(self, ctx: poglinParser.LogicalAndExpressionContext):
        left_operand = self.visit(ctx.equalityExpression(0))
        if ctx.AND():
            right_operand = self.visit(ctx.equalityExpression(1))
            temp = self.new_temp()
            self.emit("AND", temp, left_operand, right_operand)
            return temp
        return left_operand

    def visitEqualityExpression(self, ctx: poglinParser.EqualityExpressionContext):
        left_operand = self.visit(ctx.relationalExpression(0))
        if ctx.EQUALS():
            right_operand = self.visit(ctx.relationalExpression(1))
            temp = self.new_temp()
            self.emit("EQ", temp, left_operand, right_operand)
            return temp
        elif ctx.NEQUALS():
            right_operand = self.visit(ctx.relationalExpression(1))
            temp = self.new_temp()
            self.emit("NEQ", temp, left_operand, right_operand)
            return temp
        return left_operand

    def visitRelationalExpression(self, ctx: poglinParser.RelationalExpressionContext):
        left_operand = self.visit(ctx.additiveExpression(0))
        if ctx.LT():
            right_operand = self.visit(ctx.additiveExpression(1))
            temp = self.new_temp()
            self.emit("LT", temp, left_operand, right_operand)
            return temp
        elif ctx.LTE():
            right_operand = self.visit(ctx.additiveExpression(1))
            temp = self.new_temp()
            self.emit("LTE", temp, left_operand, right_operand)
            return temp
        elif ctx.GT():
            right_operand = self.visit(ctx.additiveExpression(1))
            temp = self.new_temp()
            self.emit("GT", temp, left_operand, right_operand)
            return temp
        elif ctx.GTE():
            right_operand = self.visit(ctx.additiveExpression(1))
            temp = self.new_temp()
            self.emit("GTE", temp, left_operand, right_operand)
            return temp
        return left_operand

    def visitAdditiveExpression(self, ctx: poglinParser.AdditiveExpressionContext):
        left_operand = self.visit(ctx.multiplicativeExpression(0))
        if ctx.PLUS():
            right_operand = self.visit(ctx.multiplicativeExpression(1))
            temp = self.new_temp()
            self.emit("ADD", temp, left_operand, right_operand)
            return temp
        elif ctx.MINUS():
            right_operand = self.visit(ctx.multiplicativeExpression(1))
            temp = self.new_temp()
            self.emit("SUB", temp, left_operand, right_operand)
            return temp
        return left_operand

    def visitMultiplicativeExpression(self, ctx: poglinParser.MultiplicativeExpressionContext):
        left_operand = self.visit(ctx.unaryExpression(0))
        if ctx.MULT():
            right_operand = self.visit(ctx.unaryExpression(1))
            temp = self.new_temp()
            self.emit("MUL", temp, left_operand, right_operand)
            return temp
        elif ctx.DIV():
            right_operand = self.visit(ctx.unaryExpression(1))
            temp = self.new_temp()
            self.emit("DIV", temp, left_operand, right_operand)
            return temp
        return left_operand

    def visitUnaryExpression(self, ctx: poglinParser.UnaryExpressionContext):
        if ctx.NOT():
            operand = self.visit(ctx.unaryExpression())
            temp = self.new_temp()
            self.emit("NOT", temp, operand)
            return temp
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: poglinParser.PrimaryContext):
        if ctx.INT():
            return TACOperand(int(ctx.INT().getText()))
        elif ctx.STRING():
            return TACOperand(ctx.STRING().getText()) # Mantém as aspas para o TAC
        elif ctx.ID():
            return TACOperand(ctx.ID().getText())
        elif ctx.expression(): # Para LPAREN expression RPAREN
            return self.visit(ctx.expression())
        return None # Caso não seja nenhum tipo primário reconhecido

    def visitType(self, ctx: poglinParser.TypeContext):
        # Tipos são usados na análise semântica, não geram TAC diretamente
        return None