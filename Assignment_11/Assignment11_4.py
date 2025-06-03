
# def display(X,Y):
#         print(pow(X,Y))
        
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
       
def main():
    num1 = int(input("enter a number"))
    num2 = int(input("enter a number"))
    ret = power(num1,num2)
    print(ret)

if __name__=="__main__":
    main()
