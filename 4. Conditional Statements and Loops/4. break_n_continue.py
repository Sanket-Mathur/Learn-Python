"""
Break and continue are special statements that can only be used inside a loop.
These manipulate the control flow inside a loop.
Break breaks the loop in which it has been used and comes out of it.
Continue skips the statements after it and jumps to the next iteration of the loop.
Let's see how they work.
"""

# Breaking the loop as soon as i becomes 3
for i in range(0,5):
	if i == 3:
		break
	print(i)

# Continuing the loop if i becomes 3
for i in range(0,5):
	if i == 3:
		continue
	print(i)

