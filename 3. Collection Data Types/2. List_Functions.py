"""
Let's also see the functions we can use on a list
Length of list: len(<listname>)
Maximum value: max(<listname>)
Minimum value: max(<listname>)
Sum of values: sum(<listname>)
Adding values to list:
	Appending: <listname>.append(<values>)
	Expanding: <listname>.expand(<list>)
Deleting values from list:
	Poping the last element: <listname>.pop()
	Removing element by value: <listname>.remove(<value>)
	Removing element by index: del <listname>[<index>]
Sorting the values: <listname>.sort()
Let's see some of these functions in action
"""

intList = [2, 5, 7, 1, 6]
# Let's sort them in reverse order. We can do this by using the reverse parameter in the function sort()
intList.sort(reverse=True)
print(intList)

# Minumum and maximum values; and the average
print('Minimum: %d, Minimum: %d' % (min(intList), max(intList)))
print('Average:', sum(intList)/len(intList))

# Appending 10 to our list intList and the extending list [5,7,4] in it
intList.append(10)
print(intList)
intList.extend([5, 7, 4])
print(intList)

# Understanding how different deletion functions work
# Poping last element off the list
intList.pop()
print(intList)
# Removing 1 from list
intList.remove(1)
print(intList)
# Deleting the element at index 1
del intList[1]
print(intList)

"""
Now a one last this is creating a list from a string by splitting it into at defined characters.
You can convert a string into a list converting every character into a list element, using the functions list() as <listname> = list(<string>).
But in order to break them at seperate parts is done using splitting and function used for this is split().
Let's see this in action.
"""

string = 'My name is Mr. X'
# Let's break it into a list of seperate words i.e. braking it when we meet a space.
strList = string.split(' ')
print(strList)
