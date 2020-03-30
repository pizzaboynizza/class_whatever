
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
    def __init__(self,balance): 
        self.account_balance = balance
        self.transaction_list = []
        

    def print_transactions(self, print_transactions):
        for i in self.transaction_list:
            print(i)

    def check_balance(self):
        print(self.account_balance)


    def deposit(self, deposit):
        # amount = int(input("Enter amount to deposit: "))
        self.account_balance += deposit
        self.transaction_list.append(f"You deposited {deposit}")
        print(f"You deposited {deposit}. Your account balance is {self.account_balance}" )


    def check_withdrawal(self, withdrawal):
        if self.account_balance > withdrawal:
            return True
        else:
            return False
    def withdrawal(self,withdrawal):
        # withdrawal = int(input("Enter amount to withdraw:"))
        if self.check_withdrawal(withdrawal) == True:
            self.account_balance -= withdrawal
            self.transaction_list.append(f"You withdrew {withdrawal}")
            # print_transactions()
            print(f"You withdrew ${withdrawal}!, your balance is {self.account_balance}.")
        else:
            print(f"{withdrawal} is more than your account balance of {self.account_balance}")


account1 = ATM(0)
print("Hello, Welcome to Bank blah blah's ATM!")
while True:
    # account1.deposit(600)
    user = input("Would you like to check balance, deposit,or withdrawal, history? ")
    if user == "check balance":
        print(account1.account_balance)
    elif user == "withdrawal":
        account1.withdrawal(int(input("Enter amount to withdraw:")))
    elif user == "deposit":
        account1.deposit(int(input("Enter amount to deposit: ")))
    elif user == "history":
        account1.print_transactions(account1)
    else:
        print("Please re-enter input!")
        break
#print()



