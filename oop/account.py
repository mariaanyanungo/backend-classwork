class Account:
    def __init__(self,number,name):
       self.number=number
       self.name=name
       self.balance=0

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"You have successfully deposited {amount} and your new balance is {self.balance}")
        else:
            print(f"Amount should be more than zero")  

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>0 and self.amount<self.balance:
            self.balance-=self.amount
            print(f"Your balance is {self.balance}")

        else:
            print(f"Insufficient funds")

    def check_balance(self):
        if self.balance>0:
            print(f"Your account balance is {self.balance}")
        else:
            print(f"Your account balance is 0")

    def borrow(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print(f"You borrowed {self.amount}. Your balance is {self.balance} ")
       

    def repay(self,amount):
        self.amount=amount
        if self.amount>0 and self.balance>self.amount:
            self.balance-=self.amount
            print(f"You repayed {self.amount} your account balance is now {self.balance}")
        else:
            print(f"Your balance is {self.balance}")

    def transfer(self,amount):
        self.amount=amount
        if self.amount<self.balance and self.amount>0:
           self.balance-=self.amount
           print(f"You successfully transferred {self.amount} and your balance is {self.balance}")
        elif self.amount>self.balance:
            print(f"You have insufficient funds")

    def paybill(self,amount):
        self.amount=amount
        if self.amount<self.balance and self.amount>0 and self.amount==0:
           self.balance-=self.amount
           print(f"You successfully paid a bill of {self.amount} and your balance is {self.balance}")
        elif self.amount>self.balance:
            print(f"You have insufficient funds")



        

    



    


   
