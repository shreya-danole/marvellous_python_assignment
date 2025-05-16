
def main():
    print("enter a number:")
    val = int(input())
    for i in range(val, 0, -1):
        print("* " * i)

if __name__ == "__main__":
    main()
