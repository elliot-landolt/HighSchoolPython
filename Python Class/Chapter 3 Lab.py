print("\n\tQuiz Time!")
print("\n\tQuestion 1\n")
score = 0
answer = int(input("How many Fast and Furious movies are there? \n"))
if answer == int(8):
    print("\nCorrect! +1 point!")
    score = score + 1
else:
    print("Sorry,", answer, "was incorrect. The correct answer was 8.")

print("\n\tQuestion 2\n")
answer = float(input("What is the square root of 16? \n"))
if answer == int(4):
    print("\nCorrect! +1 point!")
    score = score + 1
else:
    print("\nSorry,", answer, "was incorrect. The correct answer was 4.")

    
print("\n\tQuestion 3\n")

print("\tWho created the telephone?")
print("\tA. Albert Einstien")
print("\tB. Alexander Graham Bell")
print("\tC. Gerald Bush")
print("\tD. Winston Churchhill")

answer = input("\nEnter answer here: ")
if answer.lower() == "b" or answer.lower() == "alexander graham bell":
    print("\nCorrect! +1 point!")
    score = score + 1
else:
    print("\nSorry,", answer, "was incorrect. The correct answer was Alexander Graham Bell.")

print("\n\tQuestion 4\n")

answer = input("Who is the rival school of Parker? \n")
if answer.upper() == "LATIN":
    print("\nCorrect! +1 point!")
    score = score + 1
else:
    print("\nSorry,", answer, "was incorrect. The correct answer was Latin.")

print("\n\tQuestion 5\n")

print("\tWho is the best soccer player in the world?\n")
print("\tA. Christiano Ronaldo")
print("\tB. Neymar")
print("\tC. Gareth Bale")
print("\tD. Lionel Messi")

answer = input("Enter answer here: ")
if answer.lower() == "d" or answer.lower() == "lionel messi" or answer.lower() == "messi":
    print("\nCorrect! +1 point!")
    score = score + 1
elif answer.lower() == "a" or answer.lower() == "christiano ronaldo" or answer.lower() == "ronaldo":
    print("\nWRONG, -1 point")
    score = score - 1
else: 
    print("\nSorry,", answer, "was incorrect. The correct answer was d.")
      
print("\nCongratulations! You got", score, "out of 5 points! That's", str((score / 5) * 100) + "%")
if score == 1:
    print("Better luck next time!")
elif score == 2 or score == 3 or score == 4:
    print("Not bad!")
else:
    print("Wow! Nice job ace!")