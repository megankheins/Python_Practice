# Frequency Analysis Program

from collections import Counter

# Welcome statement
print("Welcome to the Frequency Analysis Program")

# List of non-letters to remove from phrase
non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',',','.','!','?','"',"'",'^',':',';','(',')','%','[',']','$','#','&','*','-','/','\n','\t','@','~','<','>','+','=']

# Get first phrase from user
phrase_1 = input("\nEnter a word or phrase to count the occurance of each letter: ").lower().strip()

# Remove all non_letters
for item in non_letters:
    phrase_1 = phrase_1.replace(item, '')

# Total occurances of letters in the phrase
total_letters = len(phrase_1)

# Tally the number of each letter with a counter object
letters_count = Counter(phrase_1)

# Determine and print the frequency analysis of the phrase
print("\nHere is the frequency analysis from key phrase 1:")
print("\n\tLetter\t\tOccurence\tPercentage")
for key, value in sorted(letters_count.items()):
    percent = round(100*(value/total_letters),2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percent) + "%")

# Order the elements by from most common letter to least common
ordered_count = letters_count.most_common()
phrase_1_ordered = []

# Add the letters to a list in order of most to least common
for pair in ordered_count:
  phrase_1_ordered.append(pair[0])

# Print the ordered list of phrase 1 letters
print("\nLetters ordered from highest to lowest occurence:")
for letter in phrase_1_ordered:
    print(letter,end = '')



# Get second phrase from user
phrase_2 = input("\n\nEnter a word or phrase to count the occurance of each letter: ").lower().strip()

# Remove all non_letters
for item in non_letters:
    phrase_2 = phrase_2.replace(item, '')

# Total occurances of letters in the phrase
total_letters = len(phrase_2)

# Tally the number of each letter with a counter object
letters_count = Counter(phrase_2)

# Determine and print the frequency analysis of the phrase
print("\nHere is the frequency analysis from key phrase 2:")
print("\n\tLetter\t\tOccurence\tPercentage")
for key, value in sorted(letters_count.items()):
    percent = round(100*(value/total_letters),2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percent) + "%")

# Order the elements by from most common letter to least common
ordered_count = letters_count.most_common()
phrase_2_ordered = []

# Add the letters to a list in order of most to least common
for pair in ordered_count:
  phrase_2_ordered.append(pair[0])

# Print the ordered list of phrase 1 letters
print("\nLetters ordered from highest to lowest occurence:")
for letter in phrase_2_ordered:
    print(letter,end = '')

