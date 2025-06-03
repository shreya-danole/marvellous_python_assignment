# calculate factorial

# def display(num):
#     i = 1
#     mul = 1
#     while(i<=num):
#         mul = mul * i
#         i = i + 1 
#     print(mul)

i = 1
mul =1
def display(num):
    global i, mul
    if(i<=num):
        mul = mul * i
        i = i + 1 
        display(num)

        return mul
       
def main():
    num = int(input("enter a number"))
    ret = display(num)
    print(ret)
  
  
if __name__=="__main__":
    main()
