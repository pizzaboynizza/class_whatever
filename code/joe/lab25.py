# Lab 25
# Author : Joe

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__history = []

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append(f"Deposit of ${amount}")

    def check_withdrawal(self, amount):
        if self.__balance - amount < 0 or amount == 0:
            return False
        return True
    
    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.__balance -= amount
            self.__history.append(f"Withdrawal of ${amount}")
            return amount
        self.__history.append(f"Failed withdrawal of ${amount}")
        return 0
    
    def print_transactions(self):
        for x in self.__history:
            print(f"  {x}")
        if self.__history == []:
            print("  There are no transactions to display")

def check_account(master, check, msg=True):
    try:
        temp = master[check]
    except KeyError:
        if msg:
            print(f"  '{check}' does not exist!")
        return True
    return False

def check_num(s):
    try:
        temp = s
        if temp[0] == "$":
            temp = s[1:]
        if temp[0] == "-": # no negatives allowed
            temp = "X"
        return int(temp)
    except ValueError:
        print(f"  Invalid amount {s}!")
        return -1

help_text = """
How to use:
deposit [account_name] amount\t## deposit money into an account
withdraw [account_name] amount\t## withdraw money from an account
check [account_name]\t\t## check the balance of an account
history [account_name]\t\t## look at the history of transactions in an account
new account_name\t\t\t## make a new account
remove account_name\t\t\t## remove an account
all\t\t\t\t\t## see all bank accounts
<account_name>\t\t\t## sets default account
help\t\t\t\t## display this text
quit\t\t\t\t## exit program""" 

print("Let's make an account!")
account_name = input("Enter the name of your new account: ").lower()
all_accounts = {account_name: BankAccount()}

print("\nOkay!\n", help_text)

while True:
    user_in = input("\n> ").lower()
    user_in = user_in.split()

    if user_in == []: #prevent index errors
        print("  Invalid command!")
    
    # Quit
    elif user_in[0] == "quit":
        break

    # Deposit
    elif user_in[0] == "deposit":
        if len(user_in) > 2: # if they specified the account
            account_name = user_in[1]
            user_in.pop(1)
        elif len(user_in) == 1: #they didn't put in enough arguments
            print("  Error: Expected amount to deposit!")
            continue
        to_deposit = check_num(user_in[1])
        if to_deposit < 0: # ensure valid amount
            continue
        if check_account(all_accounts, account_name): # ensure account exists
            continue
        all_accounts[account_name].deposit(to_deposit)
        print(f"  Successfully deposited ${to_deposit} in '{account_name}'")

    # Withdraw
    elif user_in[0] == "withdraw":
        if len(user_in) > 2:
            account_name = user_in[1]
            user_in.pop(1)
        elif len(user_in) == 1:
            print("  Error: Expected amount to withdraw!")
            continue
        to_withdraw = check_num(user_in[1])
        if to_withdraw < 0:
            continue
        if check_account(all_accounts, account_name):
            continue
        if all_accounts[account_name].withdraw(to_withdraw) <= 0:
            print(f"  Failed to withdraw ${to_withdraw} from '{account_name}'")
        else:
            print(f"  Successfully withdrew ${to_withdraw} from '{account_name}'")

    # Check Balance
    elif user_in[0] == "check":
        if len(user_in) > 1:
            account_name = user_in[1]
        if check_account(all_accounts, account_name):
            continue
        print(f"  '{account_name}' has a balance of ${all_accounts[account_name].check_balance()}")

    # Look at History
    elif user_in[0] == "history":
        if len(user_in) > 1:
            account_name = user_in[1]
        if check_account(all_accounts, account_name):
            continue
        print(f"  For '{account_name}':")
        all_accounts[account_name].print_transactions()

    # New Account
    elif user_in[0] == "new":
        if len(user_in) < 2:
            print("  Expected account name!")
            continue
        if not check_account(all_accounts, user_in[1], False):
            print(f"  '{user_in[1]}' already exists!")
            continue
        account_name = user_in[1]
        all_accounts[account_name] = BankAccount()
        print(f"  Successfully created new account '{account_name}'")
    
    # Remove Account
    elif user_in[0] == "remove":
        if len(user_in) < 2:
            print("  Expected account name!")
            continue
        if check_account(all_accounts, user_in[1]):
            continue
        del all_accounts[user_in[1]]
        print(f"  Successfully removed '{account_name}'")

    # Show All
    elif user_in[0] == "all":
        for k in all_accounts.keys():
            print(f"  '{k}'")
    
    # Help
    elif user_in[0] == "help":
        print(help_text)

    elif not check_account(all_accounts, user_in[0], False):
        account_name = user_in[0]
        print(f"  Set current account to '{account_name}'")
    
    else:
        print("  Invalid command!")

        
            