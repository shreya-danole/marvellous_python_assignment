# print sum of even no. from 1 and 100

def main():
    sum = 0
    for i in range(1,101):
        if(i%2==0):
            sum = sum +i
    print(sum)


if __name__=="__main__":
    main()
