import sys

def main():
    
    FileName1 = sys.argv[1]
    fobj = open(FileName1,"r")
    data = fobj.read()
    fobj.close()
    FileName2 = sys.argv[2]
    fobj = open(FileName2,"r")
    data1 = fobj.read()
    fobj.close()

    
    if(data == data1):
     print("Success")
    else:
     print("Failure")


if __name__ == "__main__":
    main()
