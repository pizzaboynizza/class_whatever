##  ATM Lab V3  ##

class Acct:
    def __init__(self):
        self.bal=1000

    def deposit(self,amount):
        self.bal += amount
    
    def wdl(self,amount):
        if self.bal>=amount:
            self.bal-=amount
            

    def dis(self):
        print('\n Available Balance=$',self.bal)


s = Acct()

print('                Welcome to Code Guild Credit Union               ')
while True:
    print('                    Please Make Your Selection                   ')
    print('[C]heck Balance [D]eposit Funds [W]ithdraw Funds [H]istory [E]xit')
    choice = input(">>>>   ").lower()

    if choice == "c":
        print(f"Your Current Balance Is:{s.bal}")

    elif choice == "d":
        print("How much would you like to deposit? ")
        dep = float(input(">>>   "))
        s.deposit(dep)
       
    elif choice == "w":
        print("How much would you like to withdraw?")
        wit = float(input(">>>   "))
        s.wdl(wit)

    elif choice == "h":
        print("No Current History")
        print("Thank You!")

    elif choice == "e":
        print("Goodbye!")
        break
    else:
        print("Invalid Input")