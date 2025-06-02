from functools import reduce
import math

def is_prime_filter(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

mul = lambda no : no*2


def main():
    print("How many elemnts:")
    size = int(input())

    data = []
    print("Enter elements are:")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Input list:",data)


    Fdata = list(filter(is_prime_filter, data))
    print("List after filter",Fdata)

    Mdata = list(map(mul,Fdata))
    print("list after map",Mdata)

    Rdata = reduce(max, Mdata)
    print("reduce output",Rdata)
   

if __name__ == "__main__":
    main()
