#Program that lets you play rock paper scissors

from random import randrange as ran
#for the computer to decide if it'll play rock, paper, scissors 

print("~~~~~~~~~~~~~ Rock, Paper, Scissor ~~~~~~~~~~~~~")
while True:
    print("You and the Computer will have 5 rounds.")

    def organizeNum(x):
        if x == 1:
            return "rock"
        elif x == 2:
            return "paper"
        else:
            return "scissor"

    def userWon():
        print("You have won that round")

    def compWon():
        print("Computer won that round")

    userPoints = 0
    compPoints = 0
    for x in range(9):
        while True:
            txt = input("Enter what you'll use in " + str(x + 1) + " round: ")
            guessUser = txt.lower()
            if guessUser == "paper" or guessUser == "rock"  or guessUser == "scissor":
                break
            else:
                print("An error occured, please try again\n")
        guessComp = organizeNum(ran(1, 4))

        if guessComp == guessUser:
            print("Draw, no one won that round")
        elif guessComp == "rock" and guessUser == "paper":
            userWon()
            userPoints = userPoints+ 1
        elif guessComp == "paper" and guessUser == "scissor":
            userWon()
            userPoints = userPoints+ 1
        elif guessComp == "rock" and guessUser == "scissor":
            compWon()
            compPoints = compPoints+ 1
        elif guessComp == "paper" and guessUser == "rock":
            compWon()
            compPoints = compPoints+ 1
        elif guessComp == "scissor" and guessUser == "paper":
            compWon()
            compPoints = compPoints + 1
        elif guessComp == "scissor" and guessUser == "rock":
            userWon()
            userPoints = userPoints+ 1
        else:
            print("An error occured this round...\n")

        if userPoints == 3 or compPoints == 3:
            break
        else:
            pass

    if userPoints > compPoints:
        print("\nIn the end, you won the game of the rock, paper, scissors!")
    elif compPoints > userPoints:
        print("\nIn the end, the computer won of the rock, paper, scissors!")
    else:
        print("\nWell after 9 round's it's a draw!")

    while True:
        yesOrNoTXT = input("Do you want to play again (y/n): ")
        yesOrNo = yesOrNoTXT.lower()
        if yesOrNo == "y" or yesOrNo == "n":
            break
        else:
            print("An error occured, try again\n")

    if yesOrNo == "n":
        print("\nThanks for playing\n")
        break
    else:
        print("\nNew game reloading...\n")

print("\nDone")
