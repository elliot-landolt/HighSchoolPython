# Ch9 Functions
import math
# 2 reasons for functions
# Organize our code
# Reuse our code

'''
Anatomy of a function

def my_function(parameter1, parameter2, ...):
    code that runs when I call the function

my_function(par1, par2, ...)
'''
# DEF means define the function
# my_function is the function name (normal name rules)
# zero or more parameters (any data type)
# after we make the function, we have to call it (and send parameters)

# Example #1 - Print Hello
def hello ():
    print("hello")

hello()
'''
# Example #2 - Say Hello to the user
def personal_greeting():
    name = input("Hello, what is your name? ")
    print("Hello", name.upper())
personal_greeting()
'''
# Example #3 - Print the area of a circle
# area = pi * radius ** 2
def area_circle(radius):
    area = math.pi * radius ** 2
    print(area)

area_circle(10)

def volume_cylinder(radius, height):
    volume = math.pi * radius ** 2 * height
    print("The volume is", volume)
    
volume_cylinder(10, 10)

# Example # 5 - Add the volumes of two cylinders above using RETURN
# return allows you to pass values back to the program
def volume_cylinder2(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume
print()
print(volume_cylinder2(10, 10))
vol1 = volume_cylinder2(10, 10)
vol2 = volume_cylinder2(5, 20)
print(vol1 + vol2)

# Example #6 - Take two numbers and return their product and sum
def sum_product(num1, num2):
    ''' this is where you put the description of the function'''
    total = num1 + num2
    product = num1 * num2
    return total, product

print(sum_product(5, 10))
print(sum_product(5, 10)[0])
print(sum_product(5, 10)[1])

# Example #7 - Take a list and return the average of all numbers

def list_avg(avg_list):
    total = 0
    for num in avg_list:
        total += num
    avg = total / len(avg_list)
    return avg

my_list = [43, 82, 45, 11, 65]
print(list_avg(my_list))

# Example 8 - Variable Scope
# functions ahve scope. Variables inside the function ONLY EXIST INSIDE the function
'''
def f():
    x = 5 # local variable
    
f()
print(x)
'''
# Example 9 - More Scoping
# If you want to know where a variable exists (where it is alive)
# look where it was BORN
y = 7 # global variable

def g():
    print(y) # functions can see global variables

g()

# Example 10 - More Scoping
# We can see global variables, but we can't change them. 

z = 5

def h():
    z += 1 # cannot change a global variable
    print(z)
   

#h()
print(z)
print()

# WARMUP
# This problem is in every intro course.
# Make a function which returns True if a number is prime
# and False if a number is not
def is_prime(num):
    if num < 2:
        return False
    else:
        for n in range(2,num):
            if num % n == 0:
                return False
        return True

print(is_prime(5))
print(is_prime(10))

# number 2 on lab
def box(height, width):
    for j in range(height):
        for i in range(width):
            print("*", end = " ")
        print()
box(7, 5)
print()
box(3, 2)
print()
box(3, 10)