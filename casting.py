#!python3


"""
Make sure you open the "Run and Debug" in the Activity Bar on the left
We especially want to pay attention to the Variables Panel to see how the variables are changing.
Note that if we have an int or a float type variable, and both are set to a value of 2, the float will always include the decimals.
"""
x = 2
y = 2.0

print(f"The value of x is {x}")
print(f"The value of y is {y}")

"""
You can change the type of a variable between integers and floats by casting them as a different type.
"""
x = float(x)
y = int(y)
print(f"The value of x is {x}")
print(f"The value of y is {y}")

"""
You can even convert a number into a string literal.
"""
x = str(x)
y = str(y)
print(x,y)

"""
Note that you will get an error/exception if you try to convert a word into a number
"""
a = "hello"
#a = int(a)
"""
Comment out line 34 and change your breakpoint so that it skips all of the code that we have just worked through
"""

"""
You can find out what the type is for a variable using the type(var) command.  It will return the type of variable
"""

a = 2
b = 3.0
c = "hello"
d = (3,4,5)
e = [2,3,4]
f = {3 : "hello", 5 : "welcome" }
print( type(a) )
print( type(b) )
print( type(c) )
print( type(d) )
print( type(e) )
print( type(f) )

"""
This can be useful for debugging purposes, but is not really useful in a program.  However, we can use a conditional statement to check the type
"""

a = 4
if type(a) == int:
    print("a is an integer")
else:
    print("a is not an integer")
if type(a) == tuple:
    print("a is a tuple")
else:
    print("a is not a tuple")

