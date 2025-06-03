
    # sum = 0
    # while num>0:
    #     digit = num % 10
    #     sum = sum +digit
    #     num = num // 10
    # print(sum) 
sum = 0
def display (num):
    global sum
    if num>0:
        digit = num % 10
        sum = sum +digit
        num = num // 10
        display(num)

        return sum
       
    
def main():
    num = int(input("enter a number"))
    ret = display(num)
    print(ret)
  
  
if __name__=="__main__":
    main()
