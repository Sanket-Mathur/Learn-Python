"""
Bitwise operators are based on both the binary conversion of a number and logic gates.
There are three types of bitwise operators in python.
& Bitwise AND
| Bitwise OR (Inclusive OR)
^ Bitwise XOR (Exclusive OR)
Let's try them out first and then I will explain what is happening.
"""

print(4 & 7)
print(4 | 7)
print(4 ^ 7)

"""
First lets convert 4 and 7 to binary.
4 = 100
7 = 111

& operator follows AND logic gates and switches 0s and 1s depending on its property(as you saw in the truth table)
  1 0 0
& 1 1 1
= 1 0 0 = 7

| operator follows OR logic gates and switches 0s and 1s depending on its property(as you saw in the truth table)
  1 0 0
| 1 1 1
= 1 1 1 = 7

^ operator follows XOR logic gates and switches 0s and 1s depending on its property. This might be new for you.
Let's see its truth table
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
Now let's solve our problem based on this
  1 0 0
^ 1 1 1
= 0 1 1 = 3
"""
