# Power-Ball Simulator

import random

# Introduction
print("------------------Power-Ball Simulator------------------")

# User selects how many balls they want to use in Powerball
white = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if white <5:
    white = 5
red = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))
if red < 1:
    red = 1

# Calculate the odds of winning
odds = 1
for i in range(5):
    odds *= (white - i)
odds *= (red/120)
print("You have a 1 in " + str(odds) + " chance of winning this lottery.")

# User can purchase tickets in intervals
interval = int(input("\nPurchase tickets in what interval: "))

# Power-Ball Welcome Statement
print("\n----------Welcome to the Power-Ball----------")

# Create the winning lottery ticket
winning_nums = []
while len(winning_nums) < 5:
    num = random.randint(1,white)
    if num not in winning_nums:
        winning_nums.append(num)
winning_nums.sort()
powerball = random.randint(1, red)
winning_nums.append(powerball)

# Print the winning ticket
print("\nTonight's winning numbers are: ", end = '')
for num in winning_nums:
    print(num, end = ' ')
input("\nPress 'Enter' to begin purchasing tickets!!!")

# Initialize variables
total_tickets = 0
tickets = []
playing = True

# Keep playing while the user hasn't won or until they quit
while playing == True and winning_nums not in tickets:
    ticket = []

    # Get white balls for ticket
    while len(ticket) < 5:
        num = random.randint(1,white)
        if num not in ticket:
            ticket.append(num)
    ticket.sort()

    # Get red ball for ticket
    red_ball = random.randint(1, red)
    ticket.append(red_ball)

    # Check if ticket has already been sold
    if ticket not in tickets:
        tickets.append(ticket)
        print(ticket)
        total_tickets += 1
    else:
        print("Generated a losing ticket ... disregard")

    # User decides if they want to stop running the program after the interval
    if total_tickets % interval == 0:
        print("\n" + str(total_tickets) + " tickets purchased so far with no winners...")
        choice = input("\nKeep purchasing tickets (y/n): ").lower().strip()
        if choice.startswith('y') != True:
            playing = False

# Lottery ended
if ticket == winning_nums:
    print("\nYou won the lottery!")
    print("Winning ticket numbers: ", end = '')
    for num in ticket:
        print(num, end = ' ')
    print("\nYou bought a total of " + str(total_tickets) + " tickets.")
else:
    print("\nYou bought " + str(total_tickets) + " tickets and still lost.")
    print("Better luck next time.")


    
        



