class Numbers:
    def __init__(self):
        self.value = int(input("Enter a number: "))

    # Method to check if the number is prime
    def checkprime(self):
        if self.value < 2:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    # Method to check if the number is perfect
    def perfect(self):
        divisors_sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                divisors_sum += i
        return divisors_sum == self.value

    # Method to find all factors of the number
    def factors(self):
        factor_list = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                factor_list.append(i)
        return factor_list

    # Method to sum all proper factors (excluding the number itself)
    def sum_all_factors(self):
        return sum(self.factors())


# Function to demonstrate all the methods
def main():
    print("First object:")
    obj1 = Numbers()
    print("Is Prime:", obj1.checkprime())
    print("Is Perfect:", obj1.perfect())
    print("Factors:", obj1.factors())
    print("Sum of all factors :", obj1.sum_all_factors())

    print("\nSecond object:")
    obj2 = Numbers()
    print("Is Prime:", obj2.checkprime())
    print("Is Perfect:", obj2.perfect())
    print("Factors:", obj2.factors())
    print("Sum of all factors :", obj2.sum_all_factors())

if __name__ == "__main__":
    main()
