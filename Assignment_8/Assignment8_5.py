#create 2 thread for even and odd

import threading

def thread1():
    print("display 1 to 50:")
    for i in range(1,51):
        print(i,end=" ")


def thread2():
    print("display 50 to 1:")
    for i in range(50,0,-1):
        print(i,end=" ")


def main():
    T1 = threading.Thread(target=thread1)
    T2 = threading.Thread(target=thread2) 

    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()
