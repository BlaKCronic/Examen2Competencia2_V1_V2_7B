# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,44,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,5,4,28,8,4,
        10,4,12,4,31,9,4,1,5,4,5,34,8,5,11,5,12,5,35,1,6,4,6,39,8,6,11,6,
        12,6,40,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,4,2,0,65,
        90,97,122,5,0,45,45,48,57,65,90,95,95,97,122,1,0,60,60,3,0,9,10,
        13,13,32,32,46,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,
        19,1,0,0,0,7,22,1,0,0,0,9,25,1,0,0,0,11,33,1,0,0,0,13,38,1,0,0,0,
        15,16,5,60,0,0,16,2,1,0,0,0,17,18,5,62,0,0,18,4,1,0,0,0,19,20,5,
        60,0,0,20,21,5,47,0,0,21,6,1,0,0,0,22,23,5,47,0,0,23,24,5,62,0,0,
        24,8,1,0,0,0,25,29,7,0,0,0,26,28,7,1,0,0,27,26,1,0,0,0,28,31,1,0,
        0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,10,1,0,0,0,31,29,1,0,0,0,32,34,
        8,2,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,
        36,12,1,0,0,0,37,39,7,3,0,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,
        0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,6,6,0,0,43,14,1,0,0,0,4,
        0,29,35,40,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    TAG_NAME = 5
    TEXT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'</'", "'/>'" ]

    symbolicNames = [ "<INVALID>",
            "TAG_NAME", "TEXT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "TAG_NAME", "TEXT", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


