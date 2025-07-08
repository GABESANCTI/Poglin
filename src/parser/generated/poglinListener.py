# Generated from grammars/poglin.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .poglinParser import poglinParser
else:
    from poglinParser import poglinParser

# This class defines a complete listener for a parse tree produced by poglinParser.
class poglinListener(ParseTreeListener):

    # Enter a parse tree produced by poglinParser#program.
    def enterProgram(self, ctx:poglinParser.ProgramContext):
        pass

    # Exit a parse tree produced by poglinParser#program.
    def exitProgram(self, ctx:poglinParser.ProgramContext):
        pass


    # Enter a parse tree produced by poglinParser#varDeclaration.
    def enterVarDeclaration(self, ctx:poglinParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by poglinParser#varDeclaration.
    def exitVarDeclaration(self, ctx:poglinParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by poglinParser#assignment.
    def enterAssignment(self, ctx:poglinParser.AssignmentContext):
        pass

    # Exit a parse tree produced by poglinParser#assignment.
    def exitAssignment(self, ctx:poglinParser.AssignmentContext):
        pass


    # Enter a parse tree produced by poglinParser#printStatement.
    def enterPrintStatement(self, ctx:poglinParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by poglinParser#printStatement.
    def exitPrintStatement(self, ctx:poglinParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by poglinParser#readStatement.
    def enterReadStatement(self, ctx:poglinParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by poglinParser#readStatement.
    def exitReadStatement(self, ctx:poglinParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by poglinParser#ifStatement.
    def enterIfStatement(self, ctx:poglinParser.IfStatementContext):
        pass

    # Exit a parse tree produced by poglinParser#ifStatement.
    def exitIfStatement(self, ctx:poglinParser.IfStatementContext):
        pass


    # Enter a parse tree produced by poglinParser#whileStatement.
    def enterWhileStatement(self, ctx:poglinParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by poglinParser#whileStatement.
    def exitWhileStatement(self, ctx:poglinParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by poglinParser#pogStatement.
    def enterPogStatement(self, ctx:poglinParser.PogStatementContext):
        pass

    # Exit a parse tree produced by poglinParser#pogStatement.
    def exitPogStatement(self, ctx:poglinParser.PogStatementContext):
        pass


    # Enter a parse tree produced by poglinParser#expression.
    def enterExpression(self, ctx:poglinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#expression.
    def exitExpression(self, ctx:poglinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:poglinParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:poglinParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:poglinParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:poglinParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#equalityExpression.
    def enterEqualityExpression(self, ctx:poglinParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#equalityExpression.
    def exitEqualityExpression(self, ctx:poglinParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#relationalExpression.
    def enterRelationalExpression(self, ctx:poglinParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#relationalExpression.
    def exitRelationalExpression(self, ctx:poglinParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:poglinParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:poglinParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:poglinParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:poglinParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#unaryExpression.
    def enterUnaryExpression(self, ctx:poglinParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by poglinParser#unaryExpression.
    def exitUnaryExpression(self, ctx:poglinParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by poglinParser#primary.
    def enterPrimary(self, ctx:poglinParser.PrimaryContext):
        pass

    # Exit a parse tree produced by poglinParser#primary.
    def exitPrimary(self, ctx:poglinParser.PrimaryContext):
        pass


    # Enter a parse tree produced by poglinParser#type.
    def enterType(self, ctx:poglinParser.TypeContext):
        pass

    # Exit a parse tree produced by poglinParser#type.
    def exitType(self, ctx:poglinParser.TypeContext):
        pass



del poglinParser