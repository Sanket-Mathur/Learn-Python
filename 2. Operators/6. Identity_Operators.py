"""
Identity operators may come in handy when comparing variables. There are a few of those in python.
is
is not
in
not in
These are very self explanatory.
Let's see these in action.
"""

s1 = 'ABC'
s2 = 'ABC'
print(s1 is s2)

i1 = 1
i2 = 10
print(i1 is not i2)

l1 = [1, 2, 3, 4, 5]
print(3 in l1)

s3 = 'Python is an easy to learn language'
print('Python' not in s3)
