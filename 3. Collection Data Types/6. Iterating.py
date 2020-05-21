"""
In this file we are going to see how to print the sequences without using iteration statements (loops).
We are going to see a very useful operator for printing the sequence.
It is the * opeator similar to pointer operator in C.
We can use this inside a print statement for printing the whole sequence iterating over every individual element.
"""

L = [1,2,3,4,5]
print(*L)

"""
You might see that the default seperation between the elements is a space i.e. ' '.
However we can change it just like we did by using the parameter named end but using the parameter sep.
sep stands for seperation.
"""

# Seperating it with a comma
print(*L, sep=', ')
# Seperating it with a newline character
print(*L, sep='\n')

"""
This might come in handy when printing out a list of a tupple instead of using loops for iterating over the elements one by one.
We will see how to do that in the further files.
"""
