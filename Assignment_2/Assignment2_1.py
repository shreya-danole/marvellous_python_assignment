from Arithmetic import Add, Sub, Mult, Div


def main():
    print("enter a first number:")
    value1= int(input())

    print("enter a second number:")
    value2= int(input())
    
    result1 = Add(value1,value2)
    print("addition is:",result1)

    result2 = Sub(value1,value2)
    print("subtraction is:",result2)

    result3 = Mult(value1,value2)
    print("multipilication is:",result3)

    result4 = Div(value1,value2)
    print("division is:",result4)


    


if __name__=="__main__":
    main()

