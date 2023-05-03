
print("Welcome to the Multiplication/Exponent Table App.")

#Gather user input
name = input("\nHello, what is your name: ").title().strip()
number = float(input("What number would you like to work with: "))
message = name + ", Math is cool!"


#Mutiplication Table
print("\nMultiplication Table for " + str(number))
print("\n\t 1.0 * " + str(number) + " = " + str(round(1*number, 4)))
print("\t 2.0 * " + str(number) + " = " + str(round(2*number, 4)))
print("\t 3.0 * " + str(number) + " = " + str(round(3*number, 4)))
print("\t 4.0 * " + str(number) + " = " + str(round(4*number, 4)))
print("\t 5.0 * " + str(number) + " = " + str(round(5*number, 4)))
print("\t 6.0 * " + str(number) + " = " + str(round(6*number, 4)))
print("\t 7.0 * " + str(number) + " = " + str(round(7*number, 4)))
print("\t 8.0 * " + str(number) + " = " + str(round(8*number, 4)))
print("\t 9.0 * " + str(number) + " = " + str(round(9*number, 4)))

#Exponent Table
print("\nExponent Table for " + str(number))
print("\n\t" + str(number) + " ** 1 = " + str(round(number**1, 4)))
print("\t" + str(number) + " ** 2 = " + str(round(number**2, 4)))
print("\t" + str(number) + " ** 3 = " + str(round(number**3, 4)))
print("\t" + str(number) + " ** 4 = " + str(round(number**4, 4)))
print("\t" + str(number) + " ** 5 = " + str(round(number**5, 4)))
print("\t" + str(number) + " ** 6 = " + str(round(number**6, 4)))
print("\t" + str(number) + " ** 7 = " + str(round(number**7, 4)))
print("\t" + str(number) + " ** 8 = " + str(round(number**8, 4)))
print("\t" + str(number) + " ** 9 = " + str(round(number**9, 4)))

#Math is cool
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.lower())
