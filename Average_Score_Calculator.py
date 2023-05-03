#Average Calculator App

# Welcome statement
print("Welcome to the Average Calculator App")


# User input
name = input("\nWhat is your name: ").title().strip()
num_grades = int(input("\nHow many grades would you like to enter: "))

grades = []
for i in range(num_grades):
    grade = int(input("Enter grade: "))
    grades.append(grade)

# Sort the grades highest to lowest
print("\nGrades Highest to Lowest:")
grades.sort(reverse=True)
for grade in grades:
    print("\t" + str(grade))

grades_2 = grades[:]
# Compute the average score
average = sum(grades) / len(grades)
average = round(average, 2)

# Summary Table
print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(num_grades))
print("\tHighest Grade: " + str(max(grades)))
print("\tLowest Grade: " + str(min(grades)))
print("\tAverage: " + str(average))

# User's desired average and calculating the score needed on next assignment
desired = float(input("\nWhat is your desired average: "))
needed_score = desired*(len(grades)+1) - sum(grades)
needed_score = round(needed_score, 2)
print("\nGood luck " + name + "!")
print("You will need to get a " + str(needed_score) + " on your next assignment to earn a " + str(desired) + " average.")


# Changing a grade
print("\nLet's see what your average could have been if you did better/worse on an assignment.")
grade_change = int(input("What grade would you like to change: "))
grades_2.remove(grade_change)
new_grade = int(input("What grade would you like to change " + str(grade_change) + " to: "))
grades_2.append(new_grade)

# Sort the grades highest to lowest again
print("\nNew Grades Highest to Lowest:")
grades_2.sort(reverse=True)
for grade in grades_2:
    print("\t" + str(grade))

# Compute the new average score
new_average = sum(grades_2) / len(grades_2)
new_average = round(new_average, 2)

# New Summary Table
print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(num_grades))
print("\tHighest Grade: " + str(max(grades_2)))
print("\tLowest Grade: " + str(min(grades_2)))
print("\tAverage: " + str(new_average))

# Compare new average to real average
print("\nYour new average would be " + str(new_average) + " compared to your real average of " + str(average) + "!")
print("That is a change of " + str(round(abs(new_average - average),2)) + " points!")

print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit.")

