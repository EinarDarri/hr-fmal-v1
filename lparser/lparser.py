from llexer import LLexer
from llexer.ltoken import LToken

class LParser:
	def __init__(self, lexer: LLexer) -> None:
		self.lexer = lexer
		self.curr_token: LToken

	def parse(self) -> None:
		self.next_token()
		self.statements()
		print()

	def next_token(self) -> None:
		self.curr_token = self.lexer.get_next_token()
		if self.curr_token.token_code == LToken.ERROR:
			self.error()
	
	def statements(self) -> None:
		if self.curr_token is None:
			return

		while self.curr_token.token_code != LToken.END:
			self.parse_statement()

	def parse_statement(self) -> None:
		pass

	def parse_expression(self) -> None:
		pass

	def parse_term(self) -> None:
		pass

	def parse_factor(self) -> None:
		pass

	def error(self) -> None:
		raise SyntaxError
		print("Syntax error")