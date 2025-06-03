def count_zeros_recursive(n):
    if n == 0:
        return 1  # Base case: If the number is 0, it has one zero
    if n < 10:
        return 0  # Base case: If the number is a single digit (not 0), it has no zeros

    last_digit = n % 10
    remaining_number = n // 10

    if last_digit == 0:
        return 1 + count_zeros_recursive(remaining_number)
    else:
        return count_zeros_recursive(remaining_number)

def main():
    num = int(input("enter a number"))
    ret = count_zeros_recursive(num)
    print(ret)

if __name__=="__main__":
    main()
