# Generated from compiler/Cluster.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,40,260,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,3,6,113,8,6,1,6,4,6,116,8,6,11,6,12,6,117,1,7,3,7,121,8,7,1,
        7,5,7,124,8,7,10,7,12,7,127,9,7,1,7,1,7,4,7,131,8,7,11,7,12,7,132,
        1,8,1,8,1,9,1,9,5,9,139,8,9,10,9,12,9,142,9,9,1,9,1,9,1,9,5,9,147,
        8,9,10,9,12,9,150,9,9,1,9,1,9,3,9,154,8,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,3,10,165,8,10,1,11,1,11,1,11,1,11,1,12,1,
        12,5,12,173,8,12,10,12,12,12,176,9,12,1,13,1,13,1,13,1,13,4,13,182,
        8,13,11,13,12,13,183,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,
        1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,28,
        1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,
        1,35,1,35,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,38,5,38,245,
        8,38,10,38,12,38,248,9,38,1,38,1,38,1,38,1,38,1,39,4,39,255,8,39,
        11,39,12,39,256,1,39,1,39,3,140,148,246,0,40,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,
        17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,
        28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,
        39,79,40,1,0,5,1,0,48,57,3,0,65,90,95,95,97,122,4,0,48,57,65,90,
        95,95,97,122,3,0,48,57,65,70,97,102,3,0,9,10,13,13,32,32,272,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,
        0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,
        0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,
        0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,1,81,1,0,
        0,0,3,84,1,0,0,0,5,88,1,0,0,0,7,93,1,0,0,0,9,98,1,0,0,0,11,104,1,
        0,0,0,13,112,1,0,0,0,15,120,1,0,0,0,17,134,1,0,0,0,19,153,1,0,0,
        0,21,164,1,0,0,0,23,166,1,0,0,0,25,170,1,0,0,0,27,177,1,0,0,0,29,
        185,1,0,0,0,31,187,1,0,0,0,33,189,1,0,0,0,35,191,1,0,0,0,37,193,
        1,0,0,0,39,195,1,0,0,0,41,198,1,0,0,0,43,201,1,0,0,0,45,203,1,0,
        0,0,47,205,1,0,0,0,49,208,1,0,0,0,51,211,1,0,0,0,53,214,1,0,0,0,
        55,217,1,0,0,0,57,219,1,0,0,0,59,221,1,0,0,0,61,223,1,0,0,0,63,225,
        1,0,0,0,65,227,1,0,0,0,67,229,1,0,0,0,69,231,1,0,0,0,71,233,1,0,
        0,0,73,235,1,0,0,0,75,237,1,0,0,0,77,240,1,0,0,0,79,254,1,0,0,0,
        81,82,5,105,0,0,82,83,5,102,0,0,83,2,1,0,0,0,84,85,5,117,0,0,85,
        86,5,115,0,0,86,87,5,101,0,0,87,4,1,0,0,0,88,89,5,101,0,0,89,90,
        5,108,0,0,90,91,5,115,0,0,91,92,5,101,0,0,92,6,1,0,0,0,93,94,5,102,
        0,0,94,95,5,117,0,0,95,96,5,110,0,0,96,97,5,99,0,0,97,8,1,0,0,0,
        98,99,5,119,0,0,99,100,5,104,0,0,100,101,5,105,0,0,101,102,5,108,
        0,0,102,103,5,101,0,0,103,10,1,0,0,0,104,105,5,114,0,0,105,106,5,
        101,0,0,106,107,5,116,0,0,107,108,5,117,0,0,108,109,5,114,0,0,109,
        110,5,110,0,0,110,12,1,0,0,0,111,113,5,45,0,0,112,111,1,0,0,0,112,
        113,1,0,0,0,113,115,1,0,0,0,114,116,7,0,0,0,115,114,1,0,0,0,116,
        117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,14,1,0,0,0,119,121,
        5,45,0,0,120,119,1,0,0,0,120,121,1,0,0,0,121,125,1,0,0,0,122,124,
        7,0,0,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,130,5,46,0,0,129,131,
        7,0,0,0,130,129,1,0,0,0,131,132,1,0,0,0,132,130,1,0,0,0,132,133,
        1,0,0,0,133,16,1,0,0,0,134,135,5,39,0,0,135,18,1,0,0,0,136,140,5,
        34,0,0,137,139,9,0,0,0,138,137,1,0,0,0,139,142,1,0,0,0,140,141,1,
        0,0,0,140,138,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,0,143,154,5,
        34,0,0,144,148,3,17,8,0,145,147,9,0,0,0,146,145,1,0,0,0,147,150,
        1,0,0,0,148,149,1,0,0,0,148,146,1,0,0,0,149,151,1,0,0,0,150,148,
        1,0,0,0,151,152,3,17,8,0,152,154,1,0,0,0,153,136,1,0,0,0,153,144,
        1,0,0,0,154,20,1,0,0,0,155,156,5,116,0,0,156,157,5,114,0,0,157,158,
        5,117,0,0,158,165,5,101,0,0,159,160,5,102,0,0,160,161,5,97,0,0,161,
        162,5,108,0,0,162,163,5,115,0,0,163,165,5,101,0,0,164,155,1,0,0,
        0,164,159,1,0,0,0,165,22,1,0,0,0,166,167,5,110,0,0,167,168,5,105,
        0,0,168,169,5,108,0,0,169,24,1,0,0,0,170,174,7,1,0,0,171,173,7,2,
        0,0,172,171,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,
        0,0,175,26,1,0,0,0,176,174,1,0,0,0,177,178,5,48,0,0,178,179,5,120,
        0,0,179,181,1,0,0,0,180,182,7,3,0,0,181,180,1,0,0,0,182,183,1,0,
        0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,28,1,0,0,0,185,186,5,43,
        0,0,186,30,1,0,0,0,187,188,5,45,0,0,188,32,1,0,0,0,189,190,5,42,
        0,0,190,34,1,0,0,0,191,192,5,47,0,0,192,36,1,0,0,0,193,194,5,37,
        0,0,194,38,1,0,0,0,195,196,5,61,0,0,196,197,5,61,0,0,197,40,1,0,
        0,0,198,199,5,33,0,0,199,200,5,61,0,0,200,42,1,0,0,0,201,202,5,62,
        0,0,202,44,1,0,0,0,203,204,5,60,0,0,204,46,1,0,0,0,205,206,5,62,
        0,0,206,207,5,61,0,0,207,48,1,0,0,0,208,209,5,60,0,0,209,210,5,61,
        0,0,210,50,1,0,0,0,211,212,5,38,0,0,212,213,5,38,0,0,213,52,1,0,
        0,0,214,215,5,124,0,0,215,216,5,124,0,0,216,54,1,0,0,0,217,218,5,
        33,0,0,218,56,1,0,0,0,219,220,5,46,0,0,220,58,1,0,0,0,221,222,5,
        44,0,0,222,60,1,0,0,0,223,224,5,61,0,0,224,62,1,0,0,0,225,226,5,
        40,0,0,226,64,1,0,0,0,227,228,5,41,0,0,228,66,1,0,0,0,229,230,5,
        123,0,0,230,68,1,0,0,0,231,232,5,125,0,0,232,70,1,0,0,0,233,234,
        5,91,0,0,234,72,1,0,0,0,235,236,5,93,0,0,236,74,1,0,0,0,237,238,
        5,45,0,0,238,239,5,62,0,0,239,76,1,0,0,0,240,241,5,47,0,0,241,242,
        5,47,0,0,242,246,1,0,0,0,243,245,9,0,0,0,244,243,1,0,0,0,245,248,
        1,0,0,0,246,247,1,0,0,0,246,244,1,0,0,0,247,249,1,0,0,0,248,246,
        1,0,0,0,249,250,5,10,0,0,250,251,1,0,0,0,251,252,6,38,0,0,252,78,
        1,0,0,0,253,255,7,4,0,0,254,253,1,0,0,0,255,256,1,0,0,0,256,254,
        1,0,0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,259,6,39,0,0,259,80,
        1,0,0,0,14,0,112,117,120,125,132,140,148,153,164,174,183,246,256,
        1,6,0,0
    ]

class ClusterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    USE = 2
    ELSE = 3
    FUNC = 4
    WHILE = 5
    RETURN = 6
    INT = 7
    FLOAT = 8
    APOSTROPHE = 9
    STRING = 10
    BOOL = 11
    NIL = 12
    ID = 13
    HEX = 14
    ADD = 15
    SUB = 16
    MUL = 17
    DIV = 18
    MOD = 19
    EEQ = 20
    NEQ = 21
    GT = 22
    LT = 23
    GTE = 24
    LTE = 25
    AND = 26
    OR = 27
    NOT = 28
    DOT = 29
    COMMA = 30
    ASSIGN = 31
    LPAREN = 32
    RPAREN = 33
    LBRACE = 34
    RBRACE = 35
    LBRACK = 36
    RBRACK = 37
    RETURNS = 38
    COMMENT = 39
    WHITESPACE = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'use'", "'else'", "'func'", "'while'", "'return'", 
            "'''", "'nil'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
            "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", "'!'", "'.'", 
            "','", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "USE", "ELSE", "FUNC", "WHILE", "RETURN", "INT", "FLOAT", 
            "APOSTROPHE", "STRING", "BOOL", "NIL", "ID", "HEX", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "EEQ", "NEQ", "GT", "LT", "GTE", "LTE", 
            "AND", "OR", "NOT", "DOT", "COMMA", "ASSIGN", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACK", "RBRACK", "RETURNS", "COMMENT", 
            "WHITESPACE" ]

    ruleNames = [ "IF", "USE", "ELSE", "FUNC", "WHILE", "RETURN", "INT", 
                  "FLOAT", "APOSTROPHE", "STRING", "BOOL", "NIL", "ID", 
                  "HEX", "ADD", "SUB", "MUL", "DIV", "MOD", "EEQ", "NEQ", 
                  "GT", "LT", "GTE", "LTE", "AND", "OR", "NOT", "DOT", "COMMA", 
                  "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "RETURNS", "COMMENT", "WHITESPACE" ]

    grammarFileName = "Cluster.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


