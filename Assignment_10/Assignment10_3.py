from functools import reduce

Checkno  = lambda no : (no>=70 and no<=90)

increase = lambda no : no+10

Mul = lambda A,B : A*B


def main():
    print("How many elemnts:")
    size = int(input())

    data = []
    print("Enter elements are:")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Input list:",data)

    Fdata = list(filter(Checkno,data))   
    print("List after filter",Fdata)

    Mdata = list(map(increase,Fdata))
    print("list after map",Mdata)

    Rdata = reduce(Mul,Mdata)
    print("reduce output",Rdata)
   

if __name__ == "__main__":
    main()
