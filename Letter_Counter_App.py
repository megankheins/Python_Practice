
print("Welcome to the Letter Counter App.")

# Get input from user.
name = input("\nWhat is your name? ").title().strip()
print("\nHello " + name + "!")

print("I am going to count the number of times that a specific letter occurs in a message.")
message = input("Please enter a message: ")
letter = input("Select the letter you would like to count from your message: ")

# Standardize to lower case.
letter = letter.lower()
message = message.lower()

# Get the count of the letters and display the amount.
letter_count = message.count(letter)
print("\nYour message has " + str(letter_count) + " " + letter + "'s in it.")
