"""
Else and Finally blocks are two statements are two blocks that are used with the try and except blocks.
The else statement will be executed if the except block is not executed.
The finally statement will be executed after the error handing blocks.
Syntax:
try:
	code
except:
	code
else:
	code
finally:
	code
"""

# Let's built the division program further

a, b = [int(x) for x in input().split()]
try:
	c = a / b
	print(c)
except ZeroDivisionError:
	print('Division by Zero not possible')
else:
	print('Division done successfully')
finally:
	print('The END')
