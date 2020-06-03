"""
Classes are the basics of object oriented programming.
These are used in order to implement the concept of object-oriented programming into python scripts.
Classes are user-defined data types consisting of variables of any data types (data members) and functions (member functions or methods).
This itself exhibits the concept of encapsulation.
Syntax:
class <class-name>:
	def <function-names>(self,...):
		function definition
	:
	:
"""

# Class personal with 2 methods printing my name and age
class personal:
	def name(self):
		print('Sanket Mathur')
	def age(self):
		print(18)

# Creating object of class personal and executing the methods
p = personal()
p.name()
p.age()

"""
The data members are defined inside a constructor (parameterized or non-parameterized).
Syntax:
class <class-name>:
	def __init__(self,...):
		self.<var-name> = <value>
	:
	:
The self keyword that you used saw inside the function parameters is an instance of that class and thus required in all methods.
The data members are also defined using the self keyword.
"""

# Class with constructor taking 2 parameters fav_char and fav_int (and obviously the self)

class favourites:
	def __init__(self, fav_char, fav_int):
		self.fav_char = fav_char
		self.fav_int = fav_int
	def printall(self):
		print('Favourite Charcter:', self.fav_char)
		print('Favourite Integer:', self.fav_int)

# Defining a few objects and executing their respective functions
obj1 = favourites('a', 9)
obj2 = favourites('x', 7)
obj1.printall()
obj2.printall()
