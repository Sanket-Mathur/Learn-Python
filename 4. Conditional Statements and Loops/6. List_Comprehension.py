"""
List comprehension is a shorter way to iterate of a list.
This was of iterating is super useful when solving problems and makes the code cleaner and look way better.
Let's see an example on how to use it.
"""

# Defining a list full of numbers and doubling all the terms using list comprehension
L = [3,2,4,6,4,5,7]
print(L)
L = [x*2 for x in L]
print(L)

# Converting list elements from to string to int
S = ['1', '2','3','4','5']
print(S)
S = [int(i) for i in S]
print(S)

"""
Now you have seen the basic examples of list comprehension.
You can use it in many different ways and this might come in handy when writing long code.
"""
