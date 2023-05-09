# Online Banking Simulator

def get_info():
    """Get the user information and store it in a dictionary to represent their bank account"""
    # Welcome statement
    print("Welcome to the Online Banking Simulator.")

    # Get user info
    name = input("\nHello, what is your name: ").title().strip()
    savings = int(input("How much money would you like to set up your savings account with: "))
    checking = int(input("How much money would you like to set up your checking account with: "))

    # Create bank account dictionary
    account_info = {
        'Name': name,
        'Savings': savings,
        'Checking': checking
        }
    return account_info


def display_info(account_info):
    """Display the account information from the bank account dictionary"""
    print("\nCurrent Account Information")
    for key, value in account_info.items():
        if type(value) == int or type(value) == float:
            print(key + ": $" + str(value))
        else:
            print(key + ": " + str(value))


def deposit(account_info, account_type, amount):
    """Deposit money into a Savings or Checking account"""
    account_info[account_type] += amount
    print("\nDeposited $" + str(amount) + " into " + account_info['Name'] + "'s " + account_type.lower() + " account.")


def withdrawl(account_info, account_type, amount):
    """Withdraw money from a Savings or Checking account"""

    # Make sure the balance would be positive after the withdrawl
    if account_info[account_type] - amount >= 0:
        account_info[account_type] -= amount
        print("\nWithdrew $" + str(amount) + " from " + account_info['Name'] + "'s " + account_type.lower() + " account.")
    else:
        print("\nSorry, by withdrawing $" + str(amount) + " your account will go negative.") 


def run_again():
    """Ask the user if they want to roll again"""
    choice = input("Would you like to make another transaction (y/n): ").lower().strip()
    if choice.startswith('y') != True:
        banking = False
    else:
        banking = True
    return banking



# The main code

# Create the user's bank account
user_info = get_info()

# Keep allowing deposits or withdrawls until the user decides to stop
banking = True
while banking:

    # Display the user's info
    display_info(user_info)

    # Ask the user for the acount, type of transation, and amount
    account = input("\nWhat account would you like to access (Savings or Checking): ").title().strip()
    transaction = input("What type of transaction would you like to make (Deposit or Withdrawl): ").lower().strip()
    money = float(input("How much money: "))

    # Call the correct function based on the type of transaction
    if account == 'Savings' or account == 'Checking':
        if transaction == 'deposit':
            deposit(user_info, account, money)
        elif transaction == 'withdrawl':
            withdrawl(user_info, account, money)
        else:
            print("\nI'm sorry, we cannot do that for you at this time.")
    else:
        print("\nSorry, you do not have that type of account with this bank.")

    # Ask if the user would like to run again
    banking = run_again()

# Display closing information
display_info(user_info)
print("\nThank you for using the Bank Online Banking Simulator.")

    
