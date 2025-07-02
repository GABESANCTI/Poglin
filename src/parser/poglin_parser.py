# src/parser/poglin_parser.py
import sys
from antlr4.error.ErrorListener import ErrorListener
from src.lexer.poglinParser import poglinParser # Importa o parser gerado

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"ERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg.replace('at ', 'encontrado ')}"
        print(error_message, file=sys.stderr)
        # Ao levantar uma exceção, a execução do compilador pode ser interrompida aqui.
        raise Exception("Erro Sintático Encontrado.")

class PoglinParserAnalyzer:
    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.parser_successful = False
        self.parse_tree = None
        self.parser = None # Armazena a instância do parser para acesso posterior (e.g., para o toStringTree)

    def analyze(self):
        self.parser = poglinParser(self.token_stream)
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(CustomErrorListener())

        try:
            # Chama a regra inicial da gramática 'program'
            self.parse_tree = self.parser.program()
            self.parser_successful = True
        except Exception as e:
            self.parser_successful = False
            # A mensagem de erro já foi impressa pelo CustomErrorListener

        return self.parser_successful

    def get_parse_tree(self):
        return self.parse_tree

    def is_successful(self):
        return self.parser_successful