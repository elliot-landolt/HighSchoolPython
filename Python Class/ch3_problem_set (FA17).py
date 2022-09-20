'''
Chapter 3 Problem Set (16pts)

Instructions:  For each of the following, enter your answer below the numbered problem.  
For questions requiring code, ensure the code runs properly without errors.

Make sure your file executes before you submit it!

If a single problem is not working properly, please comment it out of your code. If a question is commented out, it will receive partial credit.
Non working or broken code will not receive any credit for that problem.

For questions requiring written answers, use Python to print your answers.
Use complete sentences and answer the question as completely as required to demonstrate your understanding.
'''

#################################    

print("Problem 1 (1pt)")
print("Fix the following code. Look closely, it is a common syntax error.")
     
temperature = float(input("Temperature: "))
if temperature > 90:     
     print("It is hot outside.")

#################################
     
print("Problem 2 (3pts)") 
print("Write a Python program that will take in a number from the user and print to tell the user if their number is positive, negative, or zero.")
'''
Example run:
Enter a number: 5.3
Your number is positive

Example run 2:
Enter a number: 0
Your number is zero
'''
number = float(input("Enter a number: "))
if number > 0:
     print("Your number is positive.")
elif number < 0:
     print("Your number is negative.")
elif number == 0:
     print("Your number is zero")
#################################
     

print("Problem 3 (3pts)")
print("Write a python program which takes a number from the user, and prints \"Success\" if it is both greater than -10 AND less than or equal to 10.  If the number is outside this range, print Failure.")

number = float(input("Enter a number"))
if number > -10 and number <= 10:
     print("\"Success\"")
else:
     print("\"Failure\"")


'''
Example Run:
Enter a number greater than -10 and less than or equal to 10: -5.2
Success
'''
 
##################################

print("Problem 4 (2pts)") 
print("Fix the following code.  There are three things wrong.")

x = input("Enter a number: ")
if x == 3:
     print("You entered 3")

###################################
     
print("Problem 5 (2pts)")
print("There are three things wrong with this code. Fix the code.")
     
answer = input("What is the name of Dr. Bunsen Honeydew's assistant?")
if answer == "Beaker":
     print("Correct!")
else:
     print("Incorrect! It is Beaker.")
     
#####################################
      
print("Problem 6 (2pts)") 
print("Look at the code below.  Before running the code, make a prediction of what each line will print. Put your prediction in a comment to the right of the print statement.  I am not grading you for your prediction, I simply want you to think about the code. Next, run the code and see if you are correct. One of the lines creates an error.  Fix it. Make sure you understand the reason for any incorrect guesses")
     
print("3" == "3") # True
print(" 3" == "3") # True
print(3 < "3") # syntax error
print(3 < 4) # false
print(3 < 10) # false
print("3" < "4") # true
print("3" < "10") #  true
print((2 == 2) == "True" ) # true
print((2 == 2) == True ) # true
     
###################################

print("Problem 7 (1pt)")
print("Fix the following code:")

if 5 > 4:
     print("First statement is true")
elif 5 > 4 and 5 > 3:
     print("Both statements are true")

#####################################

print("Problem 8")

print("Problem 9 (3pt)") 
print("Fix the following code which has multiple errors.")
     
print("Welcome to Oregon Trail!")
     
print("A. Banker")
print("B. Carpenter")
print("C. Farmer")

money = 100     
userInput = input("What is your occupation?")
     
if userInput == "A":
     occupation = "Banker"
     money += 100
elif userInput == "B":
     occupation = "Carpenter"
     money += 70
elif userInput == "C":
     occupation = "Farmer"
     money += 50
     
print("You are a", occupation, "with", money, "dollars")
     
     

