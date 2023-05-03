
print("Welcome to the Temperature Conversion Program.")

# Get user input.
fahrenheit = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

# Convert to celcius and kelvin.
celcius = (fahrenheit - 32) * (5/9)
kelvin = celcius + 273.15

# Round temps.
fahrenheit = round(fahrenheit, 4)
celcius = round(celcius, 4)
kelvin = round(kelvin, 4)

# Summary table.
print("\nDegrees Fahrenheit:\t" + str(fahrenheit))
print("Degrees Celcius:\t" + str(celcius))
print("Degrees Kelvin:\t\t" + str(kelvin))
