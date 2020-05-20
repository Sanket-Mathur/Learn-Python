"""
Dictionaries are grouping of data under a single name where each data can be identified by a defined unique key.
These are declared inside braces i.e. '{' and '}'.
You need to provide the key and value in a format like <dictname> = {<key1>:<value1>, <key2>:<value2>, ...}
You can access the values by passing the key in brackets like <dictname>[<key>]
"""

# Let's deifne a dictionary storing age of 3 people
ageDict = {'Bob':18, 'John':20, 'Phil':17}

# Now we will print the age of John from the ageDict
print(ageDict['John'])

"""
Dictionaries are mutable as well so we can add or delete values from it.
Let's see some examples.
"""

# Adding element to the dictionary
ageDict['Robert'] = 25
print(ageDict)

# Deleting element
del ageDict['John']
print(ageDict)

"""
Now one last question might be what will happen if we have 2 values with same key.
In such situation, trying to access the value with key will print out the last one present.
Let's see this concept in action.
"""

myDict = {'A':1, 'B':2, 'A':3, 'C':4}
print(myDict['A'])
