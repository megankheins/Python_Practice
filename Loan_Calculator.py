# Loan Calculator

from matplotlib import pyplot as plt


def get_info():
    """Get user loan information and store it in a dictionary"""

    # Create the blank loan dictionary
    loan = {}

    # Get user input for loan information
    loan['Principal'] = float(input("\nEnter the loan amount: "))
    loan['Rate'] = float(input("Enter the interest rate: "))/100
    loan['Monthly Payment'] = float(input("Enter the desired monthly payment amount: "))
    loan['Money Paid'] = 0
    return loan


def display_loan(month_num, loan):
    """ Display the current loan information"""
    
    print("\n----Loan information after " + str(month_num) + " months----")
    for key, value in loan.items():
        print(key + ": " + str(value))


def interest(loan):
    """Collect the interest on the loan each month"""

    # Collecting monthly interest so you need to divde by 12
    loan['Principal'] += (loan['Principal'] * loan['Rate']) / 12
    

def loan_payment(loan):
    """Simulate making the monthly payment on the loan"""
    
    loan['Principal'] -= loan['Monthly Payment']

    # Need to make a full payment on the loan; loan is not paid off
    if loan['Principal']  >= 0:
        loan['Money Paid'] += loan['Monthly Payment']

    # Do not need to make a full payment; loan is paid off
    else:
        # Loan['princial'] is negative here
        loan['Money Paid'] += (loan['Monthly Payment'] + loan['Principal'])
        loan['Principal'] = 0


def summarize_loan_info(loan, month_num, principal):
    """Display the results of paying off your loan"""
    
    print("\nCongrats! You paid off your loan in " + str(month_num) + " months!")
    print("Your initial loan was $" + str(principal) + " at a rate of " + str(loan['Rate']*100) + "%.")
    print("Your monthly payment was " + str(loan['Monthly Payment']) + ".")
    print("You spent $" + str(round(loan['Money Paid'], 2)) + " in total.")
    print("You spent $" + str(round(loan['Money Paid'] - principal, 2)) + " on interest!")


def graph_loan_info(data, loan):
    """Create a graph that shows the principal overtime"""

    month_values = []       # List of month numbers
    principal_values = []   # List of principal values

    # Loop through data. Each value in data is a tuple
    # Value[0] is a month number and value[1] is a principal value
    for value in data:
        month_values.append(value[0])
        principal_values.append(value[1])

    # Plot the month and principal values overtime. Display the plot.
    plt.plot(month_values, principal_values)
    plt.ylabel('Principal of Loan')
    plt.xlabel('Month Number')
    plt.title(str(loan['Rate']*100) + "% Interest with $" + str(loan['Monthly Payment']) + " Monthly Payment")
    plt.show() 



# The main code

print("Welcome to the Loan Calculator")

# Initialize variables
month = 0
loan_info = get_info()
initial_principal = loan_info['Principal']
plot = []

# Display the initial loan information
display_loan(month, loan_info)
input("Press 'Enter' to begin paying off your loan.")

# Simulate the user paying off the loan
while loan_info['Principal'] > 0:

    # The monthly payment is not large enough and user will never be able to pay off the loan
    if loan_info['Principal'] > initial_principal:
        break
        
    # It is possible to pay off the loan
    month += 1
    interest(loan_info)
    loan_payment(loan_info)
    plot.append((month, loan_info['Principal']))
    display_loan(month, loan_info)

# User either paid off the loan or will never be able to
if loan_info['Principal'] == 0:
    
    # Graph the plot of the principal overtime
    summarize_loan_info(loan_info, month, initial_principal)
    graph_loan_info(plot, loan_info)

# Loan is not able to be paid off
else:
    print("\nYou will NEVER pay off your loan!")
    print("You cannot get ahead of the interest.")    
    



