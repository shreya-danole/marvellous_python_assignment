# Accept a no print its factorial 

def factorial(val):
    mul=1
    for i in range(1,val+1):
        mul=mul*i
    return mul

def main():
    val=int(input("enter a number: "))
    output = factorial(val)
    print("The factorial of give number is:",output)
   
if __name__ == "__main__":
    main()
