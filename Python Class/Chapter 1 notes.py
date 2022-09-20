# Chapter 1 Notes
# Creating a Custom Calculator

#Comments (lines that are removed from your code. Python ignores them)
# This is a single line comment
print('hello world') # Single line comments can also go after a line of code

'''
This is a multi-line comment
Everything between the triple single quotes
is a comment and is ignored by Python
'''
# Print Function
print('Hello World')

# printing multiple items
print('Francis', 'Parker') # not there is a space between each item
print(2 + 5) # we can print expressions which get evaluated.
print('Score:', 100 + 10) # We can mix text and expressions

# Escape Codes (backslashes)

# WE use espace codes to "Escape" characters.
print("This is my most \"favoritest\" course") # We need to escape the quotes

# We can use it for tabs (\t)
print('First\tMiddle\tLast')

# We can also use it for carrage returns (new line, \n)
print('One\nTwo\nThree')
print('First\n\tSecond\n\t\tThird')

# ASSIGNMENT OPERATOR (it's just the == sign)

x = 10 # make a variable x and assign a value of 10 

print(x + 10)

x = 100 # we can overwrite the variable
print(x)
x = x + 10 # can't do this in math
print(x)

x += 10 # coding shorthand
print(x)

x + 5 #This does not change the value of x, although python still does the math
print(x)

# VARIABLE NAMING
'''
Legal variable names (must start with a lowercase letter and no 
special characters)
'''
distance = 3.4
student8 = "John"
first_name = 'Sue'

# Illegal variable names
#8student = 'John'
#tax% = 0.11
#first name = "Elliot"

# Improper but Legal examples
firstName = "Elliot"
Q = 20
FirstName = "Elliot"
Really_long_or_confusing_variable_name = "No"

# Special case, use all upper case for constant variable
MAX_SPEED = 100

# OPERATORS

# + - * /
a = 5 * 8
print(a)
a = a / 2
print(a)

# floor operator (//)
# divides and eliminates the remainder (rounds down)
print(3 // 2)

# power (**)
print(4 ** 2) # four squared

# modulus (%)
print(13 % 5) # returns the remainder of division
print(7 % 2)
print(8 % 2)
print(a % 2)

y = 3
#x = 8y # this is illegal, be explicit
x = 8 * y

#x = 8 (4 + y) # this is illegal, ...
x = 8 * (4 +y)
print(x)

# MATH SPACING
# python ignores white space in equations
z = 4 * 8 * (18 // 3)
print(z)

#PEMDAS APPLIES 

avg = (3 + 5 + 8) / 3 # common error
print(avg)

# MAKE A CALCULATOR
#Area of a circle
pi = 3.1415926
radius = 5
area = pi * radius ** 2
print (area)

# MATH LIBRARY
import math # this importa  bunch of new functions from the math library
print (math.pi)
print (math.cos(1.5))
print (math.e)

# Calculator (try # 2)
import math
pi = math.pi
radius = 5
area = pi * radius ** 2
print (area)

# InPUT FUNCTION
#radius = input("Enter the radius") # waits for an input from the user (finished by RETURN)
print(radius)
print("End of program")

# Calculator (try #3)
import math
pi = math.pi
#radius = float(input("Enter the radius"))
#radius = float(radius)
area = pi * radius ** 2
print (area)

# Variable types
my_string = 'Some text'
my_int = 42
my_float = 3.14

# Kinetic Energy Calculator
# KE = 1.2 mv**2
print('This calculator returns Kinetic Energy in Joules\n')
mass = float(input("\tEnter the mass in kg: ")) # kg
velocity = float(input("\tEnter the velocity in m/s: ")) # m/s
kinetic_energy = 0.5 * mass * velocity ** 2
print("\tKinetic Energy =", kinetic_energy, "Joules")
