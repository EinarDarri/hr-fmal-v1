from collections.abc import Callable

class InvalidOperator(Exception):
	pass

ITEM_TYPE = int | str

class SInterpreter:
	COMMANDS: dict[str, Callable[[str | int | None], None]] = {
		
	}
	__stack: list[ITEM_TYPE]
	__var_map: dict[str, int]

	def __init__(self) -> None:
		self.__stack = []
		self.__var_map = {}

	def cycle(self) -> None:
		pass

	# commands
	def _push(self, item : ITEM_TYPE) -> None:
		"""
		pushes the operand op onto the stack
		"""
		self.__stack.append(item)

	def _add(self) -> None:
		"""
		addition: pops the two top elements from the stack, adds their 
		values and pushes the result back onto the stack
		"""

	def _mult(self) -> None:
		"""
		multiplication: pops the two top elements from the stack,  
		multiplies their values and pushes the result back onto the stack 
		"""
		pass

	def _uminus(self) -> None:
		"""
		unary minus: pops the top element from stack, changes its sign  
		and pushes the result back onto the stack
		"""
		pass

	def _assign(self) -> None:
		"""
		assignment: pops the two top elements from the stack, assigns  
		the first element (a value) to the second element (a variable) 
		"""
		pass

	def _print(self) -> None:
		"""
		prints the value currently on top of the stack 
		"""
		pass



if __name__ == "__main__":
	pass