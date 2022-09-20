# Ch 12 - Classes

'''
class - classification of an object. Template for an object. (capitalized)
instance - elliot is an instance of the Student() class
object - a particular instance of a class
method - a function which belongs to a class
constructor method - def__init__(self): automatically runs when you create the object
self - replace with pronoun "my". Self refrence to the object being used.
attributes - variables that belong to a class object

'''
class Student():
    ''' Class names follow normal rules, but are capitalized'''
    def __init__(self): 
        self.name = ""
        self.gpa = 4.0
        self.email = ""
        self.schedule = []
        self.sitting = False
        print("a student is born")

elliot = Student()
elliot.name = "Elliot"

# Monopoly

class Player():
    def __init__(self, token):
        self.token = token
        self.money = 1500
        self.position = 0
        self.properties = []
        print("Player", self.token, "has joined the game")
    def buy_property(self, name, cost):
        ''' buy name property for cost dollars'''
        self.money -= cost
        self.properties.append(name)
        print(self.token, "bought", name, "for", cost, "dollars")
    def pay_player(self, amount, other):
        self.money -= amount
        other.money += amount
        print(self.token, "payed", other.token, amount, "dollars")

dog = Player("Dog")
car = Player("Car")
dog.money += 200 # dog passed go
print(dog.money)
dog.buy_property("Baltic Ave", 170)
car.pay_player(400, dog)
car.buy_property("Boardwalk", 400)

# classes continued
class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        
        
        
class Enemy():
    def __init__(self, name, health):
        self.weapon = ""
        self.name = name
        self.health = health
        self.gold = 0
        self.x = 0
        self.y = 0
        print("An enemy has appeared")
    def attack(self, damage, target):
        target.health -= damage
        print(self.name, "attacked", target.name, "for", damage, "health points")

class Vampire(Enemy):
    ''' Vampire() is a child class of Enemy()'''
    ''' A vampire is a more specific example of an enemy'''
    def __init__(self, name, health):
        super().__init__(name, health)
        # super() refers to the parent class (Enemy)
        self.form = "Human"
        print("A vampire named", name, "has appeared")
    def change_form(self):
        if self.form == "Human":
            self.form = "Bat"
            print(self.name, "has changed into a", self.form)
        else:
            self.form = "Human"
            print(self.name, "has changed into a", self.form)




hero = Hero("Hiro")
enemy1 = Enemy("Fred", 100)
enemy2 = Enemy("Karen", 200)
enemy1.attack(20, hero)
vampire = Vampire("Buffy", 50)
vampire.attack(30, hero)
for i in range(2):
    vampire.change_form()
    
# copying objects
# to create a new object, you have to use the class name
vampire2 = vampire
vampire2.name = "Stuffy"

