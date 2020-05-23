"""
Logical operators are based on the principle of logical gates.
There are three types of logical operators.
and
or
not
There are just written as it is.
Let's see them in action and then we will see the truth tables for these operators in case you are not aware of them.
"""

print(True and False)
print(True or False)
# not as you might now is a unary operator i.e. used with only one value
print(not True)

"""
Let's see the truth tables of these operators.
Most of the time you write these tables using 0 and 1 representing false and trtue respectively.
But the sake of boolean operators in python, I am going to make them using true and false.

and
False and False = Flase
False and True = False
True and False = False
True and True = True

or
False or False = Flase
False or True = True
True or False = True
True or True = True

not
not False = True
not True = False
"""
