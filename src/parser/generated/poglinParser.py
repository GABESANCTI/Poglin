# Generated from grammars/poglin.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,67,8,1,10,1,12,1,70,9,1,1,1,1,1,
        1,1,1,1,5,1,76,8,1,10,1,12,1,79,9,1,1,1,3,1,82,8,1,1,1,1,1,1,1,1,
        1,1,1,1,1,5,1,90,8,1,10,1,12,1,93,9,1,1,1,1,1,1,1,1,1,3,1,99,8,1,
        1,2,1,2,1,3,1,3,1,3,5,3,106,8,3,10,3,12,3,109,9,3,1,4,1,4,1,4,5,
        4,114,8,4,10,4,12,4,117,9,4,1,5,1,5,1,5,5,5,122,8,5,10,5,12,5,125,
        9,5,1,6,1,6,1,6,5,6,130,8,6,10,6,12,6,133,9,6,1,7,1,7,1,7,5,7,138,
        8,7,10,7,12,7,141,9,7,1,8,1,8,1,8,5,8,146,8,8,10,8,12,8,149,9,8,
        1,9,1,9,1,9,3,9,154,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,
        163,8,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,
        5,1,0,16,17,1,0,18,21,1,0,12,13,1,0,14,15,1,0,10,11,175,0,24,1,0,
        0,0,2,98,1,0,0,0,4,100,1,0,0,0,6,102,1,0,0,0,8,110,1,0,0,0,10,118,
        1,0,0,0,12,126,1,0,0,0,14,134,1,0,0,0,16,142,1,0,0,0,18,153,1,0,
        0,0,20,162,1,0,0,0,22,164,1,0,0,0,24,25,5,1,0,0,25,29,5,25,0,0,26,
        28,3,2,1,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,
        0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,26,0,0,33,34,5,2,0,0,34,1,
        1,0,0,0,35,36,5,3,0,0,36,37,5,32,0,0,37,38,5,30,0,0,38,39,3,22,11,
        0,39,40,5,31,0,0,40,41,3,4,2,0,41,42,5,29,0,0,42,99,1,0,0,0,43,44,
        5,32,0,0,44,45,5,31,0,0,45,46,3,4,2,0,46,47,5,29,0,0,47,99,1,0,0,
        0,48,49,5,7,0,0,49,50,5,27,0,0,50,51,3,4,2,0,51,52,5,28,0,0,52,53,
        5,29,0,0,53,99,1,0,0,0,54,55,5,32,0,0,55,56,5,31,0,0,56,57,5,8,0,
        0,57,58,5,27,0,0,58,59,5,28,0,0,59,99,5,29,0,0,60,61,5,4,0,0,61,
        62,5,27,0,0,62,63,3,4,2,0,63,64,5,28,0,0,64,68,5,25,0,0,65,67,3,
        2,1,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        71,1,0,0,0,70,68,1,0,0,0,71,81,5,26,0,0,72,73,5,5,0,0,73,77,5,25,
        0,0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,
        1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,82,5,26,0,0,81,72,1,0,0,0,
        81,82,1,0,0,0,82,99,1,0,0,0,83,84,5,6,0,0,84,85,5,27,0,0,85,86,3,
        4,2,0,86,87,5,28,0,0,87,91,5,25,0,0,88,90,3,2,1,0,89,88,1,0,0,0,
        90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,
        0,0,0,94,95,5,26,0,0,95,99,1,0,0,0,96,97,5,9,0,0,97,99,5,29,0,0,
        98,35,1,0,0,0,98,43,1,0,0,0,98,48,1,0,0,0,98,54,1,0,0,0,98,60,1,
        0,0,0,98,83,1,0,0,0,98,96,1,0,0,0,99,3,1,0,0,0,100,101,3,6,3,0,101,
        5,1,0,0,0,102,107,3,8,4,0,103,104,5,23,0,0,104,106,3,8,4,0,105,103,
        1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,7,1,
        0,0,0,109,107,1,0,0,0,110,115,3,10,5,0,111,112,5,22,0,0,112,114,
        3,10,5,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,
        1,0,0,0,116,9,1,0,0,0,117,115,1,0,0,0,118,123,3,12,6,0,119,120,7,
        0,0,0,120,122,3,12,6,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,1,
        0,0,0,123,124,1,0,0,0,124,11,1,0,0,0,125,123,1,0,0,0,126,131,3,14,
        7,0,127,128,7,1,0,0,128,130,3,14,7,0,129,127,1,0,0,0,130,133,1,0,
        0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,13,1,0,0,0,133,131,1,0,0,
        0,134,139,3,16,8,0,135,136,7,2,0,0,136,138,3,16,8,0,137,135,1,0,
        0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,15,1,0,0,
        0,141,139,1,0,0,0,142,147,3,18,9,0,143,144,7,3,0,0,144,146,3,18,
        9,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,
        0,0,148,17,1,0,0,0,149,147,1,0,0,0,150,151,5,24,0,0,151,154,3,18,
        9,0,152,154,3,20,10,0,153,150,1,0,0,0,153,152,1,0,0,0,154,19,1,0,
        0,0,155,163,5,33,0,0,156,163,5,34,0,0,157,163,5,32,0,0,158,159,5,
        27,0,0,159,160,3,4,2,0,160,161,5,28,0,0,161,163,1,0,0,0,162,155,
        1,0,0,0,162,156,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,0,163,21,1,
        0,0,0,164,165,7,4,0,0,165,23,1,0,0,0,14,29,68,77,81,91,98,107,115,
        123,131,139,147,153,162
    ]

class poglinParser ( Parser ):

    grammarFileName = "poglin.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'start'", "'end'", "'var'", "'if'", "'else'", 
                     "'while'", "'escreva'", "'leia'", "'pog'", "'Int'", 
                     "'String'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
                     "'{'", "'}'", "'('", "')'", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "START", "END", "VAR", "IF", "ELSE", 
                      "WHILE", "ESCREVA", "LEIA", "POG", "INT_TYPE", "STRING_TYPE", 
                      "PLUS", "MINUS", "MULT", "DIV", "EQUALS", "NEQUALS", 
                      "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", "LBRACE", 
                      "RBRACE", "LPAREN", "RPAREN", "SEMI", "COLON", "ASSIGN", 
                      "ID", "INT", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_logicalOrExpression = 3
    RULE_logicalAndExpression = 4
    RULE_equalityExpression = 5
    RULE_relationalExpression = 6
    RULE_additiveExpression = 7
    RULE_multiplicativeExpression = 8
    RULE_unaryExpression = 9
    RULE_primary = 10
    RULE_type = 11

    ruleNames =  [ "program", "statement", "expression", "logicalOrExpression", 
                   "logicalAndExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "primary", "type" ]

    EOF = Token.EOF
    START=1
    END=2
    VAR=3
    IF=4
    ELSE=5
    WHILE=6
    ESCREVA=7
    LEIA=8
    POG=9
    INT_TYPE=10
    STRING_TYPE=11
    PLUS=12
    MINUS=13
    MULT=14
    DIV=15
    EQUALS=16
    NEQUALS=17
    LT=18
    LTE=19
    GT=20
    GTE=21
    AND=22
    OR=23
    NOT=24
    LBRACE=25
    RBRACE=26
    LPAREN=27
    RPAREN=28
    SEMI=29
    COLON=30
    ASSIGN=31
    ID=32
    INT=33
    STRING=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(poglinParser.START, 0)

        def LBRACE(self):
            return self.getToken(poglinParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(poglinParser.RBRACE, 0)

        def END(self):
            return self.getToken(poglinParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.StatementContext)
            else:
                return self.getTypedRuleContext(poglinParser.StatementContext,i)


        def getRuleIndex(self):
            return poglinParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = poglinParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(poglinParser.START)
            self.state = 25
            self.match(poglinParser.LBRACE)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294968024) != 0):
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(poglinParser.RBRACE)
            self.state = 33
            self.match(poglinParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return poglinParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(poglinParser.WHILE, 0)
        def LPAREN(self):
            return self.getToken(poglinParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(poglinParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(poglinParser.RPAREN, 0)
        def LBRACE(self):
            return self.getToken(poglinParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(poglinParser.RBRACE, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.StatementContext)
            else:
                return self.getTypedRuleContext(poglinParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class PogStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POG(self):
            return self.getToken(poglinParser.POG, 0)
        def SEMI(self):
            return self.getToken(poglinParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPogStatement" ):
                listener.enterPogStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPogStatement" ):
                listener.exitPogStatement(self)


    class PrintStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ESCREVA(self):
            return self.getToken(poglinParser.ESCREVA, 0)
        def LPAREN(self):
            return self.getToken(poglinParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(poglinParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(poglinParser.RPAREN, 0)
        def SEMI(self):
            return self.getToken(poglinParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)


    class AssignmentContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(poglinParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(poglinParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(poglinParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(poglinParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class ReadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(poglinParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(poglinParser.ASSIGN, 0)
        def LEIA(self):
            return self.getToken(poglinParser.LEIA, 0)
        def LPAREN(self):
            return self.getToken(poglinParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(poglinParser.RPAREN, 0)
        def SEMI(self):
            return self.getToken(poglinParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(poglinParser.IF, 0)
        def LPAREN(self):
            return self.getToken(poglinParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(poglinParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(poglinParser.RPAREN, 0)
        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.LBRACE)
            else:
                return self.getToken(poglinParser.LBRACE, i)
        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.RBRACE)
            else:
                return self.getToken(poglinParser.RBRACE, i)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.StatementContext)
            else:
                return self.getTypedRuleContext(poglinParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(poglinParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)


    class VarDeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a poglinParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(poglinParser.VAR, 0)
        def ID(self):
            return self.getToken(poglinParser.ID, 0)
        def COLON(self):
            return self.getToken(poglinParser.COLON, 0)
        def type_(self):
            return self.getTypedRuleContext(poglinParser.TypeContext,0)

        def ASSIGN(self):
            return self.getToken(poglinParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(poglinParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(poglinParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)



    def statement(self):

        localctx = poglinParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = poglinParser.VarDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(poglinParser.VAR)
                self.state = 36
                self.match(poglinParser.ID)
                self.state = 37
                self.match(poglinParser.COLON)
                self.state = 38
                self.type_()
                self.state = 39
                self.match(poglinParser.ASSIGN)
                self.state = 40
                self.expression()
                self.state = 41
                self.match(poglinParser.SEMI)
                pass

            elif la_ == 2:
                localctx = poglinParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(poglinParser.ID)
                self.state = 44
                self.match(poglinParser.ASSIGN)
                self.state = 45
                self.expression()
                self.state = 46
                self.match(poglinParser.SEMI)
                pass

            elif la_ == 3:
                localctx = poglinParser.PrintStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(poglinParser.ESCREVA)
                self.state = 49
                self.match(poglinParser.LPAREN)
                self.state = 50
                self.expression()
                self.state = 51
                self.match(poglinParser.RPAREN)
                self.state = 52
                self.match(poglinParser.SEMI)
                pass

            elif la_ == 4:
                localctx = poglinParser.ReadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.match(poglinParser.ID)
                self.state = 55
                self.match(poglinParser.ASSIGN)
                self.state = 56
                self.match(poglinParser.LEIA)
                self.state = 57
                self.match(poglinParser.LPAREN)
                self.state = 58
                self.match(poglinParser.RPAREN)
                self.state = 59
                self.match(poglinParser.SEMI)
                pass

            elif la_ == 5:
                localctx = poglinParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.match(poglinParser.IF)
                self.state = 61
                self.match(poglinParser.LPAREN)
                self.state = 62
                self.expression()
                self.state = 63
                self.match(poglinParser.RPAREN)
                self.state = 64
                self.match(poglinParser.LBRACE)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294968024) != 0):
                    self.state = 65
                    self.statement()
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self.match(poglinParser.RBRACE)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 72
                    self.match(poglinParser.ELSE)
                    self.state = 73
                    self.match(poglinParser.LBRACE)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294968024) != 0):
                        self.state = 74
                        self.statement()
                        self.state = 79
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 80
                    self.match(poglinParser.RBRACE)


                pass

            elif la_ == 6:
                localctx = poglinParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.match(poglinParser.WHILE)
                self.state = 84
                self.match(poglinParser.LPAREN)
                self.state = 85
                self.expression()
                self.state = 86
                self.match(poglinParser.RPAREN)
                self.state = 87
                self.match(poglinParser.LBRACE)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294968024) != 0):
                    self.state = 88
                    self.statement()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(poglinParser.RBRACE)
                pass

            elif la_ == 7:
                localctx = poglinParser.PogStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 96
                self.match(poglinParser.POG)
                self.state = 97
                self.match(poglinParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(poglinParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return poglinParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = poglinParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(poglinParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.OR)
            else:
                return self.getToken(poglinParser.OR, i)

        def getRuleIndex(self):
            return poglinParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)




    def logicalOrExpression(self):

        localctx = poglinParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.logicalAndExpression()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 103
                self.match(poglinParser.OR)
                self.state = 104
                self.logicalAndExpression()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(poglinParser.EqualityExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.AND)
            else:
                return self.getToken(poglinParser.AND, i)

        def getRuleIndex(self):
            return poglinParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)




    def logicalAndExpression(self):

        localctx = poglinParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.equalityExpression()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 111
                self.match(poglinParser.AND)
                self.state = 112
                self.equalityExpression()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(poglinParser.RelationalExpressionContext,i)


        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.EQUALS)
            else:
                return self.getToken(poglinParser.EQUALS, i)

        def NEQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.NEQUALS)
            else:
                return self.getToken(poglinParser.NEQUALS, i)

        def getRuleIndex(self):
            return poglinParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)




    def equalityExpression(self):

        localctx = poglinParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.relationalExpression()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.relationalExpression()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(poglinParser.AdditiveExpressionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.LT)
            else:
                return self.getToken(poglinParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.LTE)
            else:
                return self.getToken(poglinParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.GT)
            else:
                return self.getToken(poglinParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.GTE)
            else:
                return self.getToken(poglinParser.GTE, i)

        def getRuleIndex(self):
            return poglinParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)




    def relationalExpression(self):

        localctx = poglinParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.additiveExpression()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0):
                self.state = 127
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self.additiveExpression()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(poglinParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.PLUS)
            else:
                return self.getToken(poglinParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.MINUS)
            else:
                return self.getToken(poglinParser.MINUS, i)

        def getRuleIndex(self):
            return poglinParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)




    def additiveExpression(self):

        localctx = poglinParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.multiplicativeExpression()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 135
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 136
                self.multiplicativeExpression()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poglinParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(poglinParser.UnaryExpressionContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.MULT)
            else:
                return self.getToken(poglinParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(poglinParser.DIV)
            else:
                return self.getToken(poglinParser.DIV, i)

        def getRuleIndex(self):
            return poglinParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)




    def multiplicativeExpression(self):

        localctx = poglinParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.unaryExpression()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.unaryExpression()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(poglinParser.NOT, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(poglinParser.UnaryExpressionContext,0)


        def primary(self):
            return self.getTypedRuleContext(poglinParser.PrimaryContext,0)


        def getRuleIndex(self):
            return poglinParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = poglinParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unaryExpression)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(poglinParser.NOT)
                self.state = 151
                self.unaryExpression()
                pass
            elif token in [27, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(poglinParser.INT, 0)

        def STRING(self):
            return self.getToken(poglinParser.STRING, 0)

        def ID(self):
            return self.getToken(poglinParser.ID, 0)

        def LPAREN(self):
            return self.getToken(poglinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(poglinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(poglinParser.RPAREN, 0)

        def getRuleIndex(self):
            return poglinParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = poglinParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primary)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(poglinParser.INT)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(poglinParser.STRING)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(poglinParser.ID)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.match(poglinParser.LPAREN)
                self.state = 159
                self.expression()
                self.state = 160
                self.match(poglinParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(poglinParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(poglinParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return poglinParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = poglinParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





