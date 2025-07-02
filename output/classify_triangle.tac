LABEL $L0
ASSIGN a 3
ASSIGN b 4
ASSIGN c 5
LTE @_t0 a 0
LTE @_t1 b 0
OR @_t2 @_t0 @_t1
IF_TRUE @_t2 $L1
GOTO $L2
LABEL $L1
PRINT "Medidas invalidas: Lados devem ser positivos."
GOTO $L3
LABEL $L2
ADD @_t3 a b
GT @_t4 @_t3 c
ADD @_t5 a c
GT @_t6 @_t5 b
AND @_t7 @_t4 @_t6
IF_TRUE @_t7 $L4
GOTO $L5
LABEL $L4
EQ @_t8 a b
EQ @_t9 b c
AND @_t10 @_t8 @_t9
IF_TRUE @_t10 $L7
GOTO $L8
LABEL $L7
PRINT "Triangulo equilatero valido."
GOTO $L9
LABEL $L8
EQ @_t11 a b
EQ @_t12 a c
OR @_t13 @_t11 @_t12
IF_TRUE @_t13 $L10
GOTO $L11
LABEL $L10
PRINT "Triangulo isosceles valido."
GOTO $L12
LABEL $L11
PRINT "Triangulo escaleno valido."
LABEL $L12
LABEL $L9
GOTO $L6
LABEL $L5
PRINT "Medidas invalidas: Nao formam um triangulo."
LABEL $L6
LABEL $L3
POG_OP
EXIT
