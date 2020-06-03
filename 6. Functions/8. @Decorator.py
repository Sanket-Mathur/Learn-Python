"""
@ is used with those decorator function who are supposed to be in the function defined after it.
Let's use this with another decorator function.
"""

# Decorator function to cube the value returned by the function
def cube_func(func):
	def inner():
		result = func()
		return result**3
	return inner

# Using @ to call the decorator cube_func to the function defined next to it
@cube_func
def five():
	return 5

print(five())

# The function defined further will not be affected

def ten():
	return 10

print(ten())
