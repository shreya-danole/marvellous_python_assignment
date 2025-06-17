
def main():
     fobj = open("source.txt","r")
     data = fobj.read()
    
     fobj = open("destination.txt","w")
     data1 = fobj.write(data)
    
     print("data from file is:",data1)

     fobj.close()

if __name__ == "__main__":
    main()
 