
#Area and perimeter of reactangle

def Area(l,b):
    output = l*b
    return output

def Perimeter(l1,b1):
    output1 = (2*(l1+b1))
    return output1


def main():
    length = int(input("Enter length: "))
    width = int(input("Enter width:"))

    ret1 = Area(length,width)
    ret2 = Perimeter(length,width)

    print("Area: ",ret1)
    print("Perimeter: ",ret2)


if __name__=="__main__":
    main()
