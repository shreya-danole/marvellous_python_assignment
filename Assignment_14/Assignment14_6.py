class Calculator:

    def __init__(self):
        print("inside constructor")
        self.Value1 = 0    # instances varibale
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("enter a Value1:"))
        self.Value2 = int(input("enter a Value2:"))

    def Addition(self):
        result = 0.0
        result = self.Value1 + self.Value2
        return result
    
    def Subtraction(self):
        result = 0.0
        result = self.Value1 - self.Value2
        return result

    def Multiplication(self):
        result = 0.0
        result = self.Value1 * self.Value2
        return result

    def Division(self):
        result = 0.0
        result = self.Value1 / self.Value2
        return result


    
    
def main():
    obj = Calculator()
    obj.Accept()
    ret1 = obj.Addition()
    ret2 = obj.Subtraction()
    ret3 = obj.Multiplication()
    ret4 = obj.Division()

    print("Addition is:",ret1)
    print("Subtraction is:",ret2)
    print("Multiplication is:",ret3)
    print("Division is:",ret4)

    
if __name__=="__main__":
    main()
