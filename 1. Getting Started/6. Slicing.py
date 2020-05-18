"""
Slicing is the technique of using or stripping a particular sequence.
Syntax:
slice(start : end : step)
Let's first implement it on a string.
For singnle characters, index starts from 0 and increments by 1 in every character.
For a multi-character snipt, the (starting) and (ending+1) positions are seperated by ':'.
And for defining a particular pattern, we use (start):(ending+1):(Steps)
"""

s = 'Python was invented by Guido van Rossum'

# Let's first extract the first alphabet of string s
print(s[0])

# Let's now extract the name from the string s
print(s[23:39])

# To understand how steps work let's print every second character of the string s.
print(s[::2])

"""
In case we leave any place empty, it will take the index of start/end of the sequence.
eg. for printing a whole sequence we can use s(:).
Not only string but you can do it with other sequences.
Let's reverse a number defined by the user and print it back on the console.
We can do it by converting integer to a string and applying splicing to it.
And we can use -1 as steps for reversing the string.
"""

x = int(input())
s = str(x)
rev = s[::-1]
print(rev)
