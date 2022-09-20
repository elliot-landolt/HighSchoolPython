#Chapter 12 Problem Set (23pts)

#1 Write code to create an instance of this class and use dot notation to change its three attributes to those of your own pet or one you know and love: (2pts)
     
class Dog():
   def __init__(self):
      self.age = 0
      self.name = ""
      self.weight = 0
my_dog = Dog()
my_dog.age = 4
my_dog.name = "Marcell"
my_dog.weight = 20
#2 Write code to create an instance of this class and set the name and email attribute using the constructor method (that means adding parameters to this method): (2pts)
     
class Person():
   def __init__(self):
      self.name = "Elliot"
      self.email = "ealandolt@fwparker.org"
me = Person()

     
#3 For the code below, create a class that has the appropriate name and attributes that will allow the code to work. (2pts)
class Bird():
   def __init__(self):
      self.color = ""
      self.name = ""
      self.breed = ""
myBird = Bird()
myBird.color = "green"
myBird.name = "Sunny"
myBird.breed = "Sun Conure"
     
#4 Create a class that would represent a character in a simple 2D game. Include only attributes for the x position, y position, name, and strength. (3pts)
class Sprite():
   def __init__(self):
      self.x = 0
      self.y = 0
      self.name = ""
      self.strength = 50
#5 The following code has two errors.  Fix the code. (2pts)
     
class Person():
   def __init__(self, name):
      self.name = name
      self.money = 0
     
nancy = Person("Nancy")
nancy.money = 100 # set nancy's money to 100 dollars
     
#6 With the following items, identify two unique "has-a" relationships, and two unique"is-a" relationships from any item pairs.  (3pts)
'''
     * Checking account
     * Person
     * Customer
     * Withdraw
     * Bank Account
     * SSN
     * Transaction
     * Address
     * Deposit
     * Balance
Person has a bank account
Bank account has a balance
Person is a Customer
Withdraw is a transaction


'''

#7. This problem has several parts that are all contained in a single  program. Make sure that the program satisfies the requirements for each part.

#part A. Write code that defines a class named Animal: (3pts)

'''
* Add an attribute for the animal name.
* Add an eat() method for Animal that prints ''Munch munch.''
* Add a makeNoise() method for Animal that prints ''Grrr says [animal name].''
* Add a constructor for the Animal class that prints ''An animal has been born.''
'''
class Animal():
   def __init__(self):
      self.name = ""
      print("an animal has been born")
   def eat(self):
      print("Munch munch")
   def makeNoise(self):
      print("Grrr says", self.name)
dog = Animal()
dog.name = "Marcell"
dog.eat()
dog.makeNoise()

#part B. Create a class named Cat: (3pts)
class Cat(Animal):
   def __init__(self):
      super().__init__()
      print("A cat has been born")
   def makeNoise(self):
      print("Meow says", self.name)
   

'''
* Make Animal the parent.
* A makeNoise() method for Cat that prints ``Meow says [animal name].''
* A constructor for Cat that prints ``A cat has been born.'' and it calls the parent constructor.
'''

#part C.  Create a class named Dog: (3pts)
class Dog(Animal):
   def __init__(self):
      super().__init__()
      print("A dog has been born")
   def makeNoise(self):
      print("Bark says", self.name)

'''
* Make Animal the parent.
* A makeNoise() method for Dog that prints ``Bark says [animal name].''
* A constructor for Dog that prints ``A dog has been born.'' and it calls the parent constructor.
'''

#part D.  Make a single program with the following: (3pts)
''' 
* Code that creates a cat, two dogs, and an animal.
* Set the name for each animal.
* Code that calls eat() and makeNoise() for each animal. (Don't forget this part.)
'''  
     
my_cat = Cat()
my_cat.name = "Fluffy"
my_cat.eat()
my_cat.makeNoise()
my_dog1 = Dog()
my_dog2 = Dog()
my_dog1.name = "Marcel"
my_dog2.name = "Winston"
my_dog1.eat()
my_dog2.eat()
my_dog1.makeNoise()
my_dog2.makeNoise()
