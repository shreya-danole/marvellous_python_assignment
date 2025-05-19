#find largest among three numbers
def main():
    # num1 = input("Enter 1 numbers")
    # num2 = input("Enter 2 numbers")
    # num3 = input("Enter 3 numbers")

    num1, num2, num3 = map(int, input("Enter three numbers:").split())
    if (num1>num2):
        if(num1>num3):
            print("Largest number is",num1)
        else:
            print("Largest number is",num3)

    elif(num2>num3):
        print("Largest number is",num2)

    else:
        print("Largest number is",num3)


if __name__=="__main__":
    main()
