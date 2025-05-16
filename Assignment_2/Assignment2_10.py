def main():
    print("enter a number:")
    number = input()
    if not number.isdigit():
        print("Invalid input. Please enter a valid number.")
    else:
        value = int(number)
        sum_of_digits = 0
        for digit in number:
            sum_of_digits = sum_of_digits + int(digit)
        print("Sum of digits:", sum_of_digits)
        
if __name__ == "__main__":
    main()
