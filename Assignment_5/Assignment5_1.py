#Arthmetic operation on two numbers
def Sum(a,b):
    c = a+b
    return c

def Difference(a,b):
    c = a-b
    return c

def Product(a,b):
    c =a*b
    return c

def Division(a,b):
    c =a/b
    return c


def main():
    num1 = int(input("Enter first number: "))

    num2 = int(input("Enter second number: "))

    ret1 = Sum(num1,num2)
    ret2 = Difference(num1,num2)
    ret3 = Product(num1,num2)
    ret4 = Division(num1,num2)

    print("Sum: ",ret1)
    print("Difference: ",ret2)
    print("Product: ",ret3)
    print("Division: ",ret4)

if __name__ == "__main__":
    main()
