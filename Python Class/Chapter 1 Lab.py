print("Fahrenheit to Celsius calculator")
temp_fah = float(input("Enter temperature in Fahrenheit: "))
temp_cel =  (temp_fah - 32) * 5 / 9
print("Temperature in Celsius is", temp_cel)

################

print("Area of a Trapeziod")
height = float(input("Enter the height of the trapezoid"))
length_bot = float(input("Enter the length of the bottom base"))
length_top = float(input("Enter the length of the top base"))
area = 1/2 * (length_bot + length_top) * height
print("Area =", area)


#################

import math
print("Area of a circle")
radius = float(input("Enter the radius"))
area = math.pi * radius ** 2
print("The area of the cirlce is", area)

#############
import math
print("Area of cone")

radius = float(input("Enter the radius"))
height = float(input("Enter the height"))
volume = (math.pi * radius ** 2 * height) / 3
print("The volume is", volume)