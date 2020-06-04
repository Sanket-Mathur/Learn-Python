"""
Inheritance is the property on one class to inherit behaviour of another class.
Python allows inheritance by passing class name inside paranthesis which defining the derived class.
Syntax:
class base:
	:
class deriver(base):
	:
Let's see an example where we will also see which of the constructors are invoked.
"""

# Defining class Parent which will act as the base class for us
class Parent:
	def __init__(self):
		print('Constructor of parent class invoked')
	def parentFunc(self):
		print('Parent class')

# Defining class Child which will act as the derived class
class Child(Parent):
	def __init__(self):
		print('Constructor of child class invoked')
	def childFunc(self):
		print('Child class')
 
# Creating an object of Child class
child1 = Child()
child1.childFunc()
child1.parentFunc()

"""
As you can see even on inheriting the Parent class, its constructor is not invoked.
However the function parentFunc() is accessable by the object of class Child.
"""
