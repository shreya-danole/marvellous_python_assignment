#Even or odd number check


def main():
    num = int(input("Enter a number: "))

    if(num%2==0):
        print(num,"is an even number")
    else:
        print(num,"is an odd number")

if __name__=="__main__":
    main()
