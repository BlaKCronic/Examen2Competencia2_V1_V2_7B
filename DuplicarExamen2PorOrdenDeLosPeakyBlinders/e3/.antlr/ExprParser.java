// Generated from c:/Users/100204924/Documents/tec/veranos/automatas2/examen/DuplicarExamen2PorOrdenDeLosPeakyBlinders/e3/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, TAG_NAME=5, TEXT=6, WS=7;
	public static final int
		RULE_root = 0, RULE_xml = 1, RULE_content = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "xml", "content"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'<'", "'>'", "'</'", "'/>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "TAG_NAME", "TEXT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public XmlContext xml() {
			return getRuleContext(XmlContext.class,0);
		}
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(6);
			xml();
			setState(7);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class XmlContext extends ParserRuleContext {
		public List<TerminalNode> TAG_NAME() { return getTokens(ExprParser.TAG_NAME); }
		public TerminalNode TAG_NAME(int i) {
			return getToken(ExprParser.TAG_NAME, i);
		}
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public XmlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_xml; }
	}

	public final XmlContext xml() throws RecognitionException {
		XmlContext _localctx = new XmlContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_xml);
		try {
			setState(20);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(9);
				match(T__0);
				setState(10);
				match(TAG_NAME);
				setState(11);
				match(T__1);
				setState(12);
				content();
				setState(13);
				match(T__2);
				setState(14);
				match(TAG_NAME);
				setState(15);
				match(T__1);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(17);
				match(T__0);
				setState(18);
				match(TAG_NAME);
				setState(19);
				match(T__3);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContentContext extends ParserRuleContext {
		public List<TerminalNode> TEXT() { return getTokens(ExprParser.TEXT); }
		public TerminalNode TEXT(int i) {
			return getToken(ExprParser.TEXT, i);
		}
		public List<XmlContext> xml() {
			return getRuleContexts(XmlContext.class);
		}
		public XmlContext xml(int i) {
			return getRuleContext(XmlContext.class,i);
		}
		public ContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_content; }
	}

	public final ContentContext content() throws RecognitionException {
		ContentContext _localctx = new ContentContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_content);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==TEXT) {
				{
				setState(24);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TEXT:
					{
					setState(22);
					match(TEXT);
					}
					break;
				case T__0:
					{
					setState(23);
					xml();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(28);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0007\u001e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0015\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0005\u0002\u0019\b\u0002\n\u0002\f\u0002\u001c"+
		"\t\u0002\u0001\u0002\u0000\u0000\u0003\u0000\u0002\u0004\u0000\u0000\u001d"+
		"\u0000\u0006\u0001\u0000\u0000\u0000\u0002\u0014\u0001\u0000\u0000\u0000"+
		"\u0004\u001a\u0001\u0000\u0000\u0000\u0006\u0007\u0003\u0002\u0001\u0000"+
		"\u0007\b\u0005\u0000\u0000\u0001\b\u0001\u0001\u0000\u0000\u0000\t\n\u0005"+
		"\u0001\u0000\u0000\n\u000b\u0005\u0005\u0000\u0000\u000b\f\u0005\u0002"+
		"\u0000\u0000\f\r\u0003\u0004\u0002\u0000\r\u000e\u0005\u0003\u0000\u0000"+
		"\u000e\u000f\u0005\u0005\u0000\u0000\u000f\u0010\u0005\u0002\u0000\u0000"+
		"\u0010\u0015\u0001\u0000\u0000\u0000\u0011\u0012\u0005\u0001\u0000\u0000"+
		"\u0012\u0013\u0005\u0005\u0000\u0000\u0013\u0015\u0005\u0004\u0000\u0000"+
		"\u0014\t\u0001\u0000\u0000\u0000\u0014\u0011\u0001\u0000\u0000\u0000\u0015"+
		"\u0003\u0001\u0000\u0000\u0000\u0016\u0019\u0005\u0006\u0000\u0000\u0017"+
		"\u0019\u0003\u0002\u0001\u0000\u0018\u0016\u0001\u0000\u0000\u0000\u0018"+
		"\u0017\u0001\u0000\u0000\u0000\u0019\u001c\u0001\u0000\u0000\u0000\u001a"+
		"\u0018\u0001\u0000\u0000\u0000\u001a\u001b\u0001\u0000\u0000\u0000\u001b"+
		"\u0005\u0001\u0000\u0000\u0000\u001c\u001a\u0001\u0000\u0000\u0000\u0003"+
		"\u0014\u0018\u001a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}