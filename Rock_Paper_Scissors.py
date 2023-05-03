# Rock, Paper, Scissors

import random

# Welcome message
print("Welcome to a game of Rock, Paper, Scissors")

# User input
name = input("\nWhat is your name: ").title().strip()
rounds = int(input("How many rounds would you like to play: "))

# Initialize wins and move options
player_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

# Create a for loops for the desired number of rounds
for i in range(rounds):
    print("\nRound " + str(i+1))
    print(name + ": " + str(player_wins) + "\tComputer: " + str(computer_wins))

    # Player input for pick and computer random pick
    player_pick = input("Time to pick...rock, paper, scissors: ").lower().strip()
    computer_index = random.randint(0,2)
    computer_pick = options[computer_index]

    # Print out picks
    if player_pick in options:
        print("\tComputer: " + computer_pick)
        print("\t" + name + ": " + player_pick)

        # All of the potential plays
        if computer_pick == player_pick:
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif computer_pick == 'rock' and player_pick == 'scissors':
            winner = 'computer'
            phrase = 'Rock smashes scissors!'
        elif computer_pick == 'paper' and player_pick == 'rock':
            winner = 'computer'
            phrase = 'Paper covers rock!'
        elif computer_pick == 'scissors' and player_pick == 'paper':
            winner = 'computer'
            phrase = 'Scissors cut paper!'
        elif player_pick == 'rock' and computer_pick == 'scissors':
            winner = name
            phrase = 'Rock smashes scissors!'
        elif player_pick == 'paper' and computer_pick == 'rock':
            winner = name
            phrase = 'Paper covers rock!'
        elif player_pick == 'scissors' and computer_pick == 'paper':
            winner = name
            phrase = 'Scissors cut paper!'
        else:
            print("Round winner unable to be calculated.")
            winner = 'tie'
            phrase = 'It is a tie, how boring!'

        # Display the results
        print("\t" + phrase)
        if winner == name:
            player_wins += 1
            print("\t" + name + " wins round " + str(i+1) + ".")
        elif winner == 'computer':
            computer_wins += 1
            print("\tComputer wins round " + str(i+1) + ".")
        else:
            print("\tThis round is a tie.")          

    # Player move was not valid
    else:
        print("That is not a valid game option!")
        print("Computer gets the point.")
        computer_wins += 1

# Print the final game results
print("\nFinal Game Results")
print("\tRounds Played: " + str(rounds))
print("\t" + name + "'s Score: " + str(player_wins))
print("\tComputer's Score: " + str(computer_wins))

# Determine the player with more wins
if player_wins > computer_wins:
    print("\tWinner: " + name + "!")
    print("\nGreat win!")
elif computer_wins > player_wins:
    print("\tWinner: Computer")
    print("\nDo better next time ... you can't let a computer beat you.")
else:
    print("\nIt was a tie. Seems boring...you should play again.")
    
    
