# Generated from compiler/Cluster.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ClusterParser import ClusterParser
else:
    from ClusterParser import ClusterParser

# This class defines a complete generic visitor for a parse tree produced by ClusterParser.

class ClusterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ClusterParser#parse.
    def visitParse(self, ctx:ClusterParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#type.
    def visitType(self, ctx:ClusterParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#stmt.
    def visitStmt(self, ctx:ClusterParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#bodyStmts.
    def visitBodyStmts(self, ctx:ClusterParser.BodyStmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#body.
    def visitBody(self, ctx:ClusterParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#ifStmt.
    def visitIfStmt(self, ctx:ClusterParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#elseifStmt.
    def visitElseifStmt(self, ctx:ClusterParser.ElseifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#elseStmt.
    def visitElseStmt(self, ctx:ClusterParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#whileStmt.
    def visitWhileStmt(self, ctx:ClusterParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#useStmt.
    def visitUseStmt(self, ctx:ClusterParser.UseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#funcAssign.
    def visitFuncAssign(self, ctx:ClusterParser.FuncAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#varAssign.
    def visitVarAssign(self, ctx:ClusterParser.VarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#arg.
    def visitArg(self, ctx:ClusterParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#args.
    def visitArgs(self, ctx:ClusterParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#param.
    def visitParam(self, ctx:ClusterParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#params.
    def visitParams(self, ctx:ClusterParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#call.
    def visitCall(self, ctx:ClusterParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#atom.
    def visitAtom(self, ctx:ClusterParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusterParser#expr.
    def visitExpr(self, ctx:ClusterParser.ExprContext):
        return self.visitChildren(ctx)



del ClusterParser