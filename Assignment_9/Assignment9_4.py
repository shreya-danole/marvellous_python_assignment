import time
import threading
import multiprocessing

def normal(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    print(sum)

def threaded_sum(num):
    sum = 0
    for i in range(1,num+1):    
        sum = sum + i
    print(sum) 

def multiproc_sum(num):
    sum = 0
    for i in range(1,num+1):    
        sum = sum + i
    print(sum) 

def main():

    # Normal execution
    start_time = time.time()
    ret = normal(10000000)
    end_time = time.time()
    print("Time (normal):", end_time - start_time)

    # Threading
    start_time = time.time()
    T1 = threading.Thread(target=threaded_sum, args=(10000000,))   
    T1.start()
    T1.join()
    end_time = time.time()

    print ("time (Threading):",end_time-start_time)

    # Multiprocessing
    start_time = time.time()
    p = multiprocessing.Process(target=multiproc_sum,args=(10000000,))
    p.start()
    p.join()
    end_time = time.time()

    print ("time (Multiprocessing):",end_time-start_time)

if __name__ == "__main__":
    main()
