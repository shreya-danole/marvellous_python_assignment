# Accept a list and use filter to keep only even numbers


def Checkeven(data):
    if(data%2==0):
        return data

def main():
    size= int(input("how many elements to enter?"))

    data = []
    print("elemnts are: ")

    for i in range(size):
        no = int(input())
        data.append(no)

    fdata = list(filter(Checkeven,data))
    print("Even numbers: ",fdata)

if __name__=="__main__":
    main()
