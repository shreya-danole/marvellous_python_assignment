
def main():
    print("enter a number:")
    value = input()
    if not value.isdigit():
        print("Invalid input. Please enter a valid number.")
    else:
        print(len(value))

if __name__=="__main__":
    main()
