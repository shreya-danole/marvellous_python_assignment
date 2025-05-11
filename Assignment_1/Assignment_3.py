
def Add(num1,num2):
    output = num1 + num2
    return output


def main():
    print("Enter first number")
    num1 = int(input())

    print("Enter second number")
    num2 = int(input())

    result = Add(num1,num2)

    print("addition of two number is:",result)
  
    
if __name__ == "__main__":
    main()