"""
Lists are comma seperated values that allows us to access any item baisd on its index.
Values of a list are enclosed in brackets i.e '[' and ']'.
Lists are mutable data types i.e. individual elements can be added or deleted from lists.
Let's first check some basic functionality of lists.
"""

shopList = ['Apple', 'Orange', 'Banana']

# Let's print the shopList and see what will be the result.
print(shopList)

# Second element of shopList
print(shopList[1])
# As you can recall we used slicing on strings, list being a iterable sequence also follows all the slicing functionality
print(shopList[0:2])

# Adding two lists
shopList2 = ['Guava', 'Strawberries']
shopList += shopList2
# Or you can also do shopList += ['Guava', 'Strwberries']
print(shopList)

# Repeating a list
print(shopList * 3)

"""
Let us also see how create an empty list.
These will be vary useful when solving problems where you need to append the values in the list as you find them or calculate them.
There are 2 ways to this,
The first way is to just literaly define an empty list like <listname> = []
The second way is to use the function list() as <listname> = list()
Let's try the second one out and see that it is the same as the first one.
"""

myList = list()
print(myList)

"""
Now there are a lot of functions that you can appky to a list element and we will see some of them in the next file.
"""
