

class bank:

    def __init__(self):
        self.balance=0
        self.history1 = []


    def bankbalance(self):
        print("The balance is", self.balance)
        

    def deposit(self):
        amount = float(input("Enter amount to be put in: "))
        self.balance += amount
        self.history1.append(f"Amount deposited {amount}")
        print(f"Amount deposited {amount}")

    def withdraw(self):
        amount = float(input("Enter taken out: "))
        if self.balance >= amount:
            self.balance -= amount
            self.history1.append(f'This is the amount withdrew {amount}')
            print("You withdrew: ",amount)
        else:
            print("Insufficient balace")
    
    def history(self):
        self.history
        print(self.history1)

        
atm = bank()



while True:
    print("Hello welcome to your account")
    print("What would you like to do?\n1.Deposit\n2.Withdraw\n3.Check balance\n4.History\n5.Done\n")
    user = input()


    if user == '1':
        atm.deposit()
    elif user == '2':
        atm.withdraw()
    elif user == '3':
        atm.bankbalance()
    elif user == '4':
        atm.history()
    elif user == '5':
        break
