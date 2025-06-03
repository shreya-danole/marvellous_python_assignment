
# def display(no):
#     i = 1
#     while(i<=no):
#         print(i,end=" ")
#         i = i+1

i = 1
def display(no):
    global i 
    if(i<=no):
        print(i,end=" ")
        i = i+1
        display(no)

def main():
    num = int(input("enter a number"))
    display(num)
  
  
if __name__=="__main__":
    main()
