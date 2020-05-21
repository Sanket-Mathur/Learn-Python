"""
Sets are collection of values such that no value can be repeated and these are enclosed in braces i.e. '{' and '}'.
Sets are not index specific and thus indexing, spliting or slicing do not work on them.
This means that the element that you add into a set might show up in any random place instead of being properly indexed.
Let's define a set ans see it in action.
"""

mySet = {1, 2, 3, 4, 'A', 'B', 4, 5, 6}
print(mySet)

"""
Now by doing just this you might be albe to see a few differences between a set and other datatypes like lists or tupples.
Firstly we here have two 4s but on executing, I only contains one 4, i.e. value cannot be repeated.
Secondly the values 5 and 6 here are defined after 'A' and 'B' by shows up in front of them i.e. sets are not index specific.
Well if we cannot index the values, lets try adding and removing values from a set.
We use the functions update and remove for this purpose.
"""

# Let's add 7 and 8 in the set
mySet.update([7, 8])
print(mySet)
# Notice how we are using lists in order to add the elements to the set.
# Let's remove all the alphabets from the set
mySet.remove('A')
mySet.remove('B')
print(mySet)

"""
Now here's the concept a frozen set.
A frozen set is a set in which we cannot perform operations like adding values and removing values.
We can define a frozen set by using a set and passing it in the function frozenset().
"""

myFS = frozenset(mySet)
print(myFS)
