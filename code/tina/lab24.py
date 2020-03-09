

class bank:
    #Class must have init to run.
    def __init__(self):
        #We are setting balance in self as 0
        self.balance=0
        self.history1 = []


    def bankbalance(self):
        #We are calling balance with self.balance.
        print("The balance is", self.balance)
        

    def deposit(self):
        amount = float(input("Enter amount to be put in: "))
        # using amount as a ver to add to the bank account
        self.balance += amount
        # append amount of bank acount to list within the class with an F saying how much
        self.history1.append(f"Amount deposited {amount}")
        print(f"Amount deposited {amount}")

    def withdraw(self):
        amount = float(input("Enter taken out: "))
        #using a if statment to say if amount is > amount within balance remove it, if not else return insufficient balance
        if self.balance >= amount:
            self.balance -= amount
            self.history1.append(f'This is the amount withdrew {amount}')
            print("You withdrew: ",amount)
        else:
            print("Insufficient balace")
    
    def history(self):
        #this is print the list of history that is sorted with in the class. 
        self.history
        print(self.history1)

#to class a class you have to label it first to use it with in the repl        
atm = bank()



while True:
    print("Hello welcome to your account")
    print("What would you like to do?\n1.Deposit\n2.Withdraw\n3.Check balance\n4.History\n5.Done\n")
    user = input()


    if user == '1':
        #this is how you call a fuction with in a class
        atm.deposit()
    elif user == '2':
        atm.withdraw()
    elif user == '3':
        atm.bankbalance()
    elif user == '4':
        atm.history()
    elif user == '5':
        break
