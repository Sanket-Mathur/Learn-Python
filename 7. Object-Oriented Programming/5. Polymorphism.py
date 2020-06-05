"""
Polymorphism is the ability of an element to be expressed in more than one form.
In python polymorphism is implemented using the concept of duck typing.
It can be done by passing an objects of different classes to a class having function with same name.
Let's check it out with an example.
"""

# Defining class Dog
class Dog:
	def sound(self):
		print('It barks')

# Defining class Cat
class Cat:
	def sound(self):
		print('It meows')

# Defining a class which takes object of another class
class WhatSound:
	def __init__(self, animal):
		self.animal = animal
	def MakeSound(self):
		self.animal.sound()

# Declaring object and seeing how it works
D1 = Dog()
obj1 = WhatSound(D1)
C1 = Cat()
obj2 = WhatSound(C1)
obj1.MakeSound()
obj2.MakeSound()

