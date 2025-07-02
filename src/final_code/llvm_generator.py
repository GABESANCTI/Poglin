# src/final_code/llvm_generator.py
import sys
from llvmlite import ir, binding
from src.intermediario.tac_classes import TACOperand, TACInstruction
from src.semantic.symbol_table import SymbolTable 

class LLVMGenerator:
    def __init__(self, tac_instructions, symbol_table):
        self.tac_instructions = tac_instructions
        self.symbol_table = symbol_table
        self.module = ir.Module(name="poglin_module")
        self.builder = None
        self.function = None

        self.variables = {}
        self.temporaries = {}
        self.labels = {}

        self.i32 = ir.IntType(32)
        self.i8 = ir.IntType(8)
        self.i8_ptr = self.i8.as_pointer()
        self.bool_i1 = ir.IntType(1)
        self.void = ir.VoidType()

        self._declare_external_functions()

    def _declare_external_functions(self):
        printf_type = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.printf = ir.Function(self.module, printf_type, name="printf")

        scanf_type = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_type, name="scanf")

        self.str_fmt_nl = ir.Constant(ir.ArrayType(self.i8, len("%s\n\0")), bytearray("%s\n\0".encode('utf8')))
        self.int_fmt_nl = ir.Constant(ir.ArrayType(self.i8, len("%d\n\0")), bytearray("%d\n\0".encode('utf8')))
        self.read_int_fmt = ir.Constant(ir.ArrayType(self.i8, len("%d\0")), bytearray("%d\0".encode('utf8')))
        self.read_str_fmt = ir.Constant(ir.ArrayType(self.i8, len("%s\0")), bytearray("%s\0".encode('utf8')))
        self.space_str = ir.Constant(ir.ArrayType(self.i8, len(" \0")), bytearray(" \0".encode('utf8')))
        self.empty_str_nl = ir.Constant(ir.ArrayType(self.i8, len("\n\0")), bytearray("\n\0".encode('utf8')))

        strcmp_type = ir.FunctionType(self.i32, [self.i8_ptr, self.i8_ptr])
        self.strcmp = ir.Function(self.module, strcmp_type, name="strcmp")

    def _get_llvm_type(self, poglin_type):
        if poglin_type == 'Int':
            return self.i32
        elif poglin_type == 'String':
            return self.i8_ptr
        else:
            raise ValueError(f"Tipo Poglin desconhecido: {poglin_type}")

    def _get_llvm_value(self, operand: TACOperand):
        if operand.is_temp:
            return self.temporaries[operand.value]
        elif operand.is_label:
            return self.labels[operand.value]
        elif isinstance(operand.value, int):
            return ir.Constant(self.i32, operand.value)
        elif isinstance(operand.value, str) and (operand.value.startswith('"') and operand.value.endswith('"')):
            actual_string = operand.value[1:-1]
            string_with_null = actual_string + '\0'
            byte_array = bytearray(string_with_null.encode('utf8'))
            global_string_name = f"str_const_{hash(actual_string)}"
            if global_string_name not in self.module.globals:
                global_string = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len(byte_array)), name=global_string_name)
                global_string.linkage = "private"
                global_string.global_constant = True
                global_string.initializer = ir.Constant(ir.ArrayType(self.i8, len(byte_array)), byte_array)
            else:
                global_string = self.module.globals[global_string_name]
            return self.builder.gep(global_string, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
        else:
            if operand.value in self.variables:
                return self.builder.load(self.variables[operand.value], name=f"{operand.value}_val")
            raise ValueError(f"Variável '{operand.value}' não alocada ou não encontrada para LLVM IR.")

    def generate(self):
        func_type = ir.FunctionType(self.i32, [])
        self.function = ir.Function(self.module, func_type, name="main")
        entry_block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        self._allocate_variables_and_map_labels()

        for instr_index, instr in enumerate(self.tac_instructions):
            if instr.opcode == "LABEL":
                label_name = instr.dest.value
                self.builder.position_at_end(self.labels[label_name])
                continue

            if self.builder.block.is_terminated:
                if not (instr_index + 1 < len(self.tac_instructions) and self.tac_instructions[instr_index+1].opcode == "LABEL"):
                    fallthrough_block = self.function.append_basic_block(name=f"fallthrough_{instr_index}")
                    self.builder.position_at_end(fallthrough_block)

            self._generate_llvm_for_tac_instruction(instr)

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.i32, 0))

        return str(self.module)

    def _allocate_variables_and_map_labels(self):
        for instr in self.tac_instructions:
            if instr.opcode == "LABEL":
                label_name = instr.dest.value
                new_block = self.function.append_basic_block(name=label_name)
                self.labels[label_name] = new_block

        for var_name, var_type in self.symbol_table.scopes[0].items():
            llvm_type = self._get_llvm_type(var_type)
            alloca = self.builder.alloca(llvm_type, name=f"var_{var_name}")
            self.variables[var_name] = alloca

            if var_type == 'Int':
                self.builder.store(ir.Constant(self.i32, 0), alloca)
            elif var_type == 'String':
                self.builder.store(ir.Constant(self.i8_ptr, ir.Constant.null(self.i8_ptr)), alloca)

    def _generate_llvm_for_tac_instruction(self, instr: TACInstruction):
        pass  # Aqui você continua com as implementações dos opcodes como no seu original
