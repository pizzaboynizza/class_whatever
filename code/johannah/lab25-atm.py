
# Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0

class Atm():


  def __init__(self,balance=0):
    self.__balance = balance
    print(f"self.balance is ${self.balance}")
    print(f"balance is ${balance}")
    # self.__transactions = []

  def check_balance(self):
    # returns the account balance
    print(f"You have a balance of ${self.balance}")
    return self.__balance

  # def deposit(self,amount):
  #   self.__balance += amount
    # self.__transactions.append(f"deposit of ${amount}. New balance is ${self.__balance}")
  def deposit(self):
    # deposits the given amount in the account
    deposit_amount = float(input("Verify the deposit amount of cash/checks you just inserted: "))
    self.balance += deposit_amount
    print(f"The amount deposited is ${deposit_amount}")
    print(f"Your new balance after this deposit is ${self.balance}")

  def check_withdrawal(self,amount):
    # if self.__balance >= amount:
    #   return True
    # return False
    # OR
    # return self.__balance >= amount
    # returns true if the withdrawn amount won't put the account in the negative
    while True:
      amount = self.balance - amount
      if amount >= 0:
        print("Yes, your balance is enough to withdraw the inputted amount")
        return True
      else:
        return False 
    
  # def withdraw(self,amount):
  #   if self.__check_withdrawal(amount):
  #     self.__balance -= amount
      # self.__transactions.append(f"withdrawal of ${amount}. New balance is ${self.__balance}")
  # def deposit(self):
  #   else:
  #     raise ValueError("Not enough money in account to process transaction")
  def withdraw(self):
    # withdraws the amount from the account and returns it
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    if self.check_withdrawal(withdrawal_amount):
      self.balance -= withdrawal_amount
      print(f"The amount withdrawn is ${withdrawal_amount}")
      print(f"Your new balance after this withdrawal is ${self.balance}")
    else:
      print(f"Oops! You cannot withdraw ${withdrawal_amount} because you only have ${self.balance} in this account.")
    return self.balance

#   def print_transactions(self):
#     print("\n".join(self.__transactions))

# account = Atm()
# for i in range(10):
#   account.deposit(100)
#   account.withdrawal(50)
# account.print_transactions()

atm = Atm()
print(f"atm: {atm}")
print(f"atm.check_balance: {atm.check_balance()}")
atm.deposit()
print(f"atm.withdraw: {atm.withdraw()}")
# print(f"atm.check_withdrawal: {atm.check_withdrawal()}")


while True:
  action = input("Do you want to make a deposit or withdrawal (yes or no)? ")
  if action == 'yes':
    print(atm)
  else:
    break
  choose = input("Do you want to deposit or withdraw (d or w)? ")
  if choose == 'd':
    print(f"atm.check_balance: {atm.check_balance()}")
    atm.deposit()
  else:
    print(f"atm.check_balance: {atm.check_balance()}")
    print(f"atm.withdraw: {atm.withdraw()}")


'''
Version 2:
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions
'''
# round(2)
# transactions = []

'''
Version 3:
Allow the user to enter commands into a REPL
'''

account = Atm()

while True:
  print("what would you like to do? ([d]eposit, [w]ithdraw, [c]heck balance, [h]istory, [q]uit) ")
  user_input = input()
  if user_input in ["deposit","d"]:
    print("How much would you like to deposit? ")
    user_amount = input()
    account.deposit(float(user_amount))
  elif user_input in ["withdraw","w"]:
      print("How much would you like to withdraw ?")
      user_amount = input()
      try:
        account.withdraw(float(user_amount))
      except ValueError as e:
        print(e)
  elif user_input in ["check balance","check","balance","c"]:
    print(f"Your balance is ${account.check_balance()}"")
  elif user_input in ["history","h"]:
    account.print_transactions()
  elif user_input in ["quit","exit","q"]:
    break
  else:
    print("invalid input! Please try again")
