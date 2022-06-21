import math
class Category:
    
    def __init__(self,names):
        self.names = names
        self.ledger = list()    

class withdraw(Category):
    def calculate(self,amount):
        self.ledger.append({"amount": amount})
    
class deposit(Category):
    def calculate(self,amount):
        self.ledger.append({"amount": -amount})
        
while True:
    food = Category('food')
    deposit.calculate(1000)
    food = withdraw(150)
    food.calculate()
    print(food.ledger)        
    check = input("Do you want to calculate again? Y or N: ")
    if check.upper() == "Y":
        continue
    elif check.upper() == "N":
        print("Bye...")
        break

