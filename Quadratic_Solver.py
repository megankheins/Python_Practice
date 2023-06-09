# Quadratic Solver App

# Welcome message

import cmath

print("Welcome to the Quadratic Solver App")

print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

# Get user input
equations = int(input("\nHow many equations would you like to solve today: "))

# Loop and solve the equations
for i in range(1, equations + 1):
    print("\nSolving equation #" + str(i))
    print("----------------------------------------------------------------")
    
    a = float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    
    print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:")
    x1 = (-b + cmath.sqrt(b**2 - (4*a*c))) / (2*a)
    x2 = (-b - cmath.sqrt(b**2 - (4*a*c))) / (2*a)
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))


print("\nThank you for using the Quadratic Solver App. Goodbye.")



