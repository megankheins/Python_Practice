# Code Breakers Program

from collections import Counter

# Welcome statement
print("Welcome to the Code Breakers Program")

# List of non-letters to remove from phrase
non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',',','.','!','?','"',"'",'^',':',';',
               '(',')','%','[',']','$','#','&','*','-','/','\n','\t','@','~','<','>','+','=']

# Hard code a pre-determined key phrase 1
phrase_1 = """
Nearly ten years had passed since the Dursleys had woken up to find their nephew on the front
step, but Privet Drive had hardly changed at all. The sun rose on the same tidy front gardens
and lit up the brass number four on the Dursleys' front door; it crept into their living room,
which was almost exactly the same as it had been on the night when Mr. Dursley had seen that
fateful news report about the owls. Only the photographs on the mantelpiece really showed how
much time had quickly zoomed passed. Ten years ago, there had been lots of pictures of what looked like
a large pink beach ball wearing different-colored bonnets - but Dudley Dursley was no longer a
baby, and now the photographs showed a large blond boy riding his first bicycle, on a carousel
at the fair, playing a computer game with his father, being hugged and kissed by his mother.
The room held no sign at all that another boy lived in the house, too. Yet Harry Potter was
still there, asleep at the moment, but not for long. His Aunt Petunia was awake and it was her
shrill voice that made the first noise of the day. "Up! Get up! Now!" Harry woke with a jump.
His aunt rapped on the door again. "Up!" she screeched. Harry heard her walking toward the kitchen
and then the sound of the frying pan being put on the stove. He rolled onto his back and tried to
remember the dream he had just been having. It had been a good one. There had been a flying
motorcycle in it. He had a funny feeling he'd had the same dream before. His aunt was back outside
the door. "Are you up yet?" she demanded. "Nearly," said Harry. "Well, get a move on, I want you
to look after the bacon. And don't you dare let it burn, I want everything perfect on Duddy's birthday."
"""
phrase_1 = phrase_1.lower().strip()

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


# Hard code a pre-determined key phrase 2
phrase_2 = """
The bang was like a cannon blast, and the golden flames that erupted between them, at the dead
center of the circle they had been treading, marked the point where the spells collided. Harry saw
Voldemorts green jet meet his own spell, saw the Elder Wand fly high, dark against the sunrise,
spinning across the enchanted ceiling like the head of Nagini , spinning through the air toward the
master it would not kill, who had come to take full possession of it at last. And Harry, with the
unerring skill of a Seeker, caught the wand in his free hand as Voldemort fell backward, arms
splayed, the slit pupils of the scarlet eyes rolling upward. Tom Riddle hit the floor with a mundane
finality, his body feeble and shrunken, the white hands empty, the snakelike face vacant and
unknowing. Voldemort was dead, killed by his own rebounding curse, and Harry stood with two
wands in his hands, staring down at his enemys shell. 
One shivering second of silence, the shock of the moment suspends: and then the tumult broke
around Harry as the screams and the cheers and the roars of the watchers rent the air. The fierce
new sun dazzled the windows as they thundered toward him, and the first to reach him were Ron
and Hermione, and it was their arms that were wrapped around him, their incomprehensible shouts
that deafened him. Then Ginny, Neville, and Luna were there, and then all the Weasleys and Hagrid,
and Kingsley and McGonagall and Flitwick and Spout, and Harry could not hear a word that anyone
was shouting, nor tell whose hands were seizing him, pulling him, trying to hug some part of him,
hundreds of them pressing in, all of them determined to touch the Boy Who Lived, the reason it was
over at last
The sun rose steadily over Hogwarts, and the Great Hall blazed with life and light. Harry was an
indispensable part of the mingled outpourings and expressions of jubilation and mourning, of grief and celebration.
They wanted him there with them, their leader and symbol, their savior and their guide, and that he
had not slept, that he craved the company of only a few of them, seemed to occur to on one. He
must speak to the bereaved, clap their hands, witness their tears, receive their thanks, hear the new
now creeping in from every quarter as the morning drew on; that the Imperiused up and down the
country had come back to themselves, that Death Eaters were fleeing or else being captured, that
the innocent of Azkaban were being released at that very moment, and that Kingsley Shacklebolt
had been named temporary Minister of Magic.
"""
phrase_2 = phrase_2.lower().strip()

# Remove all non_letters
for item in non_letters:
    phrase_2 = phrase_2.replace(item, '')

# Total occurances of letters in the phrase
total_letters = len(phrase_2)

# Tally the number of each letter with a counter object
letters_count = Counter(phrase_2)

# Determine and print the frequency analysis of the phrase
print("\n\nHere is the frequency analysis from key phrase 2:")
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


# ENCODING OR DECODING

# User input for phrase
decision = input("\n\nWould you like to encode or decode a message: ").lower().strip()
phrase = input("What is the phrase: ").lower().strip()

# Removing non-letters from the phrase
for item in non_letters:
    phrase = phrase.replace(item, '')

# User chose to encode a message
if decision == 'encode':
    encoded_phrase = []
    for letter in phrase:
        index = phrase_1_ordered.index(letter)
        encoded_phrase.append(phrase_2_ordered[index])
    print("\nThe encoded message is: ")
    for letter in encoded_phrase:
        print(letter, end = '')

# User chose to decode a message
elif decision == 'decode':
    decoded_phrase = []
    for letter in phrase:
        index = phrase_2_ordered.index(letter)
        decoded_phrase.append(phrase_1_ordered[index])
    print("\nThe decoded message is: ")
    for letter in decoded_phrase:
        print(letter, end = '')

# Invalid option entered
else:
    print("\nInvalid response. Please enter either 'encode' or 'decode'.")


