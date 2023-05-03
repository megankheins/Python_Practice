

print("\t\tSummary Table")

#Defining our lists
num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Strings
print("\nThe variable num_strings is a " + str(type(num_strings)))
print("It contains the elements: " + str(num_strings))
print("The element " + num_strings[0] + " is a " + str(type(num_strings[0])))

#Integers
print("\nThe variable num_ints is a " + str(type(num_ints)))
print("It contains the elements: " + str(num_ints))
print("The element " + str(num_ints[0]) + " is a " + str(type(num_ints[0])))

#Floats
print("\nThe variable num_floats is a " + str(type(num_floats)))
print("It contains the elements: " + str(num_floats))
print("The element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])))

#Lists
print("\nThe variable num_lists is a " + str(type(num_lists)))
print("It contains the elements: " + str(num_lists))
print("The element " + str(num_lists[0]) + " is a " + str(type(num_lists[0])))

#Sorting different types of lists
print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: " + str(sorted(num_strings)))
print("Sorted num_ints: " + str(sorted(num_ints)))

print("Strings are sorted alphabetically while integers are sorted numerically!")
