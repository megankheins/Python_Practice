# Thesaurus Program

import random

# Welcome Statement
print("Welcome to the Thesaurus Program")
print("\nChoose a word from the thesaurus and I will give you a synonym.")

# Build the dictionary for the thesaurus of random words
thesaurus = {
    'smart': ['brilliant', 'astute', 'bright', 'sharp', 'wise'],
    'happy': ['pleased', 'joyful', 'content', 'cheerful', 'delighted'],
    'cold': ['frigid', 'wintry', 'brisk', 'crisp', 'cool'],
    'sad': ['somber', 'sorrowful', 'blue', 'melancholy', 'dismal'],
    }

# Print the words in the thesaurus
print("\nHere are the words in the thesaurus:")
for key in thesaurus.keys():
    print("\t-" + key)

# Allow the user to choose a word from the thesaurus
word = input("\nWhat word would you like a synonym for: ").lower().strip()

# Select a random synonym from the dictionary
if word in thesaurus.keys():
    random_index = random.randint(0,4)
    synonym = thesaurus[word][random_index]
    print("A synonym for " + word + " is " + synonym + ".")
else:
    print("That word is not currently available in this thesaurus.")

# User decides if they want to see the whole thesaurus
whole_thesaurus = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()

# Nested for loop to print out the whole thesaurus
if whole_thesaurus.startswith('y'):
    for key, values in thesaurus.items():
        print("\n" + key.title() + " synonyms are:")
        for value in values:
            print("\t-" + value)

# User did not want to see the whole thesaurus
else:
    print("\nGreat. I hope you enjoyed this program.")
