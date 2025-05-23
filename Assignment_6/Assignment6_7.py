def main():
    

    data = []   

    print("Enter 5 numbers:")

    for i in range(5):
        no = int(input())
        data.append(no)
    
    result = max(data)
    print("Maximum value is:",result)



if __name__ == "__main__":
    main()


    