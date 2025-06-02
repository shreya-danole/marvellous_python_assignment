#create 2 thread for even and odd

import threading

def evenfactor(no):
    data = []
    for i in range(1,no):
        if (no%i == 0):
            if(i%2==0):
                data.append(i)
    print("Even factors are:", data)
    sum=0
    for i in data:
        sum=sum+i
    print("Addition of its even factors is:",sum)

def oddfactor(no):
    data = []
    for i in range(1,no):
        if (no%i == 0):
            if( not i%2==0):
                data.append(i)
    print("Odd factors are:", data)
    sum=0
    for i in data:
        sum=sum+i
    print("Addition of its odd factors is:",sum)

def main():
    no = int(input("enter a number:"))
    T1 = threading.Thread(target=evenfactor,args=(no,))
    T2 = threading.Thread(target=oddfactor,args=(no,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
