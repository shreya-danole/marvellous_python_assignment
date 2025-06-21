import os

def Dispaly():
    print("Enter a file name : ")
    FileName = input()

    if os.path.exists(FileName):
        fobj = open(FileName,'r')
        data = fobj.read()
        print(data)

   
def main():
    Dispaly()

if __name__ == "__main__":
    main()
