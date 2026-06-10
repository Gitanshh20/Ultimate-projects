import random

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Rock-Paper-Scissor Game\n")

choices = ["rock", "paper", "scissors"]

Computer_choice  = random.choice(choices)


def Com_Vs_User():
    
    User = input("Enter Your Choice rock, paper or scissors: ")

    if User == Computer_choice:
        print("Nope, That was Tie..")

    elif (User == "rock" and Computer_choice == "scissors") or \
    (User == "paper" and Computer_choice == "rock") or \
    (User == "scissors" and Computer_choice == "paper"):
        print(f"You win!,\nComputer Choice is {Computer_choice}")

    elif User != ("rock", "paper", "scissors"):
        print("Something went Worng!!")

    else:
        print(f"Computer wins,\nIt's choose {Computer_choice}")


Com_Vs_User()
