# Database Admin Program

# Welcome message
print("Welcome to the Database Admin Program")

# Create dictionary for a database of username:password key-value pairs
database = {
    'admin01': '123456789',
    'user111': 'password1',
    'user222': 'password2',
    'user333': 'password3',
    'user444': 'password4',
    }

# User enters username
username = input("\nEnter your username: ").strip()

# Check if username is in database
if username in database.keys():

    # User enters password
    password = input("Enter your password: ")

    # Check if password is correct
    if password == database[username]:
        print("\nHello " + username + "! You are logged in!")

        # Special case for admin
        if username == 'admin01':
            print("\nHere is the current user database:")
            for key, value in database.items():
                print("Username: " + key + "\t\tPassword: " + value)
                
        # Other users have the option to change their password
        else:              
            change = input("\nWould you like to change your password (yes/no): ").lower().strip()
            if change == 'yes':
                new_password = input("What would you like you new password to be (min 8 characters): ")
                if len(new_password) > 7:
                    database[username] = new_password
                else:
                    print("\nNew password does not meet requirements. Must be at least 8 characters.")
                print("\n" + username + " your password is " + database[username])
                
            elif change == 'no':
                print("\nGreat. Your password is still ... " + password)
            else:
                print("\nInvalid response.")
                
    # Password does not match username
    else:
        print("Incorrect password.")

# Username is not in database
else:
    print("Username does not appear in database. Goodbye.")
