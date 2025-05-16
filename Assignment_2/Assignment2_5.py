def Checkprime(num):
    count = 0
    for i in range(1,num+1):
        if (num>1 and num%i==0):
           count = count +1 
    return(count)

def main():
    print("Enter a number:")
    value=int(input())
    output = Checkprime(value)

    if output == 2:
        print("It is a prime number")
    else:
        print("Not prime number")

if __name__=="__main__":
    main()
