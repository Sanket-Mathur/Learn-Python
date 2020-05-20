"""
Tupples are data structures containing a group of values that are immutable.
That means that the values cannot be changed, replaced or deleted.
Tupple can be deleted as a whole but not the values inside a tupple.
These are defined inside paranthesis  i.e. '(' and ')'.
Let's see these things in examples.
"""

MyTup = (1,6,8)
print(MyTup)

# Printing the second element of our tupple.
print(MyTup[1])

# Printing the length of tupple.
print(len(MyTup))

# Adding 2 tupples.
Tup1 = ('A', 'B', 'C')
Tup2 = (1, 2, 3)
Tup3 = Tup1 + Tup2
print(Tup3)

# Repeating Tupple.
print(Tup1 * 3)
