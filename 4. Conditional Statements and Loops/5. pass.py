"""
Another small topic in python is the pass statement.
And all this pass statement does is nothing.
This might seem very weird but it is very useful.
Unlike other languages, you just cannot leave a loop of a function empty in python.
Trying to do this will give you an error.
So to accomplish this, python programmers uses the pass statement.
Let's try using pass in a while loop.
"""

i = 0
while i < 5:
	pass
	i+=1

print('Nothing came out of the loop! What a waste of time.') 
