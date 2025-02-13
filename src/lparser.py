from llexer import LLexer
from ltoken import LToken

class STOP(Exception):
	pass

class LParser:
	def __init__(self, lexer: LLexer) -> None:
		self.lexer = lexer
		self.curr_token: LToken

	def parse(self) -> None:
		try:
			self.next_token()
			self.statements()
		except STOP:
			pass

	def next_token(self) -> None:
		self.curr_token = self.lexer.get_next_token()
		if self.curr_token.token_code == LToken.ERROR:
			self.error()
	
	def statements(self) -> None:
		if self.curr_token is None:
			return

		self.parse_statement()

		if self.curr_token.token_code == LToken.SEMICOL:
			self.next_token()
			self.statements()
			return
		
		if self.curr_token.token_code == LToken.END:
			return
		
		self.error()

	def parse_statement(self) -> None:
		token = self.curr_token.token_code

		if token == LToken.PRINT:
			self.next_token()
			if self.curr_token.token_code == LToken.ID:
				print(f"PUSH {self.curr_token.lexeme}")
				print("PRINT")
				self.next_token()
				return
		
		if token == LToken.ID:
			print(f"PUSH {self.curr_token.lexeme}")
			self.next_token()
			if self.curr_token.token_code == LToken.ASSIGN:
				self.next_token()
				self.parse_expression()
				print("ASSIGN")
				return
			
		print("Syntax error")

	def parse_expression(self) -> None:
		self.parse_term()
		if self.curr_token.token_code == LToken.PLUS:
			self.next_token()
			self.parse_expression()
			print("ADD")
			return


	def parse_term(self) -> None:
		self.parse_factor()
		if self.curr_token.token_code == LToken.MULT:
			self.next_token()
			self.parse_term()
			print("MULT")

	def parse_factor(self) -> None:
		token = self.curr_token.token_code
		if token == LToken.INT:
			print(f"PUSH {self.curr_token.lexeme}")
		elif token == LToken.ID:
			print(f"PUSH {self.curr_token.lexeme}")

		elif token == LToken.MINUS:
			self.next_token()
			self.parse_factor()
			print("UMINUS")
			return

		elif token == LToken.LPAREN:
			self.next_token()
			self.parse_expression()
		
		elif token == LToken.RPAREN:
			pass

		else:
			self.error()
		self.next_token()

	def error(self) -> None:
		print("Syntax error")
		raise STOP
