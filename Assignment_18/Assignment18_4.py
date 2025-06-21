import os
import sys
import hashlib

def CalculateChecksum(path,BlockSize=1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(BlockSize)

    while(len(Buffer)>0):
         hobj.update(Buffer)
         Buffer = fobj.read(BlockSize)

    fobj.close

    return hobj.hexdigest()


def FindDuplicate(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    
    Duplicate = {}

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)

            else:
                Duplicate[checksum] = [fname]

    return Duplicate


def main():
    Result = FindDuplicate(sys.argv[1])
    print(Result)

 
if __name__ == "__main__":
    main()
