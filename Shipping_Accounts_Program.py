# Shipping Accounts Program

# Welcome statement
print("Welcome to the Shipping Accounts Program")

# Define the valid usernames
usernames = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']

# User input
username = input("\nHi, what is your username? ").lower().strip()

# Username is valid
if username in usernames:
    print("Hello " + username + ". Welcome back to your account.")

    # Shipping price summary
    print("\nCurrent shipping prices are as follows:")
    print("Shipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    # Desired number of items
    num_items = int(input("\nHow many items would you like to ship: "))

    # Determining the cost of the items
    if num_items < 100:
        cost = num_items * 5.10
        cost = round(cost, 2)
        print("To ship " + str(num_items) + " items it will cost you $" + str(cost) + " at $5.10 per item.")
    elif num_items < 500:
        cost = num_items * 5.00
        cost = round(cost, 2)
        print("To ship " + str(num_items) + " items it will cost you $" + str(cost) + " at $5.00 per item.")
    elif num_items < 1000:
        cost = num_items * 4.95
        cost = round(cost, 2)
        print("To ship " + str(num_items) + " items it will cost you $" + str(cost) + " at $4.95 per item.")
    else:
        cost = num_items * 4.80
        cost = round(cost, 2)
        print("To ship " + str(num_items) + " items it will cost you $" + str(cost) + " at $4.80 per item.")

    # User decides if they want to ship the items
    decision = input("Would you like to place this order (y/n): ").lower().strip()
    if decision.startswith('y'):
        print("Okay, shipping your " + str(num_items) + " items.")
    else:
        print("Okay, no order is being placed at this time.")
        
# Username is not valid
else:
    print("Sorry, you do not have an account with us. Goodbye.")
        
