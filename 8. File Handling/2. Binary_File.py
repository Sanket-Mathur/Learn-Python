"""
Binary files have a .dat extension unlike text files and contains the information in binary format.
The text written in it is not readable by humans but works faster than a text file due to reduced conversions.
The modes for a binary file ends with a suffix b.
The functions for reading and writing also differs for a binary file and for those we will have to import pickle
Let's open a pre-written binary file and read what's in there.
"""

import pickle

f = open('binary.dat', 'rb')
lines = pickle.load(f)
print(lines)
f.close()

"""
Here are the different modes you can use while opening a file,
wb - write mode
rb - read mode
ab - append mode
w+b - w and a
r+b - w, r and a
a+b - a and r
The function we use to write in a binary file is
pickle.dump('<Data>', <file>)
The function we use to read from a binary file is
pickle.load(<file>)
"""
