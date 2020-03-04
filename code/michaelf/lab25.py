class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        self.transactions.append(f'user deposited {self.amount}')
        return self.balance

    def check_withdraw(self, amount):
        self.amount = amount
        if self.amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        self.transactions.append(f'user withdrew {self.amount}')
        return self.balance
    
    def print_transactions(self):
        print(self.transactions)
    

account1 = Account()
# print(account1.check_balance())
# print(account1.deposit(600))
# print(account1.check_balance())
# print(account1.check_withdraw(555))
# print(account1.withdraw(555))
# account1.print_transactions()

while True:
    user_choice = input("1. check balance\n2. deposit\n3. withdrawal\n4. transcation history\n5. quit\n>>> ")

    if user_choice == "1":
        print(account1.check_balance())
        
    if user_choice == "2":
        amount = int(input("how much would you like to deposit? "))
        print(account1.deposit(amount))

    if user_choice == "3":
        amount = int(input("How much would you like to withdraw? "))
        if account1.check_withdraw(amount) == True:
            print(account1.withdraw(amount))
        else:
            print("Insufficient funds.")

    if user_choice == "4":
        account1.print_transactions()

    if user_choice == "5":
        break
