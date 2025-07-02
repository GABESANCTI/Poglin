import sys
import os
from src.lexer.poglin_lexer import PoglinLexerAnalyzer
from src.parser.poglin_parser import PoglinParserAnalyzer
from src.ast.ast_generator import ASTGenerator

def compile_poglin(file_path, output_ast=False):
    print(f"--- Compilando arquivo: {os.path.basename(file_path)} ---")
    
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

    print(f"\nIniciando Análise Sintática para: {file_path}")
    token_stream_for_parser = lexer_analyzer.get_antlr_token_stream()
    parser_analyzer = PoglinParserAnalyzer(token_stream_for_parser)
    
    if parser_analyzer.analyze():
        print("Análise Sintática concluída com sucesso.")
        
        if output_ast:
            print("\nIniciando Geração da AST...")
            # É importante passar a instância do parser para o ASTGenerator se você for usar parser.ruleNames
            # ou outras propriedades da gramática que o gerador pode precisar para depuração ou rótulos.
            ast_generator = ASTGenerator(parser_analyzer.parser) 
            parse_tree = parser_analyzer.get_parse_tree()
            
            # Define o nome do arquivo de saída da AST
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_dir = "output"
            ast_generator.generate_ast(parse_tree, os.path.join(output_dir, f"{base_name}_ast"))
            
        return True
    else:
        print("\nAnálise Sintática falhou. Abortando compilação.")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_arquivo_poglin.pog> [--ast]")
        print("Exemplo: python main.py tests/valid_program.pog --ast")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Verifica se a flag --ast foi passada
    generate_ast_flag = False
    if len(sys.argv) > 2 and sys.argv[2] == "--ast":
        generate_ast_flag = True
        
    # Crie o diretório 'output' se não existir, antes de tentar salvar arquivos lá
    output_dir = "output"
    if generate_ast_flag and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_file):
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
        sys.exit(1)

    compile_poglin(input_file, generate_ast_flag)