
def sum(n):
   if n <= 1:
       return n
   else:
       return n + sum(n-1)

def main():
    num = int(input("enter a number"))
    ret = sum(num)
    print(ret)


if __name__=="__main__":
    main()
