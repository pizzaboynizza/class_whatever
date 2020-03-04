"""
Lab 25: ATM
Let's represent an ATM with a class containing a balance property.
A newly created account will default to a balance of 0. Implement the initializer,
as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
"""


class ATM:
    def __init__(self, balance):
        self.balance = balance
    

    def check_balance(self):
        transactions.append(f"Checked Account Balance.")
        print(f"Your current balance is ${self.balance}.")

    def deposit(self, deposit):
        self.balance += deposit
        transactions.append(f"Deposited ${deposit} into account.")
        print(f"Deposited ${deposit} into your account.\nYour new balance is ${self.balance}.")
        return self.balance

    def check_withdrawal(self, test_amount):
        if test_amount < self.balance:
            return True
        else:
            return False

    def withdraw(self, test_amount):
        # self.check_withdrawal(test_amount)
        if self.check_withdrawal(test_amount) == True:
            self.balance -= test_amount
            transactions.append(f"Withdrew ${test_amount} from account.")
            print(f"Withdrawing ${test_amount}. Your new balance is ${self.balance}")
            return self.balance
        elif self.check_withdrawal(test_amount) == False:
            print(f"Insufficient Funds. Your current balance is ${self.balance}")
        else:
            print("Something Went Wrong. Please Try Again.")

    def print_transactions(self):
        print("Transaction History:")
        for entry in transactions:
            print(entry)
        # print(", ".join(transactions))

account = ATM(0)
transactions = []
while True:
    user_in = input(f"""\nWhat would you like to do?
    1. Make a Deposit
    2. Check Your Balance
    3. Make a Withdrawal
    4. Check Your Transaction History
    5. Exit
    Enter the number for your choice: """)
    if user_in == "1":
        deposit1 = float(input("Enter the dollar($) amount that you want to deposit: $"))
        account.deposit(deposit1)
    elif user_in == "2":
        account.check_balance()
    elif user_in == "3":
        test_amount = float(input("Enter the dollars($) amount that you want to withdraw: $"))
        account.withdraw(test_amount)
    elif user_in == "4":
        account.print_transactions()
    elif user_in == "5":
        print("Okay, goodbye.")
        break
    else:
        print("Something went wrong.")