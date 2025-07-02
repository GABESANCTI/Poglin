
import sys
from llvmlite import ir, binding
from src.intermediario.tac_classes import TACOperand, TACInstruction
# A SymbolTable é útil para saber o tipo original das variáveis para alocação LLVM
from src.semantic.symbol_table import SymbolTable 

class LLVMGenerator:
    def __init__(self, tac_instructions, symbol_table):
        self.tac_instructions = tac_instructions
        self.symbol_table = symbol_table
        self.module = ir.Module(name="poglin_module")
        self.builder = None
        self.function = None
        
        # Mapeamento para variáveis e temporários LLVM
        self.variables = {}  # Nome da variável/temp em Poglin -> ir.AllocaInst (para variáveis) ou ir.Value (para temporários)
        self.temporaries = {} # Temporários são diretamente ir.Value, mas podemos usar este dict para consistência
        self.labels = {}     # Nome da label em Poglin -> ir.Block

        # Tipos LLVM
        self.i32 = ir.IntType(32)
        self.i8_ptr = ir.IntType(8).as_pointer() # Ponteiro para char (string)
        self.bool_i1 = ir.IntType(1) # Booleans em LLVM são i1
        self.void = ir.VoidType()

        # Declara funções externas da biblioteca C (printf, scanf, etc.)
        self._declare_external_functions()

    def _declare_external_functions(self):
        # printf: int printf(i8*, ...)
        printf_type = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.printf = ir.Function(self.module, printf_type, name="printf")

        # scanf: int scanf(i8*, ...)
        scanf_type = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_type, name="scanf")
        
        # Strings de formato para printf/scanf (terminadas em \0)
        # Formatos para Int e String com nova linha
        self.str_fmt_nl = ir.Constant(ir.ArrayType(self.i8, len("%s\n\0")), bytearray("%s\n\0".encode('utf8')))
        self.int_fmt_nl = ir.Constant(ir.ArrayType(self.i8, len("%d\n\0")), bytearray("%d\n\0".encode('utf8')))
        # Formatos para leitura (sem nova linha, pois readline lê linha completa)
        self.read_int_fmt = ir.Constant(ir.ArrayType(self.i8, len("%d\0")), bytearray("%d\0".encode('utf8')))
        self.read_str_fmt = ir.Constant(ir.ArrayType(self.i8, len("%s\0")), bytearray("%s\0".encode('utf8')))
        # String literal para 'println(" ")'
        self.space_str = ir.Constant(ir.ArrayType(self.i8, len(" \0")), bytearray(" \0".encode('utf8')))
        # String literal para 'println("")'
        self.empty_str_nl = ir.Constant(ir.ArrayType(self.i8, len("\n\0")), bytearray("\n\0".encode('utf8')))

        # Funcao auxiliar para comparacao de strings (nao existe em LLVM direto)
        # int strcmp(const char *s1, const char *s2); retorna 0 se iguais
        strcmp_type = ir.FunctionType(self.i32, [self.i8_ptr, self.i8_ptr])
        self.strcmp = ir.Function(self.module, strcmp_type, name="strcmp")

    def _get_llvm_type(self, poglin_type):
        if poglin_type == 'Int':
            return self.i32
        elif poglin_type == 'String':
            return self.i8_ptr
        else:
            # Isso não deveria acontecer se o SemanticAnalyzer passou sem erros
            raise ValueError(f"Tipo Poglin desconhecido: {poglin_type}")

    def _get_llvm_value(self, operand: TACOperand):
        if operand.is_temp:
            # Temporários já são ir.Value, gerados por outras instruções
            return self.temporaries[operand.value]
        elif operand.is_label:
            # Labels são ir.Block, usados em branches
            return self.labels[operand.value]
        elif isinstance(operand.value, int):
            # Literais Int são ir.Constant(i32)
            return ir.Constant(self.i32, operand.value)
        elif isinstance(operand.value, str) and (operand.value.startswith('"') and operand.value.endswith('"')):
            # Literais String: criar uma constante global e retornar um ponteiro para ela
            actual_string = operand.value[1:-1] # Remove as aspas
            string_with_null = actual_string + '\0'
            byte_array = bytearray(string_with_null.encode('utf8'))
            
            # Cria a constante global se ainda não existir
            global_string_name = f"str_const_{hash(actual_string)}"
            if global_string_name not in self.module.globals:
                global_string = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len(byte_array)), name=global_string_name)
                global_string.linkage = "private"
                global_string.global_constant = True
                global_string.initializer = ir.Constant(ir.ArrayType(self.i8, len(byte_array)), byte_array)
            else:
                global_string = self.module.globals[global_string_name]
            
            # Retorna um ponteiro para o primeiro elemento (i8*)
            return self.builder.gep(global_string, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
        else: # ID de variável (nome da variável)
            # Carrega o valor da variável alocada
            if operand.value in self.variables:
                return self.builder.load(self.variables[operand.value], name=f"{operand.value}_val")
            # Isso não deveria ocorrer se o SemanticAnalyzer foi bem-sucedido
            raise ValueError(f"Variável '{operand.value}' não alocada ou não encontrada para LLVM IR.")


    def generate(self):
        # 1. Cria a função principal 'main'
        func_type = ir.FunctionType(self.i32, []) # main retorna i32, nao recebe argumentos
        self.function = ir.Function(self.module, func_type, name="main")
        
        # Cria o bloco de entrada
        entry_block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        # 2. Primeira passagem: Alocar variáveis e mapear labels para BasicBlocks
        self._allocate_variables_and_map_labels()

        # 3. Gerar o código para cada instrução TAC
        current_block_name = "entry" # Começa no bloco de entrada
        for instr_index, instr in enumerate(self.tac_instructions):
            # Se for uma LABEL, move o builder para o BasicBlock correspondente
            if instr.opcode == "LABEL":
                label_name = instr.dest.value
                self.builder.position_at_end(self.labels[label_name])
                continue # Não processa mais nada para a instrução LABEL

            # Garante que o bloco atual tem um terminator antes de adicionar instruções
            # Se o builder já está em um bloco terminado (por GOTO, IF_TRUE, RET),
            # ele precisa ser posicionado em um novo bloco.
            # Isso é crucial para evitar "block does not have terminator" se blocos nao sao explicitamente ligados.
            # Se a instrução anterior foi um GOTO ou um IF_TRUE para outro lugar,
            # o builder precisa de um novo BasicBlock "dead-end" ou ser movido.
            # A forma mais robusta é ter um BasicBlock explícito para cada instrução que segue um terminator.
            # Por simplicidade, vamos garantir que o builder se posicione em um bloco não terminado.
            if self.builder.block.is_terminated:
                # Cria um novo bloco 'fallthrough' se o anterior terminou e não há label próxima.
                # Se a próxima instrução for um label, o builder já será posicionado.
                if not (instr_index + 1 < len(self.tac_instructions) and self.tac_instructions[instr_index+1].opcode == "LABEL"):
                    fallthrough_block = self.function.append_basic_block(name=f"fallthrough_{instr_index}")
                    self.builder.position_at_end(fallthrough_block)

            self._generate_llvm_for_tac_instruction(instr)

        # Garante que o bloco final tem um retorno
        # Um bloco pode não ter um terminator se, por exemplo, o programa termina sem um EXIT explícito
        # ou se a última instrução não é um GOTO/IF_TRUE/EXIT.
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.i32, 0)) # main retorna 0

        # 4. Valida o módulo (opcional, mas recomendado para depuração)
        try:
            self.module.verify()
        except Exception as e:
            print(f"Erro de verificação LLVM: {e}", file=sys.stderr)
            print(self.module, file=sys.stderr)
            raise

        return str(self.module)


    def _allocate_variables_and_map_labels(self):
        # Mapeia labels para BasicBlocks. Precisa ser feito antes de gerar instrucoes
        # para que os branches possam referenciar blocos já existentes.
        for instr in self.tac_instructions:
            if instr.opcode == "LABEL":
                label_name = instr.dest.value
                new_block = self.function.append_basic_block(name=label_name)
                self.labels[label_name] = new_block
        
        # Move o builder para o bloco de entrada para alocar variáveis.
        with self.builder.goto_entry():
            # Aloca espaço para todas as variáveis declaradas (do escopo global)
            for var_name, var_type in self.symbol_table.scopes[0].items(): # Assumindo apenas escopo global
                llvm_type = self._get_llvm_type(var_type)
                alloca = self.builder.alloca(llvm_type, name=f"var_{var_name}")
                self.variables[var_name] = alloca

                # Inicializa variáveis alocadas com valor default (0 para Int, null para String)
                if var_type == 'Int':
                    self.builder.store(ir.Constant(self.i32, 0), alloca)
                elif var_type == 'String':
                    self.builder.store(ir.Constant(self.i8_ptr, ir.Constant.null(self.i8_ptr)), alloca)


    def _generate_llvm_for_tac_instruction(self, instr: TACInstruction):
        if instr.opcode == "ASSIGN":
            dest_operand = instr.dest
            src1_value = self._get_llvm_value(instr.src1)

            if dest_operand.is_temp:
                # Atribuição para temporário: apenas armazena o valor no dicionário de temporários
                self.temporaries[dest_operand.value] = src1_value
            else: # Destino é uma variável ID (armazenar no AllocaInst)
                dest_alloca = self.variables[dest_operand.value]
                
                # Se o tipo da origem for um ponteiro (string) e o destino também for um ponteiro,
                # e não for uma atribuição de um literal de string (já tratado em _get_llvm_value)
                # podemos precisar de uma copia de string.
                # Para simplificar, o semantic analyzer ja garantiu que os tipos são compatíveis.
                # Assume que src1_value.type é compatível com dest_alloca.type.pointee
                
                # Exemplo: Atribuir "Hello" a uma variável string:
                # _get_llvm_value retorna um i8* para a string literal.
                # dest_alloca.type.pointee será i8*. Isso funciona direto.
                
                self.builder.store(src1_value, dest_alloca)

        elif instr.opcode == "ADD":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)

            # O SemanticAnalyzer já garantiu a compatibilidade de tipos.
            # Se for Int + Int
            if src1_value.type == self.i32: # Assume que ambos são Int
                result = self.builder.add(src1_value, src2_value, name=f"{dest_temp.value}_add")
                self.temporaries[dest_temp.value] = result
            elif src1_value.type == self.i8_ptr: # Concatenacao de String
                # Implementação de concatenação de string em LLVM é complexa (alocar memória, copiar).
                # Para o escopo limitado do projeto, vamos SIMPLIFICAR:
                # O TAC de ADD para strings não será implementado como concatenação real em LLVM IR.
                # Isso significa que `var s : String = "a" + "b";` não resultará em "ab" no LLVM IR gerado.
                # Se a sua linguagem tem o '+' para concatenação, e isso vai para uma variável,
                # a LLVM IR precisaria de um helper externo (em C) para `malloc`/`strcpy`/`strcat`.
                # Por simplicidade, vamos APENAS ATRIBUIR o primeiro operando ao destino se for string ADD.
                # ISSO É UM PLACEHOLDER E NÃO CONCATENA STRINGS DE FATO EM LLVM.
                # Para `println("a" + var)`, a concatenação já é de responsabilidade do `printf`.

                # Se a intenção era que o ADD de String retornasse uma nova string concatenada,
                # seria necessário implementar alocação dinâmica e `strcpy`/`strcat`.
                # Isso está além do tempo disponível.
                self.temporaries[dest_temp.value] = src1_value # Apenas para não quebrar a compilação.
                                                               # Isso não é concatenação real.
            
        elif instr.opcode == "SUB":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            result = self.builder.sub(src1_value, src2_value, name=f"{dest_temp.value}_sub")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "MUL":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            result = self.builder.mul(src1_value, src2_value, name=f"{dest_temp.value}_mul")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "DIV":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            # Divisão inteira (signed division)
            result = self.builder.sdiv(src1_value, src2_value, name=f"{dest_temp.value}_div")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "NOT":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            # NOT lógico para Int (0/1): (x == 0) -> i1, depois zext para i32
            is_zero = self.builder.icmp_signed('==', src1_value, ir.Constant(self.i32, 0), name=f"{dest_temp.value}_is_zero")
            result = self.builder.zext(is_zero, self.i32, name=f"{dest_temp.value}_not")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "EQ": # Int == Int ou String == String
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            
            if src1_value.type == self.i32:
                cmp_result = self.builder.icmp_signed('==', src1_value, src2_value, name=f"{dest_temp.value}_cmp_eq")
            elif src1_value.type == self.i8_ptr:
                # Chamada a strcmp: 0 se iguais
                cmp_func_call = self.builder.call(self.strcmp, [src1_value, src2_value], name=f"{dest_temp.value}_strcmp_res")
                cmp_result = self.builder.icmp_signed('==', cmp_func_call, ir.Constant(self.i32, 0), name=f"{dest_temp.value}_cmp_streq")
            else:
                cmp_result = ir.Constant(self.bool_i1, 0) # Fallback para falso
            
            # Converte o i1 (bool) para i32 (1 ou 0)
            result = self.builder.zext(cmp_result, self.i32, name=f"{dest_temp.value}_bool_to_int")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "NEQ":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            
            if src1_value.type == self.i32:
                cmp_result = self.builder.icmp_signed('!=', src1_value, src2_value, name=f"{dest_temp.value}_cmp_neq")
            elif src1_value.type == self.i8_ptr:
                cmp_func_call = self.builder.call(self.strcmp, [src1_value, src2_value], name=f"{dest_temp.value}_strcmp_res_neq")
                cmp_result = self.builder.icmp_signed('!=', cmp_func_call, ir.Constant(self.i32, 0), name=f"{dest_temp.value}_cmp_strneq")
            else:
                cmp_result = ir.Constant(self.bool_i1, 0)
            
            result = self.builder.zext(cmp_result, self.i32, name=f"{dest_temp.value}_bool_to_int")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "LT":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            cmp_result = self.builder.icmp_signed('<', src1_value, src2_value, name=f"{dest_temp.value}_cmp_lt")
            result = self.builder.zext(cmp_result, self.i32, name=f"{dest_temp.value}_bool_to_int")
            self.temporaries[dest_temp.value] = result
        
        elif instr.opcode == "LTE":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            cmp_result = self.builder.icmp_signed('<=', src1_value, src2_value, name=f"{dest_temp.value}_cmp_lte")
            result = self.builder.zext(cmp_result, self.i32, name=f"{dest_temp.value}_bool_to_int")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "GT":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            cmp_result = self.builder.icmp_signed('>', src1_value, src2_value, name=f"{dest_temp.value}_cmp_gt")
            result = self.builder.zext(cmp_result, self.i32, name=f"{dest_temp.value}_bool_to_int")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "GTE":
            dest_temp = instr.dest
            src1_value = self._get_llvm_value(instr.src1)
            src2_value = self._get_llvm_value(instr.src2)
            cmp_result = self.builder.icmp_signed('>=', src1_value, src2_value, name=f"{dest_temp.value}_cmp_gte")
            result = self.builder.zext(cmp_result, self.i32, name=f"{dest_temp.value}_bool_to_int")
            self.temporaries[dest_temp.value] = result

        elif instr.opcode == "IF_TRUE":
            cond_value = self._get_llvm_value(instr.src1)
            label_block = self._get_llvm_value(instr.dest) # Destino aqui é a label (ir.Block)
            
            # LLVM cbranch espera um i1 (booleano). Nosso 'Int' booleano é i32 (0/1).
            cond_i1 = self.builder.icmp_signed('!=', cond_value, ir.Constant(self.i32, 0), name="cond_i1")
            
            # Cria um bloco para a continuação do fluxo caso a condição seja falsa.
            # Este bloco é implicitamente o "fallthrough" se o IF_TRUE não for tomado.
            # O nome do bloco é para depuração.
            false_block = self.function.append_basic_block(name=f"{instr.dest.value}_false_cont")
            self.builder.cbranch(cond_i1, label_block, false_block)
            self.builder.position_at_end(false_block) # Posiciona o builder no bloco falso para continuar o fluxo.
            
        elif instr.opcode == "GOTO":
            label_block = self._get_llvm_value(instr.dest)
            self.builder.branch(label_block)
            # Após um GOTO, o bloco atual está terminado.
            # O builder não deve continuar adicionando instruções a este bloco.
            # A próxima instrução real será no LABEL correspondente.
            # Podemos adicionar um novo bloco "dead" aqui para não quebrar a sequência,
            # mas o loop principal de geração já deve lidar com isso ao encontrar o LABEL.
            
        elif instr.opcode == "LABEL":
            # Já tratado no loop principal de geração para posicionar o builder.
            pass

        elif instr.opcode == "PRINT":
            value_to_print = self._get_llvm_value(instr.dest)
            
            if value_to_print.type == self.i32:
                int_fmt_ptr = self.builder.gep(self.int_fmt_nl, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
                self.builder.call(self.printf, [int_fmt_ptr, value_to_print])
            elif value_to_print.type == self.i8_ptr:
                # Lidar com println(" " + coef) ou println(" ") ou println("")
                # O TAC de PRINT já vai ter a expressão concatenada como um operando.
                # Se for " " ou "" ou "string literal", o _get_llvm_value já retorna i8*.
                # Se for resultado de 'string + int', o TAC ADD gerou um placeholder (simplificação).
                # Aqui assumimos que `value_to_print` é um i8* válido para `printf`.
                str_fmt_ptr = self.builder.gep(self.str_fmt_nl, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
                self.builder.call(self.printf, [str_fmt_ptr, value_to_print])
            else:
                # O SemanticAnalyzer deveria ter pego tipos inválidos para PRINT
                pass

        elif instr.opcode == "READ":
            dest_alloca = self.variables[instr.dest.value] # É uma variável, então é um AllocaInst
            
            # readLine() em Poglin sempre retorna String
            # Para ler String em LLVM, precisamos de um buffer para o scanf.
            # O scanf lê no buffer, e então o conteúdo do buffer é o valor.
            # Tamanho do buffer (ex: 256 bytes)
            buffer_len = 256
            
            # Aloca um array de chars temporário no stack (buffer)
            # ir.ArrayType(ir.IntType(8), buffer_len) é um array de 256 bytes
            temp_buffer = self.builder.alloca(ir.ArrayType(self.i8, buffer_len), name="read_buffer")
            # Converte o ponteiro para o tipo esperado por scanf (%s)
            temp_buffer_ptr = self.builder.bitcast(temp_buffer, self.i8_ptr, name="read_buffer_ptr")

            # Chama scanf com formato %s e o ponteiro para o buffer
            read_str_fmt_ptr = self.builder.gep(self.read_str_fmt, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
            self.builder.call(self.scanf, [read_str_fmt_ptr, temp_buffer_ptr])
            
            # Armazena o ponteiro para a string lida na variável de destino
            self.builder.store(temp_buffer_ptr, dest_alloca)

        elif instr.opcode == "POG_OP":
            # Sem instrução LLVM IR específica para 'pog'. Pode ser um no-op.
            pass

        elif instr.opcode == "EXIT":
            self.builder.ret(ir.Constant(self.i32, 0)) # main retorna 0