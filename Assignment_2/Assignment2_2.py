def start(val):
    for i in range(val):
        for j in range(val):
            print("*", end=" ")
        print()
def main():
    print("enter a number:")
    val=int(input())
    result = start(val)

if __name__=="__main__":
    main()
