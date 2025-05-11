def Stars(num):
    i = 0  #counter
    for i in range(num):
        print("*",end=" ")

def main():
    print("Enter a number")
    num = int(input())
    result = Stars(num)


if __name__ == "__main__":
    main()