"""
The arithmetic operators provided by Python are as following:
+ Addition operator
- Substraction operator
* Multiplication operator
** Exponential operator
/ Division operator
// Floor division operator (Gives us the floor value only)
% Modulo operator (Calculates the reminder left on dividing values)
Let us see their basic functioanlity by assigning two integer type variables and test out operators on them.
"""

a, b = 10, 7
print(a+b, a-b, a*b, a**b, a/b, a//b, a%b)

"""
Now here you can see the operators works just fine with integers and so is the case with floating point decimals.
But you can actually use two of these operators on strings as well.
And these 2 operators are + and *, which concatinates strings and repeat a string respectively.
So lets assign a few strings and get started.
"""

string1 = "Sanket"
string2 = "Mathur"

# Let's try printing out the addition of these strings
print(string1 + string2)
# Now the problem here is on adding there is no space in between that you can see when using a ',' for printing multiple values
# An easy fix to this problem is concatinating a space character between  the two
print(string1 + ' ' + string2)

sayHi = 'Hi'
print(sayHi * 10)

# Here as you can see it repeats the string sayHi 10 times
