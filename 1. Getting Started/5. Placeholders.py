"""
Placeholders are special characters used to pre-occupy some place in between a string for other data types.
Let's look at some placeholders and see how to use them in your program.
"""

# integer placeholder
str1 = 'Arun has stored %d marks'
print(str1 % 99)

# float placeholders
str2 = 'You scored %.2f rating on your latest blogs'
print(str2 % 4.32245)

# string placeholders
fname, last = 'Tony', 'Stark'
print('%s %s is iron man' % (fname, last))

"""
Here in the last example we have used the concept of unpacking that you read in the earlier files.
There are a lot of placeholders in python that you might want to read about so surf the net a little.
There is another piece of very useful code that I would like to introduce you to in this same file.
This is the end parameter in the print() function used to define what will be the end character.
"""

# Till now you might have seen that print() functions are ended with a newline character by default, let's change it.

print('GitHub:', end=' ')
print('Sanket', end='-')
print('Mathur')
