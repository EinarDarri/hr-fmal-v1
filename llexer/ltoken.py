
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


	def __init__(self, lexeme: str, token: int = -1) -> None:
		self.lexeme: str = lexeme
		self.token: int = token