# Factorial Calculaor App

import math

# Welcome message
print("Welcome to the Factorial Calculator App")


# User input
num = int(input("\nWhat number would you like to compute the factorial of? "))

# String for what factorial we are calculating
print("\n" + str(num) + "! = ", end = '')
for i in range(1, num):
    print(str(i), end = "*")
print(str(num))

# Another option for how to print the factorial string from above
###fact_string = str(num) + "! = 1"
###for i in range(2, num + 1):
###    fact_string = fact_string + "*" + str(i)
###print(fact_string)

# Factorial calculation using math library
print("\nHere is the result from the math library:")
fact = math.factorial(num)
print("The factorial of " + str(num) + " is " + str(fact) + ".")

# Factorial calculation using my own algorithm
print("\nHere is the result from my own algorithm:")
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of " + str(num) + " is " + str(factorial) + ".")

# Closing statement
print("\nIt is shown twice that " + str(num) + "! = " + str(fact))
print("This confirms that my own algorithm matches the solution of the python math library :)")
    
