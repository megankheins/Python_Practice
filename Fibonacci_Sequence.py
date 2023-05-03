# Fibonacci Calculator

# Welcome statement

print("Welcome to the Fibonacci Calculator App.")

# User input
digits = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute: "))

# Compute the Fibonacci Sequence
print("The first 15 numbers of the Fibonacci sequence are:")

fib = [1,1]
for i in range(digits-2):
    n = fib[-2] + fib[-1]
    fib.append(n)

for num in fib:
    print(num)

# Compute the Golden Ratio    
print("\nThe corresponding Golden Ratio values are:")

golden = []
for digit in range(len(fib)-1):
    ratio = fib[digit+1] / fib[digit]
    golden.append(ratio)

for num in golden:
    print(num)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618...")
