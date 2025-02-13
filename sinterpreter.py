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

	def __get_value_from_stack(self) -> int:
		item = self.__stack.pop()
		if isinstance(item, str):
			if item not in self.__var_map:
				raise InvalidOperator(f"f {item} has not been assigned to as variable")
			return self.__var_map[item]
		elif isinstance(item, int):
			return item

	# commands
	def __push(self, item : ITEM_TYPE) -> None:
		"""
		pushes the operand op onto the stack
		"""
		self.__stack.append(item)

	def __add(self) -> None:
		"""
		addition: pops the two top elements from the stack, adds their 
		values and pushes the result back onto the stack
		"""

	def __mult(self) -> None:
		"""
		multiplication: pops the two top elements from the stack,  
		multiplies their values and pushes the result back onto the stack 
		"""
		pass

	def __uminus(self) -> None:
		"""
		unary minus: pops the top element from stack, changes its sign  
		and pushes the result back onto the stack
		"""
		pass

	def __assign(self) -> None:
		"""
		assignment: pops the two top elements from the stack, assigns  
		the first element (a value) to the second element (a variable) 
		"""
		pass

	def __print(self) -> None:
		"""
		prints the value currently on top of the stack 
		"""
		pass



if __name__ == "__main__":
	pass