
import sys
from llvmlite import ir, binding
from src.intermediario.tac_classes import TACOperand, TACInstruction
from src.semantic.symbol_table import *
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

        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

        target = binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        self.module.triple = binding.get_default_triple()
        self.module.data_layout = target_machine.target_data

    def _declare_external_functions(self):
        printf_type = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.printf = ir.Function(self.module, printf_type, name="printf")

        scanf_type = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_type, name="scanf")

        self.str_fmt_nl = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len("%s\n\0")), name="str_fmt_nl")
        self.str_fmt_nl.linkage = 'internal'
        self.str_fmt_nl.global_constant = True
        self.str_fmt_nl.initializer = ir.Constant(ir.ArrayType(self.i8, len("%s\n\0")), bytearray("%s\n\0".encode('utf8')))

        self.int_fmt_nl = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len("%d\n\0")), name="int_fmt_nl")
        self.int_fmt_nl.linkage = 'internal'
        self.int_fmt_nl.global_constant = True
        self.int_fmt_nl.initializer = ir.Constant(ir.ArrayType(self.i8, len("%d\n\0")), bytearray("%d\n\0".encode('utf8')))

        self.read_int_fmt = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len("%d\0")), name="read_int_fmt")
        self.read_int_fmt.linkage = 'internal'
        self.read_int_fmt.global_constant = True
        self.read_int_fmt.initializer = ir.Constant(ir.ArrayType(self.i8, len("%d\0")), bytearray("%d\0".encode('utf8')))

        self.read_str_fmt = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len("%s\0")), name="read_str_fmt")
        self.read_str_fmt.linkage = 'internal'
        self.read_str_fmt.global_constant = True
        self.read_str_fmt.initializer = ir.Constant(ir.ArrayType(self.i8, len("%s\0")), bytearray("%s\0".encode('utf8')))

        self.temp_str_buffer = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, 256), name="temp_str_buffer")
        self.temp_str_buffer.linkage = "internal"
        self.temp_str_buffer.global_constant = False
        self.temp_str_buffer.initializer = ir.Constant(ir.ArrayType(self.i8, 256), bytearray(256))

    def _get_llvm_type(self, poglin_type):
        if poglin_type == 'Int':
            return self.i32
        elif poglin_type == 'String':
            return self.i8_ptr
        else:
            raise ValueError(f"Tipo Poglin desconhecido: {poglin_type}")

    def _ensure_variable_allocated(self, name):
        if name not in self.variables:
            guessed_type = self.i32  # default Int
            if self.symbol_table:
                for scope in self.symbol_table.scopes:
                    if name in scope:
                        guessed_type = self._get_llvm_type(scope[name])
                        break
            alloca = self.builder.alloca(guessed_type, name=f"var_{name}")
            self.variables[name] = alloca
        return self.variables[name]

    def _get_llvm_value(self, operand: TACOperand):
        if operand is None:
            raise ValueError("Operando nulo encontrado durante a geração de LLVM IR. Verifique o gerador de TAC.")
        
        if operand.is_temp:
            if operand.value not in self.temporaries:
                raise ValueError(f"Temporária '{operand.value}' não alocada na geração LLVM.")
            return self.temporaries[operand.value]
        elif operand.is_label:
            if operand.value not in self.labels:
                raise ValueError(f"Label '{operand.value}' não encontrada na geração LLVM.")
            return self.labels[operand.value]
        elif isinstance(operand.value, int):
            return ir.Constant(self.i32, operand.value)
        elif isinstance(operand.value, str) and operand.value.startswith('"') and operand.value.endswith('"'):
            actual_string = operand.value[1:-1] + '\0'
            byte_array = bytearray(actual_string.encode('utf8'))
            global_string_name = f"str_const_{abs(hash(actual_string))}"

            if global_string_name not in self.module.globals:
                global_string = ir.GlobalVariable(self.module, ir.ArrayType(self.i8, len(byte_array)), name=global_string_name)
                global_string.linkage = "private"
                global_string.global_constant = True
                global_string.initializer = ir.Constant(ir.ArrayType(self.i8, len(byte_array)), byte_array)
            else:
                global_string = self.module.globals[global_string_name]

            return self.builder.gep(global_string, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
        else:
            var_alloca = self._ensure_variable_allocated(operand.value)
            return self.builder.load(var_alloca, name=f"{operand.value}_val")

    def generate(self):
        func_type = ir.FunctionType(self.i32, [])
        self.function = ir.Function(self.module, func_type, name="main")
        entry_block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        self._allocate_variables_and_map_labels()

        for idx, instr in enumerate(self.tac_instructions):
            if instr.opcode == "LABEL":
                self.builder.position_at_end(self.labels[instr.dest.value])
                continue

            if self.builder.block.is_terminated:
                if not (idx + 1 < len(self.tac_instructions) and self.tac_instructions[idx+1].opcode == "LABEL"):
                    fall_block = self.function.append_basic_block(name=f"fall_{idx}")
                    self.builder.position_at_end(fall_block)

            self._generate_llvm_for_tac_instruction(instr)

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.i32, 0))

        return str(self.module)

    def _allocate_variables_and_map_labels(self):
        for instr in self.tac_instructions:
            if instr.opcode == "LABEL":
                self.labels[instr.dest.value] = self.function.append_basic_block(instr.dest.value)

        self.builder.position_at_end(self.function.entry_basic_block)

        if hasattr(self.symbol_table, "global_snapshot"):
            for name, var_type in self.symbol_table.global_snapshot.items():
                self._ensure_variable_allocated(name)
        else:
            for scope in self.symbol_table.scopes:
                for name, var_type in scope.items():
                    self._ensure_variable_allocated(name)

    def _generate_llvm_for_tac_instruction(self, instr: TACInstruction):
        op = instr.opcode

        if op == "ASSIGN":
            value = self._get_llvm_value(instr.src1)
            alloca = self._ensure_variable_allocated(instr.dest.value)
            self.builder.store(value, alloca)

        elif op == "ADD":
            left = self._get_llvm_value(instr.src1)
            right = self._get_llvm_value(instr.src2)
            result = self.builder.add(left, right, name=instr.dest.value)
            self.temporaries[instr.dest.value] = result

        elif op == "PRINT":
            src = instr.src1 if instr.src1 is not None else instr.dest
            value = self._get_llvm_value(src)

            is_int = False
            if isinstance(src.value, int):
                is_int = True
            else:
                var_type = None
                if self.symbol_table:
                    for scope in self.symbol_table.scopes:
                        if src.value in scope:
                            var_type = scope[src.value]
                            break
                is_int = (var_type == "Int")

            fmt_global = self.int_fmt_nl if is_int else self.str_fmt_nl
            fmt_ptr = self.builder.gep(fmt_global, [ir.Constant(self.i32, 0), ir.Constant(self.i32, 0)])
            self.builder.call(self.printf, [fmt_ptr, value])

        elif op == "EXIT":
            self.builder.ret(ir.Constant(self.i32, 0))
