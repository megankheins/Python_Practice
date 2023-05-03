

print("Welcome to the Grade Sorter App.")

#Initialize list and get user input
grades = []

grade_1 = grades.append(int(input("\nWhat is your first grade (0-100): ")))
grade_2 = grades.append(int(input("What is your second grade (0-100): ")))
grade_3 = grades.append(int(input("What is your third grade (0-100): ")))
grade_4 = grades.append(int(input("What is your forth grade (0-100): ")))

print("\nYour grades are: " + str(grades))

# Sort from highest to lowest grade
grades.sort(reverse = True)

print("\nYour grades from highest to lowest are: " + str(grades))

#Drop the two lowest grades
print("\nYour lowest two grades will now be dropped.")
removed_grade_1 = grades.pop()
print("Removed grade: " + str(removed_grade_1))
removed_grade_2 = grades.pop()
print("Removed grade: " + str(removed_grade_2))

#Print the remaining grades and the highest grade
print("\nYour remaining grades are: " + str(grades))
print("Nice work! Your highest grade is a " + str(grades[0]) + ".")
