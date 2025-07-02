# Generated from grammars/poglin.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .poglinParser import poglinParser
else:
    from poglinParser import poglinParser

# This class defines a complete generic visitor for a parse tree produced by poglinParser.

class poglinVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by poglinParser#program.
    def visitProgram(self, ctx:poglinParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#statement.
    def visitStatement(self, ctx:poglinParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#expression.
    def visitExpression(self, ctx:poglinParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:poglinParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:poglinParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#equalityExpression.
    def visitEqualityExpression(self, ctx:poglinParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#relationalExpression.
    def visitRelationalExpression(self, ctx:poglinParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:poglinParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:poglinParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#unaryExpression.
    def visitUnaryExpression(self, ctx:poglinParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#primary.
    def visitPrimary(self, ctx:poglinParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by poglinParser#type.
    def visitType(self, ctx:poglinParser.TypeContext):
        return self.visitChildren(ctx)



del poglinParser