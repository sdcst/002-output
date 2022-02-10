#!python3

"""
print()
Basic Examples
Make sure you enable Word Wrap in your IDE
I also recommend adding a breakpointat and then stepping through your program so that you can read the content and see what happens at each step in the program
"""

#print a string literal
print("Hello world")

#print a variable
x = "Hello"
print(x)

#change the line terminator
#normally, the print statement ends with a line break: \n We can change how the line terminates by changing the end value.  In this way, we can join two different print statements onto the same line.  Note that we can also change what the line ends with to also be a symbol
print("Hello", end="")
print("a second line")

print("Game",end=":")
print("Scrabble")

#print multiple things together
# note that when you print multiple things, they CAN be a mixture of variables and string literals, but they are all separated by a space
money = 10
print("Hello","hi","Welcome","Bienvnue","$",money)

#print multiple things and change the separator
#the default separator is a space, but you can change what the separator is by adding a paramater sep=''
print("Hello","hi","Welcome","Bienvnue","$",money, sep="")
print("Hello","hi","Welcome","Bienvnue","$",money, sep="-")

#formatted output
#use of f"String literal {evaluated expression}" can add variable inside your string literals. This is one of the easiest ways to include numerical variables inside your output
x = 10
print(f"The value of x is {x}")

#Note: You can also use expressions in your formatted strings
print(f"The value of 2x is {2*x}")

#Formatted output is a superior alternative to concatenating strings with numerical values cast as strings
x = 10
print("The value of your number is " + str(x) + ".")

#You can also create a new variable for output
strX = str(x)
print("The value of your x is " + strX + ".")

#notice how this looks much cleaner
print(f"The value of your number is {x}.")
