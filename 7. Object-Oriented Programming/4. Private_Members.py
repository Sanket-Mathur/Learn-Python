"""
To define private members in a class, __ is used before the member name.
Though nothong in python is completely private and still can be accessed using Name Mangling.
This is used as,
<object-name>._<class-name>__<member-name>
"""

# Let's define the same Student class as before with some private members
class Student:
	def __init__(self, name, rollno):
		self.__name = name
		self.__rollno = rollno

# Creating object of class Student
s1 = Student('Max', 2454)

# Try using print(s1.name) and print(s1.__name) but it will result in an error

# Accessing private members using name mangling
print(s1._Student__name)
print(s1._Student__rollno) 
