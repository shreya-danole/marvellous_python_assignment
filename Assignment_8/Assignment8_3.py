#create 2 thread for even and odd

import threading

def evenlist(no):
    data = []
    for i in (no):
        if(i%2==0):
            data.append(i)
    sum=0
    for i in data:
        sum=sum+i
    print("Addition of even number is:",sum)


def oddlist(no):
    data = []
    for i in (no):
        if( not i%2==0):
            data.append(i)

    sum=0
    for i in data:
        sum=sum+i
    print("Addition of  odd numers is:",sum)


def main():
    print("Enter how number of elemnts?")
    size = int(input())

    data = list()  

    print("enter the values")

    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Entered elements are:", *data)

    T1 = threading.Thread(target=evenlist, args=(data,))
    T2 = threading.Thread(target=oddlist, args=(data,)) 

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
