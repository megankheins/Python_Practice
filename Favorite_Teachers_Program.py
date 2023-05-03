# Favorite Teachers Program

print("Welcome to the Favorite Teacher's Program")

fav_teachers = []

# Get users favorite teachers
fav_teachers.append(input("\nWho is your first favorite teacher: ").title().strip())
fav_teachers.append(input("Who is your second favorite teacher: ").title().strip())
fav_teachers.append(input("Who is your third favorite teacher: ").title().strip())
fav_teachers.append(input("Who is your fourth favorite teacher: ").title().strip())

# Print out summary of teachers list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetial order are: " + str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Insert a new favorite teacher to the list
fav_teachers.insert(0,input("\nOpps, " + fav_teachers[0] + " is no longer your favorite teacher. Who is your new FAVORITE teacher: ").title().strip())

# New summary of teachers list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetial order are: " + str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")

# Remove a teacher that you no longer like
fav_teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title().strip())

# New summary of teachers list
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetial order are: " + str(sorted(fav_teachers, reverse=True)))

print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.")
