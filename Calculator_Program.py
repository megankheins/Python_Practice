# Python Calculator Program

def add(num_1, num_2):
    """Add two numbers and result the sum"""
    value = round(num_1 + num_2, 4)
    print("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(value) + ".")
    return str(num_1) + " + " + str(num_2) + " = " + str(value)


def subtract(num_1, num_2):
    """Subtract two numbers and return the difference"""
    value = round(num_1 - num_2, 4)
    print("The difference of " + str(num_1) + " and " + str(num_2) + " is " + str(value) + ".")
    return str(num_1) + " - " + str(num_2) + " = " + str(value)


def multiply(num_1, num_2):
    """Multiply two numbers and return the product"""
    value = round(num_1 * num_2, 4)
    print("The product of " + str(num_1) + " and " + str(num_2) + " is " + str(value) + ".")
    return str(num_1) + " * " + str(num_2) + " = " + str(value)


def divide(num_1, num_2):
    """Divide two numbers and return the quotient"""
    # Denominator is not zero
    if num_2 != 0:
        value = round(num_1 / num_2, 4)
        print("The quotient of " + str(num_1) + " and " + str(num_2) + " is " + str(value) + ".")
        return str(num_1) + " / " + str(num_2) + " = " + str(value)
    # Denominator is zero, cannot divide by zero
    else:
        print("You cannot divide by zero.")
        return "DIV ERROR"


def exponent(num_1, num_2):
    """Take a number to the power of another number and return the result"""
    value = round(num_1 ** num_2, 4)
    print("The result of " + str(num_1) + " raised to the " + str(num_2) + " power is " + str(value) + ".")
    return str(num_1) + " ** " + str(num_2) + " = " + str(value)


def run_again():
    """Ask the user if they want to roll again"""
    choice = input("\nWould you like to roll again (y/n): ").lower().strip()
    if choice.startswith('y') != True:
        running = False
    else:
        running = True
    return running


# The main code

# Welcome message
print("Welcome to the Python Calculator Program")
print("Enter two numbers and an operation and the desired operation will be performed.")

# Initialize summary list
summary = []

# Run the program until the user decides not to
running = True
while running:

    # User input
    number_1 = float(input("\nEnter a number: "))
    number_2 = float(input("Enter a number: "))
    operator = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower().strip()

    # Run the appropriate function based on what the user chooses
    if operator == 'addition' or operator == 'a':
        result = add(number_1, number_2)
    elif operator == 'subtraction' or operator == 's':
        result = subtract(number_1, number_2)
    elif operator == 'multiplication' or operator == 'm':
        result = multiply(number_1, number_2)
    elif operator == 'division' or operator == 'd':
        result = divide(number_1, number_2)
    elif operator == 'exponentiation' or operator == 'e':
        result = exponent(number_1, number_2)
    else:
        print("Invalid operation. Try again.")
        result = "OPP ERROR"

    # Add result to the sumary list
    summary.append(result)

    # Allow the user to decide if they want to run again
    running = run_again()

# Display summary
print("\nCalculation Summary:")
for result in summary:
    print(result)
print("\nThank you for running the Caluclator Program.")
