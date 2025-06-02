
import threading
import time

def thread1():
  print("Thread1 start:")
  for i in range(1,6):
       print(i)
  time.sleep(1)

def thread2 ():
   print("Thread2 start:")
   for i in range(1,6):
        print(i)
   time.sleep(1)

def thread3 ():
   print("Thread3 start:")
   for i in range(1,6):
        print(i)

def main():

    T1 = threading.Thread(target=thread1)  
    T1.start()
    T1.join()


    T2 = threading.Thread(target=thread2)
    T2.start()
    T2.join()


    T3 = threading.Thread(target=thread3)
    T3.start()
    T3.join()

if __name__ == "__main__":
    main()
