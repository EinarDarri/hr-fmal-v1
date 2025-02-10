from sys import stdin
from re import match as re_match
from .constants import TokenIdentityEnum
from .ltoken import LToken

class LLexer:

	@classmethod
	def get_next_token(cls) -> LToken:
		return cls.__parse_token(cls.__read_token())

	@classmethod
	def __read_token(cls) -> str:
		token = stdin.read(1)
		return token
	
	@classmethod
	def __parse_token(cls, token : str) -> LToken:
		match TokenIdentityEnum(token):
			case TokenIdentityEnum.PLUS:
				return LToken(token, LToken.PLUS)

			case TokenIdentityEnum.MINUS:
				return LToken(token, LToken.MINUS)

			case TokenIdentityEnum.MULT:
				return LToken(token, LToken.MULT)

			case TokenIdentityEnum.LPAREN:
				return LToken(token, LToken.LPAREN)

			case TokenIdentityEnum.RPAREN:
				return LToken(token, LToken.RPAREN)

			case TokenIdentityEnum.ASSIGN:
				return LToken(token, LToken.ASSIGN)

			case TokenIdentityEnum.SEMICOL:
				return LToken(token, LToken.SEMICOL)

			case TokenIdentityEnum.END:
				return LToken(token, LToken.END)

			case TokenIdentityEnum.PRINT:
				return LToken(token, LToken.PLUS)

		if re_match(TokenIdentityEnum.INT_REGEX,token):
			return LToken(token, LToken.INT)

		if re_match(TokenIdentityEnum.ID_REGEX, token):
			return LToken(token, LToken.ID)

		return LToken("Invalid token", LToken.ERROR)