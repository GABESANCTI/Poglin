class TACOperand:
    def __init__(self, value, is_temp=False, is_label=False):
        self.value = value
        self.is_temp = is_temp
        self.is_label = is_label

    def __str__(self):
        if self.is_temp:
            return f"@{self.value}"
        elif self.is_label:
            return f"${self.value}"
        
        elif isinstance(self.value, str) and self.value.startswith('"') and self.value.endswith('"'):
            return self.value

        return str(self.value)

    def __repr__(self):
        return self.__str__()


class TACInstruction:
    def __init__(self, opcode, dest=None, src1=None, src2=None):
        self.opcode = opcode
        self.dest = dest
        self.src1 = src1
        self.src2 = src2

    def __str__(self):
        parts = [self.opcode]
        if self.dest:
            parts.append(str(self.dest))
        if self.src1:
            parts.append(str(self.src1))
        if self.src2:
            parts.append(str(self.src2))
        return " ".join(parts)

    def __repr__(self):
        return self.__str__()