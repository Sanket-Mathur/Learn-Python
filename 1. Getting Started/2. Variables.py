"""
Variables are like blocks where you can store a value and even change it.
Python allows variable to be of a dynamically defined data type.
I.e. you do not n eed to define data type of a variable at time of declaration and it may be changed anywhere throughout the program.
Defining variables in python in easy. You just need to give variable_name and its value.
"""

a = 20
# Here data type of a currently is integer. Let's print the value of a
print(a)

# Let's change the value of a and change it data type by assigning it a string
a = 'This is a string now'
print(a)

"""
We can also assign several variables at once and it's calles multiple assigning.
You can either assign different values variable wise,
Or same value to multiple variables.
"""

firstname, lastname, age = 'Sanket', 'Mathur', 18
print(firstname, lastname, age)

var1 = var2 = var3 = 20
print(var1, var2, var3)

