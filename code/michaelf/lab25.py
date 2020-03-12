class Account:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__transactions = []

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.amount = amount
        self.__balance += self.amount
        self.__transactions.append(f'user deposited {self.amount}')
        return self.__balance

    def check_withdraw(self, amount):
        self.amount = amount
        if self.amount <= self.__balance:
            return True
        else:
            return False
        #return True if self.balance >= amount else False
        #return self.balance >= amount

    def withdraw(self, amount):
        self.amount = amount
        self.__balance -= self.amount
        self.__transactions.append(f'user withdrew {self.amount}')
        return self.__balance
    
    def print_transactions(self):
        print(self.__transactions)
    

account1 = Account()
# account2 = Account()

while True:
    user_choice = input("1. check balance\n2. deposit\n3. withdrawal\n4. transaction history\n5. quit\n>>> ")

    if user_choice == "1":
        print(account1.check_balance())
        
    elif user_choice == "2":
        amount = float(input("how much would you like to deposit? "))
        print(account1.deposit(amount))

    elif user_choice == "3":
        amount = float(input("How much would you like to withdraw? "))
        if account1.check_withdraw(amount) == True:
            print(account1.withdraw(amount))
        else:
            print("Insufficient funds.")

    elif user_choice == "4":
        account1.print_transactions()

    elif user_choice == "5":
        break
    
    else:
        print("I'm sorry, i don't understand. Please try again.")

# print(account1.check_balance())
# print(account2.check_balance())