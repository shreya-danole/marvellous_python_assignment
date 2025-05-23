# Accept a list of integers from the user and use map() function to double each value

increase = lambda No : No*2

def main():
    size = int(input("Enter how number of elemnts?"))
    data = []
    print("enter the values")

    for i in range(size):
        no = int(input())
        data.append(no)
    
    Mdata = list(map(increase,data))
    print("Doubled list",Mdata)


if __name__=="__main__":
    main()
