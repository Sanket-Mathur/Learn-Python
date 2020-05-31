"""
Try and Except block is an way to deal with run-time errors.
It tests the code in the try block and if there occours any error, it executes the except block.
Syntax:
try:
	code
except ERROR(optional):
	code
"""

# Let's build a divisibility program which returns a message on the console in case of ZeroDivisionError
a, b = [int(x) for x in input().split()]
try:
	c = a / b
	print(c)
except ZeroDivisionError:
	print("Division by Zero not applicable")

"""
ZeroDivision error is a Build-in Exception error.
A list of errors is given below:
AssertionError
AttributeError
EOFError
FloatingPointError
GeneratorExit
ImportError
IndexError
KeyError.
KeyboardInterrupt
MemoryError
NameError
NotImplementedError
OSError
OverflowError
ReferenceError
RuntimeError
StopIteration
SyntaxError
IndentationError
TabError
SystemError
SystemExit
TypeError
UnboundLocalError
UnicodeError
UnicodeEncodeError
UnicodeDecodeError
UnicodeTranslateError
ValueError
ZeroDivisionError
In case you don't provide an exception with the except statement, it will by default handle all the errors.
"""
