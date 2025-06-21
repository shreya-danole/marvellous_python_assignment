import os

def Dispaly():
    print("Enter a file name : ")
    FileName = input()

    fobj = open(FileName,'r')
    data = fobj.read()


    fobj1 = open('Demo.txt','w')
    fobj1.write(data)
    fobj1 = open('Demo.txt','r')
    data1 = fobj1.read()

    print(data1)

   
def main():
    Dispaly()

if __name__ == "__main__":
    main()
