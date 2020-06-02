"""
Reduce function passes all the elements to a function expression,
and prints out a single result based on the return statement of the function.
Syntax:
reduce(<function-expression>, <list>)
Unlike other languages, you need to import the reduce function in orderto use it.
You can import the function reduce from the library functools
"""

from functools import reduce

# Add all the elements of a list
lst = [1,2,3,4,5,6,7,8,9,10]
res = reduce(lambda x,y:x+y, lst)
print(res)

# Find the largest element to a list
lst2 = [4,9,3,10,23,6,3]
res2 = reduce(lambda x,y: x if(x>=y) else y, lst2)
print(res2)
