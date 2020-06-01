"""
In python we use the keyword def to define user defined functions.
Unlike other programming languages, you don't need to define a return type.
Syntax:
def <function_name>(<param_if-any>):
	body-of-function
"""

# Let's build a function to add two numbers
def add(a, b):
	return a + b;

"""
For calling the function, you use the function-name with paranthesis within which you can pass the arguments if the function needs them
"""

# Calling the function to add 4 and 19
print(add(4, 19))
