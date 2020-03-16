class ATM:
    def __init__(self,balance): # ALWAYS FIRST INITIALIZE AN INIT METHOD
        self.account_balance = balance
#CREAT A CHECK BALACNE METHOD
    def check_balance(self):
        print(self.account_balance)


    def deposit(self, deposit):
       self.account_balance += deposit


    def check_withdrawal(self, withdrawal):
        if self.account_balance > withdrawal:
            return True
        else:
            return False
    def withdrawal(self,withdrawal):
        if self.check_withdrawal(withdrawal) == True:
            self.account_balance -= withdrawal
        else:
            print(f"Transaction failed! The amount to withdraw is more than your account balance of ${self.account_balance}!")
       

        
account = ATM(0)
account.check_balance() #to see account balance
account.deposit(100) #to deposit
account.check_balance() #to be able to see how much was deposited
account.withdrawal(150)
