import sys
import os
from src.lexer.poglin_lexer import PoglinLexerAnalyzer
from src.parser.poglin_parser import PoglinParserAnalyzer
from src.ast.ast_generator import ASTGenerator
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.intermediario.tac_generator import TACGenerator
from src.final_code.llvm_generator import LLVMGenerator 

def compile_poglin(file_path, output_ast=False, output_tac=False, output_llvm=False):
    print(f"--- Compilando arquivo: {os.path.basename(file_path)} ---")
    
    # 1. Análise Léxica: Converte o código fonte em tokens.
    print(f"\nIniciando Análise Léxica para: {file_path}")
    lexer_analyzer = PoglinLexerAnalyzer(file_path)
    if not lexer_analyzer.analyze():
        print("\nAnálise Léxica falhou. Abortando compilação.")
        return False
    print("\nAnálise Léxica concluída com sucesso.")

    # 2. Análise Sintática: Constrói a árvore de parse e valida a estrutura.
    print(f"\nIniciando Análise Sintática para: {file_path}")
    token_stream_for_parser = lexer_analyzer.get_antlr_token_stream()
    parser_analyzer = PoglinParserAnalyzer(token_stream_for_parser)
    if not parser_analyzer.analyze():
        print("\nAnálise Sintática falhou. Abortando compilação.")
        return False
    print("Análise Sintática concluída com sucesso.")

    # 3. Geração da AST (Opcional): Converte a árvore de parse em uma AST e gera visualização.
    if output_ast:
        print("\nIniciando Geração da AST...")
        ast_generator = ASTGenerator(parser_analyzer.parser)
        parse_tree = parser_analyzer.get_parse_tree()
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_dir = "output"
        ast_generator.generate_ast(parse_tree, os.path.join(output_dir, f"{base_name}_ast"))
    
    # 4. Análise Semântica: Verifica a lógica, tipos e escopos do programa.
    print(f"\nIniciando Análise Semântica para: {file_path}")
    semantic_analyzer = SemanticAnalyzer()
    parse_tree = parser_analyzer.get_parse_tree()
    
    if not semantic_analyzer.visit(parse_tree):
        print("\nAnálise Semântica falhou. Erros encontrados:")
        for error in semantic_analyzer.get_errors():
            print(error)
        return False
    print("Análise Semântica concluída com sucesso. Nenhum erro encontrado.")

    # 5. Geração de Código Intermediário (TAC): Traduz a AST em Código de Três Endereços.
    print(f"\nIniciando Geração de Código Intermediário (TAC) para: {file_path}")
    tac_generator = TACGenerator()
    tac_generator.set_symbol_table(semantic_analyzer.symbol_table)
    tac_generator.visit(parse_tree)
    
    tac_instructions = tac_generator.get_tac()
    
    if output_tac:
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        tac_output_file = os.path.join("output", f"{base_name}.tac")
        with open(tac_output_file, "w") as f:
            for instr in tac_instructions:
                f.write(str(instr) + "\n")
        print(f"Código TAC gerado com sucesso em {tac_output_file}")
    else:
        print("\n--- Código TAC Gerado ---")
        for instr in tac_instructions:
            print(instr)
        print("\nGeração de Código Intermediário (TAC) concluída com sucesso.")

    # 6. Geração de Código Final (LLVM IR): Converte o TAC em LLVM Intermediate Representation.
    if output_llvm:
        print(f"\nIniciando Geração de Código Final (LLVM IR) para: {file_path}")
        llvm_generator = LLVMGenerator(tac_instructions, semantic_analyzer.symbol_table)
        llvm_ir_code = llvm_generator.generate()

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        llvm_output_file = os.path.join("output", f"{base_name}.ll")
        with open(llvm_output_file, "w") as f:
            f.write(llvm_ir_code)
        print(f"Código LLVM IR gerado com sucesso em {llvm_output_file}")
        print("\n--- Código LLVM IR Gerado ---\n")
        print(llvm_ir_code)

    else:
        print("\nSkipping LLVM IR generation.") 

    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_arquivo_poglin.pog> [--ast] [--tac] [--llvm]")
        print("Exemplo: python main.py tests/valid_program.pog --ast --tac --llvm")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    generate_ast_flag = False
    generate_tac_flag = False
    generate_llvm_flag = False
    
    for arg in sys.argv[2:]:
        if arg == "--ast":
            generate_ast_flag = True
        elif arg == "--tac":
            generate_tac_flag = True
        elif arg == "--llvm":
            generate_llvm_flag = True
        
    output_dir = "output"
    if (generate_ast_flag or generate_tac_flag or generate_llvm_flag) and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(input_file):
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
        sys.exit(1)

    compile_poglin(input_file, generate_ast_flag, generate_tac_flag, generate_llvm_flag)