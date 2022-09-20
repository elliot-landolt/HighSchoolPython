'''
Write code that classifies a given amount of money (which you store in a variable named count), as greater monetary units. 
Your code lists the monetary equivalent in dollars, quarters, dimes, nickels, and pennies.
Your program should report the maximum number of dollars that fit in the amount, then the maximum number of quarters that fit in the remainder after you subtract the dollars, then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters, and so on for nickels and pennies.
The result is that you express the amount as the minimum number of coins needed. Modulo is helpful and recommended here , but not necessary to solve.
'''
'''
count = float(input("How much money do you have? "))
count = count * 100
dollars = count // 100
print("You have", dollars,"dollars")
cents = count - dollars * 100
print("You have",cents,"cents")

if cents > 25:
    quarter = cents // 25
    print("You have",quarter,"quarters")

dime = cents % 25

if dime >= 10:
    print("You have", int(dime / 10), "dimes")

nickel = cents % 5

if nickel >= 5:
    print("You have", int(nickel / 10), "nickels")
    
penny = cents % 1

if penny >= 1:
    print("You have", int(penny / 10), "pennies")
'''
count = float(input("Enter Money "))

count = count * 100
dollars = count // 100
print("You have", dollars,"dollars")
cents = count - dollars * 100
print("you have", cents, "cents")
quarters = 0
dimes = 0
nickels = 0
pennies = 0

if cents <= 25:
    quarter = cents // 25
    print("You have",quarter,"quarters")
    cents = cents - (quarters * 25)
dime = cents % 25

if dime >= 10:
    print("You have", int(dime / 10), "dimes")

nickel = cents % 5

if nickel >= 5:
    print("You have", int(nickel / 10), "nickels")
    
penny = cents % 1

if penny >= 1:
    print("You have", int(penny / 10), "pennies")    
