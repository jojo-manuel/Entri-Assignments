# Mini Project: Banking System Using Python

account_number = "1001"
pin = "1234"
username = "jojo"
balance = 5000


# Login function
def login():
    account = input("Enter Account Number: ")
    password = input("Enter PIN: ")

    if account == account_number and password == pin:
        print("Login Successful!")
        print("Welcome", username)
        return True
    else:
        print("Invalid Account Number or PIN")
        return False


# Deposit function
def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Deposit Successful!")
        print("Current Balance:", balance)
    else:
        print("Amount must be greater than zero")


# Withdraw function
def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Amount must be greater than zero")

    elif amount > balance:
        print("Insufficient Balance")

    else:
        balance = balance - amount
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)


# Main program
if login():

    while True:

        print("\n===== BANKING SYSTEM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Logged out successfully")
            break

        else:
            print("Invalid choice")