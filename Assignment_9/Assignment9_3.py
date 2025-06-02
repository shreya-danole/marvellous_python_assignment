
import multiprocessing


def factorial(val):
    mul=1
    for i in range(1,val+1):
        mul=mul*i
    return mul

def main():
    Numbers = [1,2,3,4,5]
    p = multiprocessing.Pool()
    result = p.map(factorial,Numbers)
    
    p.close()
    p.join()
    print(result)


if __name__ == "__main__":
    main()
