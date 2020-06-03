"""
Decorator function is a function that returns another function and at the same time decorates that function or give that function a special meaning.
Let's see how can we make a decorator function with an example.
"""

# Decorator function to double the return value of another function
def decor(func):
	def inner():
		result = func()
		return result*2
	return inner

# Calling the function decor on another function num()
def num():
	return 5
result = decor(num)

print(result())
