"""
Filter function selects particular elements from a list depending on a function expression.
Syntax:
filter(<function-expression>, <list>)
Let's see how can we eleminate all the odd numbers from a list.
"""

lst = [10,20,11,34,53,13,42]
result = list(filter(lambda x:x%2==0, lst))
print(result)

"""
The filter requires a function returning boolean values.
Based on which it filters out the elements for which the function returns a False value.
We can even use a normal function instead of lambda in the above example.
The function name will be passed as a parameter.
And let's try it that way.
"""

def even(x):
	return x%2 == 0

result = list(filter(even, lst))
print(result)
