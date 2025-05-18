def add(data):
    sum = 0
    for value in data:
        sum = sum +value 
    return sum

def main():
    print("Enter how number of elemnts?")
    size = int(input())

    data = list()   #empty list

    print("enter the values")

    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Entered elements are:", *data)

    result = add(data)
    print(f"The sum of the numbers is: {result}")

if __name__ == "__main__":
    main()


    