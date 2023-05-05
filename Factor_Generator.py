# Factor Generator

# Welcome statement
print("Welcome to the Factor Generator")

# Keep the program running while True
while True:

    # User input for number
    number = int(input("\nEnter a number to determine all factors of that number: "))

    # Initialize factors list
    factors = []

    # Find all factors in number
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)

    # Print out all factors        
    print("\nThe factors of " + str(number) + " are:")
    for number in factors:
        print(number)

    # Print a summary pf the paired factors that equal the number
    print("\nIn summary: ")
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(number))

    # User decides if they want to stop running the program
    choice = input("\nRun again (y/n): ").lower().strip()
    if choice.startswith('y') != True:
        print("\nThank you for using the Factor Generator. Have a great day.")
        break

#### Option 2 for printing summary table
###    while factors:
###        num_1 = factors[0]
###        num_2 = factors[-1]
###        print(str(num_1) + " * " + str(num_2) + " = " + str(number))
###        factors.remove(num_1)
###        if num_2 in factors:
###                factors.remove(num_2)
