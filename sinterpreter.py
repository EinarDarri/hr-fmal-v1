from collections.abc import Callable

class InvalidOperator(Exception):
	def __init__(self, nameOfOperator:str, *args: object) -> None:
		MESSAGE = f"Error for operator: {nameOfOperator}"
		super().__init__(MESSAGE, *args)

class VariableNotAssignedException(Exception):
	pass

ITEM_TYPE = int | str

class SInterpreter:
	__COMMANDS: dict[str, Callable[[],None] | Callable[[ITEM_TYPE], None]]
	__stack: list[ITEM_TYPE]
	__var_map: dict[str, int]

	def __init__(self) -> None:
		self.__COMMANDS = {
			"PUSH": self.__push,
			"ADD": self.__add,
			"MULT": self.__mult,
			"UMINUS": self.__uminus,
			"ASSIGN": self.__assign,
			"PRINT": self.__print
		}
		self.__stack = []
		self.__var_map = {}

	def cycle(self) -> None:
		pass

	def __get_value_from_stack(self) -> int:
		"""
			:raises IndexError (if the stack is empty)
			:raises VariableNotAssignedException
		"""
		
		item = self.__stack.pop()
		if isinstance(item, str):
			if item not in self.__var_map:
				raise VariableNotAssignedException(f"f {item} has not been assigned to as variable")
			return self.__var_map[item]
		elif isinstance(item, int):
			return item

	# commands
	def __push(self, *args : ITEM_TYPE) -> None:
		"""
		pushes the operand op onto the stack
		"""
		if len(args) != 1:
			raise InvalidOperator("PUSH")

		self.__stack.append(args[0])

	def __add(self) -> None:
		"""
		addition: pops the two top elements from the stack, adds their 
		values and pushes the result back onto the stack
		"""
		try:
			v1 = self.__get_value_from_stack()
			v2 = self.__get_value_from_stack()
		except IndexError:
			raise InvalidOperator("ADD")
		except VariableNotAssignedException:
			raise InvalidOperator("ADD")
		res = v1 + v2
		self.__stack.append(res)

	def __mult(self) -> None:
		"""
		multiplication: pops the two top elements from the stack,  
		multiplies their values and pushes the result back onto the stack 
		"""
		try:
			v1 = self.__get_value_from_stack()
			v2 = self.__get_value_from_stack()
		except IndexError:
			raise InvalidOperator("MULT")
		except VariableNotAssignedException:
			raise InvalidOperator("MULT")
		res = v1 * v2
		self.__stack.append(res)

	def __uminus(self) -> None:
		"""
		unary minus: pops the top element from stack, changes its sign  
		and pushes the result back onto the stack
		"""
		try:
			v1 = self.__get_value_from_stack()
		except IndexError:
			raise InvalidOperator("UMINUS")
		except VariableNotAssignedException:
			raise InvalidOperator("UMINUS")
		self.__stack.append(-v1)

	def __assign(self) -> None:
		"""
		assignment: pops the two top elements from the stack, assigns  
		the first element (a value) to the second element (a variable) 
		"""
		try:
			v1 = self.__get_value_from_stack()
			v2 = self.__stack.pop()
		except IndexError:
			raise InvalidOperator("ASSIGN")
			#raise InvalidOperator("The stack is empty, value can't be retrieved")
		
		if not isinstance(v2,str):
			raise InvalidOperator("ASSIGN")
			#raise InvalidOperator(f"Can't assign {v2} as a variable")

		self.__var_map[v2] = v1
		

	def __print(self) -> None:
		"""
		prints the value currently on top of the stack 
		"""
		try:
			print(self.__stack[-1])
		except IndexError:
			raise InvalidOperator("PRINT")



if __name__ == "__main__":
	raise InvalidOperator("Push")