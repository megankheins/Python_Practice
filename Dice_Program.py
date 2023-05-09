# Python Dice Program

import random


def dice_sides():
    """Ask the user how many sides they want on their die"""
    sides = int(input("\nHow many sides would you like on your dice: "))
    return sides
    

def dice_num():
    """Ask the user how many dice they want to roll"""
    rolls = int(input("How many dice would you like to roll: "))
    return rolls


def roll_dice(sides, dice):
    """Simulate the user rolling the dice"""
    print("\nYou rolled " + str(num_dice) + " " + str(num_sides) + " sided dice.")
    print("\n-----Results are as follows-----")
    rolls = []
    for i in range(dice):
        roll = random.randint(1, sides)
        print("\t" + str(roll))
        rolls.append(roll)
    return rolls


def sum_dice(total_rolls):
    """Calculate the total value of all of the rolled dice"""
    total = 0
    for i in total_rolls:
        total += i
    print("The total value of your roll is " + str(total) + ".")


def roll_again():
    """Ask the user if they want to roll again"""
    choice = input("\n\nWould you like to roll again (y/n): ").lower().strip()
    if choice.startswith('y') != True:
        playing = False
    else:
        playing = True
    return playing


# The main code
        
# Welcome Statement
print("Welcome to the Python Dice Program")

# User can decide how long they want to keep playing
rolling = True
while rolling:

    # Get values for number of sides and number of dice from user
    num_sides = dice_sides()
    num_dice = dice_num()

    # Roll the dice
    dice_rolls = roll_dice(num_sides, num_dice)

    # Sum the total value of all rolls
    sum_dice(dice_rolls)

    # Roll again
    rolling = roll_again()


print("\nThank you for using the Python Dice Program.")
