"""
Conditional statements are those statements which controls the flow of specific blocks of program.
The if statement takes in a condition and the block of this if statement will only be executed in the statement in true.
The else statement is used with the if statement when you want to execute another block if the condition is false.
Let's first see the example of an if statement without else
Then an if-else statement
"""

a = 30
if(a >= 10):
	print('a is greater than or equal to 10')

a = 7
if(a % 2 == 0):
	print('a is an even number')
else:
	print('a is an odd number')

# Now here a condition of nested if-else statements
a = 20
if(a < 30):
	if(a > 10):
		print('a is less than 30 but greater than 10')
	else:
		print('a is less than 30 and 10')
else:
	print('a is greater than 30')

"""
Now take care that these statement are ended with an colon, ':', which you might miss a few time if you code in other languages.
Unlike others python don't use braces '{}' to contain a block of code. Instead it uses indentation.
This is pretty important because this means that even misplacing 1 space may cause an error or even crash.
An equal amount of space is to be given before the line of the block which also increases as the nesting increases.
""" 
