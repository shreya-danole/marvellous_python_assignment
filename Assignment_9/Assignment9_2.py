
import multiprocessing

def process1(num):
  for i in num:
       ans = i**2
       print(ans)

def main():
    Numbers = [1,2,3,4,5]
    p = multiprocessing.Process(target=process1, args=(Numbers,))
    p.start()
    p.join()

if __name__ == "__main__":
    main()
