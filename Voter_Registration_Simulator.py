# Voter Registration Simulator

# Welcome message
print("Welcome to the Voter Registration App")

# User input
name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

# List of party options
parties = ["Democratic", "Republican", "Independent", "Libertarian", "Green"]

# If statement based on users age
if age >= 18:
    print("\nCongrats " + str(name) + "! You are old enough to register to vote.")

    # Display the political parties
    print("\nHere are a list of political parties to join.")
    for party in parties:
        print("\t- " + party)

    # User decides the party they want to join
    party = input("\nWhat party would you like to join: ").title().strip()

    # Output based on the user's selection
    if party in parties:
        print("\nCongrats " + str(name) + "! You have joined the " + party + " party!")
        if party == "Democratic" or party == "Republican":
            print("That is a major party.")
        elif party == "Independent":
            print("You are an independent person.")
        else:
            print("That is not a major party.")
    else:
        print("That party is not in the available options.")
        
# Not old enough to vote
else:
    print("\nSorry, you are not old enough to register to vote.")
