from enum import StrEnum

class TokenIdentityEnum(StrEnum):
	PLUS = "+"
	MINUS = "-"
	MULT = "*"
	LPAREN = "("
	RPAREN = ")"
	ASSIGN = "="
	SEMICOL = ";"
	INT_REGEX = "[0-9]+"
	ID_REGEX = "[A-Za-z]+"
	END = "end"
	PRINT = "print"

	@classmethod
	def is_member(cls, token: str) -> bool:
		"""
		Utility method to check if a provided token is actually a member of this enum.

		:returns: True if the token is a member of this enum. False otherwise.
		"""
		return token in cls._value2member_map_

class LToken:

	# this should be an IntEnum
	ID = 0
	ASSIGN = 1
	SEMICOL = 2
	INT = 3
	PLUS = 4
	MINUS = 5
	MULT = 6
	LPAREN = 7
	RPAREN = 8
	PRINT = 9
	END = 10
	ERROR = -1

	def __init__(self, lexeme: str, token_code: int = -1) -> None:
		self.lexeme: str = lexeme
		self.token_code: int = token_code

	def __str__(self) -> str:
		return f"LToken({self.lexeme}, {self.token_code})"
	
	@property
	def is_valid(self) -> bool:
		return self.token_code != LToken.ERROR