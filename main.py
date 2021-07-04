import random

options = ["Rock", "Paper", "Scissors"]

class Player():
    def __init__(self,name):
        self.name = name


## Introduction ##
print("Welcome to: Rock, Paper, Scissors")

## Generating Players ##
comp = Player("Computer")
name = input("What is your name? ")
player = Player(name)

## GAMEPLAY ##
print("The game is starting")
print("Rock, Paper, Scissors shoot!")

random.shuffle(options)
comp_choice = options[0]

random.shuffle(options)
player_choice = options[0]

print("The computer chose: {}".format(comp_choice))
print("{a} chose: {b}".format(a=name,b=player_choice))

## Deciding Who Wins ##
if comp_choice == "Rock" and player_choice == "Scissors":
    print("Computer wins!")
else:
    if comp_choice == "Scissors" and player_choice == "Rock":
        print("{} wins!".format(name))

if comp_choice == "Rock" and player_choice == "Paper":
    print("{} wins!".format(name))
else:
    if comp_choice == "Paper" and player_choice == "Rock":
        print("Computer wins!")

if comp_choice == "Scissors" and player_choice == "Paper":
    print("Computer wins!")
else:
    if comp_choice == "Paper" and player_choice == "Scissors":
        print("{} wins!".format(name))

if comp_choice == player_choice:
    print("We have a draw!")