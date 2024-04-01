# Generated from compiler/Cluster.g4 by ANTLR 4.13.0
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
        4,1,40,210,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,59,8,2,1,3,1,3,1,3,3,3,64,8,3,1,4,1,4,5,4,68,8,4,
        10,4,12,4,71,9,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,79,8,5,10,5,12,5,82,
        9,5,1,5,3,5,85,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,5,9,103,8,9,10,9,12,9,106,9,9,1,10,1,10,1,10,1,
        10,3,10,112,8,10,1,10,1,10,1,10,3,10,117,8,10,1,10,1,10,1,11,3,11,
        122,8,11,1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,5,13,133,8,
        13,10,13,12,13,136,9,13,1,14,1,14,1,14,1,15,1,15,1,15,5,15,144,8,
        15,10,15,12,15,147,9,15,1,16,1,16,1,16,3,16,152,8,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,
        17,169,8,17,1,17,1,17,1,17,3,17,174,8,17,1,18,1,18,1,18,1,18,1,18,
        3,18,181,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,200,8,18,1,18,3,18,203,8,
        18,5,18,205,8,18,10,18,12,18,208,9,18,1,18,0,1,36,19,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,0,4,1,0,15,16,1,0,17,19,1,
        0,20,25,1,0,26,27,226,0,41,1,0,0,0,2,46,1,0,0,0,4,58,1,0,0,0,6,63,
        1,0,0,0,8,65,1,0,0,0,10,74,1,0,0,0,12,86,1,0,0,0,14,91,1,0,0,0,16,
        94,1,0,0,0,18,98,1,0,0,0,20,107,1,0,0,0,22,121,1,0,0,0,24,127,1,
        0,0,0,26,129,1,0,0,0,28,137,1,0,0,0,30,140,1,0,0,0,32,148,1,0,0,
        0,34,173,1,0,0,0,36,180,1,0,0,0,38,40,3,4,2,0,39,38,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,
        44,45,5,0,0,1,45,1,1,0,0,0,46,50,5,13,0,0,47,48,5,36,0,0,48,49,5,
        13,0,0,49,51,5,37,0,0,50,47,1,0,0,0,50,51,1,0,0,0,51,3,1,0,0,0,52,
        59,3,22,11,0,53,59,3,20,10,0,54,59,3,10,5,0,55,59,3,16,8,0,56,59,
        3,18,9,0,57,59,3,36,18,0,58,52,1,0,0,0,58,53,1,0,0,0,58,54,1,0,0,
        0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,5,1,0,0,0,60,64,3,
        4,2,0,61,62,5,6,0,0,62,64,3,36,18,0,63,60,1,0,0,0,63,61,1,0,0,0,
        64,7,1,0,0,0,65,69,5,34,0,0,66,68,3,6,3,0,67,66,1,0,0,0,68,71,1,
        0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,
        73,5,35,0,0,73,9,1,0,0,0,74,75,5,1,0,0,75,76,3,36,18,0,76,80,3,8,
        4,0,77,79,3,12,6,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,
        81,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,83,85,3,14,7,0,84,83,1,0,
        0,0,84,85,1,0,0,0,85,11,1,0,0,0,86,87,5,3,0,0,87,88,5,1,0,0,88,89,
        3,36,18,0,89,90,3,8,4,0,90,13,1,0,0,0,91,92,5,3,0,0,92,93,3,8,4,
        0,93,15,1,0,0,0,94,95,5,5,0,0,95,96,3,36,18,0,96,97,3,8,4,0,97,17,
        1,0,0,0,98,99,5,2,0,0,99,104,5,10,0,0,100,101,5,30,0,0,101,103,5,
        10,0,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,
        0,0,0,105,19,1,0,0,0,106,104,1,0,0,0,107,108,5,4,0,0,108,109,5,13,
        0,0,109,111,5,32,0,0,110,112,3,30,15,0,111,110,1,0,0,0,111,112,1,
        0,0,0,112,113,1,0,0,0,113,116,5,33,0,0,114,115,5,38,0,0,115,117,
        3,2,1,0,116,114,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,
        3,8,4,0,119,21,1,0,0,0,120,122,3,2,1,0,121,120,1,0,0,0,121,122,1,
        0,0,0,122,123,1,0,0,0,123,124,5,13,0,0,124,125,5,31,0,0,125,126,
        3,36,18,0,126,23,1,0,0,0,127,128,3,36,18,0,128,25,1,0,0,0,129,134,
        3,24,12,0,130,131,5,30,0,0,131,133,3,24,12,0,132,130,1,0,0,0,133,
        136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,27,1,0,0,0,136,134,
        1,0,0,0,137,138,3,2,1,0,138,139,5,13,0,0,139,29,1,0,0,0,140,145,
        3,28,14,0,141,142,5,30,0,0,142,144,3,28,14,0,143,141,1,0,0,0,144,
        147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,31,1,0,0,0,147,145,
        1,0,0,0,148,149,5,13,0,0,149,151,5,32,0,0,150,152,3,26,13,0,151,
        150,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,5,33,0,0,154,
        33,1,0,0,0,155,174,5,7,0,0,156,174,5,8,0,0,157,174,5,10,0,0,158,
        174,5,11,0,0,159,174,5,12,0,0,160,174,5,13,0,0,161,162,5,32,0,0,
        162,163,3,36,18,0,163,164,5,33,0,0,164,174,1,0,0,0,165,166,3,2,1,
        0,166,168,5,34,0,0,167,169,3,26,13,0,168,167,1,0,0,0,168,169,1,0,
        0,0,169,170,1,0,0,0,170,171,5,35,0,0,171,174,1,0,0,0,172,174,5,14,
        0,0,173,155,1,0,0,0,173,156,1,0,0,0,173,157,1,0,0,0,173,158,1,0,
        0,0,173,159,1,0,0,0,173,160,1,0,0,0,173,161,1,0,0,0,173,165,1,0,
        0,0,173,172,1,0,0,0,174,35,1,0,0,0,175,176,6,18,-1,0,176,181,3,32,
        16,0,177,181,3,34,17,0,178,179,5,28,0,0,179,181,3,36,18,5,180,175,
        1,0,0,0,180,177,1,0,0,0,180,178,1,0,0,0,181,206,1,0,0,0,182,183,
        10,4,0,0,183,184,7,0,0,0,184,205,3,36,18,5,185,186,10,3,0,0,186,
        187,7,1,0,0,187,205,3,36,18,4,188,189,10,2,0,0,189,190,7,2,0,0,190,
        205,3,36,18,3,191,192,10,1,0,0,192,193,7,3,0,0,193,205,3,36,18,2,
        194,195,10,7,0,0,195,196,5,29,0,0,196,202,5,13,0,0,197,199,5,32,
        0,0,198,200,3,26,13,0,199,198,1,0,0,0,199,200,1,0,0,0,200,201,1,
        0,0,0,201,203,5,33,0,0,202,197,1,0,0,0,202,203,1,0,0,0,203,205,1,
        0,0,0,204,182,1,0,0,0,204,185,1,0,0,0,204,188,1,0,0,0,204,191,1,
        0,0,0,204,194,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,
        0,0,0,207,37,1,0,0,0,208,206,1,0,0,0,21,41,50,58,63,69,80,84,104,
        111,116,121,134,145,151,168,173,180,199,202,204,206
    ]

class ClusterParser ( Parser ):

    grammarFileName = "Cluster.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'use'", "'else'", "'func'", "'while'", 
                     "'return'", "<INVALID>", "<INVALID>", "'''", "<INVALID>", 
                     "<INVALID>", "'nil'", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'&&'", "'||'", "'!'", "'.'", 
                     "','", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'->'" ]

    symbolicNames = [ "<INVALID>", "IF", "USE", "ELSE", "FUNC", "WHILE", 
                      "RETURN", "INT", "FLOAT", "APOSTROPHE", "STRING", 
                      "BOOL", "NIL", "ID", "HEX", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EEQ", "NEQ", "GT", "LT", "GTE", "LTE", "AND", 
                      "OR", "NOT", "DOT", "COMMA", "ASSIGN", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACK", "RBRACK", "RETURNS", 
                      "COMMENT", "WHITESPACE" ]

    RULE_parse = 0
    RULE_type = 1
    RULE_stmt = 2
    RULE_bodyStmts = 3
    RULE_body = 4
    RULE_ifStmt = 5
    RULE_elseifStmt = 6
    RULE_elseStmt = 7
    RULE_whileStmt = 8
    RULE_useStmt = 9
    RULE_funcAssign = 10
    RULE_varAssign = 11
    RULE_arg = 12
    RULE_args = 13
    RULE_param = 14
    RULE_params = 15
    RULE_call = 16
    RULE_atom = 17
    RULE_expr = 18

    ruleNames =  [ "parse", "type", "stmt", "bodyStmts", "body", "ifStmt", 
                   "elseifStmt", "elseStmt", "whileStmt", "useStmt", "funcAssign", 
                   "varAssign", "arg", "args", "param", "params", "call", 
                   "atom", "expr" ]

    EOF = Token.EOF
    IF=1
    USE=2
    ELSE=3
    FUNC=4
    WHILE=5
    RETURN=6
    INT=7
    FLOAT=8
    APOSTROPHE=9
    STRING=10
    BOOL=11
    NIL=12
    ID=13
    HEX=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    MOD=19
    EEQ=20
    NEQ=21
    GT=22
    LT=23
    GTE=24
    LTE=25
    AND=26
    OR=27
    NOT=28
    DOT=29
    COMMA=30
    ASSIGN=31
    LPAREN=32
    RPAREN=33
    LBRACE=34
    RBRACE=35
    LBRACK=36
    RBRACK=37
    RETURNS=38
    COMMENT=39
    WHITESPACE=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ClusterParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterParser.StmtContext)
            else:
                return self.getTypedRuleContext(ClusterParser.StmtContext,i)


        def getRuleIndex(self):
            return ClusterParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = ClusterParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434934) != 0):
                self.state = 38
                self.stmt()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(ClusterParser.EOF)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterParser.ID)
            else:
                return self.getToken(ClusterParser.ID, i)

        def LBRACK(self):
            return self.getToken(ClusterParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(ClusterParser.RBRACK, 0)

        def getRuleIndex(self):
            return ClusterParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ClusterParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ClusterParser.ID)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 47
                self.match(ClusterParser.LBRACK)
                self.state = 48
                self.match(ClusterParser.ID)
                self.state = 49
                self.match(ClusterParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varAssign(self):
            return self.getTypedRuleContext(ClusterParser.VarAssignContext,0)


        def funcAssign(self):
            return self.getTypedRuleContext(ClusterParser.FuncAssignContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ClusterParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(ClusterParser.WhileStmtContext,0)


        def useStmt(self):
            return self.getTypedRuleContext(ClusterParser.UseStmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ClusterParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.varAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.funcAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.useStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyStmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ClusterParser.StmtContext,0)


        def RETURN(self):
            return self.getToken(ClusterParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_bodyStmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyStmts" ):
                return visitor.visitBodyStmts(self)
            else:
                return visitor.visitChildren(self)




    def bodyStmts(self):

        localctx = ClusterParser.BodyStmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bodyStmts)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 28, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(ClusterParser.RETURN)
                self.state = 62
                self.expr(0)
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ClusterParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ClusterParser.RBRACE, 0)

        def bodyStmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterParser.BodyStmtsContext)
            else:
                return self.getTypedRuleContext(ClusterParser.BodyStmtsContext,i)


        def getRuleIndex(self):
            return ClusterParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ClusterParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ClusterParser.LBRACE)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434998) != 0):
                self.state = 66
                self.bodyStmts()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(ClusterParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ClusterParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(ClusterParser.BodyContext,0)


        def elseifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterParser.ElseifStmtContext)
            else:
                return self.getTypedRuleContext(ClusterParser.ElseifStmtContext,i)


        def elseStmt(self):
            return self.getTypedRuleContext(ClusterParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ClusterParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ClusterParser.IF)
            self.state = 75
            self.expr(0)
            self.state = 76
            self.body()
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.elseifStmt() 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 83
                self.elseStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ClusterParser.ELSE, 0)

        def IF(self):
            return self.getToken(ClusterParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(ClusterParser.BodyContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_elseifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifStmt" ):
                return visitor.visitElseifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifStmt(self):

        localctx = ClusterParser.ElseifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ClusterParser.ELSE)
            self.state = 87
            self.match(ClusterParser.IF)
            self.state = 88
            self.expr(0)
            self.state = 89
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ClusterParser.ELSE, 0)

        def body(self):
            return self.getTypedRuleContext(ClusterParser.BodyContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = ClusterParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ClusterParser.ELSE)
            self.state = 92
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ClusterParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(ClusterParser.BodyContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = ClusterParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ClusterParser.WHILE)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(ClusterParser.USE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterParser.STRING)
            else:
                return self.getToken(ClusterParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterParser.COMMA)
            else:
                return self.getToken(ClusterParser.COMMA, i)

        def getRuleIndex(self):
            return ClusterParser.RULE_useStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseStmt" ):
                return visitor.visitUseStmt(self)
            else:
                return visitor.visitChildren(self)




    def useStmt(self):

        localctx = ClusterParser.UseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_useStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ClusterParser.USE)
            self.state = 99
            self.match(ClusterParser.STRING)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 100
                self.match(ClusterParser.COMMA)
                self.state = 101
                self.match(ClusterParser.STRING)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ClusterParser.FUNC, 0)

        def ID(self):
            return self.getToken(ClusterParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ClusterParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ClusterParser.RPAREN, 0)

        def body(self):
            return self.getTypedRuleContext(ClusterParser.BodyContext,0)


        def params(self):
            return self.getTypedRuleContext(ClusterParser.ParamsContext,0)


        def RETURNS(self):
            return self.getToken(ClusterParser.RETURNS, 0)

        def type_(self):
            return self.getTypedRuleContext(ClusterParser.TypeContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_funcAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncAssign" ):
                return visitor.visitFuncAssign(self)
            else:
                return visitor.visitChildren(self)




    def funcAssign(self):

        localctx = ClusterParser.FuncAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ClusterParser.FUNC)
            self.state = 108
            self.match(ClusterParser.ID)
            self.state = 109
            self.match(ClusterParser.LPAREN)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 110
                self.params()


            self.state = 113
            self.match(ClusterParser.RPAREN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 114
                self.match(ClusterParser.RETURNS)
                self.state = 115
                self.type_()


            self.state = 118
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClusterParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ClusterParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def type_(self):
            return self.getTypedRuleContext(ClusterParser.TypeContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_varAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssign" ):
                return visitor.visitVarAssign(self)
            else:
                return visitor.visitChildren(self)




    def varAssign(self):

        localctx = ClusterParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 120
                self.type_()


            self.state = 123
            self.match(ClusterParser.ID)
            self.state = 124
            self.match(ClusterParser.ASSIGN)
            self.state = 125
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ClusterParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterParser.ArgContext)
            else:
                return self.getTypedRuleContext(ClusterParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterParser.COMMA)
            else:
                return self.getToken(ClusterParser.COMMA, i)

        def getRuleIndex(self):
            return ClusterParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ClusterParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.arg()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 130
                self.match(ClusterParser.COMMA)
                self.state = 131
                self.arg()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ClusterParser.TypeContext,0)


        def ID(self):
            return self.getToken(ClusterParser.ID, 0)

        def getRuleIndex(self):
            return ClusterParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ClusterParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.type_()
            self.state = 138
            self.match(ClusterParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterParser.ParamContext)
            else:
                return self.getTypedRuleContext(ClusterParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterParser.COMMA)
            else:
                return self.getToken(ClusterParser.COMMA, i)

        def getRuleIndex(self):
            return ClusterParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ClusterParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.param()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 141
                self.match(ClusterParser.COMMA)
                self.state = 142
                self.param()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClusterParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ClusterParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ClusterParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(ClusterParser.ArgsContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ClusterParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ClusterParser.ID)
            self.state = 149
            self.match(ClusterParser.LPAREN)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434880) != 0):
                self.state = 150
                self.args()


            self.state = 153
            self.match(ClusterParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ClusterParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ClusterParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(ClusterParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ClusterParser.BOOL, 0)

        def NIL(self):
            return self.getToken(ClusterParser.NIL, 0)

        def ID(self):
            return self.getToken(ClusterParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ClusterParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusterParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ClusterParser.RPAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(ClusterParser.TypeContext,0)


        def LBRACE(self):
            return self.getToken(ClusterParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ClusterParser.RBRACE, 0)

        def args(self):
            return self.getTypedRuleContext(ClusterParser.ArgsContext,0)


        def HEX(self):
            return self.getToken(ClusterParser.HEX, 0)

        def getRuleIndex(self):
            return ClusterParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ClusterParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(ClusterParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(ClusterParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(ClusterParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.match(ClusterParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.match(ClusterParser.NIL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.match(ClusterParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 161
                self.match(ClusterParser.LPAREN)
                self.state = 162
                self.expr(0)
                self.state = 163
                self.match(ClusterParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 165
                self.type_()
                self.state = 166
                self.match(ClusterParser.LBRACE)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434880) != 0):
                    self.state = 167
                    self.args()


                self.state = 170
                self.match(ClusterParser.RBRACE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 172
                self.match(ClusterParser.HEX)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def call(self):
            return self.getTypedRuleContext(ClusterParser.CallContext,0)


        def atom(self):
            return self.getTypedRuleContext(ClusterParser.AtomContext,0)


        def NOT(self):
            return self.getToken(ClusterParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterParser.ExprContext)
            else:
                return self.getTypedRuleContext(ClusterParser.ExprContext,i)


        def ADD(self):
            return self.getToken(ClusterParser.ADD, 0)

        def SUB(self):
            return self.getToken(ClusterParser.SUB, 0)

        def MUL(self):
            return self.getToken(ClusterParser.MUL, 0)

        def DIV(self):
            return self.getToken(ClusterParser.DIV, 0)

        def MOD(self):
            return self.getToken(ClusterParser.MOD, 0)

        def EEQ(self):
            return self.getToken(ClusterParser.EEQ, 0)

        def NEQ(self):
            return self.getToken(ClusterParser.NEQ, 0)

        def GT(self):
            return self.getToken(ClusterParser.GT, 0)

        def LT(self):
            return self.getToken(ClusterParser.LT, 0)

        def GTE(self):
            return self.getToken(ClusterParser.GTE, 0)

        def LTE(self):
            return self.getToken(ClusterParser.LTE, 0)

        def AND(self):
            return self.getToken(ClusterParser.AND, 0)

        def OR(self):
            return self.getToken(ClusterParser.OR, 0)

        def DOT(self):
            return self.getToken(ClusterParser.DOT, 0)

        def ID(self):
            return self.getToken(ClusterParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ClusterParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ClusterParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(ClusterParser.ArgsContext,0)


        def getRuleIndex(self):
            return ClusterParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ClusterParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 176
                self.call()
                pass

            elif la_ == 2:
                self.state = 177
                self.atom()
                pass

            elif la_ == 3:
                self.state = 178
                self.match(ClusterParser.NOT)
                self.state = 179
                self.expr(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 204
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = ClusterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 183
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ClusterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 185
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 186
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 187
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = ClusterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 189
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = ClusterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 192
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = ClusterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 195
                        self.match(ClusterParser.DOT)
                        self.state = 196
                        self.match(ClusterParser.ID)
                        self.state = 202
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                        if la_ == 1:
                            self.state = 197
                            self.match(ClusterParser.LPAREN)
                            self.state = 199
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434880) != 0):
                                self.state = 198
                                self.args()


                            self.state = 201
                            self.match(ClusterParser.RPAREN)


                        pass

             
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




