
print("Welcome to the MPH to MPS Conversion App.")

# User input.
mph_speed = float(input("\nWhat is your speed in miles per hour: "))

#Convert to meters per second.
mps_speed = round(0.44704 * mph_speed, 2)

# Print the result.
print("Your speed in meters per second is " + str(mps_speed) + ".")
