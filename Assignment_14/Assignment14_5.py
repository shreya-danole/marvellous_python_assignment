
class BankAccount:
   
    def __init__(self,A,B,C):
        print("inside constructor")
        self.Name = A
        self.Amount_number = B
        self.Balance = C

    def Display(self):
        print("name of book:"+self.Name)
        print("amount of book:",self.Amount_number)
        print("amount of book:",self.Balance)
      
    def Deposit(self):
        deposit_amount = int(input("enter amount to deposit:"))
        self.Balance = self.Balance + deposit_amount
        print(deposit_amount,"amount deposited")
    
    def Withdraw(self):
        withdraw_amount = int(input("enter amount to withdraw:"))
        self.Balance = self.Balance - withdraw_amount
        print(withdraw_amount,"withdrawn successfully.")
   

def main():
    account1 = BankAccount("abc",234,500)
    account1.Deposit()
    account1.Withdraw()
    account1.Display()


if __name__=="__main__":
    main()
