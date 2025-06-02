#create 2 thread for even and odd

import threading

def even():
  for i in range(1,21):
        if i %2 ==0:
            print(i)

def odd ():
   for i in range(1,20):
      if not i%2==0:
          print(i)

def main():
    print("First 10 even numbers are:")
    Even = threading.Thread(target=even)  
    Even.start()
    Even.join()

    print("First 10 odd numbers are:")
    Odd = threading.Thread(target=odd)
    Odd.start()
    Odd.join()

if __name__ == "__main__":
    main()
