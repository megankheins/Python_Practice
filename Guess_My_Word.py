# Guess My Word Program

import random

# Welcome statement
print("Welcome to the Guess My Word Program")

# Program runs while the flag variable is True

# Categories of words
category_dict = {
'sports': ['soccer', 'football', 'volleyball', 'hockey', 'baseball', 'curling'],
'fruits': ['apple', 'banana', 'mango', 'strawberry', 'lemon', 'watermelon'],
'clothing': ['pants', 'shirt', 'sweater', 'socks', 'shoes', 'sweatshirt'],
'vegetables': ['carrot', 'broccoli', 'asparagus', 'celery', 'cauliflower', 'peas'],
'colors': ['blue', 'red', 'periwinkle', 'orange', 'yellow', 'violet']
}

# Create a list of categories
categories = []
for key in category_dict.keys():
    categories.append(key)

# Allow the user to continue playing while running
playing = True
while playing:

    # Get a random category
    int_1 = random.randint(0,len(categories)-1)
    category = categories[int_1]

    # Get a random word from the category
    int_2 = random.randint(0,len(category_dict[category])-1)
    word = category_dict[category][int_2]

    # Print out the category and the amount of letters in the word
    print("\nGuess a " + str(len(word)) + " letter word from the following category: " + category.title())
    blank_word = []
    for i in word:
        blank_word.append('-')

    # Initialize variables for guess and amount of guesses
    guess = ''
    guesses = 0

    # Loop through and allow the user to guess while the guess is incorrect
    while guess != word:
        print("".join(blank_word))
        guess = input("\nEnter your guess: ").lower().strip()
        guesses += 1

        # Check if the guess is correct
        if guess == word:
            print("\nCorrect! You guessed the word in " + str(guesses) + " guesses.")
            break

        # Guess is incorrect
        else:
            print("\nThat is incorrect. Let us reveal a letter to help you!")
            need_help = True
            while need_help:
                digit = random.randint(0, len(word)-1)
                if blank_word[digit] == '-':
                    blank_word[digit] = word[digit]
                    need_help = False
                               
    
    # User decides if they want to keep running the program
    control = input("\n\nWould you like to run the program again (y/n): ").lower().strip()
    if control.startswith('y') != True:
        playing = False
        print("\nThank you for playing Guess My Word.")
        


