
class BankAccount:
    ROI = 10.5
     
    def __init__(self):
        print("inside constructor")
        self.Name = input("enter name :")
        self.Amount = int(input("enter a amount:"))

    def Display(self):
        print("name of book:"+self.Name)
        print("amount of book:",self.Amount)
      
    def Deposit(self):
        deposit_amount = int(input("enter amount to deposit:"))
        self.Amount = self.Amount + deposit_amount
        print(deposit_amount,"amount deposited")
    
    def Withdraw(self):
        withdraw_amount = int(input("enter amount to withdraw:"))
        self.Amount = self.Amount - withdraw_amount
        print(withdraw_amount,"withdrawn successfully.")
   

    def CalculateInttrest(self):
        interest = (self.Amount*BankAccount.ROI) /100
        print("interset on current ammount is:",interest)
        
    

def main():
    print("Creating account 1")
    account1 = BankAccount()
    account1.Deposit()
    account1.Withdraw()
    account1.CalculateInttrest()
    account1.Display()


    print("Creating account 2")
    account2 = BankAccount()
    account2.Deposit()
    account2.Withdraw()
    account2.CalculateInttrest()
    account2.Display()


if __name__=="__main__":
    main()
