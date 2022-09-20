# Number 1

def min3 (num1, num2, num3):
    lowest = num1
    if num2 <= lowest:
        lowest = num2
    if num3 <= lowest:
        lowest = num3
    return lowest

print(min3(5, 4, 3))

# Number 2

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

# Number 3

def find(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            print("Number", key, "found at position", i)
        
    


my_list_other = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
     
find(my_list_other, 12)
find(my_list_other, 91)
find(my_list_other, 80)

# Number 4
import random
def create_list(size):
    my_list = []
    for i in range(size):
        my_list.append(random.randrange(1, 7))
    return my_list
print(create_list(5))

# Number 5
def count_list(my_list, num):
    how_many = 0
    for i in range(len(my_list)):
        if my_list[i] == num:
            how_many += 1
    return how_many

my_list2 = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2 ,2, 1]
print(count_list(my_list2, 5))

# Number 6
def average_list(my_list):
    total = 0
    for i in my_list:
        total += i
    average = total / len(my_list)
    return average


avg = average_list([1,2,3])
print(avg)

# Number 7
my_list = create_list(10000)
print(count_list(my_list, 1))
print(count_list(my_list, 2))
print(count_list(my_list, 3))
print(count_list(my_list, 4))
print(count_list(my_list, 5))
print(count_list(my_list, 6))
print(average_list(my_list))
