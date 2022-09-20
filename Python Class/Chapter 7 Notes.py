import random
import pygame
import math

#  CHAPTER 7 Lists

# previous variable types (int, float, str, booleans)
my_int = -3
my_float = 3.1315
my_string = "HI"
my_bool = False

# New types for this chapter - Lists and Tuples

# List
# list items can be int, float, string, bool, lists, tuples...
my_list = [300, 500, 100, 200]
grocery_list = ["spam", "eggs", "chesse", "melk", "sugar"]

# What we can do with lists
# [0, 1, 2, 3, 4...]
print(my_list)
print(my_list[0]) # index zero has a value of 300
my_list[1] = 600 # we can assign indexes to new values
print(my_list)

# iterate through a list
for item in grocery_list:
    print(item)
# add to a list
grocery_list.append("spinach")
print(grocery_list)

# Tuple
# like a list, but is immutable (you can't change it)
my_tuple = (255, 200, 100)
print(my_tuple[2])

for item in my_tuple:
    print(item)

# my_tuple[0] = 100 # can't do this (it's immutable)
# my_tuple.append(300) # I said it's immutable
my_tuple = (100, 200, 100, 300) # you can overwrite a tuple
print(my_tuple)

# iterating through a list
# for-each loop
for item in grocery_list:
    print(item)

# index variable loop
# this is more complex, but more powerful

for i in range(len(my_list)):
    print(my_list[i])

# length function
print(len(my_list))

# why use index variable??
print(my_list)
for number in my_list:
    number += 1
print(my_list)

for i in range(len(my_list)):
    my_list[i] += 1
print(my_list)

# a for-each loop uses a copy of the value not the actual list
# the index variable loop uses the actual list

# Find the sum of all the numbers in the following list
my_list2 = [5, 3, 6, 9, 2, 11, 43, 2, 7, 8]

total = 0

for item in my_list2:
    total += item
print(total)
# Average the list
print(total/len(my_list2))

# alter my_list2 to be the square of each number

for i in range(len(my_list2)):
    my_list2[i] **= 2
print(my_list2)

# 2d lists
my_2dlist = [[11, 22, 33],[44, 55],[66, 77, 88, 99]]
print(len(my_2dlist))
print(my_2dlist[0]) # prints 11, 22, 33
print(my_2dlist[0][2]) # prints 33
print(my_2dlist[2][1]) # prints 77
 

# for show
for my_list in my_2dlist:
    for num in my_list:
        print(num)
        
# String slicing
# strings can be indexed like a list
# think of them as lists of characters

name = "Francis W. Parker"
print(name[3]) # prints n
print(name[7]) # prints a space
print(name[9]) # prints a .

# we can also index multiple characters at once
print(name[3:7].upper()) # Everyones favorite show (7 not included)
print(name[12:15]) # print ark

# we can index from beginning or to the end of a list
print(name[:4]) # print Fran
print(name[14:]) # print ker

# we can use negative indices
print(name[-1]) # print r
# print last three letters
print(name[-3:])

# Other things you can do with strings
a = "purple"
b = "octopus"
c = "sandwich"

print(a + b) # concatenate
print(a + " " + b)
print(a + b + c)

print(a * 5) # print multiple times
print(5 * a)

print((a + b + c) * 20 + "!!!!")

# end = (default is \n)
print(a, end = " ")
print(b, end = "&")
print(c)

# Roll two dice 1000 times and them (append) to a list
import random
rolls = []
seven = 0
for i in range(1000):
    dice = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    total = dice + dice2
    rolls.append(total)
    if total == 7:
        seven += 1
print(rolls)
print(1000//seven, "percent of numbers are sevens! There were", seven, "sevens!")
# what percentage are sevens (go back through the list and find out)

# for any number 1-12, print the corresponding 3 letter abbv
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
#n = int(input("Enter a month number: "))

#print(months[n * 3 - 3: n * 3])

# find the highest number in this list. (iterate through to find it)
my_list = [8, 3, 18, 13, 5, 10, 16]

highest = my_list[0]
for i in range(len(my_list)):
    if my_list[i] > highest:
        highest = my_list[i]
print(highest)

