# Use of this module is : Clear the Terminal

import os
os.system('cls' if os.name == 'nt' else 'clear')

# It imports random thing or number

import random

# In this list of Fruit Computer pick one Fruit of them

Option = ["Apple", "Kivi", "Mango","Orange","Grapes","Strawberry","Watermelon", "Pineapple", "Banana", "Pomigranat", "Dragon Fruit"]
 
Guess = random.choice(Option)

print("We are Playing a Game You want to Guess the fruit\nMake Sure that the First word of our fruit is Captial")

guess_no = 0

while True:

    User_Ans = input("\nGuess the fruit: ")

    guess_no += 1 
    if User_Ans == Guess:
        print(f"\nCorrect, You Guess it The fruit was {Guess} and You Take {guess_no} attempts to find the Fruit.")
        break

    else:
        print("\nIncorrect, Try again")

