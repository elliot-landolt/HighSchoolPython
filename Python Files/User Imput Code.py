import sys
import random
import os
print('What is your name?')
name = sys.stdin.readline()
print('Hello', name)

print('How was your day?')
day = sys.stdin.readline()
print('it\'s good to hear that your day was' , day)

grocery_list = ['Corn', 'Lobster']
to_do_list = ['Dishes', 'Laundry']
#print('Which list do you want to access?')
#access = sys.stdin.readline

access = input('which list do you want?')



if access == 'groceries' :
    print('Accessing', access)
    print(grocery_list)
elif access== 'to do list':
    print('Accessing', access)
    print(to_do_list)
else :
    print('we could not find that list')

#print('fair life choco milk')

#print('%s is my best %s and he scored %d points' %
     # ('Devonta Freeman', 'Running Back', 39))
