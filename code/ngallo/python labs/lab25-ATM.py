## Nick Gallo - Lab25-ATM - 03/04/2020
class Atm:

    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def check_balance(self, check_balance): 
        print(f"okay, your balance is ${self.balance}. ")
        
    def deposit(self, deposit):
        balance_to_append = int(input("How much would you like to deposit? $"))
        self.balance += balance_to_append
        self.history.append(f"You deposited: {balance_to_append}")
        print(f"okay, you've deposited ${balance_to_append} into your account. Your total balance of: ${self.balance}")

    def get_history(self, get_history):
        for i in self.history:
            print(i)
        print(f"your current balance: ${self.balance}")

    def withdraw(self, withdraw):
        withdraw = int(input(f"How much would you like to withdraw? Keep in mind your balance is ${self.balance}: $"))
        if self.balance < withdraw:
            print(f"Your request was denied due insufficient funds. \n Try again by withdrawing an amount that is less than or equal to ${self.balance}")
            balance.withdraw(balance)
        else:
            self.balance -= withdraw
            self.history.append(f"You withdrew {withdraw}: ")
            print(f"okay, lets withdraw ${withdraw} of your account. Your balance is now ${self.balance}.")
            

balance = Atm(0)

print("\n---- Welcome to Chasen Bank International ----\n")

while True:
    user_input = input("What would you like to do (deposit, withdraw, check balance, history or done)? \n")

    if user_input == "check balance":
        balance.check_balance(balance)
    elif user_input == "deposit":
        balance.deposit(balance)
    elif user_input == "withdraw":
        balance.withdraw(balance)
    elif user_input == "history":
        balance.get_history(balance)
    elif user_input == "done":
        print("Goodbye!")
        break
    else:
        print("Try a proper input")


'''
Lab 25: ATM
Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
Version 2
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

Version 3
Allow the user to enter commands into a REPL.

> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance, history)?
> check balance
> balance: $5

'''