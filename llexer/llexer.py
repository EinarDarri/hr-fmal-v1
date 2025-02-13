from sys import stdin
from re import match as re_match
from .ltoken import LToken, TokenIdentityEnum


class LLexer:
	MODE_DEFAULT = -1
	MODE_INT = 0
	MODE_STR = 1
	MODE_OP = 2

	__current_lexeme = ""
	__remaining_lexeme = ""
	__operators =  ["(", ")", "-", "+", "=", "*", ";"]

	@classmethod
	def get_next_token(cls) -> LToken:
		cls.__get_next_lexeme()
		return cls.__parse_token()
	
	@classmethod
	def __get_mode(cls, lex: str) -> int:
		if lex == "":
			return LLexer.MODE_DEFAULT
		if lex.isalpha():
			return LLexer.MODE_STR
		elif lex.isdigit():
			return LLexer.MODE_INT
		elif cls.__is_operator(lex):
			return LLexer.MODE_OP
		else:
			raise Exception("Invalid lex provided to __get_mode")

	@classmethod
	def __get_next_lexeme(cls) -> None:
		current_mode: int = cls.__get_mode(cls.__remaining_lexeme)
		cls.__current_lexeme = cls.__remaining_lexeme
		cls.__remaining_lexeme = ""
		next_char = ""
		# If there is a lexeme from a prior operation cached in the Lexer and it's an operator, return a new token with said lexeme.
		if cls.__is_operator(cls.__current_lexeme):
			return
		while(True):
			next_char = stdin.read(1)
			# Ignore newline/carriage return
			if next_char == "\n" or next_char == "\r":
				continue
			# Assume a whitespace indicates the end of the token
			elif next_char == " ":
				break

			if current_mode == LLexer.MODE_DEFAULT:
				if next_char.isalpha():
					# Expect characters
					current_mode = LLexer.MODE_STR
				elif next_char.isdigit():
					# Expect numbers
					current_mode = LLexer.MODE_INT
				elif cls.__is_operator(next_char):
					# Expect operators
					current_mode = LLexer.MODE_OP
			elif current_mode == LLexer.MODE_STR:
				if next_char.isalpha() is False:
					cls.__remaining_lexeme = next_char
					return
			elif current_mode == LLexer.MODE_INT:
				if next_char.isdigit() is False:
					cls.__remaining_lexeme = next_char
					return
			elif current_mode == LLexer.MODE_OP:
				if cls.__is_operator(next_char) is False:
					cls.__remaining_lexeme = next_char
					return
			cls.__current_lexeme += next_char

	@classmethod
	def __is_operator(cls, lex: str) -> bool:
		"""
		Returns `True` if the provided lexeme is an operator, otherwise returns `False`.
		"""
		return lex in cls.__operators

	@classmethod
	def __parse_token(cls) -> LToken:
		"""
		Parses a single lexeme to a token.
		"""
		lexeme = cls.__current_lexeme
		if TokenIdentityEnum.is_member(lexeme) is False:
			if re_match(TokenIdentityEnum.INT_REGEX, lexeme):
				return LToken(lexeme, LToken.INT)

			if re_match(TokenIdentityEnum.ID_REGEX, lexeme):
				return LToken(lexeme, LToken.ID)
		else:
			token_identity = TokenIdentityEnum(lexeme)
			if token_identity == TokenIdentityEnum.PLUS:
				return LToken(lexeme, LToken.PLUS)

			elif token_identity == TokenIdentityEnum.MINUS:
				return LToken(lexeme, LToken.MINUS)

			elif token_identity == TokenIdentityEnum.MULT:
				return LToken(lexeme, LToken.MULT)

			elif token_identity == TokenIdentityEnum.LPAREN:
				return LToken(lexeme, LToken.LPAREN)

			elif token_identity == TokenIdentityEnum.RPAREN:
				return LToken(lexeme, LToken.RPAREN)

			elif token_identity == TokenIdentityEnum.ASSIGN:
				return LToken(lexeme, LToken.ASSIGN)

			elif token_identity == TokenIdentityEnum.SEMICOL:
				return LToken(lexeme, LToken.SEMICOL)

			elif token_identity == TokenIdentityEnum.END:
				return LToken(lexeme, LToken.END)

			elif token_identity == TokenIdentityEnum.PRINT:
				return LToken(lexeme, LToken.PLUS)
		return LToken("Invalid token", LToken.ERROR)
	
