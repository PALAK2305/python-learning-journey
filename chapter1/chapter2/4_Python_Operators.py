# Operators are used to perform operations on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators -: Arithmetic operators are used with numeric values to perform common mathematical operations:
# eg

x = 15
y = 4

print(x + y) #Addition	
print(x - y) #Subtraction
print(x * y) #Multiplication
print(x / y) #Division
print(x % y) #Modulus
print(x ** y) #Exponentiation
print(x // y) #Floor division


# Assignment operators
# eg
a = 4-2 # assign 4-2 in a
print (a)
b =3
b += 6
print(b)


# Comparison operators

x = 5
y = 3

print(x == y) #Equal
print(x != y) #Not equal
print(x > y) #Greater than
print(x < y) #Less than
print(x >= y) #	Greater than or equal to
print(x <= y) #	Less than or equal to


# Logical operators
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# eg
x = 5

print(x > 0 and x < 10)


# Identity operators -: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y

# The is operator returns True if both variables point to the same object:
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


# Membership operators -: Membership operators are used to test if a sequence is presented in an object:
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# eg
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)


# Bitwise operators :- Bitwise operators are used to compare (binary) numbers
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# eg
print(6 & 3)