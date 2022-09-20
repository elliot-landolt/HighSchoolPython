# Chapter 4 - Loops and Random Numbers

for i in range(10):
    print("I will not chew gum in class")
print("This only prints once")

# i is the variable we increment
for i in range(10):
    print(i)

# range function - 3 ways to write it.
# range(number_of_loops) # see above
# range(start_number, end_number) # start included, end not
for j in range(1, 11):
    print(j)

# range(start, end, count_by)
for i in range(0, 1000, 11):
    print(i)

# Examples
# even numbers from 40 to 60

for i in range(40, 61, 2):
    print(i)


# countdown from 10 to 1

for i in range(10, 0, -1):
    print(i)

# Nested Loops
for i in range(10):
    print("A")
    for j in range(10):
        print("B")
        #for k in range(10):
            #print("C")
'''
total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total += new_number
    print("The total is: ", total)
'''  
# What is the value of sum?
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
print(a)
 
# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
 
# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

# RANDOM NUMBERS

import random # imports random library

# randrange funciton - generates random int (3 ways to write)
print(random.randrange(10)) # zero included, last number is not
print(random.randrange(10, 20)) # start and end (end not included)
print(random.randrange(10, 20, 2)) # even numbers 10-18

# random function - generates random float from 0 to 1
print(random.random()) # no input to the function
print(round(random.random(), 3)) # round to 3 decimal places

# random number float from 0 to 5
print(random.random() * 5)

# to get range of any float, multiply for range, and add for offset
# random float from 5 to 10

print(random.random() * 5 + 5)

#  WHILE LOOP
# can do anything a FOR loop can do

# count to 10
for i in range (1, 11):
    print(i)

j = 0
while j < 10:
    j += 1
    print(j)
    
# use a while loop to print evens from 10 to 20

number = 10

while number >= 10 and number <= 20:
    print(number)
    number += 2
    
# Beware the infinite loop - very bad python!
'''
while 10 > 1:
    print("INFINITYY!!!")

i = 0
while i < 10:
    j += 1
    print(j)
'''
'''
i = 10

while i < 20:
    i -= 2 
    print(i)
'''

# some things are easier with WHILE

i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2

# THE GAME LOOP

done = False
print("Welcome to the Dragon Quest 2")
while not done:
    answer = input("Do you want to attack the sleeping dragon? ")
    if answer.lower() == "yes" or answer.lower() == "y":
        print("Poor choice. You die.")
        done = True
    else:
        print("The dragon is blocking the door")
    
print("Thank you for playing Dragon Quest 2")

