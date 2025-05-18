from functools import reduce

Checkeven  = lambda no : (no%2==0)

square = lambda no : no**2

add = lambda A,B : A+B


def main():
    print("How many elemnts:")
    size = int(input())

    data = []
    print("Enter elements are:")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Input list:",data)

    Fdata = list(filter(Checkeven,data))   
    print("List after filter",Fdata)

    Mdata = list(map(square,Fdata))
    print("list after map",Mdata)

    Rdata = reduce(add,Mdata)
    print("reduce output",Rdata)
   

if __name__ == "__main__":
    main()
