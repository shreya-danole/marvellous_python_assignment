def search(data):
    print("enter elemnt to search")
    no = int(input())
    count = 0
    for i in data:
        if(i == no):
            count = count +1
    return count


def main():
    size = int(input("Enter the number of elements: "))

    data = list()   #empty list

    print("enter the values")

    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Input Elements:", *data)

    result = search(data)
    print("output:",result)



if __name__ == "__main__":
    main()


    