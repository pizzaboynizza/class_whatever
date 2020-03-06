class ATM:
#'''FIRST WE NEED TO STORE VALUES TO FIELDS IN OBJECTS'''
    def __init__ (self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self):
        amount = int(input("Please enter an amount to add to your account: "))
        self.balance += amount
        self.history.append(f'User deposited {amount}')
        print("Your current balance is:", self.balance)
        return self.history
        
    def withdrawal(self):
        amount = int(input("Please enter the amount to withdrawal: "))
        (amount * -1)
        self.balance -= amount
        self.history.append(f'User removed {amount}')
        print("Your current balance is:", self.balance)
        return self.history

    def check_balance(self):   
        print(self.balance)
        
    def print_history(self):
        print(bank.history)
        

bank = ATM()
#this says go look in ATM set thebalance to zero, and that's it
#check if/else (this is good!)
#if
stay_in_loop = True
while stay_in_loop is True:
    print("Welcome to the worst ATM Ever!")
    choice = input("Please choose <1> for check balance, <2> for make deposit, <3> for make a withdrawal, or <4> for print transaction history")
    if  choice == '1':
        bank.check_balance()
        stay_in_loop = False
    if  choice == '2':
        print("Let's Deposit!")
        bank.deposit()
        stay_in_loop = False
    if choice == '3':
        print("Let's Withdrawal!")
        bank.withdrawal()
        stay_in_loop = False
    if choice == '4':
        print("Let's print history!")
        bank.print_history()
        stay_in_loop = False
    else:
        another_transaction = input("Would you like another transaction? ")
        if another_transaction == "yes":
            stay_in_loop = True
            continue
        if another_transaction == "no":
            print("Thank you, goodbye!")
            stay_in_loop = False
            continue
else:
    print("Thank you! Have a nice day")
    