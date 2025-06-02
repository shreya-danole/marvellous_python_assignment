import threading

def small(value):
    print("Thread id of small is:",threading.get_ident())
    print("Thread name of main is:", threading.current_thread().name)
    count = 0
    for i in value:
        if i.islower():
            count = count+ 1
    print("no of small characters:", count)

def capital(value):
    print("Thread id of capital is:",threading.get_ident())
    print("Thread name of main is:", threading.current_thread().name)
    count = 0
    for i in value:
        if i.isupper():
            count = count+ 1
    print("no of capital characters:", count)

def digits(value):
    print("Thread id of digits is:",threading.get_ident())
    print("Thread name of main is:", threading.current_thread().name)
    count = 0
    for i in value:
        if i.isdigit():
            count = count+ 1
    print("no of digits:", count)

def main():
    print("Thread id of main is:",threading.get_ident())
    print("Thread name of main is:", threading.current_thread().name)
    string_value = input("Enter a string: ")

    T1 = threading.Thread(target=small, args=(string_value,))
    T2 = threading.Thread(target=capital, args=(string_value,))
    T3 = threading.Thread(target=digits, args=(string_value,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()
