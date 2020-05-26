"""
While loop similar to for loop is also an iterative statement.
However, while loop executes the block based on the expression provided to it.
It repeats the block until the condition in true.
"""

# Let's build a similar loop for printing 1 to 10 but using while loop
i = 1
while(i <= 10):
	print(i)
	i += 1

"""
Similar to the for loop, else statement can also be used with the while loop.
This statement will be executed when the control flow didn't even enter the loop because of the condition to be false.
"""

while(i < 5):
	print('i is less than 5')
	i += 1
else:
	print('i is greater than 5')

"""
Unlike other languages, python does not have an exit-controlled loop or do-whie loop.
while loop is used in places where you might not be sure when the loop in going to end.
You often use break and continue statements with a while loop that we'll discuss about in the next file.
"""
