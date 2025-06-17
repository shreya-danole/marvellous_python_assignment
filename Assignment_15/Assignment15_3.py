import sys

def main():
    
    FileName = sys.argv[1]
    fobj = open(FileName,"r")
    data = fobj.read()
    fobj = open("Demo.txt","w")
    fobj.write(data)
    fobj = open("ABC.txt","r")
    data1 = fobj.read()
    
    print("data from file is:",data1)

    fobj.close()

if __name__ == "__main__":
    main()
