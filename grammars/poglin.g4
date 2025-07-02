grammar poglin;

// Palavras-chave
START: 'start';
END: 'end';
VAR: 'var';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINTLN: 'println';
READLINE: 'readLine';
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

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
INT: [0-9]+ ;
STRING: '"' ( ~["\\\r\n] | '\\' . )* '"' ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;

// Regras principais
program: START LBRACE statement* RBRACE END ;

statement
    : VAR ID COLON type ASSIGN expression SEMI
    | ID ASSIGN expression SEMI
    | PRINTLN LPAREN expression RPAREN SEMI
    | ID ASSIGN READLINE LPAREN RPAREN SEMI
    | IF LPAREN expression RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?
    | WHILE LPAREN expression RPAREN LBRACE statement* RBRACE
    | POG SEMI
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