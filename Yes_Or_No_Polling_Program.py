# Yes or No Issue Polling Program

# Welcome message
print("Welcome to the Yes or No Issue Polling Program")

# User input
issue = input("\nWhat is the yes or no issue you will be voting on today: ")
num_voters = int(input("What is the number of voters you will allow to vote: "))
admin_password = input("Enter a password for polling results: ")

# Initialize variables
voting_results = {}
yes = 0
no = 0

# Collect each voters information
for voters in range(num_voters):
    name = input("\nEnter your full name: ").title().strip()

    # Make sure that the person has not already voted
    if name not in voting_results.keys():
        print("Here is our issue: " + issue)
        vote = input("What do you think...yes or no: ").lower().strip()
        if vote == 'yes'or vote == 'y':
            yes += 1
        elif vote == 'no' or vote == 'n':
            no += 1
        else:
            print("Invalid answer. Your vote will not count.")

        # Add vote to the voting results dictionary
        voting_results[name] = vote
        print("Thank you " + name + "! Your vote of " + vote + " has been recorded.")
        

    # Person has already voted with this name
    else:
        print("Sorry, a voter with the name " + name + " has already voted.")

# Print the number of people who voted and their names
print("\nThe following " + str(len(voting_results)) + " people voted:")
for key in voting_results.keys():
    print(key)

# Print the winning issue
print("\nOn the following issue: " + issue)
if yes > no:
    print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
    print("No wins." + str(no) + " votes to " + str(yes) + ".")
else:
    print("It was a tie.")

# Request admin password to view the detailed results
password = input("\nTo see the voting results enter the admin password: ")
if password == admin_password:
    for key,value in voting_results.items():
        print("Voter: " + key + "\t\tVote: " + value)
else:
    print("\nPassword incorrect. You cannot view the voter polling information.")

# Closing statement
print("\nThank you for using the Yes or No Issue Polling Program.")
