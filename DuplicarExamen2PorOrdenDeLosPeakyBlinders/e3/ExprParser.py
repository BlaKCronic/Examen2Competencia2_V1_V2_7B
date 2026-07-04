# Generated from ./Expr.g4 by ANTLR 4.13.2
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
        4,1,7,30,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,5,2,25,8,2,10,2,12,2,
        28,9,2,1,2,0,0,3,0,2,4,0,0,29,0,6,1,0,0,0,2,20,1,0,0,0,4,26,1,0,
        0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,1,0,0,10,11,5,5,0,
        0,11,12,5,2,0,0,12,13,3,4,2,0,13,14,5,3,0,0,14,15,5,5,0,0,15,16,
        5,2,0,0,16,21,1,0,0,0,17,18,5,1,0,0,18,19,5,5,0,0,19,21,5,4,0,0,
        20,9,1,0,0,0,20,17,1,0,0,0,21,3,1,0,0,0,22,25,5,6,0,0,23,25,3,2,
        1,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,
        1,0,0,0,27,5,1,0,0,0,28,26,1,0,0,0,3,20,24,26
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'</'", "'/>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TAG_NAME", "TEXT", "WS" ]

    RULE_root = 0
    RULE_xml = 1
    RULE_content = 2

    ruleNames =  [ "root", "xml", "content" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    TAG_NAME=5
    TEXT=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xml(self):
            return self.getTypedRuleContext(ExprParser.XmlContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.xml()
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XmlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TAG_NAME)
            else:
                return self.getToken(ExprParser.TAG_NAME, i)

        def content(self):
            return self.getTypedRuleContext(ExprParser.ContentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_xml




    def xml(self):

        localctx = ExprParser.XmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_xml)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(ExprParser.T__0)
                self.state = 10
                self.match(ExprParser.TAG_NAME)
                self.state = 11
                self.match(ExprParser.T__1)
                self.state = 12
                self.content()
                self.state = 13
                self.match(ExprParser.T__2)
                self.state = 14
                self.match(ExprParser.TAG_NAME)
                self.state = 15
                self.match(ExprParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(ExprParser.T__0)
                self.state = 18
                self.match(ExprParser.TAG_NAME)
                self.state = 19
                self.match(ExprParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TEXT)
            else:
                return self.getToken(ExprParser.TEXT, i)

        def xml(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.XmlContext)
            else:
                return self.getTypedRuleContext(ExprParser.XmlContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_content




    def content(self):

        localctx = ExprParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==6:
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 22
                    self.match(ExprParser.TEXT)
                    pass
                elif token in [1]:
                    self.state = 23
                    self.xml()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





