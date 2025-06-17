import os 

def main():
    print("Enter the name of that you want to read:")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in the current directory")
        fobj = open(FileName,"r")
        data = fobj.read()
    
        print("data from file is:",data)

        fobj.close()

    else:
        fobj = open(FileName,"w")
        fobj.write("Display contents of Demo,txt on console")
        fobj = open(FileName,"r")
        data = fobj.read()
    
        print("data from file is:",data)

        fobj.close()

if __name__ == "__main__":
    main()
