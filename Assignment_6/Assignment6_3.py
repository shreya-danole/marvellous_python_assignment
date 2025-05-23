# accept no from user and print its multiplication table up to 10

def mult(no):
    for i in range(1,11):
        print(no,"*",i,"=",no*i)

def main():
    no = int(input("Enter a number: "))
    mult(no)

if __name__=="__main__":
    main()
