"""
Map functions performs some operations to the elements of list that is provided to the function.
Syntax:
map(<function-expression>, <list>)
Let's see a few examples of how to use these functions.
"""

# Double all the elements of a list
lst = [1,2,3,4,5,6,7]
result = list(map(lambda x:x*2, lst))
print(result)

"""
Similar to the filter you can also pass in user-defined function or built-in function name.
Let's try to pass in the int function and convert a string containing numbers to a list of integers.
"""

st = '9 8 7 6 5'
int_l = list(map(int, st.split()))
print(int_l)
