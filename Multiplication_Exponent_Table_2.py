

print("Welcome to the Multiplication/Exponent Table App.")

#Gather user input
name = input("\nHello, what is your name: ").title().strip()
number = float(input("What number would you like to work with: "))
message = name + ", Math is cool!"

# Multiplication Table
print("\nMultiplication Table for " + str(number))
print()

for x in range(1,10):
    print("\t" + str(x) + " * " + str(number) + " = " + str(round(x*number, 4)))

#Exponent Table
print("\nExponent Table for " + str(number))
print()

for x in range(1,10):
    print("\t" + str(number) + " ** " + str(x) + " = " + str(round(number**x, 4)))
