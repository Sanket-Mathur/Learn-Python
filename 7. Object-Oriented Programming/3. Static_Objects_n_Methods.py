"""
Static objects are those objects that can be even called by an object or the class name itself.
It is defined inside a class like a normal variable unlike data members of that class.
"""

class Student:
	branch = "CSE"
	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno

stud = Student('John', 123456)
print(stud.name)
print(stud.rollno)
print(stud.branch)

# Calling branch with class name
print(Student.branch)

"""
Similar to the static objects, static methods can also be defined.
For this we use @staticmethod inside the class just before defining the method.
"""

class College:
	def __init__(self, name, rank):
		self.name = name
		self.rank = rank
	@staticmethod
	def general():
		print('This class contains the name and rank of a college')

c = College('XYZ', 5)
c.general()

# Calling general with class name
College.general()


