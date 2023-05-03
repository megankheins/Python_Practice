# Basketball Roster Program

# Welcome message
print("Welcome to the Basketball Roster Program")

roster = []

# Building roster from user input
player = input("\nWho is your point guard: ").title().strip()
roster.append(player)
player = input("Who is your shooting guard: ").title().strip()
roster.append(player)
player = input("Who is your small forward: ").title().strip()
roster.append(player)
player = input("Who is your power forward: ").title().strip()
roster.append(player)
player = input("Who is your center: ").title().strip()
roster.append(player)

# Print the starting line up
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard: " + "\t\t" + roster[0])
print("\t\tShooting Guard: " + "\t" + roster[1])
print("\t\tSmall Forward :" + "\t\t" + roster[2])
print("\t\tPower Forward: " + "\t\t" + roster[3])
print("\t\tCenter: " + "\t\t" + roster[4])

# Small forward gets injured
injured = roster.pop(2)
print("\nOh no, " + injured + " is injured.")
print("Your roster only has " + str(len(roster)) + " players.")

# Replace the injured player with new player
new_player = input("Who will take " + injured + "'s spot: ").title().strip()
roster.insert(2, new_player)


# Print the new starting line up
print("\n\tYour new starting 5 for the upcoming basketball season")
print("\t\tPoint Guard: " + "\t\t" + roster[0])
print("\t\tShooting Guard: " + "\t" + roster[1])
print("\t\tSmall Forward :" + "\t\t" + roster[2])
print("\t\tPower Forward: " + "\t\t" + roster[3])
print("\t\tCenter: " + "\t\t" + roster[4])

#Wish the new player good luck
print("\nGood luck " + roster[2] + " you will do amazing!")
print("Your roster now has " + str(len(roster)) + " players.")
