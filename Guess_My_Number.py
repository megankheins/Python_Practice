# Guess My Number

import random

# Welcome message
print("Welcome to the Guess My Number App")

# Get user name
name = input("\nHello, what is your name? ").title().strip()
print("Well " + name + ", I am thinking of a number between 1 and 20.")

# Create random number
number = random.randint(1,20)

# Allow user to guess the random number (5 tries)
for i in range(1,6):
    guess = int(input("\nTake a guess: "))
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    elif guess == number:
        break
    else:
        print("Invalid response.")

if guess == number:
    print("\nGreat, you guessed the number in " + str(i) + " tries!")
else:
    print("\nGame over. The number I was thinking of was " + str(number) + ".")

    
