"""
Let's say we only want to open the file if it exists in the system (necessary in read mode), we will check if the file exists or not.
For this we will use os module and if the file doesn't exist, we will exit the program using the sys module.
"""

import os, sys

if os.path.isfile('data.txt'):
	f = open('data.txt', 'a+')
else:
	sys.exit()


f.write('Add this line as well\n')
f.seek(0)
s = f.read()
print(s)

"""
f.seek(0) is used to move the cursor to the start of the file so that it can read the document
"""

