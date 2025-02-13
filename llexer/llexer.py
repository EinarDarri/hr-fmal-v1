from sys import stdin
from re import match as re_match
from .ltoken import LToken, TokenIdentityEnum


class LLexer:
	MODE_INT = 0
	MODE_STR = 1
	MODE_OP = 2

	__current_lexeme = ""
	__remaining_lexeme = ""

	@classmethod
	def get_next_token(cls) -> LToken:
		cls.__get_next_lexeme()
		return cls.__parse_token()
	
	@classmethod
	def __get_mode(cls, lex: str) -> int:
		if lex == "":
			return -1
		elif lex.isalpha():
			return LLexer.MODE_STR
		elif lex.isdigit():
			return LLexer.MODE_INT
		else:
			return LLexer.MODE_OP

	@classmethod
	def __get_next_lexeme(cls) -> None:
		current_mode: int = cls.__get_mode(cls.__remaining_lexeme)
		cls.__current_lexeme = cls.__remaining_lexeme
		cls.__remaining_lexeme = ""
		if current_mode == LLexer.MODE_OP:
			return
		next_char = ""
		while(True):
			next_char = stdin.read(1)
			if next_char == " " or next_char == "\n" or next_char == 0:
				break
			if current_mode == -1:
				if next_char.isalpha():
					current_mode = LLexer.MODE_STR
				elif next_char.isdigit():
					current_mode = LLexer.MODE_INT
				else:
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
			cls.__current_lexeme += next_char

	@classmethod
	def __is_operator(cls, lex: str) -> bool:
		return lex in "()-+=*;"

	@classmethod
	def __parse_token(cls) -> LToken:
		lexeme = cls.__current_lexeme
		# print("lex is: ", lexeme)
		if TokenIdentityEnum.is_member(lexeme) is False:
			if re_match(TokenIdentityEnum.INT_REGEX, lexeme):
				return LToken(lexeme, LToken.INT)

			if re_match(TokenIdentityEnum.ID_REGEX, lexeme):
				return LToken(lexeme, LToken.ID)
		else:
			match TokenIdentityEnum(lexeme):
				case TokenIdentityEnum.PLUS:
					return LToken(lexeme, LToken.PLUS)

				case TokenIdentityEnum.MINUS:
					return LToken(lexeme, LToken.MINUS)

				case TokenIdentityEnum.MULT:
					return LToken(lexeme, LToken.MULT)

				case TokenIdentityEnum.LPAREN:
					return LToken(lexeme, LToken.LPAREN)

				case TokenIdentityEnum.RPAREN:
					return LToken(lexeme, LToken.RPAREN)

				case TokenIdentityEnum.ASSIGN:
					return LToken(lexeme, LToken.ASSIGN)

				case TokenIdentityEnum.SEMICOL:
					return LToken(lexeme, LToken.SEMICOL)

				case TokenIdentityEnum.END:
					return LToken(lexeme, LToken.END)

				case TokenIdentityEnum.PRINT:
					return LToken(lexeme, LToken.PLUS)
		print(lexeme, " INVALID")
		return LToken("Invalid token", LToken.ERROR)