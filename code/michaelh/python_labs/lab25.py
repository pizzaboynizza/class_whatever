'''
# Lab 25: ATM

Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

- `check_balance()` returns the account balance
- `deposit(amount)` deposits the given amount in the account
- `check_withdrawal(amount)` returns true if the withdrawn amount won't put the account in the negative
- `withdraw(amount)` withdraws the amount from the account and returns it

## Version 2

Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function `print_transactions()` to your class for printing out the list of transactions.

## Version 3

Allow the user to enter commands into a REPL.
```
> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance, history)?
> check balance
> balance: $5
```
'''
class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.__append_history(f'Deposit {amount}')
        self.balance += amount

    def check_withdrawal(self, amount):
        return self.balance - amount > 0

    def withdraw(self, amount):
        self.balance -= amount
        self.__append_history(f'Withdraw {amount}')
        return self.balance

    def __append_history(self, history_str):
        self.history.append(history_str)

    def print_transactions(self):
        print('\n'.join(self.history))

# a1 = Account()
# a1.deposit(10)
# a2 = Account()
# a2.deposit(100)
# print(a1.history is a2.history)
# print(a1.history, a2.history)


while True:
    REPL_function = input('What would you like to do (deposit, withdraw, check balance, history, done)? ').lower()

    if REPL_function == 'done':
        break
    elif REPL_function == 'deposit':
        while True:
            amount = input('How much would you like to deposit? ')
            try:
                a1.deposit(int(amount))
                break
            except ValueError:
                print('Try again!')
    elif REPL_function == 'withdraw':
        while True:
            amount = input('How much would you like to withdraw? ')
            try:
                a1.withdraw(int(amount))
                break
            except ValueError:
                print('Try again!')
    elif REPL_function == 'check balance':
        print(a1.check_balance())
    elif REPL_function == 'history':
        a1.print_transactions()
    else:
        print('You cannot do that.')