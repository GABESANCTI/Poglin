# main.py
import sys
from src.lexer.poglin_lexer import PoglinLexerAnalyzer
from src.parser.poglin_parser import PoglinParserAnalyzer

def compile_poglin(file_path):
    print(f"Iniciando Análise Léxica para: {file_path}")
    lexer_analyzer = PoglinLexerAnalyzer(file_path)
    
    # Executa a análise léxica
    if not lexer_analyzer.analyze():
        print("\nAnálise Léxica falhou. Abortando compilação.")
        return False

    # Exibe os tokens gerados (para depuração)
    tokens_data = lexer_analyzer.get_token_data_list()
    print("\n--- Tokens Gerados ---")
    for token_info in tokens_data:
        print(f"<Tipo: {token_info['type']}, Lexema: '{token_info['lexeme']}', Linha: {token_info['line']}, Coluna: {token_info['column']}>")
    print("\nAnálise Léxica concluída com sucesso.")

    # Início da Análise Sintática
    print(f"\nIniciando Análise Sintática para: {file_path}")
    
    # Pega o CommonTokenStream do analisador léxico para passar ao analisador sintático
    token_stream_for_parser = lexer_analyzer.get_antlr_token_stream()
    parser_analyzer = PoglinParserAnalyzer(token_stream_for_parser)
    
    # Executa a análise sintática
    if parser_analyzer.analyze():
        print("Análise Sintática concluída com sucesso.")
        # Você pode inspecionar a parse_tree aqui, se precisar.
        # print(parser_analyzer.get_parse_tree().toStringTree(recog=parser_analyzer.parser))
        
        # Próximo passo: Geração da AST visualizável
        # ... (será implementado na próxima etapa)
        return True
    else:
        print("\nAnálise Sintática falhou. Abortando compilação.")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_arquivo_poglin.pog>") # AQUI FOI ALTERADO!
        sys.exit(1)
    
    input_file = sys.argv[1]
    compile_poglin(input_file)