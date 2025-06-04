
class Demo:
    Value = 123    
     
    def __init__(self,A,B):     
        print("inside constructor")
        self.no1 = A      # instances varibale
        self.no2 = B   


    def fun(self):     # instances method
        print("inside instance methode fun ")
        print("no1 is:",self.no1)
        print("no2 is:",self.no2)
    
    def gun(self):     # instances method
        print("inside instance methode gun ")
        print("no1 is:",self.no1)
        print("no2 is:",self.no2)

def main():
   
    obj1 = Demo(11,21)    
    obj2 = Demo(51,101) 

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()
       
if __name__=="__main__":
    main()
