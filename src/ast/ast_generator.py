import sys
from antlr4 import ParseTreeVisitor
from src.lexer.poglinVisitor import poglinVisitor
from src.lexer.poglinParser import poglinParser
from graphviz import Digraph

class ASTGenerator(poglinVisitor):
    def __init__(self, parser_instance=None):
        self.dot = Digraph(comment='Abstract Syntax Tree', graph_attr={'rankdir': 'TB'})
        self.node_count = 0
        self.parser = parser_instance # Necessario para obter nomes simbolicos dos tokens
        self.node_map = {} # Mapeia contextos do ANTLR para nos da AST
        
    def new_node(self, label, context):
        node_id = f'node{self.node_count}'
        self.node_count += 1
        self.dot.node(node_id, label)
        self.node_map[context] = node_id
        return node_id

    def add_edge(self, parent_id, child_id, label=''):
        if child_id: # Adiciona verificacao para garantir que child_id nao e None
            self.dot.edge(parent_id, child_id, label=label)

    # Métodos visit para as regras da gramática
    def visitProgram(self, ctx: poglinParser.ProgramContext):
        node_id = self.new_node("PROGRAM", ctx)
        for statement_ctx in ctx.statement():
            child_id = self.visit(statement_ctx)
            self.add_edge(node_id, child_id) # add_edge ja tem a verificacao
        return node_id

    def visitStatement(self, ctx: poglinParser.StatementContext):
        # Cada alternativa da regra 'statement' é verificada
        if ctx.VAR():
            # VAR ID COLON type ASSIGN expression SEMI
            node_id = self.new_node("VAR_DECLARATION", ctx)
            id_node = self.new_node(f"ID: {ctx.ID().getText()}", ctx.ID())
            self.add_edge(node_id, id_node, "name")
            
            type_node = self.visit(ctx.type_())
            self.add_edge(node_id, type_node, "type")

            expr_node = self.visit(ctx.expression()) # ctx.expression() existe aqui
            self.add_edge(node_id, expr_node, "value")
            return node_id
        
        elif ctx.ASSIGN() and ctx.READLINE():
            # ID ASSIGN READLINE LPAREN RPAREN SEMI
            node_id = self.new_node("READLINE_ASSIGNMENT", ctx) # Nome mais claro
            id_node = self.new_node(f"ID: {ctx.ID().getText()}", ctx.ID())
            self.add_edge(node_id, id_node, "target")
            return node_id

        elif ctx.ASSIGN(): # Isso significa ID ASSIGN expression SEMI (reatribuição)
            node_id = self.new_node("ASSIGNMENT", ctx)
            id_node = self.new_node(f"ID: {ctx.ID().getText()}", ctx.ID())
            self.add_edge(node_id, id_node, "target")
            
            expr_node = self.visit(ctx.expression()) # ctx.expression() existe aqui
            self.add_edge(node_id, expr_node, "value")
            return node_id

        elif ctx.PRINTLN():
            # PRINTLN LPAREN expression RPAREN SEMI
            node_id = self.new_node("PRINTLN_CALL", ctx)
            expr_node = self.visit(ctx.expression()) # ctx.expression() existe aqui
            self.add_edge(node_id, expr_node, "argument")
            return node_id
            
        elif ctx.IF():
            node_id = self.new_node("IF_STATEMENT", ctx)
            
            # Condição
            cond_node = self.visit(ctx.expression())
            self.add_edge(node_id, cond_node, "condition")
            
            # Bloco THEN:
            # Vamos iterar pelos filhos do contexto para encontrar os statements do THEN.
            # Assumimos que o primeiro '{' e '}' delimitam o THEN block.
            then_block_id = self.new_node("THEN_BLOCK", ctx.LBRACE(0))
            self.add_edge(node_id, then_block_id)
            
            in_current_block = False
            brace_count = 0
            # Percorre todos os filhos do contexto 'if'
            for child in ctx.children:
                if child == ctx.LBRACE(0): # Início do bloco THEN
                    in_current_block = True
                    brace_count += 1
                    continue
                if child == ctx.RBRACE(0) and brace_count == 1: # Fim do bloco THEN
                    in_current_block = False
                    brace_count -=1
                    continue # Sai do loop para este bloco
                
                if in_current_block and isinstance(child, poglinParser.StatementContext):
                    child_ast_node_id = self.visit(child)
                    if child_ast_node_id: self.add_edge(then_block_id, child_ast_node_id)
            
            # Bloco ELSE (se existir)
            if ctx.ELSE():
                else_block_id = self.new_node("ELSE_BLOCK", ctx.LBRACE(1))
                self.add_edge(node_id, else_block_id)

                in_current_block = False
                brace_count = 0
                for child in ctx.children:
                    if child == ctx.LBRACE(1): # Início do bloco ELSE
                        in_current_block = True
                        brace_count += 1
                        continue
                    if child == ctx.RBRACE(1) and brace_count == 1: # Fim do bloco ELSE
                        in_current_block = False
                        brace_count -= 1
                        continue
                    
                    if in_current_block and isinstance(child, poglinParser.StatementContext):
                        child_ast_node_id = self.visit(child)
                        if child_ast_node_id: self.add_edge(else_block_id, child_ast_node_id)
            return node_id

        elif ctx.WHILE():
            node_id = self.new_node("WHILE_LOOP", ctx)
            self.add_edge(node_id, self.visit(ctx.expression()), "condition")
            
            # Bloco do WHILE
            loop_block_id = self.new_node("LOOP_BLOCK", ctx.LBRACE(0))
            self.add_edge(node_id, loop_block_id)

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
                    continue
                
                if in_current_block and isinstance(child, poglinParser.StatementContext):
                    child_ast_node_id = self.visit(child)
                    if child_ast_node_id: self.add_edge(loop_block_id, child_ast_node_id)
            return node_id
        
        elif ctx.POG():
            return self.new_node("POG_STATEMENT", ctx)
        
        # Caso base: se nenhuma das alternativas acima foi casada, pode haver um erro ou uma regra nova
        # Geralmente, esse ponto não deve ser atingido se todas as alternativas são cobertas.
        # Mas para segurança, se o visitChildren for chamado, ele tentará visitar filhos.
        # return self.visitChildren(ctx) # Removido para garantir que sempre retorne um ID de nó específico

    # Types
    def visitType(self, ctx: poglinParser.TypeContext):
        return self.new_node(f"TYPE: {ctx.getText()}", ctx)

    # Expressions (mantidos como estavam, pois eles já eram chamados corretamente)
    def visitLogicalOrExpression(self, ctx: poglinParser.LogicalOrExpressionContext):
        if len(ctx.logicalAndExpression()) > 1: # Se tiver operador OR
            node_id = self.new_node("OR_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.logicalAndExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.logicalAndExpression(1)), "right")
            return node_id
        return self.visit(ctx.logicalAndExpression(0)) # Se nao tiver OR, visita o filho

    def visitLogicalAndExpression(self, ctx: poglinParser.LogicalAndExpressionContext):
        if len(ctx.equalityExpression()) > 1: # Se tiver operador AND
            node_id = self.new_node("AND_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.equalityExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.equalityExpression(1)), "right")
            return node_id
        return self.visit(ctx.equalityExpression(0))

    def visitEqualityExpression(self, ctx: poglinParser.EqualityExpressionContext):
        if ctx.EQUALS():
            node_id = self.new_node("EQ_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.relationalExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.relationalExpression(1)), "right")
            return node_id
        elif ctx.NEQUALS():
            node_id = self.new_node("NEQ_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.relationalExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.relationalExpression(1)), "right")
            return node_id
        return self.visit(ctx.relationalExpression(0))

    def visitRelationalExpression(self, ctx: poglinParser.RelationalExpressionContext):
        if ctx.LT():
            node_id = self.new_node("LT_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.additiveExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.additiveExpression(1)), "right")
            return node_id
        elif ctx.LTE():
            node_id = self.new_node("LTE_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.additiveExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.additiveExpression(1)), "right")
            return node_id
        elif ctx.GT():
            node_id = self.new_node("GT_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.additiveExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.additiveExpression(1)), "right")
            return node_id
        elif ctx.GTE():
            node_id = self.new_node("GTE_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.additiveExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.additiveExpression(1)), "right")
            return node_id
        return self.visit(ctx.additiveExpression(0))

    def visitAdditiveExpression(self, ctx: poglinParser.AdditiveExpressionContext):
        if ctx.PLUS():
            node_id = self.new_node("ADD_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.multiplicativeExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.multiplicativeExpression(1)), "right")
            return node_id
        elif ctx.MINUS():
            node_id = self.new_node("SUB_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.multiplicativeExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.multiplicativeExpression(1)), "right")
            return node_id
        return self.visit(ctx.multiplicativeExpression(0))

    def visitMultiplicativeExpression(self, ctx: poglinParser.MultiplicativeExpressionContext):
        if ctx.MULT():
            node_id = self.new_node("MUL_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.unaryExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.unaryExpression(1)), "right")
            return node_id
        elif ctx.DIV():
            node_id = self.new_node("DIV_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.unaryExpression(0)), "left")
            self.add_edge(node_id, self.visit(ctx.unaryExpression(1)), "right")
            return node_id
        return self.visit(ctx.unaryExpression(0))

    def visitUnaryExpression(self, ctx: poglinParser.UnaryExpressionContext):
        if ctx.NOT():
            node_id = self.new_node("NOT_EXPR", ctx)
            self.add_edge(node_id, self.visit(ctx.unaryExpression()), "operand")
            return node_id
        return self.visit(ctx.primary()) # Unary pode ser NOT ou Primary. Se nao for NOT, eh Primary.

    def visitPrimary(self, ctx: poglinParser.PrimaryContext):
        if ctx.INT():
            return self.new_node(f"INT_LITERAL: {ctx.INT().getText()}", ctx)
        elif ctx.STRING():
            return self.new_node(f"STRING_LITERAL: {ctx.STRING().getText()}", ctx)
        elif ctx.ID():
            return self.new_node(f"ID_REF: {ctx.ID().getText()}", ctx)
        elif ctx.expression(): # Para LPAREN expression RPAREN
            return self.visit(ctx.expression())
        return None # Caso nao caia em nenhum, retorna None (para evitar erro)

    def generate_ast(self, parse_tree, output_filename="ast"):
        # Começa a visita a partir da raiz da árvore de parse
        self.visit(parse_tree)
        try:
            self.dot.render(output_filename, format='png', view=False, cleanup=True) # Adicionado cleanup=True
            print(f"AST gerada com sucesso em {output_filename}.png")
        except Exception as e:
            print(f"Erro ao renderizar a AST com Graphviz: {e}", file=sys.stderr)
            print("Certifique-se de que o Graphviz está instalado e no PATH do sistema.", file=sys.stderr)