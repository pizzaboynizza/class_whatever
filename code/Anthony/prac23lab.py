class ATM:
    def __init__ (self, balance =0):
        self.balance = balance
        self.transactions = [] # an empty list for transactions

    
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f" You deposited {amount}: New balance is {self.balance}")
    

    def check_withdrawal(self, amount):
        return self.balance >= amount


    def withdrawal(self, amount):
        if self.check_withdrawal(amount): #checks if amount to withdraw is higher/less than balance
            self.balance -= amount #withdraw from balance
            self.transactions.append(f" You deposited {amount}: New balance is {self.balance}")
        else:
           raise ValueError ("{self.withdrawal} is greater than {self.balance}, please enter an amount lower than {self.balance}")
    
    def print_transactions(self):
        print("\n".join(self.transactions)) #"\n".join makes the list print in a new line every transaction
    
account = ATM()
    

while True:
    print("What would you like to do? ([d]eposit, [w]ithdrwa, [c]heck balance, [h]istory, [q]uit)?")
    user_input = input()

    if user_input in ["deposit", "d"]:
        print("How much would you like to deposit? ")
        user_amount = input()
        account.deposit(float(user_amount))
    elif user_input in ["withdrwawal", "w"]:
        print("How much would you like to withdraw? ")
        user_amount = input()
        try:
            account.withdrawal(float(user_amount))
        except ValueError as e:
            print(e)

    elif user_input in ["check balance", "balance", "c"]:
        print(f"You account balance is ${account.check_balance()}")
    elif user_input in ["history", "h"]:
        account.print_transactions()
    elif user_input in ["quit", "exit", "q"]:
        break
    else:
        print("Sorry, please reenter ")




