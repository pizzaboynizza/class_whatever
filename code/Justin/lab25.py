
class Account: 
    def __init__(self): 
        self.balance=0
        self.history = []
        print("Hello!!!")

    def deposit(self): 
        amount = float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        output_one = print("Amount Deposited:", amount)
        self.history.append("Amount Deposited:")
        self.history.append(amount)
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount
            self.history.append("Amount Withdrawn:")
            self.history.append(amount)
            print("Amount Withdrawn", amount)
        else: 
            output_two = print("\n Insufficient balance")
            self.history.append(amount)

    def print_transactions(self): 
        print("Net Available Balance=",self.balance)
        print(self.history)
           
a = Account()
   
a.deposit() 
a.withdraw()
a.print_transactions()
  

