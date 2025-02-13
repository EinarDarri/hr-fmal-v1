TOKEN_IDENTITY_MAP = {
	"PLUS": "+",
	"MINUS": "-",
	"MULT": "*",
	"LPAREN": "(",
	"RPAREN": ")",
	"ASSIGN": "=",
	"SEMICOL": ";",
	"INT_REGEX": "[0-9]+",
	"ID_REGEX": "[A-Za-z]+",
	"END": "end",
	"PRINT": "print"
}

def get_key_from_value(val: str) -> str:
	for key, value in TOKEN_IDENTITY_MAP.items():
		if value == val:
			return key
	raise Exception(f"Value ({val}) not found in TOKEN_IDENTITY_MAP")

def is_token(lex: str) -> bool:
	return lex in TOKEN_IDENTITY_MAP.values()

VALUE_IDENTITY_MAP = {
	0: "ID",
	1: "ASSIGN",
	2: "SEMICOL",
	3: "INT",
	4: "PLUS",
	5: "MINUS",
	6: "MULT",
	7: "LPAREN",
	8: "RPAREN",
	9: "PRINT",
	10: "END",
	-1: "ERROR",
}

def get_identity_from_value(val: str) -> int:
	for key, value in VALUE_IDENTITY_MAP.items():
		if value == val:
			return key
	raise Exception(f"Value ({val}) not found in VALUE_IDENTITY_MAP")

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
	
	@property
	def is_valid(self) -> bool:
		return self.token_code != LToken.ERROR
	
	def __str__(self) -> str:
		return f"given string '{self.lexeme}', token : {VALUE_IDENTITY_MAP[self.token_code]}"