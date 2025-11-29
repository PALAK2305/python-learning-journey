# There may be times when you want to specify a type on to a variable. This can be done with casting.
# type() function is used to find the data type of a given variable in python.
# eg
a = 31
t = type(a)  #class <int>
print(t)

a = "31.3"
t = type(a)  #class <str>
print(t)

a = 31.3
t = type(a)  #class <float>
print(t)

a = "31.3"
b = float(a)
t = type(b) 
print(t)

