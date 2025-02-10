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
	ID_REGEX = "[A-Za-Z]+"
	END = "end"
	PRINT = "print"