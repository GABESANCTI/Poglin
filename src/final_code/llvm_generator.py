# src/final_code/llvm_generator.py
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

        # Inicializa target triple e datalayout corretos para a máquina local
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
        elif isinstance(operand.value, str) and operand.value.startswith('"') and operand.value.endswith('"'):
            actual_string = operand.value[1:-1] + '\0'
            byte_array = bytearray(actual_string.encode('utf8'))
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

        for scope in self.symbol_table.scopes:
            for name, var_type in scope.items():
                if name not in self.variables:
                    llvm_type = self._get_llvm_type(var_type)
                    alloca = self.builder.alloca(llvm_type, name=f"var_{name}")
                    self.variables[name] = alloca
                    if var_type == 'Int':
                        self.builder.store(ir.Constant(self.i32, 0), alloca)
                    elif var_type == 'String':
                        self.builder.store(ir.Constant(self.i8_ptr, None), alloca)

    def _generate_llvm_for_tac_instruction(self, instr: TACInstruction):
        op = instr.opcode

        if op == "ASSIGN":
            value = self._get_llvm_value(instr.arg1)
            dest_alloca = self.variables[instr.dest.value]
            self.builder.store(value, dest_alloca)

        elif op in ("ADD", "SUB", "MUL", "DIV"):
            left = self._get_llvm_value(instr.arg1)
            right = self._get_llvm_value(instr.arg2)
            if op == "ADD":
                result = self.builder.add(left, right, name=instr.dest.value)
            elif op == "SUB":
                result = self.builder.sub(left, right, name=instr.dest.value)
            elif op == "MUL":
                result = self.builder.mul(left, right, name=instr.dest.value)
            elif op == "DIV":
                result = self.builder.sdiv(left, right, name=instr.dest.value)
            self.temporaries[instr.dest.value] = result

        elif op in ("EQ", "NEQ", "LT", "LE", "GT", "GE"):
            left = self._get_llvm_value(instr.arg1)
            right = self._get_llvm_value(instr.arg2)
            cmp_map = {
                "EQ": "==", "NEQ": "!=", "LT": "<", "LE": "<=", "GT": ">", "GE": ">="
            }
            result = self.builder.icmp_signed(cmp_map[op], left, right, name=instr.dest.value)
            self.temporaries[instr.dest.value] = result

        elif op in ("AND", "OR"):
            left = self._get_llvm_value(instr.arg1)
            right = self._get_llvm_value(instr.arg2)
            if op == "AND":
                result = self.builder.and_(left, right, name=instr.dest.value)
            elif op == "OR":
                result = self.builder.or_(left, right, name=instr.dest.value)
            self.temporaries[instr.dest.value] = result

        elif op == "NOT":
            value = self._get_llvm_value(instr.arg1)
            result = self.builder.not_(value, name=instr.dest.value)
            self.temporaries[instr.dest.value] = result

        elif op == "JUMP":
            label = self.labels[instr.dest.value]
            self.builder.branch(label)

        elif op == "IFZ":  # Se falso, pula
            condition = self._get_llvm_value(instr.arg1)
            false_block = self.labels[instr.dest.value]
            next_block = self.function.append_basic_block(name="ifz_next")
            self.builder.cbranch(condition, next_block, false_block)
            self.builder.position_at_end(next_block)

        elif op == "PRINT":
            value = self._get_llvm_value(instr.arg1)
            fmt_ptr = self.builder.gep(self.int_fmt_nl, [self.i32(0), self.i32(0)]) if instr.arg1.type == "Int" else self.builder.gep(self.str_fmt_nl, [self.i32(0), self.i32(0)])
            self.builder.call(self.printf, [fmt_ptr, value])

        elif op == "READ":
            dest_alloca = self.variables[instr.dest.value]
            fmt_ptr = self.builder.gep(self.read_int_fmt, [self.i32(0), self.i32(0)]) if instr.dest.type == "Int" else self.builder.gep(self.read_str_fmt, [self.i32(0), self.i32(0)])
            self.builder.call(self.scanf, [fmt_ptr, dest_alloca])

        elif op == "LABEL":
            # Já tratado no loop principal
            pass

        else:
            print(f"WARNING: Operação TAC não implementada: {instr}")
