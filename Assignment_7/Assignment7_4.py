# Accept a list and use filter to keep only even numbers

from functools import reduce
Product = lambda A,B :A*B

def main():
    size= int(input("how many elements to enter?"))

    data = []
    print("elemnts are: ")

    for i in range(size):
        no = int(input())
        data.append(no)

    rdata = reduce(Product,data)
    print("Product: ",rdata)

if __name__=="__main__":
    main()
