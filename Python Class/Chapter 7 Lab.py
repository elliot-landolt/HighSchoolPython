room_list = []
room = ["You are in the bedroom, it looks like the bed was just made.\nThere are doors to the North and East, \nthere is a staircase to the South", 3, 1, 8, None]
room_list.append(room)
room = ["You are in the Coat Room, some of the umbrellas look wet.\nThere is a door to the North, East and West.", 4, 2, None, 0]
room_list.append(room)
room = ["You are in the family room, there is a fire in the fireplace.\nThere is a door to the North and West", 4, None, None, 1]
room_list.append(room)
room = ["You are in the Kitchen, a pot of tea is on the stove.\nThere is a door to the North, East and South", 5, 4, 0, None]
room_list.append(room)
room = ["You are in the dining room, the table is set for a dinner.\nThere is a door to the North, South and West", 7, None, 2, 3]
room_list.append(room)
room = ["You are in the guest room, the bed is messy.\nThere is a door to the East and South ", None, 6, 3, None]
room_list.append(room)
room = ["You are in the bathroom, the toilet is clogged!\nThere is a door to the East, South and West", None, 7, 4, 5]
room_list.append(room)
room = ["You are in the living room, there is a boardgame out.\nThere is a door to the South and West", None, None, 4, 6]
room_list.append(room)
room = ["You are in the TV room, Fox News is on.\nThere is a door to the East and North\nYou can also go south back down the stairs", 10, 9, 0, None]
room_list.append(room)
room = ["You are in the Kids Room, looks like they forgot to put away their toys.\nThere is a door to the North, East and West", 11, 14, None, 8]
room_list.append(room)
room = ["You are in the Play Room, the XBox was left on.\nThere is a door to the North, East and South", 12, 11, 8, None]
room_list.append(room)
room = ["You are in the Pool area! The pool looks very warm.\nThere is a door to the North, West and South", 13, None, 9, 10]
room_list.append(room)
room = ["You are in the Wine cellar, it is very cold and big.\nThere is a door to the East and South", None, 13, 10, None]
room_list.append(room)
room = ["You are in the Classroom, the room smells of chalk. \nThere is a door to the South and West and to the East is a door to a balcony.", None, 14, 11, 12]
room_list.append(room)
room = ["You are on the Balcony! \nWhat a nice view, you can exit through the South door or the North door.", 13, None, 9, None]
room_list.append(room)


current_room = 0




print("\nWelcome to the Fun House Adventure! \nYou are trapped inside a modern villa. \nYou are inclined to find out where you are!\nTo quit, type q or quit.\nYou can also type inventory!")

done = False
taken = False
no_key = False
no_leave = False
while not done:
    print("\n")
    print(room_list[current_room][0])
    user = input("\nWhich direction do you want to travel in? ")
    # north
    if user.lower() == "north" or user.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("\nYou can't go this direction!")
        else:
            current_room = next_room
    # east
    elif user.lower() == "east" or user.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("\nYou can't go this direction!")
        else:
            current_room = next_room
    # south
    elif user.lower() == "south" or user.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("\nYou can't go this direction!")
        else:
            current_room = next_room        
   
    # west
    elif user.lower() == "west" or user.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("\nYou can't go this direction!")
        else:
            current_room = next_room
    
    # inventory
    elif user.lower() == "inventory" or user.lower() == "i":
        if taken == True:
            print("\nYou have a key")
        elif taken == False:
            print("\nYou have empty hands!")
        else:
            print("Invalid Answer")
    
    # quit
    elif user.lower() == "quit" or user.lower() == "q":
        done = True
    else:
        print("Answer invalid, please try again")    
    
    
    # KEY
    if current_room == 10 and no_key == False:
        print("\nYou found a mysterious key!")
        key = input("Would you like to take it? ")
        if key.lower() == "yes" or key.lower() == "y":
            taken = True
        elif key.lower() == "no" or key.lower() == "n":
            print("Ok.")
            taken = False
            no_key == False
        else:
            print("Invalid Answer")
    
    # TRAPDOOR
    if current_room == 5 and taken == True and no_leave == False:
        print("\nYOU FOUND THE SECRET penis! Use the key to leave the house forever!")
        leave = input("Would you like to leave? ")
        if leave.lower() == "yes" or leave.lower() == "y":
            done = True
        elif leave.lower() == "no" or leave.lower() == "n":
            done = False
            no_leave = True
            print("Ok.")
        else:
            print("Invalid answer, you are trapped forever")
  
    
print("\nThanks for playing!")
print("\t\t\tBy: Elliot Landolt")