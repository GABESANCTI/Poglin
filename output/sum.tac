LABEL $L0
ASSIGN num1_str "0"
ASSIGN num2_str "0"
ASSIGN sum_result ""
PRINT "Digite o primeiro numero:"
READ num1_str
PRINT "Digite o segundo numero:"
READ num2_str
ADD @_t0 num1_str num2_str
ASSIGN sum_result @_t0
ADD @_t1 "A concatenacao e: " sum_result
PRINT @_t1
POG_OP
EXIT
