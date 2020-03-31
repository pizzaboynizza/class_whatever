class ATM():
    def __init__(self,balance): 
        self.account_balance = balance
        self.transaction_list = []

    def print_transactions(self, print_transactions):
        for i in self.transaction_list:
            print(i)

    def check_balance(self):
        print(self.account_balance)


    def deposit(self, deposit):
       self.account_balance += deposit
       self.transaction_list.append(f"You deposited {deposit}")
    #    print_transactions(self, print_transactions)


    def check_withdrawal(self, withdrawal):
        if self.account_balance > withdrawal:
            return True
        else:
            return False
    def withdrawal(self,withdrawal):
        if self.check_withdrawal(withdrawal) == True:
            self.account_balance -= withdrawal
            self.transaction_list.append(f"You withdrew {withdrawal}")
            # print_transactions()

        else:
            print(f"{withdrawal} is more than your account balance of {self.account_balance}")
       

     # Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.
        # if transaction == "deposit":
        #     self.account_balance += deposit
        #     transaction_list.append("You deposited {deposit}")
        # elif transaction = "withdrawal":
        #     self.account_balance -= withdrawal
        #     transaction_list.append("You withdrew {withdrawal}")
        # print(transaction_list)
            

account = ATM(0)
account.check_balance() #to see account balance
account.deposit(100) #to deposit
account.check_balance() #to be able to see how much was deposited
account.withdrawal(150)
account.print_transactions(account)
