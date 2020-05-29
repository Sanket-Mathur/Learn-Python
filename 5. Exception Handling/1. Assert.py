"""
Assert statement is a way of printing out an error on the console.
This will give you a run-time error.
This might be useful when testing the applications and some specific feature.
Syntax:
assert <condition>, <Error Message>
The assert statement will generate an error if the condition comes out to be false.
"""

x = int(input('Enter a number lesser than 10\n>'))
assert x < 10, "Wrong Number"
print('The number you entered was really less than 10.')
