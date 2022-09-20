print("\nWelcome to Bank Robber!\nYou have robbed a bank to make your way across the great American countryside.\nThe cops want their money back and are chasing you down! \nSurvive your American journey and out run the cops. \nKeep in mind that when traveling faster you lose more money.You are starting with seven MILLION dollars!")
import random

end = False

done = False

miles_traveled = 0

thirst = 0

camel_stamina = 0

natives = -40

canteen = 3

money = 7000000

full_speed = 0

moderate_speed = 0


while not done:
    print("\nWould you like to:")
    print("\n\t A. Drink from your canteen")
    print("\t B. Ahead moderate speed")
    print("\t C. Ahead full speed")
    print("\t D. Stop for fuel and sleep")
    print("\t E. Status check")
    print("\t Q. Quit")
    
    user_choice = input("\nYour choice? ")
    
    
    if user_choice.lower() == "q" or user_choice.lower() == "quit":
        done = True    
    
    elif user_choice.lower() == "e" or user_choice.lower() == "status check":
        print("\nMiles traveled: ", miles_traveled, "\nDrinks left in canteen: ", canteen, "\nthe cops are ", miles_traveled - natives, "miles behind you. You have ", "{:6,}".format(money), "dollars!")
    
    elif user_choice.lower() == "d" or user_choice.lower() == "stop for the night":
        camel_stamina = 0
        print("\nYour car is fueled!")
        natives += random.randrange(9, 15)
    
    elif user_choice.lower() == "c" or user_choice.lower() == "ahead at full speed":
        full_speed = random.randrange(10,20)
        miles_traveled += full_speed
        print("\nYou traveled ", full_speed, "miles")
        thirst += 2
        camel_stamina += random.randrange(2, 4)
        natives += random.randrange(9, 15)
        money -= random.randrange(500000,1000000)
    
    elif user_choice.lower() == "b" or user_choice.lower() == "ahead at moderate speed":
        moderate_speed = random.randrange(5, 13)
        miles_traveled += moderate_speed
        print("\nYou traveled ", moderate_speed, "miles")
        thirst += 1
        camel_stamina += random.randrange(1,3)
        natives += random.randrange(9, 15)
        money -= random.randrange(100000,500000)
    
    elif user_choice.lower() == "a" or user_choice.lower() == "drink from canteen":
        if canteen == 0:
            print("No water!")
        elif canteen >= 1:
            print("\nYou were thirsty!")
            thirst = 0
            canteen -= 1
    else:
        print("\nInvalid Answer")
    
    if random.randrange(1, 200) == 137:
        print("YOU FOUND THE HIDEOUT! ALL SETTTINGS RESET!")
        camel_stamina = 0
        thirst = 0
        canteen = 3    
    
    
    if thirst >= 6 and thirst < 8:
        print("You are thirsty!")
    
    elif thirst > 6:
        print("You died of thirst!")
        done = True
        end = True
    
    if camel_stamina >= 5 and camel_stamina < 9:
        print("Your car is almost out of fuel!")
    
    elif camel_stamina > 12:
        print("Your car ran out of fuel!")
        done = True
        end = True
    
    if natives >= miles_traveled:
        print("The cops caught you! You were put in jail!")
        done = True
        end = True
    
    elif natives >= miles_traveled - 15:
        print("\nThe cops are getting close!")
    
    

    if end == True: 
        play_again = input("\nThanks for playing Bank Robber! Wanna play again? ")
    
        if play_again.lower() == "yes" or play_again.lower() == "y":
            end = False
            done = False
            miles_traveled = 0
            thirst = 0
            camel_stamina = 0
            natives = -40
            canteen = 3
            money = 7000000
            full_speed = 0
            moderate_speed = 0            
        elif play_again.lower() == "no" or play_again.lower() == "n":
            done = True
            end = False            
            print("\n\t\tMade by Elliot Landolt")
        else:
            print("Invalid answer")
