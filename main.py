# main.py (ATUALIZADO)
import sys
import os
from src.lexer.poglin_lexer import PoglinLexerAnalyzer
from src.parser.poglin_parser import PoglinParserAnalyzer
from src.ast.ast_generator import ASTGenerator
from src.semantic.semantic_analyzer import SemanticAnalyzer # Importa o analisador semantico

def compile_poglin(file_path, output_ast=False):
    print(f"--- Compilando arquivo: {os.path.basename(file_path)} ---")
    
    # Análise Léxica
    print(f"\nIniciando Análise Léxica para: {file_path}")
    lexer_analyzer = PoglinLexerAnalyzer(file_path)
    if not lexer_analyzer.analyze():
        print("\nAnálise Léxica falhou. Abortando compilação.")
        return False

    tokens_data = lexer_analyzer.get_token_data_list()
    print("\n--- Tokens Gerados ---")
    for token_info in tokens_data:
        print(f"<Tipo: {token_info['type']}, Lexema: '{token_info['lexeme']}', Linha: {token_info['line']}, Coluna: {token_info['column']}>")
    print("\nAnálise Léxica concluída com sucesso.")

    # Análise Sintática
    print(f"\nIniciando Análise Sintática para: {file_path}")
    token_stream_for_parser = lexer_analyzer.get_antlr_token_stream()
    parser_analyzer = PoglinParserAnalyzer(token_stream_for_parser)
    if not parser_analyzer.analyze():
        print("\nAnálise Sintática falhou. Abortando compilação.")
        return False
    print("Análise Sintática concluída com sucesso.")

    # Geração da AST (Opcional)
    if output_ast:
        print("\nIniciando Geração da AST...")
        ast_generator = ASTGenerator(parser_analyzer.parser)
        parse_tree = parser_analyzer.get_parse_tree()
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_dir = "output"
        ast_generator.generate_ast(parse_tree, os.path.join(output_dir, f"{base_name}_ast"))
    
    # Análise Semântica (NOVA ETAPA)
    print(f"\nIniciando Análise Semântica para: {file_path}")
    semantic_analyzer = SemanticAnalyzer()
    parse_tree = parser_analyzer.get_parse_tree() # Reutiliza a arvore de parse
    
    if semantic_analyzer.visit(parse_tree): # O visitor retorna True se nao houver erros
        print("Análise Semântica concluída com sucesso. Nenhum erro encontrado.")
        return True
    else:
        print("\nAnálise Semântica falhou. Erros encontrados:")
        for error in semantic_analyzer.get_errors():
            print(error)
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_arquivo_poglin.pog> [--ast]")
        print("Exemplo: python main.py tests/valid_program.pog --ast")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    generate_ast_flag = False
    if len(sys.argv) > 2 and sys.argv[2] == "--ast":
        generate_ast_flag = True
        
    output_dir = "output"
    if generate_ast_flag and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(input_file):
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
        sys.exit(1)

    compile_poglin(input_file, generate_ast_flag)