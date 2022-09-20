import random
import sys
import os

print ("Hello World")

name = "Elliot"
print(name)

print("5+20=", 5+2)

grocery_list = ["sauce", "curry", "hamburgers"]

print("first item", grocery_list[0])
print("second item", grocery_list[1])

homework = ["math", "science", "english"]

chores = [homework, grocery_list]

print(chores)

grocery_list.append("Carrots")
print(chores)

grocery_list.remove("Carrots")
print(chores)
print(len(chores))

print(

)

print("tuples")

pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = list(new_tuple)
len(new_tuple)
print(new_tuple)

print(""
      ""
      "")
print("dictionaries")
sports = {'soccer' : 'ball', 'basketball' : 'ball', 'hockey' : 'puck'}

print(sports['soccer'])
print(len(sports))
print(sports.get('basketball'))
print(sports.keys())
print(sports.values())

print('''''')
print('conditionals')

age = 21

if age > 12 :
    print('you are old')
else :
    print('you are young')

print('''''')
if age >= 21 :
    print('you can drink')
elif age>= 16 :
    print('you can drive')
else :
    print('you are young')

print('''''')


if ((age >= 12)and (age <= 16)) :
    print('you are in school')
elif((age == 21)or (age == 16)):
    print('you are 16 or 21')

print('''''')
print('looping')
print('''''')

for x in range(0, 10) :
    print(x,'', end='')
print('\n')

for y in grocery_list :
    print(y)

for x in [2,3,4,5,6] :
    print(x)


num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range (0,3) :
    for y in range (0,3) :
        print(num_list[x][y])

for x in range(0, 15) :
    print(x, '', end='')
print('\n')


time = 1200

if time > 1000 :
    print('dont for get to complete chores')
    print(chores)

else :
    print('dont forget to set alarm')

random_num = random.randrange(0,100)
print(random_num)

while(random_num != 15) :
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20) :
    if(i%2 == 0) :
        print(i)
    elif(i == 9) :
        break
    else:
        i += 1 # i = i + 1
        continue
    i += 1

print('''''')
print('functions')
print('''''')

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum
print(addNumber(1, 4))

string = addNumber(1,4)

print('''''')
print('gathering user imput')
print('''''')

print('What is your name?')

name = "Bob" #sys.stdin.readline()

print('Hello', name)

long_string = 'if u fall i will catch u - the floor'
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4]+ 'kobe')
print('%c is my %s letter and my number %d number is %.5f'%
      ('X', 'favorite', 1, .14))
print(long_string.capitalize())
print(long_string.find('floor'))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace('floor', 'ground'))

quote_list = long_string.split(' ')
print(quote_list)

print('''''')
print('Files')
print('''''')

test_file = open('test.txt', 'wb')
print(test_file.mode)
print(test_file.name)
test_file.write(bytes('write me to the file\n', 'UTF-8'))
test_file.close()

test_file = open('test.txt', 'r+')

text_in_file = test_file.read()
print(text_in_file)

os.remove('test.txt')


print('\n Objects \n')

class Animal:
#    name = ''
#    height = 0
#    weight = 0
#    sound = ''


    def __init__(self, name = '', height = 0, weight = 0, sound = ''):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

#    def set_name(self,  name):
#        self.__name = name

#    def get_name(self):
#        return self.__name

#    def set_height(self, height):
#        self.__height = height

#    def get_height(self):
#        return self.__height

#    def set_weight(self, weight):
#        self.__weight = weight

#    def get_weight(self):
#        return self.__weight

#    def set_sound(self, sound):
#        self.__sound = sound

#    def get_sound(self):
#        return self.__sound

    def get_type(self):
        print('Animal')

    def toString(self):
        return '{} is {} cm tall and {} pounds and says {}'.format(self.name, self.height,
                                                                  self.weight, self.sound)

cat = Animal('Julius', 30, 50, 'meow')

print(cat.toString())

class Dog(Animal):
#    __owner = ''
#    __name = ''
#    __height = 0
#    __weight = 0
#    __sound = ''

    def __init__(self, name, height, weight, sound, owner = 'anya'):
        super(Dog, self).__init__(name, height, weight, sound)
        self.owner = owner

#    def set_owner(self, owner):
#        self.__owner = owner

#    def get_owner(self):
#        return self.__owner

    def get_type(self):
        print('Dog')

    def toString(self):
        return '{} is {} cm tall and {} pounds and says {} and is owned by {}'.format(self.name, self.height,
                                                                   self.weight, self.sound, self.owner)

#    def multiple_sounds(self, how_many=None):
#        if how_many is None:
#            print(self.get_sound())
#        else:
#            print(self.get_sound() * how_many)


spot = Dog('spot', 32, 25, 'woof', 'Elliot')

print(spot.toString())

marcel = Dog('Marcel', 45, 32, 'woof')
print(marcel.toString())


