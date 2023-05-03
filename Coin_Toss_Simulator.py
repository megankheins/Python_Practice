# Coin Toss Simulator

import random

# Welcome Statement
print("Welcome to the Coin Toss Simulator")

# User input
print("\nI will flip a coin a set number of times.")
flips = int(input("How many times would you like me to flip the coin: "))
results = input("Would you like to see the results of each flip (y/n): ").lower().strip()

# Initializing the variables
heads = 0
tails = 0

# Simulate flipping a coin
for i in range(flips):
    x = random.randint(1, 2)
    if x == 1:
        heads += 1
        if results.startswith('y'):
            print('HEADS')
    else:
        tails += 1
        if results.startswith('y'):
            print('TAILS')
            
    if heads == tails:
        print("At " + str(heads + tails) + " flips, the number of heads and tails were equal at " + str(heads) + " each.")

# Results for percent of heads/tails
heads_percent = round((heads/flips)*100, 2)
tails_percent = round((tails/flips)*100, 2)

# Display the results
print("\nResults of Flipping A Coin " + str(flips) + " Times: ")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t" + str(heads) + "/" + str(flips) + "\t\t" + str(heads_percent) + "%" )
print("Tails\t\t" + str(tails) + "/" + str(flips) + "\t\t" + str(tails_percent) + "%" )
