// Generated from d:/FACULDADE/Compiladores/FINAL/compiler_poglin/grammars/poglin.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class poglinParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		START=1, END=2, VAR=3, IF=4, ELSE=5, WHILE=6, ESCREVA=7, LEIA=8, POG=9, 
		INT_TYPE=10, STRING_TYPE=11, PLUS=12, MINUS=13, MULT=14, DIV=15, EQUALS=16, 
		NEQUALS=17, LT=18, LTE=19, GT=20, GTE=21, AND=22, OR=23, NOT=24, LBRACE=25, 
		RBRACE=26, LPAREN=27, RPAREN=28, SEMI=29, COLON=30, ASSIGN=31, ID=32, 
		INT=33, STRING=34, WS=35, COMMENT=36;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_expression = 2, RULE_logicalOrExpression = 3, 
		RULE_logicalAndExpression = 4, RULE_equalityExpression = 5, RULE_relationalExpression = 6, 
		RULE_additiveExpression = 7, RULE_multiplicativeExpression = 8, RULE_unaryExpression = 9, 
		RULE_primary = 10, RULE_type = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "expression", "logicalOrExpression", "logicalAndExpression", 
			"equalityExpression", "relationalExpression", "additiveExpression", "multiplicativeExpression", 
			"unaryExpression", "primary", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'start'", "'end'", "'var'", "'if'", "'else'", "'while'", "'escreva'", 
			"'leia'", "'pog'", "'Int'", "'String'", "'+'", "'-'", "'*'", "'/'", "'=='", 
			"'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", "'{'", "'}'", 
			"'('", "')'", "';'", "':'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "START", "END", "VAR", "IF", "ELSE", "WHILE", "ESCREVA", "LEIA", 
			"POG", "INT_TYPE", "STRING_TYPE", "PLUS", "MINUS", "MULT", "DIV", "EQUALS", 
			"NEQUALS", "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", "LBRACE", "RBRACE", 
			"LPAREN", "RPAREN", "SEMI", "COLON", "ASSIGN", "ID", "INT", "STRING", 
			"WS", "COMMENT"
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
	public String getGrammarFileName() { return "poglin.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public poglinParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode START() { return getToken(poglinParser.START, 0); }
		public TerminalNode LBRACE() { return getToken(poglinParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(poglinParser.RBRACE, 0); }
		public TerminalNode END() { return getToken(poglinParser.END, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(START);
			setState(25);
			match(LBRACE);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4294968024L) != 0)) {
				{
				{
				setState(26);
				statement();
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(RBRACE);
			setState(33);
			match(END);
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
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends StatementContext {
		public TerminalNode WHILE() { return getToken(poglinParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(poglinParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(poglinParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(poglinParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(poglinParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public WhileStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PogStatementContext extends StatementContext {
		public TerminalNode POG() { return getToken(poglinParser.POG, 0); }
		public TerminalNode SEMI() { return getToken(poglinParser.SEMI, 0); }
		public PogStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintStatementContext extends StatementContext {
		public TerminalNode ESCREVA() { return getToken(poglinParser.ESCREVA, 0); }
		public TerminalNode LPAREN() { return getToken(poglinParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(poglinParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(poglinParser.SEMI, 0); }
		public PrintStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends StatementContext {
		public TerminalNode ID() { return getToken(poglinParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(poglinParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(poglinParser.SEMI, 0); }
		public AssignmentContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReadStatementContext extends StatementContext {
		public TerminalNode ID() { return getToken(poglinParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(poglinParser.ASSIGN, 0); }
		public TerminalNode LEIA() { return getToken(poglinParser.LEIA, 0); }
		public TerminalNode LPAREN() { return getToken(poglinParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(poglinParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(poglinParser.SEMI, 0); }
		public ReadStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends StatementContext {
		public TerminalNode IF() { return getToken(poglinParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(poglinParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(poglinParser.RPAREN, 0); }
		public List<TerminalNode> LBRACE() { return getTokens(poglinParser.LBRACE); }
		public TerminalNode LBRACE(int i) {
			return getToken(poglinParser.LBRACE, i);
		}
		public List<TerminalNode> RBRACE() { return getTokens(poglinParser.RBRACE); }
		public TerminalNode RBRACE(int i) {
			return getToken(poglinParser.RBRACE, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(poglinParser.ELSE, 0); }
		public IfStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclarationContext extends StatementContext {
		public TerminalNode VAR() { return getToken(poglinParser.VAR, 0); }
		public TerminalNode ID() { return getToken(poglinParser.ID, 0); }
		public TerminalNode COLON() { return getToken(poglinParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(poglinParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(poglinParser.SEMI, 0); }
		public VarDeclarationContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(98);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				_localctx = new VarDeclarationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				match(VAR);
				setState(36);
				match(ID);
				setState(37);
				match(COLON);
				setState(38);
				type();
				setState(39);
				match(ASSIGN);
				setState(40);
				expression();
				setState(41);
				match(SEMI);
				}
				break;
			case 2:
				_localctx = new AssignmentContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				match(ID);
				setState(44);
				match(ASSIGN);
				setState(45);
				expression();
				setState(46);
				match(SEMI);
				}
				break;
			case 3:
				_localctx = new PrintStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(48);
				match(ESCREVA);
				setState(49);
				match(LPAREN);
				setState(50);
				expression();
				setState(51);
				match(RPAREN);
				setState(52);
				match(SEMI);
				}
				break;
			case 4:
				_localctx = new ReadStatementContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(54);
				match(ID);
				setState(55);
				match(ASSIGN);
				setState(56);
				match(LEIA);
				setState(57);
				match(LPAREN);
				setState(58);
				match(RPAREN);
				setState(59);
				match(SEMI);
				}
				break;
			case 5:
				_localctx = new IfStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				match(IF);
				setState(61);
				match(LPAREN);
				setState(62);
				expression();
				setState(63);
				match(RPAREN);
				setState(64);
				match(LBRACE);
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4294968024L) != 0)) {
					{
					{
					setState(65);
					statement();
					}
					}
					setState(70);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(71);
				match(RBRACE);
				setState(81);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ELSE) {
					{
					setState(72);
					match(ELSE);
					setState(73);
					match(LBRACE);
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4294968024L) != 0)) {
						{
						{
						setState(74);
						statement();
						}
						}
						setState(79);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(80);
					match(RBRACE);
					}
				}

				}
				break;
			case 6:
				_localctx = new WhileStatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(83);
				match(WHILE);
				setState(84);
				match(LPAREN);
				setState(85);
				expression();
				setState(86);
				match(RPAREN);
				setState(87);
				match(LBRACE);
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4294968024L) != 0)) {
					{
					{
					setState(88);
					statement();
					}
					}
					setState(93);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(94);
				match(RBRACE);
				}
				break;
			case 7:
				_localctx = new PogStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(96);
				match(POG);
				setState(97);
				match(SEMI);
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
	public static class ExpressionContext extends ParserRuleContext {
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			logicalOrExpression();
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
	public static class LogicalOrExpressionContext extends ParserRuleContext {
		public List<LogicalAndExpressionContext> logicalAndExpression() {
			return getRuleContexts(LogicalAndExpressionContext.class);
		}
		public LogicalAndExpressionContext logicalAndExpression(int i) {
			return getRuleContext(LogicalAndExpressionContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(poglinParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(poglinParser.OR, i);
		}
		public LogicalOrExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrExpression; }
	}

	public final LogicalOrExpressionContext logicalOrExpression() throws RecognitionException {
		LogicalOrExpressionContext _localctx = new LogicalOrExpressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_logicalOrExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			logicalAndExpression();
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(103);
				match(OR);
				setState(104);
				logicalAndExpression();
				}
				}
				setState(109);
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

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndExpressionContext extends ParserRuleContext {
		public List<EqualityExpressionContext> equalityExpression() {
			return getRuleContexts(EqualityExpressionContext.class);
		}
		public EqualityExpressionContext equalityExpression(int i) {
			return getRuleContext(EqualityExpressionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(poglinParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(poglinParser.AND, i);
		}
		public LogicalAndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndExpression; }
	}

	public final LogicalAndExpressionContext logicalAndExpression() throws RecognitionException {
		LogicalAndExpressionContext _localctx = new LogicalAndExpressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_logicalAndExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			equalityExpression();
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(111);
				match(AND);
				setState(112);
				equalityExpression();
				}
				}
				setState(117);
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

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityExpressionContext extends ParserRuleContext {
		public List<RelationalExpressionContext> relationalExpression() {
			return getRuleContexts(RelationalExpressionContext.class);
		}
		public RelationalExpressionContext relationalExpression(int i) {
			return getRuleContext(RelationalExpressionContext.class,i);
		}
		public List<TerminalNode> EQUALS() { return getTokens(poglinParser.EQUALS); }
		public TerminalNode EQUALS(int i) {
			return getToken(poglinParser.EQUALS, i);
		}
		public List<TerminalNode> NEQUALS() { return getTokens(poglinParser.NEQUALS); }
		public TerminalNode NEQUALS(int i) {
			return getToken(poglinParser.NEQUALS, i);
		}
		public EqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityExpression; }
	}

	public final EqualityExpressionContext equalityExpression() throws RecognitionException {
		EqualityExpressionContext _localctx = new EqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_equalityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			relationalExpression();
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EQUALS || _la==NEQUALS) {
				{
				{
				setState(119);
				_la = _input.LA(1);
				if ( !(_la==EQUALS || _la==NEQUALS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(120);
				relationalExpression();
				}
				}
				setState(125);
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

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalExpressionContext extends ParserRuleContext {
		public List<AdditiveExpressionContext> additiveExpression() {
			return getRuleContexts(AdditiveExpressionContext.class);
		}
		public AdditiveExpressionContext additiveExpression(int i) {
			return getRuleContext(AdditiveExpressionContext.class,i);
		}
		public List<TerminalNode> LT() { return getTokens(poglinParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(poglinParser.LT, i);
		}
		public List<TerminalNode> LTE() { return getTokens(poglinParser.LTE); }
		public TerminalNode LTE(int i) {
			return getToken(poglinParser.LTE, i);
		}
		public List<TerminalNode> GT() { return getTokens(poglinParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(poglinParser.GT, i);
		}
		public List<TerminalNode> GTE() { return getTokens(poglinParser.GTE); }
		public TerminalNode GTE(int i) {
			return getToken(poglinParser.GTE, i);
		}
		public RelationalExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalExpression; }
	}

	public final RelationalExpressionContext relationalExpression() throws RecognitionException {
		RelationalExpressionContext _localctx = new RelationalExpressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_relationalExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			additiveExpression();
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3932160L) != 0)) {
				{
				{
				setState(127);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3932160L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(128);
				additiveExpression();
				}
				}
				setState(133);
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

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveExpressionContext extends ParserRuleContext {
		public List<MultiplicativeExpressionContext> multiplicativeExpression() {
			return getRuleContexts(MultiplicativeExpressionContext.class);
		}
		public MultiplicativeExpressionContext multiplicativeExpression(int i) {
			return getRuleContext(MultiplicativeExpressionContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(poglinParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(poglinParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(poglinParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(poglinParser.MINUS, i);
		}
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			multiplicativeExpression();
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(135);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(136);
				multiplicativeExpression();
				}
				}
				setState(141);
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

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public List<UnaryExpressionContext> unaryExpression() {
			return getRuleContexts(UnaryExpressionContext.class);
		}
		public UnaryExpressionContext unaryExpression(int i) {
			return getRuleContext(UnaryExpressionContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(poglinParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(poglinParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(poglinParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(poglinParser.DIV, i);
		}
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_multiplicativeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			unaryExpression();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(143);
				_la = _input.LA(1);
				if ( !(_la==MULT || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(144);
				unaryExpression();
				}
				}
				setState(149);
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

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExpressionContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(poglinParser.NOT, 0); }
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpression; }
	}

	public final UnaryExpressionContext unaryExpression() throws RecognitionException {
		UnaryExpressionContext _localctx = new UnaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_unaryExpression);
		try {
			setState(153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(NOT);
				setState(151);
				unaryExpression();
				}
				break;
			case LPAREN:
			case ID:
			case INT:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				primary();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class PrimaryContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(poglinParser.INT, 0); }
		public TerminalNode STRING() { return getToken(poglinParser.STRING, 0); }
		public TerminalNode ID() { return getToken(poglinParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(poglinParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(poglinParser.RPAREN, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_primary);
		try {
			setState(162);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(155);
				match(INT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(157);
				match(ID);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 4);
				{
				setState(158);
				match(LPAREN);
				setState(159);
				expression();
				setState(160);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(poglinParser.INT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(poglinParser.STRING_TYPE, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			_la = _input.LA(1);
			if ( !(_la==INT_TYPE || _la==STRING_TYPE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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
		"\u0004\u0001$\u00a7\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u001c\b\u0000\n\u0000\f\u0000"+
		"\u001f\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001"+
		"C\b\u0001\n\u0001\f\u0001F\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0005\u0001L\b\u0001\n\u0001\f\u0001O\t\u0001\u0001\u0001"+
		"\u0003\u0001R\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u0001Z\b\u0001\n\u0001\f\u0001]\t\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001c\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003"+
		"j\b\u0003\n\u0003\f\u0003m\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0005\u0004r\b\u0004\n\u0004\f\u0004u\t\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0005\u0005z\b\u0005\n\u0005\f\u0005}\t\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0005\u0006\u0082\b\u0006\n\u0006\f\u0006\u0085"+
		"\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007\u008a\b\u0007"+
		"\n\u0007\f\u0007\u008d\t\u0007\u0001\b\u0001\b\u0001\b\u0005\b\u0092\b"+
		"\b\n\b\f\b\u0095\t\b\u0001\t\u0001\t\u0001\t\u0003\t\u009a\b\t\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00a3\b\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0000\u0000\f\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0010\u0012\u0014\u0016\u0000\u0005\u0001\u0000\u0010\u0011"+
		"\u0001\u0000\u0012\u0015\u0001\u0000\f\r\u0001\u0000\u000e\u000f\u0001"+
		"\u0000\n\u000b\u00af\u0000\u0018\u0001\u0000\u0000\u0000\u0002b\u0001"+
		"\u0000\u0000\u0000\u0004d\u0001\u0000\u0000\u0000\u0006f\u0001\u0000\u0000"+
		"\u0000\bn\u0001\u0000\u0000\u0000\nv\u0001\u0000\u0000\u0000\f~\u0001"+
		"\u0000\u0000\u0000\u000e\u0086\u0001\u0000\u0000\u0000\u0010\u008e\u0001"+
		"\u0000\u0000\u0000\u0012\u0099\u0001\u0000\u0000\u0000\u0014\u00a2\u0001"+
		"\u0000\u0000\u0000\u0016\u00a4\u0001\u0000\u0000\u0000\u0018\u0019\u0005"+
		"\u0001\u0000\u0000\u0019\u001d\u0005\u0019\u0000\u0000\u001a\u001c\u0003"+
		"\u0002\u0001\u0000\u001b\u001a\u0001\u0000\u0000\u0000\u001c\u001f\u0001"+
		"\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001"+
		"\u0000\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000"+
		"\u0000\u0000 !\u0005\u001a\u0000\u0000!\"\u0005\u0002\u0000\u0000\"\u0001"+
		"\u0001\u0000\u0000\u0000#$\u0005\u0003\u0000\u0000$%\u0005 \u0000\u0000"+
		"%&\u0005\u001e\u0000\u0000&\'\u0003\u0016\u000b\u0000\'(\u0005\u001f\u0000"+
		"\u0000()\u0003\u0004\u0002\u0000)*\u0005\u001d\u0000\u0000*c\u0001\u0000"+
		"\u0000\u0000+,\u0005 \u0000\u0000,-\u0005\u001f\u0000\u0000-.\u0003\u0004"+
		"\u0002\u0000./\u0005\u001d\u0000\u0000/c\u0001\u0000\u0000\u000001\u0005"+
		"\u0007\u0000\u000012\u0005\u001b\u0000\u000023\u0003\u0004\u0002\u0000"+
		"34\u0005\u001c\u0000\u000045\u0005\u001d\u0000\u00005c\u0001\u0000\u0000"+
		"\u000067\u0005 \u0000\u000078\u0005\u001f\u0000\u000089\u0005\b\u0000"+
		"\u00009:\u0005\u001b\u0000\u0000:;\u0005\u001c\u0000\u0000;c\u0005\u001d"+
		"\u0000\u0000<=\u0005\u0004\u0000\u0000=>\u0005\u001b\u0000\u0000>?\u0003"+
		"\u0004\u0002\u0000?@\u0005\u001c\u0000\u0000@D\u0005\u0019\u0000\u0000"+
		"AC\u0003\u0002\u0001\u0000BA\u0001\u0000\u0000\u0000CF\u0001\u0000\u0000"+
		"\u0000DB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EG\u0001\u0000"+
		"\u0000\u0000FD\u0001\u0000\u0000\u0000GQ\u0005\u001a\u0000\u0000HI\u0005"+
		"\u0005\u0000\u0000IM\u0005\u0019\u0000\u0000JL\u0003\u0002\u0001\u0000"+
		"KJ\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000"+
		"\u0000MN\u0001\u0000\u0000\u0000NP\u0001\u0000\u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000PR\u0005\u001a\u0000\u0000QH\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000Rc\u0001\u0000\u0000\u0000ST\u0005\u0006\u0000\u0000"+
		"TU\u0005\u001b\u0000\u0000UV\u0003\u0004\u0002\u0000VW\u0005\u001c\u0000"+
		"\u0000W[\u0005\u0019\u0000\u0000XZ\u0003\u0002\u0001\u0000YX\u0001\u0000"+
		"\u0000\u0000Z]\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001"+
		"\u0000\u0000\u0000\\^\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"^_\u0005\u001a\u0000\u0000_c\u0001\u0000\u0000\u0000`a\u0005\t\u0000\u0000"+
		"ac\u0005\u001d\u0000\u0000b#\u0001\u0000\u0000\u0000b+\u0001\u0000\u0000"+
		"\u0000b0\u0001\u0000\u0000\u0000b6\u0001\u0000\u0000\u0000b<\u0001\u0000"+
		"\u0000\u0000bS\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000c\u0003"+
		"\u0001\u0000\u0000\u0000de\u0003\u0006\u0003\u0000e\u0005\u0001\u0000"+
		"\u0000\u0000fk\u0003\b\u0004\u0000gh\u0005\u0017\u0000\u0000hj\u0003\b"+
		"\u0004\u0000ig\u0001\u0000\u0000\u0000jm\u0001\u0000\u0000\u0000ki\u0001"+
		"\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000l\u0007\u0001\u0000\u0000"+
		"\u0000mk\u0001\u0000\u0000\u0000ns\u0003\n\u0005\u0000op\u0005\u0016\u0000"+
		"\u0000pr\u0003\n\u0005\u0000qo\u0001\u0000\u0000\u0000ru\u0001\u0000\u0000"+
		"\u0000sq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000t\t\u0001\u0000"+
		"\u0000\u0000us\u0001\u0000\u0000\u0000v{\u0003\f\u0006\u0000wx\u0007\u0000"+
		"\u0000\u0000xz\u0003\f\u0006\u0000yw\u0001\u0000\u0000\u0000z}\u0001\u0000"+
		"\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|\u000b"+
		"\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000~\u0083\u0003\u000e"+
		"\u0007\u0000\u007f\u0080\u0007\u0001\u0000\u0000\u0080\u0082\u0003\u000e"+
		"\u0007\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000"+
		"\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000"+
		"\u0000\u0000\u0084\r\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000"+
		"\u0000\u0086\u008b\u0003\u0010\b\u0000\u0087\u0088\u0007\u0002\u0000\u0000"+
		"\u0088\u008a\u0003\u0010\b\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a"+
		"\u008d\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b"+
		"\u008c\u0001\u0000\u0000\u0000\u008c\u000f\u0001\u0000\u0000\u0000\u008d"+
		"\u008b\u0001\u0000\u0000\u0000\u008e\u0093\u0003\u0012\t\u0000\u008f\u0090"+
		"\u0007\u0003\u0000\u0000\u0090\u0092\u0003\u0012\t\u0000\u0091\u008f\u0001"+
		"\u0000\u0000\u0000\u0092\u0095\u0001\u0000\u0000\u0000\u0093\u0091\u0001"+
		"\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0011\u0001"+
		"\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0096\u0097\u0005"+
		"\u0018\u0000\u0000\u0097\u009a\u0003\u0012\t\u0000\u0098\u009a\u0003\u0014"+
		"\n\u0000\u0099\u0096\u0001\u0000\u0000\u0000\u0099\u0098\u0001\u0000\u0000"+
		"\u0000\u009a\u0013\u0001\u0000\u0000\u0000\u009b\u00a3\u0005!\u0000\u0000"+
		"\u009c\u00a3\u0005\"\u0000\u0000\u009d\u00a3\u0005 \u0000\u0000\u009e"+
		"\u009f\u0005\u001b\u0000\u0000\u009f\u00a0\u0003\u0004\u0002\u0000\u00a0"+
		"\u00a1\u0005\u001c\u0000\u0000\u00a1\u00a3\u0001\u0000\u0000\u0000\u00a2"+
		"\u009b\u0001\u0000\u0000\u0000\u00a2\u009c\u0001\u0000\u0000\u0000\u00a2"+
		"\u009d\u0001\u0000\u0000\u0000\u00a2\u009e\u0001\u0000\u0000\u0000\u00a3"+
		"\u0015\u0001\u0000\u0000\u0000\u00a4\u00a5\u0007\u0004\u0000\u0000\u00a5"+
		"\u0017\u0001\u0000\u0000\u0000\u000e\u001dDMQ[bks{\u0083\u008b\u0093\u0099"+
		"\u00a2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}