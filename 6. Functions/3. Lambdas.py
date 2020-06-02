"""
Lambdas are annonmous functions which must return some value.
Syntax:
<name> = lambda <variable> : <expression>
Now since lambdas are usually written in a single line, are short one line functions.
The functions which are short and does not contain much functionality are written the lambdas.
Let's see a few examples
"""

# Function to return cube of a number
sq = lambda x: x**3
print(sq(5))

# Function to print if the number is even or odd
e_o = lambda x: 'Even' if(x%2==0) else 'Odd' # Such syntax of if-else is often used while defining lambdas
print(e_o(2))
print(e_o(5))
