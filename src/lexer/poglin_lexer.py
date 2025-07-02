# src/lexer/poglin_lexer.py
import sys
from antlr4 import FileStream, CommonTokenStream
from src.lexer.poglinLexer import poglinLexer 
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        symbol_text = offendingSymbol.text if offendingSymbol else ''
        error_message = f"ERRO LÉXICO [Linha {line}, Coluna {column}]: Símbolo '{symbol_text}' inválido."
        print(error_message, file=sys.stderr)
        raise Exception("Erro Léxico Encontrado.")

class PoglinLexerAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tokens_data = [] 
        self.lexer = None
        self.token_stream = None
        self.has_errors = False

    def analyze(self):
        try:
            input_stream = FileStream(self.file_path, encoding='utf-8')
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.file_path}' não encontrado.", file=sys.stderr)
            return False

        self.lexer = poglinLexer(input_stream)
        self.lexer.removeErrorListeners()
        self.lexer.addErrorListener(CustomErrorListener())

        try:
            self.token_stream = CommonTokenStream(self.lexer)
            self.token_stream.fill() # Processa a entrada e preenche o stream de tokens

            for token in self.token_stream.tokens:
                if token.type != -1: # Ignora o token EOF (-1)
                    self.tokens_data.append({
                        'type': poglinLexer.symbolicNames[token.type],
                        'lexeme': token.text,
                        'line': token.line,
                        'column': token.column
                    })
        except Exception as e:
            self.has_errors = True
            # A mensagem de erro já foi impressa pelo CustomErrorListener
            return False

        return not self.has_errors

    def get_token_data_list(self):
        return self.tokens_data

    def get_antlr_token_stream(self):
        # Retorna o CommonTokenStream que o analisador sintático usará
        return self.token_stream

    def get_antlr_lexer(self):
        # Retorna a instância do PoglinLexer (o lexer gerado pelo ANTLR)
        return self.lexer