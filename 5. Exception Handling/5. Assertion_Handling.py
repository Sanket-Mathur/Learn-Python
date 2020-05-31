"""
We have seen the use of assert before.
But it is not good to show errors or crash the whole program.
We use AssertionError to handle this error.
"""

try:
	x = int(input('Enter a number greater than 10\n>'))
	assert x > 10, 'Wrong Number'
except AssertionError:
	print('You had one job!!!')
else:
	print('Good Job')
