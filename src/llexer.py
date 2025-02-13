from sys import stdin
from re import match as re_match
from ltoken import LToken, TOKEN_IDENTITY_MAP, is_token, get_key_from_value, get_identity_from_value


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
			raise Exception(f"Invalid lex ({lex}) provided to __get_mode")

	@classmethod
	def __get_next_lexeme(cls) -> None:
		current_mode: int = cls.MODE_DEFAULT
		cls.__current_lexeme = cls.__remaining_lexeme
		cls.__remaining_lexeme = ""
		next_char = ""

		# If there is a lexeme from a prior operation cached in the Lexer and it's an operator, return a new token with said lexeme.
		if cls.__is_operator(cls.__current_lexeme):
			return
		else:
			current_mode = cls.__get_mode(cls.__current_lexeme)

		while(True):
			next_char = stdin.read(1)
			# Ignore newline/carriage return/whitespace
			if next_char == "\n" or next_char == "\r":
				continue
			if next_char == " ":
				break
			# If the mode is "DEFAULT", it can be overridden to ensure consistent lexemes (e.g. only chars for variables, only numbers for values...)
			if current_mode == cls.MODE_DEFAULT:
				current_mode = cls.__get_mode(next_char)
			# If the tokens are not of the same type, cache the next token and return.
			if cls.__get_mode(next_char) != current_mode:
				cls.__remaining_lexeme = next_char
				break
			# print(cls.__current_lexeme, next_char)
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
		if is_token(lexeme) is False:
			if re_match(TOKEN_IDENTITY_MAP["INT_REGEX"], lexeme):
				return LToken(lexeme, LToken.INT)

			if re_match(TOKEN_IDENTITY_MAP["ID_REGEX"], lexeme):
				return LToken(lexeme, LToken.ID)
		else:
			token_identity = get_identity_from_value(get_key_from_value(lexeme))
			return LToken(lexeme, token_identity)
		print("LEX: ", int.from_bytes(lexeme.encode()))
		return LToken("Invalid token", LToken.ERROR)
	
