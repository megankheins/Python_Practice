# Bianary/Hexidecimal Converter App

# Welcome Message
print("Welcome to the Binary/Hexidecimal Converter App")

# Get user input
number = int(input("\nCompute binary and hexidecimal values up to the following decimal number: "))
full_nums = range(1, number + 1)

print("Generating lists....complete!")

print("\nUsing slices, we will not show a portion of each list.")
start = int(input("What decimal would you like to start at: "))
stop = int(input("What decimal would you like to stop at: ")) + 1
nums = list(range(start, stop))
binary_num = []
hex_num = []

print("\nDecimal values from " + str(start) + " to " + str(stop - 1) + ":")
for i in nums:
    print(i)


print("\nBinary values from " + str(start) + " to " + str(stop - 1) + ":")
for i in nums:
    binary_num.append(bin(i))
    print(bin(i))


print("\nHexidecimal values from " + str(start) + " to " + str(stop - 1) + ":")
for i in nums:
    hex_num.append(hex(i))
    print(hex(i))


full_list = input("\nPress Enter to see all values from 1 to " + str(number) + ".")
print("Decimal----Binary----Hexidecimal")
print("-------------------------------------------------------------")
for i in full_nums:
    print(str(i) + "----" + str(bin(i)) + "----" + str(hex(i)))
