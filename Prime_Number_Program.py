# Prime Number Program

import time

# Welcome Statement
print("Welcome to the Prime Number Program")

# Run the program as long as the flag variable running is True
running = True
while running:

    # User input
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = int(input("Enter 1 or 2: "))

    # User chose to calculate a specific prime number
    if choice == 1:
        number = int(input("\nEnter a number to determine if it is prime or not: "))
        flag = True
        for i in range(2,number):
            if (number % i) == 0:
                flag = False
                break

        # Display if the number is prime or not
        if flag:
            print(str(number) + " is a prime!") 
        else:
            print(str(number) + " is a not prime!")

    # User chose to see all the prime numbers within a range
    elif choice == 2:
        lower = int(input("\nEnter the lower bound of your range: "))
        upper = int(input("Enter the upper bound of your range: "))

        # Initialize a list for prime numbers
        primes = []

        # Store the current time
        start = time.time()
        
        for number in range(lower, upper+1):
            flag = True
            if number == 1:
                flag = False
            else:
                for i in range(2, number):
                    if (number % i) == 0:
                        flag = False
                        break
            if flag:
                primes.append(number)

        # Store the current time again after the program runs
        end = time.time()

        # Determine the total time it took to run
        time = round(end - start, 4)

        # Print a summary of time it took and prime numbers
        print("\nCalculations took a total of " + str(time) + " seconds.")  
        print("\nThe following numbers between " + str(lower) + " and " + str(upper) + " are prime.")
        enter = input("Press enter to continue.")
        for number in primes:
            print(number)
            
    # User chose an invalid option              
    else:
        print("\nThat is not a valid option. Try again.")

    # User decides if they want to keep running the program
    control = input("\nWould you like to run the program again (y/n): ").lower().strip()
    if control.startswith('y') != True:
        running = False
        print("\nThank you for running the Prime Number Program.")
        

