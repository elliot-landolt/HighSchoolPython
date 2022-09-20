# CHAPTER 3 NOTES

# If Statements
# if condition:
#     indented block of code

# Comparisons
a = 3
b = 4
c = 4
d = 5

if b > a:
    print("b is greater than a") # this prints

if b >= c:    print("b is greater than or equal to c") # this prints

if c > d:
    print("c is greater than d") # this does not print

if b == c:
    print("b is equal to c") # use == for comparasion and = for variable assignment

if d != a:
    print(" d is not equal to a") # checks the opposite of ==

# make a program that asks the user their age
# then tells them if they are old enough to vote

#if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
# Indentations
if b == 4:
    print("b is four")
    print("Second line")
    print("Third Line")

# Indent levels have to match
# no re-indentation is allowed
# let wing help you. Use shift tab when needed. 

# AND and OR (compound comparisions)
a = 3
b = 4
c = 4
d = 5

if a < b and d > c:
    print("both are true")
    
if a > b and d > c:
    print("both are true 2")

if a > d or c == b:
    print("one or both of these is true")
if a > d or c != b:
    print("one or both is true")

# Boolean values (true or false)
my_boolean = True # new variable/data type

if my_boolean:
    print("this is true")
if False:
    print("This would never print")

x = a > d # this gets evaluated
y = d > a
print(x, y)

# any number that is non-zero evaluates as true
# only false and 0 (integer zero) evaluate as false
if a and b and c and d:
    print("a is true????")
e = 0
if e:
    print("e is true") # this does not print (it is false)

# else and else if (elif)
temp = 75

# if statements can be linked with elif statements
# else statements are the "catchall" condition
if temp < 50:
    print("its cold outside")
elif temp >= 50 and temp < 70:
    print("It is cool outside")
elif temp == 75:
    print("it is 75 degrees outside")
else:
    print("Its hot outside")


# Text Comparasons
'''
school = input("Where do you go to school? ")

# need to change the case before comparison
if school.upper() == "PARKER" or school.upper() == "FRANCIS PARKER" or school.upper() == "FRANCIS W PARKER":
    print("Go Colonels")
elif school.upper() == "Latin":
    print("Oh. Good for you.")
else:
    print("I hear that", school, "is a fine institution.")
'''
# String comparisons

if "a" > "z":
    print("string a is greater than string z")
else:
    print("string a is less than string z")

if "apple" > "app":
    print("apple greater than app")
else:
    print("app > apple")

if "10" < "9":
    print("That's weird!")

# Concatentation (we can add text together!)
print("Francis", "W", "Parker")
first = "Francis"
middle = "W."
last = "Parker"
print(first, middle, last)
print(first + middle + last) # this is concatenation
full_name = first + " " + middle + " " + last
print(full_name)

score = 5
print("Your score is", str(score) + "%") # cant combine strings with int or float, convert to str()

# Let's make a multiple choice question
print("Question #1")
print("What is the capital of illinois?\n")
print("\tA. Chicago")
print("\tB. Springfield")
print("\tC. Peoria")
print("\tD. Rockford\n")

answer = input("Enter your letter choice: ")
if answer.upper() == "B" or answer.upper() == "SPRINGFIELD":
    print("Correct!")
else:
    print("Sorry", answer, "is incorrect")
    
print("\n\nQuestion #2")
answer = float(input("What is 21 squared?\n"))

if answer == 21 ** 2:
    print("You are correct!")
else:
    print("Wrong! the answer is", 21 ** 2)
    
answer = input("What is Francis Parker's middle name?")

if answer.upper() == "WAYLAND":
    print("Correct!")
elif answer.lower() == "w" or answer.lower() == "w.":
    print("Close, the full name is Wayland.")
else:
    print("Incorrect")

