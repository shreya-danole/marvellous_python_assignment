
def main():
    print("enter a number:")
    val = int(input())
    for i in range(val):
        for j in range(i+1):
            print(j+1, end=" ")
        print()

if __name__ == "__main__":
    main()
