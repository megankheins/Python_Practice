# Even Odd Number Sorter

# Welcome Statement
print("Welcome to the Even Odd Number Sorter")


running = True

while running:
    # User input
    numbers = input("\nEnter a string of numbers separated by a comma (,): ")

    # Remove the white spaces
    numbers = numbers.replace(' ', '')

    # Use the split method to add the values to a list
    numbers = numbers.split(sep = ",")

    # Initialize lists for even and odd numbers
    evens = []
    odds = []

    # Print out if the value is even or odd
    print("\n---- Result Summary ----")
    for value in numbers:
        value = int(value)
        if value % 2 == 0:
            evens.append(value)
            print("\t" + str(value) + " is even!")
        else:
            odds.append(value)
            print("\t" + str(value) + " is odd!")

    # Sort lowest to highest
    evens.sort()
    odds.sort()

    # Print the even values
    print("\nThe following " + str(len(evens)) + " numbers are even:")
    for value in evens:
        print("\t" + str(value))

    # Print the odds values
    print("\nThe following " + str(len(odds)) + " numbers are odd:")
    for value in odds:
        print("\t" + str(value))

    # Break out of the loop whenever the user chooses
    choice = input("\nWould you like to run the program again (y/n): ").lower().strip()
    if choice == 'n':
        print("\nThank you for using this number sorter. Goodbye.")
        running = False
