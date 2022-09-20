#Chapter 07 Problem Set (20pts)


#1  Create six variables called: my_int, my_float, my_string, my_boolean, my_list, and my_tuple.
# Set each variable equal to an appropriate value of that type.  (3pts)
# This is similar to what we did at the beginning of our notes for this chapter.
my_int = 1
my_float = 3.14
my_string = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)
my_boolean = False
my_string = "Hello"


#2. Using an index for my_list2, print the names Idle and Palin. (1pts)
my_list2 = ["Cleese", "Gilliam", "Idle", "Chapman", "Jones", "Palin"]

print(my_list2[2], my_list2[5])

#3. Use a for loop to print each item in my_list3 below. (2pts)
my_list3 = [5, 2, 6, 8, 101]
for item in my_list3:
    print(item)

#4. Use a for loop and the append method to add the numbers 1 to 100 to my_list4.  Then print out the list. (2pts)
'''
sample run
[1, 2, 3, 4, 5, ... , 99, 100]
'''
my_list4 = []
for i in range(1, 101):
    my_list4.append(i)
print(my_list4)
#5  Print the number 1, 2 and 3 using indices for my_list5 below (3pts)
my_list5 = [[38, 11, 66], [5, [43, 3], 1], [0, 90, 7], [4, 10, 33, 2, [30, 77]]]
print(my_list5[1][2], my_list5[3][3], my_list5[1][1][1])

#6. Using the string called "my_text" below, do the following using string indices: (4pts)

my_text = "The quick brown fox jumped over the lazy dogs."

print(len(my_text))
print(my_text[-7])
print(my_text[:7])
print(my_text[12:18])
# a. Print the length of my_text.
# b. Print the letter "y" from my_text.
# c. Print "The qui" from my_text
# d. Print the text "own fo" from my_text.

#7 Write a loop that will take in a list of five numbers from the user, adding each to an array. Then print the array. (2pts)
'''
sample run
Enter a number: 5
Enter a number: 3
Enter a number: 6
Enter a number: 1
Enter a number: 4
[5, 3, 6, 1, 4]
'''
my_list6 = []
for i in range(5):
    answer = int(input("Enter a number: "))
    my_list6.append(answer)
    
print(my_list6)
#10. Write a program that takes an array like the following, and prints the average. (3pts)
# Use the len function, don't just use 15, because that won't work if the list size changes. 

total = 0
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

for item in my_list:
    total += item
   
average = total/len(my_list)    
print(average)