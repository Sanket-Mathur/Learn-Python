"""
A for loop is a iterative statement used to loop over a range of numbers of elements of a sequence.
Syntax:
for <loop-variable> in <range>:
	#body-of-loop
Let's see how we can use the range construct first
"""

# Looping over the numbers 1 to 5
for i in range(1,6):
	print(i)

"""
You can even leave the first argument of range() blank, it will start the range from 0 by default eg. range(10) is 0 to 9
You can also provide a third argument in range() defining the number of steps
"""

# Loop to print the series 0, 5, 10,...30
for i in range(0,31,5):
	print(i, end=', ')

# Looping over a list to find the sum of the elements
L = [2, 42, 2, 7, 1]
sum = 0
for i in L:
	sum += i
print('\nSum:', sum)

"""
Python offers a special condition for the loops, i.e. the else statements like those you used in if-else
An else statement with a loop is executed when the loop block isn't even executed once.
"""

for i in range(-2):
	print(i)
else:
	print('Loop wasn\'t executed even once')
