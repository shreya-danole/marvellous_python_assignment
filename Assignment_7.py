def Check(num):
    if num%5 == 0:
        print("True")
    else:
        print("False")

def main():
    print("Enter a number")
    num = int(input())
    result = Check(num)

if __name__ == "__main__":
    main()