
class Atm():


  def __init__(self,balance=0):
    self.balance = balance
    self.transactions = []

  def check_balance(self):
    # This function returns the account balance
    print(f"You have a balance of ${self.balance}")
    return self.balance

  def deposit(self,amount):
    # This function deposits the given amount in the account
    # deposit_amount = float(input("Verify the deposit amount of cash/checks you just inserted: "))
    self.balance += amount
    self.transactions.append(f"deposit of ${amount}. New balance is ${self.balance}")

  def check_withdrawal(self,amount):
    # This function returns true if the withdrawn amount won't put the account in the negative
    while True:
      amount = self.balance - amount
      if amount >= 0:
        # print("Yes, your balance is enough to withdraw the inputted amount")
        return True
      else:
        print("Sorry, you cannot withdraw that amount because your balance is not enough")
        return False
    
  def withdraw(self,amount):
    # This function withdraws the amount from the account and returns it
    # withdrawal_amount = float(input("Enter the withdrawal amount: "))
    if self.check_withdrawal(amount):
      self.balance -= amount
      self.transactions.append(f"withdrawal of ${amount}. New balance is ${self.balance}")
      # print(f"The amount withdrawn is ${withdrawal_amount}")
      # print(f"Your new balance after this withdrawal is ${self.balance}")
    else:
      # print(f"Oops! You cannot withdraw ${withdrawal_amount} because you only have ${self.balance} in this account.")
      raise ValueError("Oops! There's not enough money in this account.")
    # return self.balance


  def print_transactions(self):
    print("\n".join(self.transactions))



atm = Atm()
# atm.deposit(amount)

# for i in range(10):
#   atm.deposit(100)
#   atm.withdraw(50)
# atm.print_transactions()


while True:
  user_input = input("What would you like to do? ([d]eposit, [w]ithdraw, [c]heck balance, transaction [h]istory, [q]uit) ")
  atm.print_transactions()
  if user_input == 'd':
    print("How much would you like to deposit? ")
    user_amount = input()
    atm.deposit(float(user_amount))
  elif user_input == 'w':
      print("How much would you like to withdraw? ")
      user_amount = input()
      try:
        atm.withdraw(float(user_amount))
      except ValueError as e:
        print(e)
  elif user_input == 'c':
    print(f"Your balance is ${atm.check_balance()}")
  elif user_input in ['h','t']:
    atm.print_transactions()
  elif user_input == 'q':
    break
  else:
    print("Invalid input. Please try again.")