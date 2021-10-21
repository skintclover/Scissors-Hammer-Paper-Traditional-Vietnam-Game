from random import randint
print("Type: Scissors, Hammer, Paper")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "Scissors"

if computer == 1:
    computer = "Hammer"

if computer == 2:
    computer = "Paper"        

print("---")
print("You Chooses: " + player )
print("---")
print("Computer Chooses: " + computer )

if player == "Scissors":
        if computer == "Scissors":
            print("Tie")
        if computer == "Hammer":
            print("Lose")
        if computer == "Paper":
            print("Win!")       

if player == "Hammer":
        if computer == "Scissors":
            print("Win!")
        if computer == "Hammer":
            print("Tie")
        if computer == "Paper":
            print("Lose")        

if player == "Paper":
        if computer == "Scissors":
            print("Lose")
        if computer == "Hammer":
            print("Win!")
        if computer == "Paper":
            print("Tie")        


