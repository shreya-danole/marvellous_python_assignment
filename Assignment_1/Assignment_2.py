def ChkNum(Number):
    if Number %2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
        
def main():
    print("enter a number")
    Num = int(input())
    result = ChkNum(Num)
    
if __name__ == "__main__":
    main()