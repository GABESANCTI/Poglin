grammar poglin;

// Palavras-chave (DEFINIR ANTES de ID!)
START: 'start';
END: 'end';
VAR: 'var';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
ESCREVA: 'escreva';
LEIA: 'leia';
POG: 'pog';

INT_TYPE: 'Int';
STRING_TYPE: 'String';

// Operadores e símbolos
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

EQUALS: '==';
NEQUALS: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COLON: ':';
ASSIGN: '=';

// Literais e identificadores
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
INT: [0-9]+ ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"' ;

// Espaços e comentários
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;

// ------------------ Regras ------------------

program: START LBRACE statement* RBRACE END ;

statement
    : VAR ID COLON type ASSIGN expression SEMI          #varDeclaration
    | ID ASSIGN expression SEMI                         #assignment
    | ESCREVA LPAREN expression RPAREN SEMI             #printStatement
    | ID ASSIGN LEIA LPAREN RPAREN SEMI                 #readStatement
    | IF LPAREN expression RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)? #ifStatement
    | WHILE LPAREN expression RPAREN LBRACE statement* RBRACE                                #whileStatement
    | POG SEMI                                          #pogStatement
    ;

expression: logicalOrExpression ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression (AND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQUALS | NEQUALS) relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((LT | LTE | GT | GTE) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((MULT | DIV) unaryExpression)*
    ;

unaryExpression
    : NOT unaryExpression
    | primary
    ;

primary
    : INT
    | STRING
    | ID
    | LPAREN expression RPAREN
    ;

type: INT_TYPE | STRING_TYPE ;
