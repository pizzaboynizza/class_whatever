# # Lab 25: ATM
# # Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

# # check_balance() returns the account balance
# # deposit(amount) deposits the given amount in the account
# # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# # withdraw(amount) withdraws the amount from the account and returns it.

# # what are my arguments doing?
# # what is self.balance doing?
# # Why do I need to say self.balance instead of just balance.
# class ATM:
#     def __init__(self, balance=0):
#         self.balance = balance
        
#     def check_balance(self, check_balance):
#         print(self.balance)

#     def check_withdrawal(self, check_withdrawal):
#         if balance >= 0:
#             print("True")
        

#     def withdraw(self, withdraw):
#         self.balance -= withdraw 
#         print(self.balance)

#     def deposit(self, deposit):
#         self.balance += deposit
#         print(self.balance)


# balance = ATM(int(234))

# ''' refer to balance.check_balance(balance).... go to the class first by using balance  .check_balance says look inside the class ATM and find check_balance and choose the argument I have saved in balance.'''
# balance.check_balance(balance)
# balance.withdraw(int(input("how much do you want to withdraw?: ")))
# balance.deposit(int(input("how much would you like to deposit?: ")))

# # Version 2
# # Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.



# # make a string that goes into transactions under withdraw and deposit.
# # self is = to balance which is 234.
# class ATM:
#     def __init__(self, balance=0):
#         self.balance = balance
#         self.transactions = []
        
#     def check_balance(self, check_balance):
#         print("your balance is", self.balance)

#  '''if balance is greater than what the user typed in then call withdraw using self.withdraw()
# go to the def withdraw method and replace withdraw argument with check withdrawl argument from check withdrawl method.'''
#     def check_withdrawal(self, check_withdrawal):
#         if self.balance >= check_withdrawal:
#             self.withdraw(check_withdrawal)
#         else:
#             print("your balance is below zero")
            
            
        
#     def withdraw(self, withdraw):
#         self.balance -= withdraw 
#         print(self.balance)
#         self.transactions.append(f"you withdrew {withdraw} dollars." )
#         self.transactions_list(self.deposit)

#     def deposit(self, deposit):
#         self.balance += deposit
#         print(self.balance)
#         self.transactions.append(f"you deposited {self.balance} dollars." )
#         print("self transanctions", self.transactions)

#     def transactions_list(self, deposit):
#         for x in self.transactions:
#             print(x)


# balance = ATM(int(234))

# ''' refer to balance.check_balance(balance).... go to the class first by using balance  .check_balance says look inside the class ATM and find check_balance and choose the argument I have saved in balance.'''
# balance.check_balance(balance)
# balance.check_withdrawal(int(input("how much do you want to withdraw?: ")))
# balance.deposit(int(input("how much would you like to deposit?: ")))





# Version 3
# Allow the user to enter commands into a REPL.

# > what would you like to do (deposit, withdraw, check balance, history)?
# > deposit
# > how much would you like to deposit?
# > $5
# > what would you like to do (deposit, withdraw, check balance, history)?
# > check balance
# > balance: $5


class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []
        
    def check_balance(self, check_balance):
        print("your balance is", self.balance)

#  '''if balance is greater than what the user typed in then call withdraw using self.withdraw()
# go to the def withdraw method and replace withdraw argument with check withdrawl argument from check withdrawl method.'''
    def check_withdrawal(self, check_withdrawal):
        if self.balance >= check_withdrawal:
            self.withdraw(check_withdrawal)
        else:
            print("your balance is below zero")
            
    def withdraw(self, withdraw):
        self.balance -= withdraw 
        print("your remaining balance is: ", self.balance)
        self.transactions.append(f"you withdrew {withdraw} dollars." )
        self.transactions_list(self.deposit)

    def deposit(self, deposit):
        self.balance += deposit
        print("your balance is: ", self.balance)
        self.transactions.append(f"you deposited {self.balance} dollars." )
        print("self transanctions", self.transactions)

    def transactions_list(self, deposit):
        for x in self.transactions:
            print("transactions_list: ", x)



while True:
    REPL = input('What would you like to do (deposit, withdraw, check balance, history, done)? ')

    if REPL == 'done':
            break
    elif REPL == 'deposit':
        while True:
            REPL = ("what would you like to do (deposit, withdraw, check balance, history)?")
            if REPL == "deposit":
                self.balance += deposit
                print(self.balance)
            elif REPL == "withdraw":
                self.balance -= withdraw
                print(self.balance)
            elif REPL == "check_balance":
                print(balance)
            elif REPL == "history":
                print(self.transanctions)

''' refer to balance.check_balance(balance).... go to the class first by using balance  .check_balance says look inside the class ATM and find check_balance and choose the argument I have saved in balance.'''
balance.check_balance(balance)
balance.withdraw(int(input("how much do you want to withdraw?: ")))
balance.deposit(int(input("how much would you like to deposit?: ")))

balance = ATM(int(5000))








