# Accept a list and use filter to keep only prime numbers


def checkprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
        

def main():
    size= int(input("how many elements to enter?"))

    data = []
    print("elemnts are: ")

    for i in range(size):
        no = int(input())
        data.append(no)

    fdata = list(filter(checkprime,data))
    print("Prime numbers: ",fdata)

if __name__=="__main__":
    main() 
