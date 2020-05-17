"""
Type conversion as clear from the name is the technique of converting ont data type to another.
The basic data types and their types conversions are as following:
integer: int()
float: float()
string: str()
ascii: ord()
binary: bin()
octal: oct()
hexadecimal: hex()
"""

s = '42'
print(int(s))
print(float(s))

i = 50
print(bin(i))
print(oct(i))
print(hex(i))

# But what if you want to convert an binary to integer. You can use the base property in int()
print(int('1000',2))
# And so on with octal and hexadecimal

# Let's end this with checking the acsii value of A

print(ord('A'))

"""
These are not all type conversions.
There are a few more data types and conversion function made my grouping of values that we will see later.
"""
