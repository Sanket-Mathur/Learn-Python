"""
File handling is the technique of handling a file through a program and perform operations like writing, reading and appending the file.
The file can be opened in various different modes(with different properties).
For now let's open/create a file in write mode and write something in it.
"""

f = open('text.txt', 'w')
f.write('How are you doing?')
f.close()

"""
Now no matter how many times you run the code, the file will only contain one line.
This is happening because the file is opened in write mode which will keep on overwriting the file if exists.
For adding the lines each time you open the code, the file should be opened in append mode.
Here are the different modes you can use while opening a file,
w - write mode
r - read mode
a - append mode
w+ - w and r
r+ - w, r and a
a+ - a and r
The function we use to write in a binary file is
<file>.write('<Data>')
The function we use to read from a binary file is
<file>.read()
We will see another example with a+ mode in the third file
"""
