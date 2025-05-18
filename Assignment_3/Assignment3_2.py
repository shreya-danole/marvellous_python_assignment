def main():
    print("Enter how number of elemnts?")
    size = int(input())

    data = list()   #empty list

    print("enter the values")

    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Entered elements are:", *data)

    result = max(data)
    print("Maximum value is:",result)



if __name__ == "__main__":
    main()


    