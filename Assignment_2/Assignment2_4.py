
def ans(no):
    data = []
    for i in range(1,no):
        if (no%i == 0):
            data.append(i)
    return data


def main():
    print("enter a number:")
    num=int(input())
    output =ans(num)
    sum=0
    for i in output:
        sum=sum+i
    print("addition of its facotrs is:",sum)


if __name__=="__main__":    
    main()
