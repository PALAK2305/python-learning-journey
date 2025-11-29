# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# eg 
name = "hello"
nameshort = name[0:3] #start from index 0 all the way till 3(excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

#negative slicing
name = "hello"

print(name[0:5])

print(name[-4:-1])
print(name[1:4])


#slicing with skip value

# eg
word = "amazing"
print(word[1:6:2])

# eg 
a = "0123456789"
print(a[1:7:3])

#eg
a = "abcdefghijklmnopqrstuvwxyz"
print(a[1:9:4])

# function

# len
a = "Hello, World!"
print(len(a)) #length of string

#modify
name = "Hello, World! "

print(len(name))
print(name.startswith("Hel"))
print(name.endswith("ld"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.strip()) #remove white spaces from the beginning or the end
print(name.replace("H", "J"))
print(name.split(",")) # returns ['Hello', ' World!']

#String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

# eg
# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# eg 
# to add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# format string

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
# Example
# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

# eg
age = 36
txt = f"My name is John, I am {age}"
txt = f"my cost of dress is, rupess {age:.2f}"
txt = f"i have cake {2*4}"
print(txt)

# escape character

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

#  eg
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


a = "palak is a good girl" \
"but not a bad girl"
print (a)