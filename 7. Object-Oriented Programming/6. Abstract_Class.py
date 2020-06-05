"""
An abstract class is like a frame which is used to define another class.
Objects of abstract class cannot be defined since it does not provide any functionality whatsoever.
An abstract class is defined by passing ABC in parameters with class definition as you did in inheritance.
In an abstract class, abstract method is defined using @abstractmethod above the method definition.
In order to use these operations, we first need to import these from the module abc
Any other class can use this abstract class by inheriting it.
"""

from abc import abstractmethod, ABC

# Abstract Class
class furniture(ABC):
	@abstractmethod
	def result(self):
		pass

# Defining some classes using our furniture abstract class
class Table(furniture):
	def result(self):
		print('This is a table')

class Chair(furniture):
	def result(self):
		print('This is a chair')

# Declaring some objects and using them
T1 = Table()
C1 = Chair()
T1.result()
C1.result()
