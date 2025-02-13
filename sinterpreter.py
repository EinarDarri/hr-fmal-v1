from collections.abc import Callable

class InvalidOperator(Exception):
	pass

ITEM_TYPE = int | str

class SInterpreter:
	COMMANDS: dict[str, Callable[[str | int | None], None]] = {
		
	}
	__stack: list[str]
	__var_map: dict[str, int]

	def __init__(self) -> None:
		self.__stack = []
		self.__var_map = {}

	def cycle(self) -> None:
		pass

	# commands
	@classmethod
	def _push(cls, item : ITEM_TYPE) -> None:
		"""
		pushes the operand op onto the stack
		"""
		pass

	@classmethod
	def _add(cls) -> None:
		"""
		addition: pops the two top elements from the stack, adds their 
		values and pushes the result back onto the stack
		"""
		pass

	@classmethod
	def _mult(cls) -> None:
		"""
		multiplication: pops the two top elements from the stack,  
		multiplies their values and pushes the result back onto the stack 
		"""
		pass

	@classmethod
	def _uminus(cls) -> None:
		"""
		unary minus: pops the top element from stack, changes its sign  
		and pushes the result back onto the stack
		"""
		pass

	@classmethod
	def _assign(cls) -> None:
		"""
		assignment: pops the two top elements from the stack, assigns  
		the first element (a value) to the second element (a variable) 
		"""
		pass

	@classmethod
	def _print(cls) -> None:
		"""
		prints the value currently on top of the stack 
		"""
		pass



if __name__ == "__main__":
	pass