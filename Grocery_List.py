# Grocery List App

import datetime

# Create the datetime object and store the current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# Welcome notice
print("Welcome to the Grocery List App.")
grocery_list = ['Meat', 'Cheese']
print("Current Date and Time: " + month + "/" + day + "\t" + hour + ":" + minute)
print("You currently have " + grocery_list[0] + " and " + grocery_list[1] + " in your list.")

# User input for grocery items
item_1 = input("\nType of food to add to the grocery list: ").title().strip()
grocery_list.append(item_1)

item_2 = input("Type of food to add to the grocery list: ").title().strip()
grocery_list.append(item_2)

item_3 = input("Type of food to add to the grocery list: ").title().strip()
grocery_list.append(item_3)

# Sort grocery list
print("\nHere is your grocery list: ")  
print(grocery_list)
print("Here is your grocery list sorted: ")
grocery_list.sort()
print(grocery_list)

#Simulate shopping
print("Simulating grocery shopping...")

#Removing first food item
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)

food_1 = input("What food did you just buy: ").title().strip()
grocery_list.remove(food_1)
print("Removing " + str(food_1) + " from the list...")

#Removing second food item
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)

food_2 = input("What food did you just buy: ").title().strip()
grocery_list.remove(food_2)

#Removing third food item
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)

food_3 = input("What food did you just buy: ").title().strip()
grocery_list.remove(food_3)

#Replacing items
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)

print("\nSorry, the store is out of " + str(grocery_list[-1]))
grocery_list.pop()
replacement_1 = input("What food would you like instead: ").title().strip()
grocery_list.insert(0, replacement_1)

print("\nHere is what remains on your grocery list: ")
print(str(grocery_list))


