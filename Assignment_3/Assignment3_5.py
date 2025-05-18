from MarvellousNum import ChkPrime

def ListPrime(numbers):
    """Return the sum of prime numbers in the list."""
    return sum(num for num in numbers if ChkPrime(num))

def main():
        
        n = int(input("Enter how many numbers you want to input: "))
        numbers = []

        for i in range(n):
            num = int(input())
            numbers.append(num)

        print("Input Elements:", *numbers)

        result = ListPrime(numbers)
        print("Sum of prime numbers is:", result)


if __name__ == "__main__":
    main()
