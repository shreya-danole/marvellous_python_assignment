import os
import sys

def DirectoryWatcher(DirectoryName, Extension):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("Path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    
    if(flag==False):
        print("Path is valid but target is not directory")
        exit()
    print("Absloute apth is:"+DirectoryName)

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            # fname = os.path.join(FolderName,fname)
            if(fname.endswith(Extension)):
                print(fname)
            

def main():

    DirectoryWatcher(sys.argv[1], sys.argv[2])

if __name__ =="__main__":
    main()
