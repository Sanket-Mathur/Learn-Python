"""
There are a few assignment operators in python.
First is the simple assignment operator i.e. '='
It is used to assign the value to a variable or constant.
Next are the short-hand assignment operators.
+= Addition assignment operators
-= Substraction assignment operator
*= Multiplication assignment operator
**= Exponential assignment operator
/= Division assignment operator
//= Floor division assignment operator
%= Modulo assignment operator
"""

# You must have seen various examples of assignment operator by now here's one if you missed it.
a = 4
b = 2
print(a, b)

# Addition assignment operator
a += b
# Short-hand of a = a + b
print(a, b)

# Exponential assignment operator
b **= 5
# short hand of b = b ** 5
print(a, b)

# Floor division assignment operator
b //= a
# Short hand of b = b // a
print(a, b)
