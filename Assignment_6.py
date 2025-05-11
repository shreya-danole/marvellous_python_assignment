def Check(Number):
    if Number > 0:
        print("Positive Number")

    elif Number < 0:
        print("Negative Number")
    else:
        print("Zero")
        
def main():
    print("enter a number")
    Num = int(input())
    result = Check(Num)
    
if __name__ == "__main__":
    main()