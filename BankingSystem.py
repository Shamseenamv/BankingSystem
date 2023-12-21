#Write a python program to replicate a Banking system. The following features are mandatory:
# 1. Account login
# 2. Amount Depositing
# 3. Amount Withdrawal

from decimal import Decimal, InvalidOperation

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, balance):
        try:
            balance = Decimal(balance)
        except InvalidOperation:
            print("Invalid initial balance. Please enter a valid numeric value.")
            return

        if account_number.isdigit() and account_number not in self.accounts:
            password = input("Enter a password for the account: ")
            self.accounts[account_number] = {"name": name, "balance": balance, "password": password}
            print("Account created successfully.")
        else:
            print("Invalid account number or account already exists.")

    def login(self, account_number, password):
        if account_number in self.accounts and self.accounts[account_number]['password'] == password:
            print(f"Logged in as {self.accounts[account_number]['name']}.")
            return True
        else:
            print("Invalid account number or password.")
            return False

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            try:
                amount = Decimal(amount)
            except InvalidOperation:
                print("Invalid deposit amount. Please enter a valid numeric value.")
                return

            if amount > 0:
                self.accounts[account_number]['balance'] += amount
                print(f"Deposited ${amount:.2f}. New balance: ${self.accounts[account_number]['balance']:.2f}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Account does not exist.")

    def withdraw(self, account_number, password, amount):
        if account_number in self.accounts and self.accounts[account_number]['password'] == password:
            try:
                amount = Decimal(amount)
            except InvalidOperation:
                print("Invalid withdrawal amount. Please enter a valid numeric value.")
                return

            if amount > 0 and self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.accounts[account_number]['balance']:.2f}")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                print("Insufficient balance.")
        else:
            print("Account does not exist or incorrect password.")


print("*****Welcome to XYZ bank*****")

bank = Bank()

while True:
    print("\n1. Create Account\n2. Login\n3. Deposit\n4. Withdraw\n5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        name = input("Enter your name: ")
        balance = input("Enter initial balance: ")
        bank.create_account(account_number, name, balance)
    elif choice == "2":
        account_number = input("Enter account number: ")
        password = input("Enter your password: ")
        bank.login(account_number, password)
    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = input("Enter the amount to deposit: ")
        bank.deposit(account_number, amount)
    elif choice == "4":
        account_number = input("Enter account number: ")
        password = input("Enter your password: ")
        amount = input("Enter the amount to withdraw: ")
        bank.withdraw(account_number, password, amount)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
